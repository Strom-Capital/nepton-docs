---
id: 4409591067409
title: Examples of setting annual leave
url: https://support.nepton.com/hc/en-gb/articles/4409591067409-Examples-of-setting-annual-leave
locale: en-gb
category: Support
category_id: 360000446658
section: Examples for setting up setting groups
section_id: 360001483898
section_path:
- Worktime calculations and management
- Setting groups
- Examples for setting up setting groups
labels:
- vuosilomalaskenta
- loma
- lomasaldo
promoted: false
updated_at: '2025-11-07T08:05:28Z'
edited_at: '2024-08-16T10:39:56Z'
---

# Examples of setting annual leave

This articles presents some examples on how to take annual leave calculations into use. Instructions for managing annual leave balance can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002481737>), and instructions for annual leave earning set up can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002560698>).
## Example 1
The service has been in use, but the annual leave calculations are taken into use on April 1st 2024.
When annual leave calculation is introduced retroactively, the amount of leave entitlement carried over from the previous holiday year must be set for each person. The amount of annual leave entitlement is set for March of the previous holiday year (March 1, 2023) with the event type Annual leave balance reset. The amount of the annual leave balance to be set is the accumulated annual leave that was valid on March 1, 2023. The holiday entitlement earned in March 2023 is included in the holiday earning accumulation, and any annual holiday taken in March is taken into account as a deduction from it.
For example, a person should have 30 days of vacation right from April 1, 2024. The person has been on vacation for 6 days in March 2023, and his annual leave calculation earnings are in use, resulting in 2.5 days of vacation entitlement per month. When you want 30 days as the entitlement to be valid on April 1, 2024, the setting for the March annual leave balance is set to 30 + 6 - 2.5 days, i.e. 33.5 days.
The annual leave balance reset event type gives the annual leave balance a new starting value. Annual leave accrual or use of the annual leave balance before setting the annual leave balance reset, are not taken into account in the calculations, so all previous accruals must be included in the set value of the annual leave balance.
## Example 2
The service has been in use and annual leave calculations are activated in the middle of the holiday year, on October 1st. 
\- All annual leave earning settings are set to be valid from October 1st onwards.
-If annual leave days have NOT been recorded in Nepton, all earned and unused days by September 30th must be recorded using Annual leave earning change event, for 30th of September. From now on (1.10.) all used Annual leave days will be recorded in Nepton.
\- If the annual leave days have been recorded in Nepton, the unused Annual leave days of the previous holiday year on September 30, and the days accumulated since April 1 are counted together and recorded in the service with Annual leave balance reset event. From now on (1.10.) all used Annual leave days will be recorded in Nepton. 
## Example 3
Annual leave calculations are taken into use at the same time with Nepton. 
Nepton is taken into use for example on September 1st. Person A has 6 days of unused annual leave. This 6 days is recorded in Nepton with Annual leave balance reset for March of the current year (so 1.3.). In this case, person will have 6 days to use on the current holiday year.
Since the service is taken into use on September 1st, there are no events recorded before that, and no data of earned holidays from time between April 1st and August 31st.
In this example person A has earned 2,5 days of annual leave per month, so in total 12,5 days. This 12,5 days are set for the first day of use, so September 1st. 
This accrual of 12,5 days (and all other days that will be earned starting September 1st) person A can use during the next holiday year, so starting in next year's April.
