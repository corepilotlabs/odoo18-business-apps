# OCR Invoice Capture in Odoo 19 Needs Validation, Not Extraction Alone

OCR can reduce typing, but extraction alone does not make an accounting transaction safe. The harder questions come after the text is read.

## Typical risks

A scanned supplier invoice may contain a supplier name, invoice number, subtotal, tax and total, but the workflow can still fail if:

- the wrong supplier is matched
- the invoice is a duplicate
- subtotal + tax does not equal total
- the tax or account mapping is uncertain
- the document contains only a subtotal but no true total
- low-confidence values are accepted automatically

## CorePilot approach

**Smart Transaction Capture** uses a controlled path from document evidence to an Odoo 19 draft accounting document:

**Capture → Parse → Match → Validate → Confidence → Review / Fail Closed → Draft → Verify**

The purpose is not to eliminate review at any cost. It is to automate the repetitive part while stopping when the evidence is inconsistent or incomplete.

See the [Smart Transaction Capture product brief](../products/smart-transaction-capture.md).

For product questions: **corepilotlabssupport@gmail.com**
