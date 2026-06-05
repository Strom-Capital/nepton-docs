---
id: 360019742118
title: Edit or set accrual value to multiple people at once
url: https://support.nepton.com/hc/en-gb/articles/360019742118-Edit-or-set-accrual-value-to-multiple-people-at-once
locale: en-gb
category: Support
category_id: 360000446658
section: Accruals
section_id: 360000705197
section_path:
- Worktime calculations and management
- Accruals
labels:
- saldoasetus
- saldotilanne
promoted: false
updated_at: '2025-06-09T08:19:30Z'
edited_at: '2025-06-09T08:19:30Z'
---

# Edit or set accrual value to multiple people at once

It is possible to set or change an accrual value for multiple persons at once using [event import](<https://support.nepton.com/hc/en-gb/articles/360002868137>). This may be necessary, for example, when the service is first taken into use and the starting balances need to be set for all employees.
The accrual is changed or set by using the Accrual Reset event type. At least the following columns must be imported:
  * Employee number
  * Event type code. Must be set before import in **Worktime > Administration > Working community settings > Integrations > Event import**.
  * New value for accrual. Can be moved either in HH:MM format or in decimals.
  * Start date
  * Start time
  * End date
  * End time


The data fields (columns) and their technical requirements as well as an example file are described in more detail [here](<https://support.nepton.com/hc/en-gb/articles/360002868137>).
