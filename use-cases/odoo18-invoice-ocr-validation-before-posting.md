# Odoo 18 Invoice OCR Validation Before Posting

## The question

**How do you speed up invoice capture in Odoo 18 without trusting OCR blindly?**

Odoo 18 supports document digitization for vendor bills. The important control question is what happens when the extracted supplier, tax, total, reference, or accounting mapping is uncertain.

## The business risk

OCR reduces typing, but extraction is only the first step. A reliable workflow should still detect:

- uncertain supplier matching,
- inconsistent subtotal, tax and total values,
- duplicate invoice references,
- weak account or tax mapping confidence,
- documents that require human review before a draft is accepted.

## CorePilot approach

**Capture → extract → score confidence → validate totals and duplicates → review exceptions → create a controlled draft → verify**

CorePilot **Smart Transaction Capture for Odoo 18** is positioned as a validation and control layer around document-driven transaction entry, not as a claim that OCR itself is infallible.

## Product

→ [Smart Transaction Capture for Odoo 18](../products/smart-transaction-capture.md)

## Have this problem in your Odoo workflow?

Describe the document type, the fields that matter, and the failure you are trying to prevent. Do not post customer invoices, credentials, or sensitive financial data publicly.

**Product inquiries:** corepilotlabssupport@gmail.com

**Public, non-sensitive feature request:** https://github.com/corepilotlabs/odoo18-business-apps/issues