# CorePilot Labs — Frequently Asked Questions

## What does CorePilot Labs build?

CorePilot Labs builds focused business-control applications for Odoo. The current Odoo 19 line covers ERP/accounting diagnostics, purchase-price control, transaction capture and inventory-close control.

## Is this repository the commercial source-code repository?

No. This repository is the public product, documentation and release-evidence layer. Commercial source code remains private.

## Which products are currently published?

**ERP Control Suite** is the current published commercial Odoo 19 product. Purchase Price Control, Smart Transaction Capture and Inventory Close Control are validated Odoo 19 commercial candidates whose release gates are documented here while their publication path is finalized.

## Why publish validation identifiers if the CI repository is private?

They provide traceability without exposing commercial source. They identify the private release-gate runs used when the public validation summary was prepared.

## What does “fail closed” mean?

For a sensitive workflow, fail-closed behavior means the product stops or requires review when required evidence is incomplete, inconsistent or below the accepted confidence threshold. It should not silently guess and continue.

## Does every CorePilot product modify Odoo data automatically?

No. The control model depends on the workflow. Some functions are read-only diagnostics. Sensitive actions can require a Dry Run, review or explicit approval before execution, followed by post-action validation.

## What is the difference between ERP Control Suite and the focused products?

ERP Control Suite is a broader control application for ERP/accounting diagnostics, reporting, reconciliation, inventory and cutover work. The focused products target narrower operational problems such as purchase-price variance, document capture or inventory close.

## Are the products for Odoo 18 or Odoo 19?

The active public product line is **Odoo 19**. This repository was originally created during the Odoo 18 launch line, which is why its repository name still contains `odoo18`. The current documentation and release evidence describe the Odoo 19 line.

## What license is used?

The commercial product line uses **OPL-1** unless a specific product states otherwise.

## Can I report a feature request publicly?

Yes. Use GitHub Issues for non-sensitive feature requests and documentation corrections. Do not post database exports, credentials, invoices, customer data or security-sensitive information in public issues.

## How do I contact support?

Email **corepilotlabssupport@gmail.com**.

For sensitive security matters, follow [SECURITY.md](SECURITY.md).
