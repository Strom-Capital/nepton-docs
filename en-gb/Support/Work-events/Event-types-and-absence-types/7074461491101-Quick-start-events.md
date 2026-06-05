---
id: 7074461491101
title: Quick start events
url: https://support.nepton.com/hc/en-gb/articles/7074461491101-Quick-start-events
locale: en-gb
category: Support
category_id: 360000446658
section: Event types and absence types
section_id: 360005841257
section_path:
- Work events
- Event types and absence types
labels: []
promoted: false
updated_at: '2026-02-25T05:52:17Z'
edited_at: '2026-02-25T05:52:16Z'
---

# Quick start events

Quick start events are a customisable, convenient, and quick way for employees to record fully or partially prefilled work events in Nepton Mobile. Available at working community and/or setting group levels they can be used by all employees in a single click.
## Configuration
If quick start events are not configured, quick start shows by default the users default event type and lunch if user is permitted to record those types of events.
Quick start events are configured for Working community and/or Setting group levels, and can make use of inheritance. See the related settings respectively in **Worktime > Administration > Working Community / Setting group Settings > Work hours > Quick start events.**
Note that when configuring quick start events, the fields and options available are context-sensitive, and therefore might be different when configured at the working community level vs. setting group level. For example if working community level has a quick start event configured which includes a supplement that is not available for certain setting group, the members of this setting group can record an event based on the quick start event but are not able to use the supplement they are not permitted to set.
![](https://support.nepton.com/hc/article_attachments/32929142855837)
A new quick start event is added by clicking "Add quick start event". This opens up the event editing form, but instead of recording an event, this is used to save the event as a template that people can use when they quick start that event.
Each quick start event requires a title, which is used for displaying it when listing quick start events. Titles should be descriptive so that people can recognise and distinguish them without reviewing all their details.
If projects are enabled, a selection is visible for whether the quick start event should include default project. If this is checked, then recording an event from the quick start event will automatically include the recording user's default project to the recorded event.
![](https://support.nepton.com/hc/article_attachments/32929132213789)
"In use" - columns selection defines whether quick start event is enabled or not. Newly added quick start events are in use by default. If it is required to disable a quick start event, it can be set by selecting "No" in the "In use" - column. "In use" supports setting inheritance so if a quick start event should be shown for a parent setting group but not shown for a child setting group, "In use" can be set to "Yes" for parent setting group and then "No" for child setting group to achieve this.
Quick start event can be deleted by clicking the X button in the "Delete" column.
If a travel invoice quick start event is created, if you want to add trip dates and durations, and the quick start event will have the travel and trip dates prefilled based on the current date and the saved duration. If trip dates and durations are not meaningful for the quick start event, they can be left empty.
![20221129-quickstart-events-guidance-e3.PNG](https://support.nepton.com/hc/article_attachments/7985939150621)
Note that some event types like event requests, travel invoices, and administrative ones, can not be directly started even if they are in the quick start menu because they always have more details needed from the person recording them. The "Start" button is not shown for these, instead they can be opened by clicking "Add" button for editing before being saved/started.
Also if a quick start event has something configured that the person is not permitted to add, quick starting is not possible but instead a work recording based on the event can be done by clicking "Add", where user is asked to check the items that were present in the quick start event that could not be used in their event. See troubleshooting - chapter below for more info.
### Languages
The name of the quick start event can be translated into languages used in the organization. This way, the quick start event is displayed according to the user's language preference. When editing the quick start event, a 'Other languages' button appears next to the Name field, allowing you to create translations for different languages.
![quick-start-language.png](https://support.nepton.com/hc/article_attachments/32028611863325)
### User permissions
The permissions assigned to the work time role of the user affect the way events can be created using the quick start events. The minimum permissions required for a user to create an event with a quick start option, is the permission to review own events and the permission to record real time events (both basic level permissions). The permission to edit events allows user to modify the entry during creation or after starting it. You can read about the worktime roles [here](<https://support.nepton.com/hc/en-gb/articles/360002554338>)
## Use
Quick start events are shown both in mobile and calendar view.
### Mobile view
Quick start events are shown in user's mobile view where they can:
  * Record an event based on it by clicking "Start" if the event can be clocked by the person
  * Click the quick start event name which opens the event editing form and person can record their event having prefilled values from the quick start event.
  * If an event can not be quick-started, a recording based on the event can be added by clicking "Add"


![20221129-quickstart-events-guidance-e4.PNG](https://support.nepton.com/hc/article_attachments/7985902575005)  
_Quick start shows a list of configured quick start events. Events can be quick started by clicking "Start" or opened for editing by clicking the quick start event title._  

![20221129-quickstart-events-guidance-e5.PNG](https://support.nepton.com/hc/article_attachments/7985940809501)
 _Event editing form opens with prefilled values based on the quick start event._
### Calendar view
Quick Start events can be used in calendar view by clicking on the date. A new window will pop-up with the quick start events under the Add event function. 
![](https://support.nepton.com/hc/article_attachments/32929142860573)
When clicking on the quick event, a new event editing window will pop up. The event is already pre-filled with the quick start event information, but it can also be manually edited or directly Saved.
![](https://support.nepton.com/hc/article_attachments/32929132215709)
Alternatively a quick start event can be started by clicking on "Start":
![](https://support.nepton.com/hc/article_attachments/32929132217117)
In which case the pre-made event starts from that second and is active until ended.
## Troubleshooting
If a quick start event is set up in a way that it is set for a person, but includes preset values that are not available for the user to set (such as a supplement that is set to be not used anymore, overtime target that is set to be not in use anymore or a project that has already been completed), quick start view will indicate this with an info icon and an event can't be clocked based on it. The event can still be opened for editing with "Add" button. The values that could not be set for the user are defaulted, i.e. if there was an overtime target not available, it uses default overtime target and if there was a supplement that could not be set, it is not included in the event editing form.
![20221129-quickstart-events-guidance-e6.PNG](https://support.nepton.com/hc/article_attachments/7985941262493)
_If event can not be quick started, it will have an info-icon next to it. It can be opened for editing by clicking "Add" - button._
![20221129-quickstart-events-guidance-e7.PNG](https://support.nepton.com/hc/article_attachments/7985904113949)
_When opening an event, person is informed of fields they should check before saving the event._
