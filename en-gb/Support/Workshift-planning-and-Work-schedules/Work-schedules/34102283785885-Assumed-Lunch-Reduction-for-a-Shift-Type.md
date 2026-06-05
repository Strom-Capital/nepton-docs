---
id: 34102283785885
title: Assumed Lunch Reduction for a Shift Type
url: https://support.nepton.com/hc/en-gb/articles/34102283785885-Assumed-Lunch-Reduction-for-a-Shift-Type
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
updated_at: '2026-02-26T08:49:49Z'
edited_at: '2026-02-20T09:00:23Z'
---

# Assumed Lunch Reduction for a Shift Type

This article explains how an assumed lunch reduction can be defined for a shift type in shift planning. The reduction can be set individually for each shift type. The assumed lunch reduction can only be defined for shift types in the work schedule.
## General rules for the assumed lunch reduction
The assumed lunch reduction can be defined only for event types that are listed under the **Work** category in the Event type list. If the event type is selected from the **Absence** category, the field used for setting the assumed lunch reduction will not be shown.
If no specific assumed lunch reduction is defined for a shift type, the reduction is determined as follows:
  * the shift’s assumed lunch reduction is taken from the Location settings under the**** Planning tab, or
  * from the Planning settings located under the Employees tab in the Administration section


If lunch break settings are defined both the assumed lunch reduction is always determined using the Location settings.
If no assumed lunch reduction should be applied to the shift type, the shift type’s reduction must be set to **0 minutes**. This ensures that no reduction is created.
## Defining the Assumed Lunch Reduction
The assumed lunch reduction is defined in the work schedule when creating a shift type. The reduction is set individually for each shift type, and the defined value affects all shifts created using that shift type.
The assumed lunch reduction is defined as follows:
  1. Create a new work schedule and schedule period, or open an existing work schedule.
  2. Create a new shift type or open an existing shift type.
  3. Add the desired **assumed lunch reduction** to the shift type.
  4. Save the changes.


![Screenshot 2026-02-20 105710.png](https://support.nepton.com/hc/article_attachments/34103435994909)
