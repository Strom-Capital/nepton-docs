---
id: 360002519157
title: Adding, enabling and editing event types
url: https://support.nepton.com/hc/en-gb/articles/360002519157-Adding-enabling-and-editing-event-types
locale: en-gb
category: Support
category_id: 360000446658
section: Event types and absence types
section_id: 360005841257
section_path:
- Work events
- Event types and absence types
labels:
- tapahtumatyypit
- Tapahtumatyypin lisääminen
- urakkatyö
- virkamatka
- tapahtumatyyppien muokkaus
- käyttäytyminen
- event types
promoted: false
updated_at: '2026-02-24T13:22:48Z'
edited_at: '2026-02-24T13:22:48Z'
---

# Adding, enabling and editing event types

By default there are multiple different [Event types](<https://support.nepton.com/hc/en-gb/articles/360002520778-Event-types>) in Nepton. This article describes how to add, enable, and edit new event types directly in the service. A custom event type can be needed, for example, if the name of the event type needs to be changed. The article also describes how the visibility of the event types is managed.
There is also a separate article for[ Default and Assumed Event Types](<https://support.nepton.com/hc/en-gb/articles/360002558717>).
## Adding a new event type
The configuration is made in the menu **Work time > Administration > Working community settings > Work hours > Event types**.
Click **Add Event Type**.
![](https://support.nepton.com/hc/article_attachments/34194975561117)
Enter a **name** for the new event type. Please make sure that the name is clearly different from the names of the service's default event types. This text will appear in the event list when a new event is added or an event is edited. The name can be up to 64 characters long. You can also provide a translation for the name in another language by clicking "Other languages". In this case, if Nepton is used in English, for example, the user will see the English name entered for the event type instead of the original Finnish name.
Enter a **code** for the event type. The code can be anything, but it must be unique. This makes it easier to handle the event type in, for example, rule sets for integrations and setting exception settings. The code can be up to 64 characters long.
Select the **behavior** for the event type, i.e. how the calculations with the new event type is performed. For example, if you select work as the behavior, the new event type behaves in the same way as the work event type. **NOTE:** If behavior is, for example Work time shortening leave, then Work time shortening leave [accrual](<https://support.nepton.com/hc/en-gb/articles/360005073918-Accruals>) needs to be in use. Otherwise visibility selection for this event type can't be set.
At the moment it is not possible in the service to create an event type from Travel invoice so that it would include the supplements and calculations of a Travel invoice.
When all the fields have been entered, click **Add**.
![](https://support.nepton.com/hc/article_attachments/16686866347677)
Error is shown if event type with the same name and behavior already exists.
![](https://support.nepton.com/hc/article_attachments/16686895768349)
## Event type activation and visibility
When a new event type is added, it will appear in the list. The listing is in alphabetical order. The new event type must be activated at either the Working community settings level or the Setting groups level, depending on how widely the event type is used in the work community (i.e. the new event type can be visible and selectable to all or only to a specific group). Activation of the event type is done by ticking the selection (at the Working community settings level) or by selecting the "Yes" option from the menu (at the Setting groups level). Event types can be taken into use for example only for terminals, but not the calendar view.
When editing events = calendar view  
On terminal = recording terminals, current page and mobile  
From direct link = Not in use anymore
The setting is saved from the Save button at the bottom of the page.
Working community settings options:  

![](https://support.nepton.com/hc/article_attachments/34194995292957)
Setting groups options:
![](https://support.nepton.com/hc/article_attachments/34194995293469)
## Event type settings
The settings of the event types are shown in a table format. The event types are listed below and the settings for them are listed in rows. It is therefore possible to make event type-specific settings. Working community level settings are slightly wider than setting group level settings.
The first setting is "**Marked time total** ". If this setting is activated, the calendar view will have its own row, where the total time marked for this type of event is calculated daily and weekly. Below is an example of a situation where the marked time total has been activated for Remote work:
![](https://support.nepton.com/hc/article_attachments/20871445760029)
After this comes the "in use" section, where you can specify on which devices the event type is used. This is explained in more detail in the text of the previous heading (Event type activation and visibility).
The next setting is "**Expose begin and end time on terminal** ". This is often used, for example, for annual leave or balance leave, when these event types should be able to be recorded in advance from the terminal. Options in the setting are Not exposed (default, same as Not set), Optional or Mandatory. The Optional selection enables, but does not force, the recording of start and end times. Selecting Mandatory forces the recording of start and end times.
![](https://support.nepton.com/hc/article_attachments/34194975567133)
Activating "**Requested from supervisor in advance** " turns the event type into an [event request](<https://support.nepton.com/hc/en-gb/articles/360017787717>).
By activating "**Show in planning view** " the event types are shown in the shift planning calendar. For example, if this is activated for the event type "Annual leave", and the person has recorded annual leave for the future in their calendar, the shift planner will see these Annual leave events when planning shifts for these days. All absences are displayed in the planning view with just "Absence". For example, here Vuoro, V. has recorded Annual leave for the period of 19.8.-25.8., and it appears in the planning view like this:
![](https://support.nepton.com/hc/article_attachments/20873019670429)
Note! The event type is displayed in the planning view after the activation is  
done. Any events recorded before activation are not automatically updated  
in the planning view. If the old event is modified after activation, then it  
will be updated in planning.
## Removing event type from use
If an event type is out of date, and you no longer want it to appear in the event menu when adding a new event, it can be disabled either at the Working community level or Setting group level. In the event type row under "In use", set "NO" (or uncheck the box at work community level) to the options from which you want to remove it.
Removal of event type visibility is done by removing it from use. This does not affect history of created events but prevents new events being created with this event type.
![](https://support.nepton.com/hc/article_attachments/34194995298333)
## Editing existing event type
If event type with behavior _Emergency Work_ was created before 18.04.2024, it currently has behavior _No change_. Salary calculations of this event type has not changed. If event type is saved again with behavior Emergency Work, it inherits behavior of standard Emergency Work event type (e.g. minimum compensation of 1 hour, is daily overtime).
At the working community settings level, the pen image in front of the event type indicates that this is a new event type added directly to the service, not a standard event type. At the setting groups level, this is indicated by the * sign. From the pen image, you can also edit event type information and behavior. Event types can only be edited at the Working community settings level.
![mceclip6.png](https://support.nepton.com/hc/article_attachments/4407098482449)
![mceclip5.png](https://support.nepton.com/hc/article_attachments/4407098476305)
Edit event type view contains fields for _original name_ and  _name_. The differences are:
  * Original name: Name which was used when the event type was created. This can't be changed and no new event type can be created with **this name and behavior**. If event type was created with multiple translations, original name is the translation which was set for language which was used in the service when creating the event. 
  * Name: Name of the event type which is shown, for example, in worktime calendar. It is possible to modify translations with Other languages action. If translations are not modified, original name and name can be the same. 


![](https://support.nepton.com/hc/article_attachments/16686895772957)
Changes made here also have a retroactive effect - if you want the changes to take effect only from today, you must create an entirely new event type instead of editing it and change the deployment settings for both event types in both the working community settings and each of the setting groups.
