# Odoo 18 Inventory and Accounting Do Not Match

## The question

**Why can inventory valuation and accounting appear inconsistent in Odoo 18, and how should the investigation be controlled?**

Inventory valuation touches both stock operations and accounting. When the values do not reconcile, the correct response is not a blind adjustment. The investigation needs to establish which records, dates, products, locations, valuation layers, or journal entries created the difference.

## Investigation checklist

A controlled investigation should examine:

- product-category valuation configuration,
- costing method and valuation method,
- stock moves around the affected period,
- inventory valuation layers and related journal entries,
- archived products or locations that still have accounting impact,
- timing differences around receipts, deliveries, returns and corrections,
- manual journal entries that bypass the expected stock/accounting flow.

## CorePilot approach

**Detect mismatch → isolate affected scope → trace stock/accounting evidence → identify cause → plan correction → verify balances after action**

This scenario fits the diagnostic and reconciliation capabilities of **ERP Control Center for Odoo 18**.

## Product

→ [ERP Control Center for Odoo 18](../products/erp-control-suite.md)

## Need help tracing the mismatch?

Describe the symptom, period, and expected result without sharing confidential exports publicly.

**Product inquiries:** corepilotlabssupport@gmail.com

**Public, non-sensitive problem report:** https://github.com/corepilotlabs/odoo18-business-apps/issues