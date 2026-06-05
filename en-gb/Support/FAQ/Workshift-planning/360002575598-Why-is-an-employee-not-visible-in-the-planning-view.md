---
id: 360002575598
title: Why is an employee not visible in the planning view?
url: https://support.nepton.com/hc/en-gb/articles/360002575598-Why-is-an-employee-not-visible-in-the-planning-view
locale: en-gb
category: Support
category_id: 360000446658
section: Workshift planning
section_id: 360005884838
section_path:
- FAQ
- Workshift planning
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-08-23T09:58:58Z'
edited_at: '2024-08-09T08:56:55Z'
---

# Why is an employee not visible in the planning view?

This instruction presents the most common situations and reasons why the shift planner does not see all the locations they need or the people working in the locations in the planning view of the Planning section.
## 1\. View filters
Make sure that the view is not unnecessarily filtered in the **View settings**.
![](https://support.nepton.com/hc/article_attachments/20768472637341)
![](https://support.nepton.com/hc/article_attachments/20768472639773)
**\- Person list** : the view is limited according to each person list. If the person missing from the planning view is not a member of the selected person list, the person is not shown in the planning view either.  
**\- Location** : If the highest possible location (category) is selected, all people from lower level locations are also displayed in the planning view. However, if a certain sub-location is selected to which the missing person does not belong, the person will not be shown in the planning view either.  
**\- Primary supervisors** : If a supervisor who is not the primary supervisor of the person missing from the planning view is selected in the primary supervisors field, the person will not be shown in the planning view either.  
**\- Tasks** : If tasks have been added to the service, only the shifts to which the selected task is attached to are displayed. If the person does not have any planned shifts with the selected task, the person will not appear in the planning view either.
## 2\. No unit has been assigned for the person
You can add [the unit information](<https://support.nepton.com/hc/en-gb/articles/360002595478>) in the person's information in the Employees section, if the unit information is missing. A person can belong to several units, in which case one of the units is primary and the rest are secondary. However, unit primacy has only informative value.
![](https://support.nepton.com/hc/article_attachments/20769059036701)
## 3\. The person has not been added to the location
Make sure that the person is connected to their shift planning location. Adding people to locations is done from the top bar of the Planning section in the **Locations**.
![](https://support.nepton.com/hc/article_attachments/20770539041309)
In the Locations section, first select the location (planning level) where the person works. Under the Location Persons menu in the planning level, you can already see persons attached to the office. Check under the "Available persons" section if there is still a person missing from the planning view in the list. Add a person to the location using the Add button in front of the name. Adding a person to the location does not need to be saved separately.
![](https://support.nepton.com/hc/article_attachments/20770539047197)
The structure of the Locations follows the so-called waterfall model. If a person works in several locations, they can be assigned to the highest location. In this way, shifts can be planned for a person at all sub-locations.  
For example, in the picture above - If a person worked at both locations Espoon keskus and Leppävaara, he could be assigned to the location Espoo.
If a person is missing under the Persons to be added section, there can be two reasons:
1) No unit has been added for the person in the Employees section.  
2) A unit has been assigned to the person, but the location to which the person is being added is under a different unit.
Regardless of which reason it is, the correct unit information must be added to the person's information.
