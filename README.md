<p align="center"><img src="assets/brand/corepilot-cover.svg" alt="CorePilot Labs — Odoo 19 Business Control Tools" width="100%"></p>

# CorePilot Labs — Odoo Business Control Tools

[![Public Showcase Quality](https://github.com/corepilotlabs/odoo18-business-apps/actions/workflows/showcase-quality.yml/badge.svg)](https://github.com/corepilotlabs/odoo18-business-apps/actions/workflows/showcase-quality.yml)

**Detect problems earlier. Build evidence. Approve safely. Verify the result.**

CorePilot Labs builds focused control applications for **Odoo 19** around real accounting and operational failure points. We do not position the product line as “more automation.” The design goal is controlled action: understand the exception, show the evidence, introduce a checkpoint when the risk requires it, and verify what actually happened.

> **Repository note:** this public repository was originally created for the Odoo 18 launch line. The active showcase and current release evidence now document the Odoo 19 product line. Commercial source code remains private.

## Product line

| Product | Business problem | Status | Price |
|---|---|---|---:|
| [ERP Control Suite](products/erp-control-suite.md) | Diagnose, control and verify ERP/accounting problems | **Published** | **$199** |
| [Purchase Price Control](products/purchase-price-control.md) | Detect price increases and improve purchase approval evidence | Validated Odoo 19 candidate | $99 planned |
| [Smart Transaction Capture](products/smart-transaction-capture.md) | Convert document evidence into verified accounting drafts | Validated Odoo 19 candidate | $149 planned |
| [Inventory Close Control](products/inventory-close-control.md) | Detect inventory-close risks before execution and verify the result | Validated Odoo 19 candidate | $129 planned |

## The CorePilot control model

**Detect → Explain → Evidence → Review / Dry Run → Approval → Execute → Verify**

The exact steps depend on the workflow. Read-only diagnostics do not need artificial friction. High-impact accounting or operational actions should not continue on weak evidence or an unverified assumption.

## Problem library

Start from the business problem rather than the product name:

- [How to detect purchase-price increases in Odoo 19](use-cases/odoo-purchase-price-increase-control.md)
- [Why OCR invoice capture needs validation](use-cases/odoo-invoice-ocr-validation.md)
- [What to check before an inventory close](use-cases/odoo-inventory-close-reconciliation.md)
- [How to diagnose accounting and ERP issues systematically](use-cases/odoo-accounting-diagnostics-control.md)

## Release evidence

The current Odoo 19 candidates have completed automated runtime gates covering install, test execution, upgrade/retest, installed-state verification and uninstall/reinstall smoke checks where applicable. The public summary records the private CI traceability identifiers without exposing source code.

→ [Read RELEASE_VALIDATION.md](RELEASE_VALIDATION.md)

## Public site

The repository contains a responsive customer-facing landing page:

- [English landing page](index.html)
- [الصفحة العربية](ar.html)
- [Buyer FAQ](FAQ.md)

The site is prepared for GitHub Pages publishing once Pages is enabled for this repository.

## Public vs private

**Public here:** product positioning, safety principles, release evidence, problem-led educational content, support routes and non-sensitive feature requests.

**Private:** commercial source code, credentials, customer data, database exports and private runtime logs.

## Support

**corepilotlabssupport@gmail.com**

Use [SUPPORT.md](SUPPORT.md) for product support guidance and [SECURITY.md](SECURITY.md) for sensitive security matters. Do not post customer or security-sensitive data in public GitHub Issues.

---

**CorePilot Labs** · Odoo 19 business-control tools · Commercial source stays private
