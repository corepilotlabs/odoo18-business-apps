# Odoo 18 purchase price variance: detect the change before approval

A purchase order can be technically valid and still be commercially risky if the buyer cannot see how the current price compares with previous purchases or alternative vendors.

## A stronger approval pattern

Before approving a materially higher price, compare:

- previous price from the same vendor,
- historical average price,
- best historical price,
- alternative-vendor prices where comparable,
- unit of measure and currency normalization,
- the financial impact of the variance.

The goal is not to overwrite the vendor's quoted or invoiced price. The goal is to preserve the source evidence, show the variance clearly, and require review only when the exception is material.

## Where Purchase Price Control fits

**Purchase Price Control for Odoo 18** is built around this control point. It adds price history, vendor intelligence, variance/risk visibility and controlled approval for higher-price purchases.

This creates an audit trail around the decision rather than silently changing the commercial evidence.

[See Purchase Price Control](../products/purchase-price-control.md)

Private procurement review: **corepilotlabssupport@gmail.com**
