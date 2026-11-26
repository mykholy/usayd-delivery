"""Verify original source digests; permit only explicitly recorded LF CSV blobs."""
import hashlib
import re
from pathlib import PurePosixPath

HEX = re.compile(r"[0-9a-f]{64}")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def index_variants(document, original):
    if document["schema_version"] != 1:
        raise ValueError("Unsupported CSV variant schema")
    result = {}
    for entry in document["entries"]:
        path = entry["path"]
        before = entry["original_sha256"]
        after = entry["lf_sha256"]
        posix = PurePosixPath(path)
        if (path in result or posix.is_absolute() or ".." in posix.parts
                or posix.suffix != ".csv" or path not in original
                or not HEX.fullmatch(before) or not HEX.fullmatch(after)
                or before != original[path] or before == after):
            raise ValueError("Invalid CSV LF variant: " + path)
        result[path] = after
    return result


def verify_bytes(path, data, expected, variants):
    actual = digest(data)
    if actual == expected:
        return "original"
    # No runtime normalization, whitespace trimming, or broad file exemptions.
    if path in variants and actual == variants[path]:
        return "lf_variant"
    raise ValueError("SHA256 mismatch: " + path)
