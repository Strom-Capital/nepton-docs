---
id: 360017908457
title: Planning view calculations
url: https://support.nepton.com/hc/en-gb/articles/360017908457-Planning-view-calculations
locale: en-gb
category: Support
category_id: 360000446658
section: General worktime calculation settings
section_id: 19210968853277
section_path:
- Workshift planning and Work schedules
- General worktime calculation settings
labels: []
promoted: false
updated_at: '2024-08-23T11:23:40Z'
edited_at: '2024-02-21T07:20:12Z'
---

# Planning view calculations

When creating a work shift plan in Planning > Planning view, Nepton supports decision making by projecting work totals including planned and clocked events, against your contractual obligations with workers. This article details how those projections are calculated, and what each value and colour-coding represents.
## Totals columns
By default, the planning view only has one total column called "View". This represents the totals for the currently selected view and filters.
There are two values in each totals column. The first represents the target set for the person, and the second one represents the total work hours planned and/or realised for the person.
**Note:** Realised events are those marked in Worktime and configured to be shown in planning via Worktime > Administration > Working Community settings > Work hours > Event types.
![WSP_12.png](https://support.nepton.com/hc/article_attachments/360018245318)
You can include additional information and totals in the planning view, by opening the "View settings" menu. Select the relevant information you want to include, such as the levelling period. Click "Apply" to apply the changes.
![](https://support.nepton.com/hc/article_attachments/16916683525021)
Additional total columns will be shown if they are relevant, based on the selected filters. 
## Defining a person's contracted hours (aka Target)
The 'Target' value represents weekly work obligation set for a person, in hours. Weekly work obligations are set in the form of minimum and maximum work hours per week. The minimum and maximum work hours per week can be set on each person's information page, via Employees > Persons.
![WSP_16.png](https://support.nepton.com/hc/article_attachments/360018245378)
## Target work hours
A person's target values are shown in three different colors in planning view.
### Blue - Projected work hours are less than the target
If the total work hours are less than the minimum work hours per week, then target value is shown in blue. The target value shows the difference of minimum work hours minus total work hours (minimum work hours per week - total work hours). In the example below, the set value for minimum work hours per week is 32 h and total work hours are 30 h, so the target value is 2:00 h.
![WSP_07.png](https://support.nepton.com/hc/article_attachments/360018245278)
### Green - Projected work hours are within target Min/Max
If the total work hours are between minimum work hours and maximum work hours per week, then target value is shown in green color with a plus sign. The target value shows the difference of total work hours minus minimum work hours per week (total work hours - minimum work hours per week). For instance, in example below the set value for minimum work hours per week is 32 h and total work hours are 37:30 h, so the target value is +5:30 h.
![WSP_08.png](https://support.nepton.com/hc/article_attachments/360018185637)
### Red - Projected work hours are over the target
If the total work hours are greater than maximum work hours per week, then target value is shown in red color with a plus sign. The target value shows the difference of total work hours minus maximum work hours per week (total work hours - maximum work hours per week). For instance, in example below the set value for maximum work hours per week is 40 h and total work hours are 45:30 h, so the target value is +5:30 h.
![WSP_09.png](https://support.nepton.com/hc/article_attachments/360018245298)
### Black dash - A person does not have targets set
If a person does not have targets defined in their information, then a black dash ("-") is shown with mouse-over text "Target: Not set"
![WSP_18.png](https://support.nepton.com/hc/article_attachments/360018185777)
## Projected work hours
The second value in the 'View' totals columns, is the total work hours planned for the person. The total hours break down is shown when you hover the mouse on the total hours value.
![WSP_10.png](https://support.nepton.com/hc/article_attachments/360018185657)
### Public holidays
If there is no workshift activity on a public holiday then its length is added to the total work hours normally. Public holiday length can be set in Employees > administration > Planning section.
![WSP_15.png](https://support.nepton.com/hc/article_attachments/360018245398)
If there is a workshift activity on a public holiday then we have a setting which dictates how public holiday length is added to total work hours. The setting can be set in Employees > administration > Planning section.
![WSP_20.png](https://support.nepton.com/hc/article_attachments/360018245418)
**Example 1**
Public holiday length : **8h**
Workshift length on public holiday: **8h**
Public holidays contribute full daily work obligation in addition to any planned work on the day = **false**
total work hours = **8h** (only workshift length (8h) is added to the total work hours)
![WSP_23.png](https://support.nepton.com/hc/article_attachments/360018245458)
**Example 2  
**
Public holiday length : **8h**
Workshift length on public holiday:**8h**
Public holidays contribute full daily work obligation in addition to any planned work on the day = **true**
total work hours = **16h**(publich holiday length (8h) + workshift length (8h) is added to the total work hours)
![WSP_24.png](https://support.nepton.com/hc/article_attachments/360018245478)
### Activity types that never contribute towards projected work hours
The following activity types never contribute towards the work cost totals:
  * Sick Leave
  * Annual Holiday
  * Absence
  * Dining
  * Balance Leave
