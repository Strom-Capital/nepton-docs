---
id: 360018588898
title: Project manager
url: https://support.nepton.com/hc/en-gb/articles/360018588898-Project-manager
locale: en-gb
category: Support
category_id: 360000446658
section: Project management
section_id: 360000707398
section_path:
- Project management
labels: []
promoted: false
updated_at: '2026-05-22T07:34:17Z'
edited_at: '2026-05-21T12:33:28Z'
---

# Project manager

A person can be appointed as a project manager for a project. The person gets the right to view and approve the hours recorded for the projects they are the project manager for. In addition, the project manager can report all hours targeted for the project in project reports, regardless of the supervisor-subordinate relationship.
If a person is appointed as the project manager for a parent project, he automatically gets the project manager status for its subprojects, even if they are added to the project tree afterwards. If the person is appointed as the project manager for an individual subproject, he only has project manager rights for this project.
## Appointing a project manager
### In person settings
Projects managed by an individual can be managed in the **Worktime > Administration > Persons** section. Select **Projects managed by person** function and select the person.
![](https://support.nepton.com/hc/article_attachments/36252386330653)
In **Select projects** you can search for projects and from the project hierarchy appearing under **All Projects** you can select single projects for which the person will be added as a project manager.
Project manager rights for a project can be removed from the person by removing the project from the Selected projects list.
Confirm the changes by pressing **Save**.
### In project settings
Project management can also be defined in the project details. Go to **Worktime > Projects > Project administration**. Select the desired project as the target and add one or more project managers to the project under Project managers. Save the information. If a person has been added as a project manager through the project details, the same project will appear in the person's management under Projects managed by the person.
![](https://support.nepton.com/hc/article_attachments/36252373830045)
## Project manager permissions
Being a project manager gives a person the rights to monitor hours targeted for the project they manage without a supervisor-subordinate relationship, and to approve the hours targeted for the project.
### Reports
Project reports can be found in the menu **Workhours > Projects > Reports**. The project manager has visibility into the hours targeted for the project through project reports. Even if a person would not otherwise have visibility into other people's working hours or calendars, they can still see all the hours recorded for the project managed by them. Project manager can pull out project-related reports and view the hours recorded for them through this. The exception is the EU / ELY Centre project report, which requires a separate worktime role right to retrieve, as the report contains information about sick leave, absences and annual leave.
![](https://support.nepton.com/hc/article_attachments/36253643002141)
### Approving project hours
The project manager can also approve hours that are targeted to a project they manage. Project hours are approved in the menu **Worktime > Work hours > Approve project hours**.
![](https://support.nepton.com/hc/article_attachments/36253659727773)
The project hours approval view works the same as the [hours approval view](<https://support.nepton.com/hc/en-gb/articles/360002519197>) for supervisors, but only the hours targeted to the managed project are presented for approval to the project manager.
![](https://support.nepton.com/hc/article_attachments/36253643004701)
**NOTE** : Projects attached to travel invoices are not approved in this view. Approving a travel invoice always approves the project attached to it. Similarly, removing approval from a travel invoice always removes approval from the project attached to it.
When projects and supplements are attached to an event, the supplements will appear in the project hours approval view as the same amount for both projects, regardless of the project duration in the event. If a supplement of €100 has been set for an event, and the event is divided 50% between two projects, the same €100 will appear for both projects in the project approval view.
At the working community level/settings group level, it is also possible to set that when a project manager approves project hours, the person's entire event is approved, even if the project manager does not otherwise have the right to approve events and is not a supervisor. The setting can be found in the menu **Worktime > Administration > Working community / setting group settings > Work hours > Event locking and approval**.
![](https://support.nepton.com/hc/article_attachments/36253659729949)
## Additional permissions with worktime role
The project manager can also be given additional rights through worktime roles. The worktime role rights include project-related rights at all levels. The lower-level permissions include the ability to view projects:
![](https://support.nepton.com/hc/article_attachments/36253826510365)
This permission grants the right to view (not edit) the entire project list and the details of each project (name, code, notes, dates, etc.). This does not affect the recording of project time for events.
The following permissions are found in the medium-level permissions:
![](https://support.nepton.com/hc/article_attachments/36253809904157)
Separate permission to take out the EU/ELY Centre project report.
Possibility to create new projects when recording work hours with a barcode scanner on a terminal.
Possibility to report sick and absence hours for the project you manage, even if you would not otherwise see them.
Among the higher-level rights, the rights related to projects are:
![](https://support.nepton.com/hc/article_attachments/36253826514333)
The first gives the right to add, edit and delete projects from project management, as well as add project managers to projects.
The next gives the right to report on events recorded for projects of all persons.
The project manager cannot add projects to persons unless he has been separately assigned the worktime role permission ''Can manage people's settings and projects''. This worktime role permission gives the right to edit other persons' settings at the Person level, so the use of this setting should be carefully considered before assigning it to the project manager.
A person can have multiple worktime roles simultaneously. Instructions on how to set a worktime role for a person can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002553397>).
