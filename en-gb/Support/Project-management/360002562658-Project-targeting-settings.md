---
id: 360002562658
title: Project targeting settings
url: https://support.nepton.com/hc/en-gb/articles/360002562658-Project-targeting-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Project management
section_id: 360000707398
section_path:
- Project management
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-05-22T07:34:17Z'
edited_at: '2026-05-21T05:15:28Z'
---

# Project targeting settings

Project settings can be managed both on **Working community** and **Setting group** levels.
## Settings in Working community level
### Working community level
All other project-related settings in Working community level are under "projects" (Worktime > Administration > Working community level > Projects).
![](https://support.nepton.com/hc/article_attachments/36217009558429)
**Service enabled** \- Defines whether project targeting is in use. When the service is enabled, Projects menu will appear in the Worktime section.
**How many levels of parent projects are included in the project name** \- If the value is for example 2, are the projects parent and the parent project's parent project names shown.
Below is an example of how the parent projects are shown:
![](https://support.nepton.com/hc/article_attachments/19182786907293)
**Show the project description in the interface** \- Project description is visible both in adding a new event view and when viewing an existing event.  
**Include the project code in the project name** \- Parent and child project codes are shown before the project name as in the picture below:
![](https://support.nepton.com/hc/article_attachments/19183397590813)
**Show only projects assigned to person in the worktime** \- When adding an event, only the projects related to the user or his/her person group are shown. Instructions: [How to add a project to a person or person group.](<https://support.nepton.com/hc/en-gb/articles/360006776758-Adding-projects-to-person-or-person-group>)
  * If the value of the setting is "No", all projects are visible to the user, if there are 50 or less projects in total. If there are more than 50 projects, the most recently used ones are displayed.
  * A default project can only be a project that is attached to the person or his/her person group. Instructions: [Setting a person's default project](<https://support.nepton.com/hc/en-gb/articles/360002563098-Adding-default-project-to-a-person>).


**Stop active projects when logging out from the terminal** \- The project is terminated when logging out via terminal, and the same project will not continue automatically when starting a new event. If this setting is set to "No", either the default project or the project that was in the last entry will continue in the next event, regardless of who made the entry and whether it was done via terminal or another way.
**Target the worktime event to the project of the planned work shift** \- If the setting is set to "no", the person's default project is used.
**How near to the scheduled shift the event must be recorded in order to use the project of the planned work shift -** When a new real-time event is created, the person's default project is automatically added to it. With this setting it can be set so, that the project added to the event is the project for which the person's working time is planned for, when the person starts their work shift in close enough time to the planned shift. The project will then come from the shift. The amount of time within the work needs to be started before the shift is set in the setting.
The value of his setting doesn't matter, if the setting "Target the worktime event to the project of the planned work shift" has been set to "no". 
**Minimum number of projects users must select for events-** If this is set to bigger than 0, is adding a project to every event mandatory. More about setting projects mandatory in [this article](<https://support.nepton.com/hc/en-gb/articles/360002561457-Making-project-mandatory-for-events>).
**Maximum number of projects users can select for events-** defines, how many projects can be added to each event.  
**Show the project duration input -** Defines, whether project length can be added to events. Length can be given both in hours/minutes or percentages: ![](https://support.nepton.com/hc/article_attachments/19188579174557)
Further instructions for targeting event to multiple projects can be found [here](<https://support.nepton.com/hc/en-gb/articles/4411705615377-Targeting-events-to-projects-general>).
### Project types
Instructions for Project types and adding new project types are in [this article](<https://support.nepton.com/hc/en-gb/articles/360002562338-Project-types>).
In this section, each project type can be given a translation to any Nepton use language. Additionally a hint text can be given to project types. The text is shown to users under the heading "projects" when adding or editing an event.
![](https://support.nepton.com/hc/article_attachments/36217009560477)
## Settings in setting group level
Project settings in setting group level can be found: **Worktime > Administration > Setting groups > *select wanted setting group* > Setting group settings > Projects.**
In setting group settings the settings of the projects are narrower than the settings in the working community. In the settings group in the project settings, the number of parent projects displayed in the project name, targeting the event to the project of the work shift, and the accuracy with which the event recording is assigned to the project of the planned work shift can be defined.
Minimum and maximum numbers of required projects and the option for adding the length of the project can also be set for each setting group.
![](https://support.nepton.com/hc/article_attachments/36217070346653)
## Current Status
The setting for displaying projects on terminals and the Current status view can be found in **Worktime > Administration > Working community settings > Current status.** When this is set to Yes, all new events are automatically targeted to the user's default project, or alternatively by the scheduled shift's project if it is set to be on.
![](https://support.nepton.com/hc/article_attachments/31526827552541)
