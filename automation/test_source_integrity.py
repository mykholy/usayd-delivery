import unittest
from source_integrity import digest, index_variants, verify_bytes


class SourceIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.raw = b"a,b\r\n1,2\r\n"
        self.lf = self.raw.replace(b"\r\n", b"\n")
        self.path = "data.csv"
        self.original = {self.path: digest(self.raw)}
        self.entry = {"path": self.path, "original_sha256": digest(self.raw), "lf_sha256": digest(self.lf)}

    def test_exact_original_and_exact_lf_accepted(self):
        variants = index_variants({"schema_version": 1, "entries": [self.entry]}, self.original)
        self.assertEqual(verify_bytes(self.path, self.raw, digest(self.raw), variants), "original")
        self.assertEqual(verify_bytes(self.path, self.lf, digest(self.raw), variants), "lf_variant")

    def test_modified_content_rejected(self):
        variants = index_variants({"schema_version": 1, "entries": [self.entry]}, self.original)
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            verify_bytes(self.path, b"a,b\n1,3\n", digest(self.raw), variants)

    def test_unlisted_csv_and_binary_fail(self):
        for path in ("other.csv", "design.jpg"):
            with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
                verify_bytes(path, self.lf, digest(self.raw), {})

    def test_wrong_original_and_duplicate_rejected(self):
        for entries in ([dict(self.entry, original_sha256="0"*64)], [self.entry, self.entry]):
            with self.assertRaisesRegex(ValueError, "Invalid CSV"):
                index_variants({"schema_version": 1, "entries": entries}, self.original)

    def test_binary_variant_rejected(self):
        entry = dict(self.entry, path="design.jpg")
        with self.assertRaisesRegex(ValueError, "Invalid CSV"):
            index_variants({"schema_version": 1, "entries": [entry]}, {"design.jpg": digest(self.raw)})


if __name__ == "__main__":
    unittest.main()
