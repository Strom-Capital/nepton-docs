---
id: 360003961118
title: Work time percentage
url: https://support.nepton.com/hc/en-gb/articles/360003961118-Work-time-percentage
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- työaikaprosentti
- osa-aikaisuus
- work time percentage
- part time
promoted: false
updated_at: '2026-09-23T09:37:04Z'
edited_at: '2026-09-23T09:37:04Z'
---

# Work time percentage

If a person has a reduced daily working time, for example 60% of normal, a work time percentage can be set for them. More detailed description about part-time options can be found in [this](<https://support.nepton.com/hc/en-gb/articles/360002559018-Configure-setting-group-for-part-timers>) article.
If the normal daily working time was 7 hours 30 minutes and the weekly working time 37 hours 30 minutes, 60% of the working time would be
  * 4 hours 30 minutes daily
  * 22 hours and 30 minutes weekly


The work time percentage can be set via **Employees > Persons >** search the person you were looking for and open the person's information from the magnifying glass icon and go to the **Employment information** section.
![](https://support.nepton.com/hc/article_attachments/39355908086173)
NOTE! The working time percentage is entered without a percentage sign. An empty field and 100% are both interpreted as full-time (100%). The work time percentage field works with the[ validity function](<https://support.nepton.com/hc/en-gb/articles/360004856937>).
The work time percentage does not affect:
  * daily and weekly maximum TES time
  * daily work time interpreted from a shift
  * if the daily or weekly work time comes from a daily exception entry
  * leveling period hours, unless it is [configured that work time percentage considers work time percentage](<https://support.nepton.com/hc/en-gb/articles/14849123960989>)


## Work time changing in the middle of work week
When an employee's work percentage changes during the workweek, the system does not know which percentage to use for calculating the length of work week. In such cases, the balance accrual at the end of the week might not be correct. To address this, manually adjust the balance for the next day using the balance reset or balance change methods, please see instructions [here](<https://support.nepton.com/hc/en-gb/articles/360002481797-Setting-and-changing-the-value-of-balance>).
Alternatively, you can set an exception to the length of this specific workweek in the person’s work calendar. To do this, add up the required hours for different work obligations to determine the total weekly work obligation.
For example: 
Monday to Wednesday (when person is under 60% obligation): 3 x 6 hours = 18 hours  
Thursday to Friday (when person is under 100% obligation): 2 x 7.5 hours = 15 hours  
The total work obligation for the week is 33 hours. 
You can set an exception to the work week obligation by clicking on a date in that week and selecting Length of work week:
![](https://support.nepton.com/hc/article_attachments/39355783397021)
A new window will open, where you can set an exception for the length of the work week. Save the changes by pressing Save. You can remove the exceptions you have made in the same view by clicking the cross button. The exception set in this way will only apply to the work week in question.
![](https://support.nepton.com/hc/article_attachments/39355783403293)
