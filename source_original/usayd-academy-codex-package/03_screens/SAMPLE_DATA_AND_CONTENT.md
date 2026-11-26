# Sample data and content slots

- **Owner content (CONTENT_REQUIRED):** 40 slots — prices, teacher names/photos/bios on public pages, testimonials, legal entity, approved texts. In the design they are amber boxes marked “owner content”. In production the block is **hidden** until the academy supplies approved content. Never fill them with invented text.
- **Runtime sample data:** 356 slots — learner and teacher names inside signed-in screens, counts, IDs and amounts. They are illustrative only (dotted underline) and come from the API at runtime.
- **Quran text:** never sample. Every ayah block is a placeholder until the licensed source (O-06) is connected.
- Full list: `CONTENT_SLOTS.csv`. Test environments may use seeded fictional data; it must never appear in production or marketing.
- Action contracts: 641 in-place controls across the screens — `ACTION_CONTRACTS.csv` and §14 of each screen spec.
