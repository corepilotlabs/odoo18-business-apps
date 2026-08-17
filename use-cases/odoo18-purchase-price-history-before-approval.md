# Odoo 18 Purchase Price History Before Approval

## The question

**How can a buyer see that a purchase price has increased before approving the RFQ or purchase order?**

A purchase order can be technically valid while still being commercially weak. The risk appears when the current price is reviewed without enough historical or supplier context.

## What should be visible before approval

A useful purchasing control should surface:

- the previous price paid to the same vendor,
- the historical average for the item,
- the best relevant historical price,
- alternative-vendor context where comparable,
- the percentage and value of the price variance,
- the potential financial impact before approval.

## Why this matters in Odoo 18

Odoo provides the purchasing workflow. CorePilot **Purchase Price Control for Odoo 18** adds a control layer around the price decision so the approver sees the evidence before accepting an increase.

## CorePilot approach

**Detect increase → compare history → explain variance → show supplier context → require the appropriate approval → keep traceability**

The goal is not to block normal purchasing. It is to make unusual price movement visible at the moment when someone can still act on it.

## Product

→ [Purchase Price Control for Odoo 18](../products/purchase-price-control.md)

## Have this problem in your Odoo database?

Describe the purchasing scenario without sending confidential data. We can first determine whether standard Odoo configuration already covers the need or whether an additional control is justified.

**Product inquiries:** corepilotlabssupport@gmail.com

**Public, non-sensitive feature request:** https://github.com/corepilotlabs/odoo18-business-apps/issues