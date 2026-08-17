# Odoo 18 OCR vendor bills: extraction is not the same as validation

OCR can read invoice fields, but accounting risk starts when incomplete or ambiguous OCR output is accepted as trusted data.

Typical problems include truncated vendor names, split invoice references, uncertain tax/account mapping, duplicate invoices, and totals that do not reconcile.

## A controlled capture pattern

1. Extract the document fields without posting anything.
2. Normalize and match the supplier identity.
3. Reconstruct and validate the invoice reference.
4. Check for duplicates before draft creation.
5. Validate subtotal, tax and total consistency.
6. Match accounts and taxes with confidence scoring.
7. Route low-confidence cases to review instead of guessing.
8. Create only a draft accounting document, then verify the created result against the source evidence.

## Where Smart Transaction Capture fits

**Smart Transaction Capture for Odoo 18** follows this pattern: OCR-assisted extraction with supplier/account/tax matching, confidence checks, duplicate detection and fail-closed review when the evidence is inconsistent.

It is designed to complement Odoo's accounting workflow, not blindly replace human judgment with OCR output.

[See Smart Transaction Capture](../products/smart-transaction-capture.md)

Private workflow review: **corepilotlabssupport@gmail.com**
