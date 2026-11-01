# Book One — audio-reader failure analysis and pre-merge repair log
**Repository:** DevelopPioneerNavigate/the-diesel-paradox · **Branch:** feature/book-one-foundation · **PR:** #1
**Source of truth:** all 42 canonical Markdown chapters · **Status:** pre-merge quality repair

## Reproduced in the previously published listening PDF
Input examined: the exact previous 1,032-page chapters-only `The_Diesel_Paradox_Book_One_Listening_Edition.pdf` exported from the successful GitHub Actions artifact.
- All 42 PDF chapter bookmarks were present; text was selectable, **but extraction quality was not suitable to certify audiobook playback**.
- **1,031 of 1,032 pages** repeated `DPN TECHNOLOGY / THE DIESEL PARADOX` and `LISTENING EDITION / CANON V3.1` in the extracted text layer. Some TTS readers announce these or stop reading at them.
- The PDF text extractor returned **approximately 29,248 layout line breaks**. This is a characteristic of typeset PDF, not 29,248 source prose paragraph breaks; TTS engines vary in whether they reconstruct them.
- At least **121 body-to-body page transitions appeared to split sentences**. An example: a page ends `cryogenic thermal` and the next begins `lag, vibration from the west-side pumps.`. This is a playback boundary problem even if not a missing manuscript sentence.
- Chapter-opening pages repeated production labels such as `CHAPTER 01` and source chapter titles. The frontmatter incorrectly asserted `The entire novel is not complete` after 42/42 chapter drafts existed.
- These are independently observed file structure problems; they are **not evidence of specific behavior of the user's undisclosed audiobook app**.

## Repairs on feature branch
1. **Preferred audio format:** add an EPUB3 reflowable edition with 42 one-chapter-per-XHTML sections, native chapter navigation (EPUB3 nav plus legacy NCX), natural unwrapped paragraph text and **no fixed page breaks or page furniture**.
2. **Fallback:** a continuous UTF-8 TXT edition with canonical chapter order, Markdown emphasis cleaned but no missing prose, and paragraphs separated naturally; no running header/footer.
3. **Approved cover:** use the exact original 1024x1536 PNG assembled from eight checked Git source parts; verify SHA-256 `5ba1bd629ff9b7b86bbcc4e1a2f956f4965078989fe46e66d508d6f6cf976e06`. Never invent or silently substitute new cover artwork.
4. **Existing PDF:** remove repeated running header/footer extraction text, correct completed-draft frontmatter, avoid duplicating chapter production labels, and keep short paragraphs together where possible. PDF remains fixed-layout and **is not guaranteed TTS-safe in every reader**.
5. **Regression gate:** `scripts/validate_accessible.py` verifies exact paragraph-for-paragraph prose equality for all 42 EPUB chapters against Markdown, count/order, continuous TXT coverage, cover checksum, 42 PDF bookmarks, removal of repeated page furniture and the finale. CI uploads EPUB, TXT and PDFs in one artifact.

## Interpretation and remaining acceptance
- **This repair targets source integrity and audiobook compatibility, not text-to-speech voice or pronunciation.** Apps may differ in format support, automatic page navigation, sentence chunk length, handling of chapter headings, memory usage and speech engine.
- Real-device acceptance requires import of the regenerated **EPUB** (not PDF), playback across the original Chapter 1 sample, a mid-book section, and Chapter 42 ending with pauses/resume. Test uninterrupted speech at former PDF page boundaries. If the specific app is PDF-only, prefer **TXT** if available or its accessible reading mode.
- Editorial work remains: complete literary/technical copyedit, normalize occasional name variations only after contextual review, approve interior artwork, verify final pagination/typesetting and obtain creator permission before merge. The earlier 194,277-word first-draft ledger is an inventory, not line-level certification.
- **Do not merge PR #1 automatically.** Distinguish GitHub Actions PASS from tested audio playback on user's chosen device.
