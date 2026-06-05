---
id: 25649119586717
title: Levelling period calculation improvements
url: https://support.nepton.com/hc/en-gb/articles/25649119586717-Levelling-period-calculation-improvements
locale: en-gb
category: News and events
category_id: 4407530962705
section: News
section_id: 4407542715409
section_path:
- News
labels: []
promoted: false
updated_at: '2025-03-11T13:00:05Z'
edited_at: '2025-03-07T11:30:09Z'
---

# Levelling period calculation improvements

This article contains information about changes done in the release on 22.3.2025.
The levelling period calculations are being improved in the release done in the release window on 22.3.2025. They have been optimized with performance enhancements that speed up payroll data retrieval, reporting, approvals and the use of Worktime calendar. Additionally, levelling period settings have been standardized, simplifying configuration. Outdated settings that are not used in the service anymore have been removed. The improvements for levelling period calculations also apply for flexible work hours accrual.
**Streamlining of levelling period calculations**
Levelling period is configured by enabling the levelling period accrual in Worktime settings **Work hours** **> Accrual and overtime hours > Accrual is in use > Levelling period** **hours**.
Retired method of configuring levelling periods, which was previously used by a limited number of customers, has been discontinued. Customers who this concerns have been contacted. Levelling period is now always configured in the same way. If levelling periods have previously been defined using the retired method and need to be recalculated retroactively, the new method must also be configured so that it is in use retroactively.
With the removal of the outdated method, the levelling period date selection that has been selectable in some manual integration runs, will also be removed. Going forward, the levelling period dates in integrations will always be determined based on the dates set for the levelling period in levelling period accrual configurations.
[Setting up a levelling period](<https://support.nepton.com/hc/en-gb/articles/360002559537>)  
[Retired method for setting up a levelling period](<https://support.nepton.com/hc/en-gb/articles/4405550230173>)
**Levelling period settings**
Levelling period settings have been clarified. Levelling period calculation settings can be configured under **Work hours** **> Accrual and overtime hours > Levelling period** **hours > Levelling period overtime calculations**. Previously, some of these settings were located seperately under **Work hours > Levelling period** \- section, but they have now been moved under Levelling period accrual settings to keep all related settings in one place.
[Configuring levelling period overtime calculations](<https://support.nepton.com/hc/en-gb/articles/4410630282257>)
**Levelling period attention triangle in calendar**
If levelling period calculations on a day do not match with calculations recorded earlier, an attention triangle will be displayed in Worktime calendar in a similar way as is done for balance accruals. See [retrospective change of settings and recalculation of accrual value](<https://support.nepton.com/hc/en-gb/articles/4411220910865>) for instructions if levelling period compensation needs to be recalculated.
![](https://support.nepton.com/hc/article_attachments/25649518754845)
**Overtime compensations for the levelling period can be included in salary exports grouped by project**
A new setting "Group levelling period compensation by project in salary export" has been added to the levelling period calculation settings. Overtime compensations for the levelling period will be grouped to correspond with work performed under different projects in the levelling period. Previously, certain integrations processed this breakdown without a specific setting, but now this will be configured separely if needed. Enabling this functionality will slightly impact calculation performance.
