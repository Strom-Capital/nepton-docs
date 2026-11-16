---
id: 13554423857181
title: Managing a Person's Work Schedule Group
url: https://support.nepton.com/hc/en-gb/articles/13554423857181-Managing-a-Person-s-Work-Schedule-Group
locale: en-gb
category: Support
category_id: 360000446658
section: Work schedules
section_id: 10363010715933
section_path:
- Workshift planning and Work schedules
- Work schedules
labels: []
promoted: false
updated_at: '2026-07-09T08:09:24Z'
edited_at: '2026-07-09T08:02:46Z'
---

# Managing a Person's Work Schedule Group

Once a work schedule has been created and at least one work schedule period has been published, it must be ensured that the correct employees see the planned shifts assigned to them. This requires keeping work schedule group memberships up to date and managing them carefully. Work schedule group memberships can only be managed after at least one period using that particular work schedule group has been published.  
## The Significance of Work Schedule Group Information
Based on the work schedule group information, planned shifts are generated for the employee in the shift planning view, as well as shifts in the Worktime calendar. Since planned shifts often also determine the length of the workday and affect work time calculations, it is important that the employee always has the correct work schedule group information in effect from the correct date.
## Adding a person to a work schedule group
An employee can be added to a work schedule group in several ways. In all cases, the basic principle is the same: work schedule group information is added for the person, and a Start date is defined, from which the shifts will be generated. The addition can be made in the following ways:
  * Manually on the Person's Information page
  * Manually on the Members tab of the Work Schedule
  * Through person import. For large numbers of employees, it is advisable to manage work schedule groups via person import. 


![Screenshot 2026-07-09 at 10.53.47.png](https://support.nepton.com/hc/article_attachments/37480487397277)
When adding a work schedule group, it is important to note that the Start date determines from which date the shifts will be generated. The shifts are visible from that date onward in both the planning view and the work time calendar.
## Changing a person's work schedule group
If a person's work schedule group changes, a new work schedule group entry must always be added for them, rather than modifying the existing work schedule group. If the work schedule group is changed simply by selecting a new value from the dropdown, the person's previous shifts on the calendar will also change as a result of the work schedule group change, which is not desirable. The work schedule group can be changed using the same methods as when adding it: on the Person's Information page, on the Members tab of the Work Schedule, or through person import.
## Removing a person from a work schedule group
When an employee is no longer part of shift planning and shifts should no longer be generated for them from the work schedule, the work schedule group membership must be ended in a controlled manner. The correct approach is to add a new work schedule group entry for the person, selecting "-" (empty work schedule group) as the work schedule group, and defining the Start date from which shifts will no longer be generated. This stops shift generation in a controlled way without affecting previously generated shifts.
A person's work schedule group should never be removed by unchecking it. Removing the work schedule group by unchecking it deletes the person's shifts from the Worktime calendar, and the effect extends retroactively over the entire period during which the work schedule group was in effect.
If the work schedule group has already been removed from a person by unchecking it, the shift exceptions will not be removed automatically. In this case, the person must be added as a resource at the work schedule's location, and the shifts must be removed manually. 
## System warnings
When a person's work schedule group information is edited on the Members tab of the Work Schedule or on the Person's Information page, the system displays a warning that varies depending on the action being performed. The warning is shown differently depending on whether a work schedule group is being added as a new entry, an existing work schedule group is being changed by directly swapping the value, or the work schedule group is being removed by unchecking it. This ensures the user is always informed of the effects the action will have on the person's shifts and work time history before confirming the change.
![Screenshot 2026-07-09 at 10.53.56.png](https://support.nepton.com/hc/article_attachments/37480487398429)
