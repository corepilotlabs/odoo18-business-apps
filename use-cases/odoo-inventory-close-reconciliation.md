# Inventory Close Reconciliation in Odoo 19

Inventory close problems are often caused by timing gaps that look harmless during the month and become accounting differences at period end.

## Common close risks

Before closing inventory, finance and inventory teams may need to identify:

- received purchases that are not yet billed
- vendor bills posted before the related receipt
- delivered sales that are not yet invoiced
- customer invoices posted before delivery
- missing inventory valuation accounts
- differences between inventory valuation and accounting valuation
- a close date that is already covered or incorrectly backdated

## CorePilot approach

**Inventory Close Control** analyzes the selected date before execution, separates blockers from warnings, locks the Dry Run evidence, requires a backup reference and Accounting Manager approval, then uses Odoo 19 native inventory closing and validates the result afterward.

The control path is:

**Analyze → Resolve blockers → Dry Run evidence lock → Backup → Approval → Native close → Post-close verification**

See the [Inventory Close Control product brief](../products/inventory-close-control.md).

For product questions: **corepilotlabssupport@gmail.com**
