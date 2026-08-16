# How to Detect Purchase Price Increases in Odoo 19

A purchase order can pass every technical validation and still cost more than it should. The control problem is usually not whether a price exists; it is whether the buyer can see enough history before approving it.

## Typical risk

A supplier quotes a higher unit price than the previous purchase. The increase may be reasonable, but without context the approver cannot quickly answer:

- What was the previous vendor price?
- What is the vendor's historical average?
- What was the best historical price?
- Is another approved vendor cheaper?
- How much potential savings is being missed?

## CorePilot approach

**Purchase Price Control** adds price-history and vendor-comparison evidence to the Odoo 19 purchasing workflow. It highlights variance and risk before high-price orders are approved rather than reporting the problem after the purchase is complete.

The control path is:

**Current price → Historical comparison → Alternative vendor evidence → Risk / savings → Controlled approval**

See the [Purchase Price Control product brief](../products/purchase-price-control.md).

For product questions: **corepilotlabssupport@gmail.com**
