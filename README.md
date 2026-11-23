# AHL shot selection: shot categories (round 1)

The work done on 23 Nov 2026 to add shot categories to the F1 consultation shot-selection sheet, so editors can mark which shot each Good/Bad clip is. This is for training the AI shot-selection skill.

## What is in this repo

| Path | What it is |
|---|---|
| `map/build.py` | Builds the category mind map pages (HTML) |
| `map/0-overview.*` | One-page overview: all products, plus the answers so far |
| `map/topper.*`, `clipon.*`, `stickon.*`, `transplant.*` | One page per product, listing each section and its shot names |
| `map/Shot-Category-Map.pdf` | All five pages in one PDF |
| `docs/decisions.md` | What was asked, who answered, and what was decided |
| `docs/sheet-changes.md` | Exactly what changed in the Google Sheet |
| `docs/plan.md` | Who does what next, with dates |
| `docs/messages.md` | The WhatsApp messages sent to the editors |

To rebuild the map: `python3 map/build.py`. It writes the HTML pages. The PNG and PDF files were made from the HTML with headless Chrome.

## Sources

- 4 folder-structure PDFs from the editors' Drive: Alchemane Topper, AHL Clip-On, AHL Stick-On, AHL Hair Transplant
- Mohit's WhatsApp list (22 Nov) and his answers (23 Nov)
- Editors' Figma comments on the "F1 Consultation – Shot Selection Board"

## Where the live work is

- Google Sheet "F1 Shot Selection – Good vs Bad Shots": the Shots tab (new Shot name column E), Lists tab (column H), Progress tab
- Figma "F1 Consultation – Shot Selection Board": the question boards under each product page
