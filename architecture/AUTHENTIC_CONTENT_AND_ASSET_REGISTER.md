# USYD-T0707: Authentic Content, Media, and Content Slots Register
**Jira Key:** [USYD-65](https://mykholy.atlassian.net/browse/USYD-65)  
**Task ID:** `USYD-T0707`  
**Candidate Sprint:** `S00`  
**Authoritative Specifications:** `03_screens/CONTENT_SLOTS.csv`, `00_AUDIT_AND_CHECKLIST.md`, `DECISION_LOG.md`

---

## 1. Executive Summary & Brand Invariants

Usayd Academy («أكاديمية أُسَيْد») is a Quranic learning platform. In Quranic education, authenticity of religious text, authentic scholarship credentials, honest pricing, and transparent testimonials are strict moral and legal obligations.

### 1.1 Non-Negotiable Brand Invariants
1. **Academy Name Spelling:** Always written as **«أُسَيْد»** with proper diacritics (damma on alif, fatha on seen, sukun on yaa). Never written without tashkeel or misspelled.
2. **Tagline:** **«اقرأ بصوتٍ تدنو له الملائكة»** (Alluding to the authentic narration in Sahih al-Bukhari and Sahih Muslim regarding the companion Usayd ibn Hudayr, may Allah be pleased with him). Quoted Hadith text on public pages requires explicit Academic Board sign-off (D-44).
3. **No Fabricated Data in Production:** Zero mock testimonials, zero generated stock photos of fake teachers, zero placeholder prices, and zero unverified Quranic verses in production environments.

---

## 2. Complete Content Slots Inventory (40 Required Slots)

Based on the canonical inventory in `CONTENT_SLOTS.csv`, the following 40 content slots are marked `CONTENT_REQUIRED` and must remain gated or hidden until authentic content is provided and signed off:

### 2.1 Pricing and Commercial Slots (Decisions O-01 & O-02)
| Screen ID | Slot Type | Description (AR) | Governance Rule |
|---|---|---|---|
| `UX-GLOB-002` | `CONTENT_REQUIRED` | السعر (باقة ١) | Hidden until commercial entity signs pricing tiers |
| `UX-GLOB-002` | `CONTENT_REQUIRED` | السعر (باقة ٢) | Hidden until commercial entity signs pricing tiers |
| `UX-GLOB-002` | `CONTENT_REQUIRED` | السعر (باقة ٣) | Hidden until commercial entity signs pricing tiers |
| `UX-GLOB-006` | `CONTENT_REQUIRED` | السعر الإجمالي | Displays breakdown in local currency; no hardcoded USD |
| `UX-GLOB-006` | `CONTENT_REQUIRED` | الكيان التجاري المعتمد | Displays legal business name, tax registration number |
| `UX-GLOB-007` | `CONTENT_REQUIRED` | سياسة التسعير والتجديد | Text written by approved pricing/legal team |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | السعر (خطة مبتدئ) | Pricing slot on public landing page |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | السعر (خطة متقدم) | Pricing slot on public landing page |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | السعر (خطة إتقان) | Pricing slot on public landing page |
| `UX-PUBLIC-003` | `CONTENT_REQUIRED` | السعر / الخطة | Public pricing page slot |
| `UX-PUBLIC-004` | `CONTENT_REQUIRED` | السعر (شهري) | Public subscription comparison |
| `UX-PUBLIC-004` | `CONTENT_REQUIRED` | السعر (فصلي) | Public subscription comparison |
| `UX-PUBLIC-004` | `CONTENT_REQUIRED` | السعر (سنوي) | Public subscription comparison |

### 2.2 Teacher Bios, Photos, and Verification Slots
| Screen ID | Slot Type | Description (AR) | Governance Rule |
|---|---|---|---|
| `UX-LEARNER-006` | `CONTENT_REQUIRED` | نبذة المعلم المعتمدة | Written by teacher, reviewed and certified by Academic Lead |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | صورة معتمدة من المعلم (١) | Real, verified teacher photo with written media consent |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | اسم المعلم (١) | Real name and Ijazah credentials |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | صورة معتمدة من المعلم (٢) | Real, verified teacher photo with written media consent |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | اسم المعلم (٢) | Real name and Ijazah credentials |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | صورة معتمدة من المعلم (٣) | Real, verified teacher photo with written media consent |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | اسم المعلم (٣) | Real name and Ijazah credentials |
| `UX-PUBLIC-005` | `CONTENT_REQUIRED` | صورة معتمدة من المعلم (١..٦) | 6 teacher photo cards on faculty directory |
| `UX-PUBLIC-005` | `CONTENT_REQUIRED` | اسم المعلم (١..٦) | 6 teacher name cards on faculty directory |
| `UX-PUBLIC-006` | `CONTENT_REQUIRED` | اسم المعلم وتفاصيل الإجازة | Full teacher profile with scanned/verified Ijazah documents |
| `UX-PUBLIC-006` | `CONTENT_REQUIRED` | نبذة المعلم الذاتية | Personal bio reviewed by Academic Board |

### 2.3 Consented Testimonials (Decision D-26)
| Screen ID | Slot Type | Description (AR) | Governance Rule |
|---|---|---|---|
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | شهادة طالب معتمدة (١) | Real quote with explicit written learner/guardian consent |
| `UX-PUBLIC-001` | `CONTENT_REQUIRED` | شهادة طالب معتمدة (٢) | Real quote with explicit written learner/guardian consent |

*Rule:* If consented testimonials are unavailable at launch, the testimonial section container must be removed from the DOM, never rendered with placeholder text.

### 2.4 Legal & Academic Authority Slots
| Screen ID | Slot Type | Description (AR) | Governance Rule |
|---|---|---|---|
| `UX-LEARNER-029` | `CONTENT_REQUIRED` | الكيان المعتمد وسياسة الخصوصية | Official legal company name, jurisdiction, DPO contact |
| `UX-PUBLIC-010` | `CONTENT_REQUIRED` | قصة الاسم ومصدرها الأكاديمي | Authentic narration verified by Academic Board |

---

## 3. Quranic Text Licensing & Corpus Standards (Decision O-06)

1. **Digital Corpus Authority:** Must use an authenticated digital Quran corpus (e.g., King Fahd Glorious Quran Printing Complex Uthmanic Script, Hafs 'an 'Asim).
2. **Text Integrity Protection:**
   - Quranic text must never be stored as unverified user input.
   - Text rendering must preserve complete diacritics (tashkeel), stop signs (waqf), and verse markers without font corruption.
   - In offline mode (FR-MOB-004), only licensed and cached surahs may be rendered.
3. **Safe Fallback:** Until the digital license is signed, the application displays verse references (e.g., [البقرة: ٢٥٥]) rather than unverified text blocks.

---

## 4. Visual Media & Kids Illustrations (Decisions D-36 & D-37)

1. **Faceless Cartoon Graphics:** For Kids Mode, illustration sets must feature flat, thick outlines with geometric or Islamic abstract motifs, containing **no human or animal faces** unless explicitly approved by the owner.
2. **Teacher Photography Guidelines:**
   - Professional, modest attire.
   - Neutral, non-distracting background.
   - High resolution (minimum 400x400 px, WebP/SVG format).
   - Written model release on file with compliance team.

---

## 5. Verification & Production Release Gating Rule

A pull request or production release candidate containing new screens must fail verification if:
1. Any `CONTENT_REQUIRED` slot displays generic lorem ipsum or unapproved placeholder strings in a production environment.
2. Fake names, fake reviews, or unauthorized Quran text are detected.
3. The feature flag gating the slot is enabled without documented sign-off from the designated authority (Legal, Commercial, or Academic).
