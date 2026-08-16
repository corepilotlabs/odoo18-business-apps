# Inventory Close Control — Odoo 19

**Price:** $129  
**Publisher:** CorePilot Labs  
**Support:** corepilotlabssupport@gmail.com

## The problem

Inventory close errors often come from timing gaps or valuation issues that become visible only after period close. Examples include received-not-billed purchases, billed-not-received purchases, delivered-not-invoiced sales, invoiced-not-delivered sales, missing valuation accounts or inventory/accounting value differences.

## What it does

Inventory Close Control analyzes the selected close date before execution, classifies blockers and warnings, locks a Dry Run evidence signature, requires a backup reference and Accounting Manager approval, executes Odoo 19 native inventory close, then validates the post-close result.

## Core capabilities

- Inventory valuation vs accounting valuation
- Trial-balance integrity check
- Missing valuation-account detection
- Received not billed
- Billed not received
- Delivered not invoiced
- Invoiced not delivered
- Already-covered / backdated close-date control
- Dry Run SHA-256 evidence lock
- Evidence-change guard after approval
- Mandatory backup reference
- Accounting Manager approval
- Native Odoo 19 inventory close execution
- Post-close reconciliation verification

## Release facts

- Technical module: `corepilot_inventory_close_intelligence`
- Version: 19.0.1.0.0
- OPL-1
- Automated Odoo 19 install, TransactionCase tests, upgrade/retest and uninstall/reinstall gate passed
- Verified CI run: 31938504038

## Best fit

Finance and inventory teams that need a controlled, auditable period-close workflow instead of discovering inventory/accounting differences after the close.
