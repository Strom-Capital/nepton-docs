---
id: 360002554338
title: Worktime roles
url: https://support.nepton.com/hc/en-gb/articles/360002554338-Worktime-roles
locale: en-gb
category: Support
category_id: 360000446658
section: Permissions
section_id: 360000705217
section_path:
- Permissions
labels:
- NEPTONNEEDSREVIEW
- käyttäjäroolit
- katseluoikeudet
- työajan rooli
- lisäoikeus
- lisäoikeudet
- käyttöoikeus
- käyttöoikeudet
promoted: false
updated_at: '2026-11-13T13:57:01Z'
edited_at: '2026-11-13T13:57:01Z'
---

# Worktime roles

Person's worktime role gives permissions to see and edit information in the Work time section.
There is another role for viewing and editing person's information, as well as shift planning. More on this topic in [roles](<https://support.nepton.com/hc/en-gb/articles/360002425637>).
From service point of view, **admin user** has Administrator as role and All permissions as Worktime role.
In general, employees have narrower permissions than supervisors. Administrators have the most extensive permissions. There are few existing worktime roles in the service by default, but worktime roles can also be modified or completely new ones created. A person can have more than one worktime role at the same time.
Worktime roles can be viewed and edited in **Worktime > Administration > Worktime roles**.  
![](https://support.nepton.com/hc/article_attachments/19334264959901)
Choose the worktime role you want to edit, then choose "worktime role permissions" as action.
![](https://support.nepton.com/hc/article_attachments/31848137613469)
The worktime roles below can be found in the service by default. There might be other worktime roles established in your environment instead of or in addition to the ones below.
"**Kaikki oikeudet (All permissions)** " grants permission to lower, medium and high level rights.
"**Omien sekä alaisten tietojen muokkausoikeus (Permission to edit own and subordinates' data)** " gives the permission to edit the person's own and subordinate's data. This work time role usually has all the lower-level permissions, most of the medium-level permissions, and at least some of the higher-level permissions.
"**Omien tietojen katseluoikeus, alaisten muokkausoikeus (Permission to view own data, edit data of subordinates** " gives permission to see your own events and modify the events of subordinates. This worktime role can have very limited rights, i.e. people can only report hours using Current Status, mobile or terminal and add comments in the calendar. Or they may have most of the lower level rights and some of the medium-level rights.
## Worktime role permissions
The current permissions of worktime roles can be changed by selecting the desired rights from the list and then clicking Save. New worktime roles can also be created, and their permissions can be customized by selecting the wanted rights from the list. The permissions are divided into three different levels; lower level, medium level and higher level. Permissions can be given to a worktime role either one whole level at a time (by selecting 'All lower level rights' for example), or you can choose a permission to be granted from each level individually. What each permission does is explained in more detail below.
### Lower-level permissions
Title | Description  
---|---  
**Communication** \- The following permissions relate to the **old Communication service** , which is no longer available for new customers. These **do not apply to the new**[**Notifications**](<https://support.nepton.com/hc/en-gb/articles/32259026029213>)**feature**.  
Can read notifications |  Persons with this permission can view notifications from the Communication pages. ![mceclip0.png](https://support.nepton.com/hc/article_attachments/360010983418) _Note: This permission relates to the old Communication service, not the new Notifications feature. The Communication service must be enabled for deployment this permission to have any effect._  
Can create new notifications |  Persons with this permission can create notifications for other persons. _Note: This permission relates to the old Communication service, not the new Notifications feature. The Communication service must be enabled for deployment this permission to have any effect._  
Can edit/delete their own notifications |  Persons with this permission can edit and delete their own notifications once created. _Note: This permission relates to the old Communication service, not the new Notifications feature. The Communication service must be enabled for deployment this permission to have any effect._  
**Work hours**  
Can record own real-time events in the current status page and mobile |  Persons with this permission can use the "Current status" page and mobile pages to record events (i.e. "start work", "stop work" etc.) in real-time. _Note: activity reporting functionality must be enabled for deployment._  
Can review own events |  Persons with this permission can see their own events in the calendar and reports. _Note: activity reporting functionality must be enabled for deployment._  
Can view attachments in own events |  Persons with this permission can view files that have been attached to their own events. _Note: attachment support must be enabled for deployment._  
Can create and edit own event notes | Persons with this permission can create "Notes" events and add notes to other event types.  
Can edit own request message |   
Can define hour to hour for own working events |  Persons with this permission can _set_ their own work events to earn "Hour to hour" time after they have fulfilled their daily/weekly work obligations. ![mceclip4.png](https://support.nepton.com/hc/article_attachments/360010913517) If they are not permitted to _set_ the overtime target, they will still be able to see it. _Note: The overtime targeting options visible to users can be configured in the Worktime settings under Work hours > Accruals and overtime hours. To be able target Hour to hour time to an accrual like Balance, the accrual must be enabled and the corresponding "Visible overtime options" must also be enabled._  
Can set overtime for own working events | Same as above but for overtime pay. Overtime paid to salary, overtime paid to balance etc.  
Can set supplements for own work events |  Persons with this permission are permitted to add supplements to events e.g. lunch coupons, expenses etc. _Note: supplements must be configured in Worktime settings._  
Can view rules for worktime calculation |  Persons with this permission can view their own working hours, permitted work times and expected working times by clicking on the date in the calendar view. ![](https://support.nepton.com/hc/article_attachments/19335290828957)  
**Shifts**  
Can review personal work shifts |  Persons with this permission can view their own planned work shifts. _![mceclip7.png](https://support.nepton.com/hc/article_attachments/360010915577)__Note: Work shift planning must be enabled for deployment._  
Can view work shifts of users in own person group | Same as above but permits to also view planned work shifts from persons in the same Person group.  
**Sick leave**  
Can view own sick leave compensation | Persons with this permission can _view_ (not edit) the Compensation field (e.g. Paid, unpaid) on their own sick leave events.  
Can view own medical certificate | Persons with this permission can _view_ (not edit) the medical certificate field (e.g. Received, not received) on their own sick leave events.  
**Projects**  
Can review projects |  Can persons in this role _view_ (not edit) the full project list and details of each project (name, code, notes, dates etc). This does NOT affect recording of project time against an event. _Note: project functionality must be enabled for deployment._  
### Medium-level permissions
Title | Description  
---|---  
**Communication** \- The following permissions relate to the **old Communication service** , which is no longer available for new customers. These **do not apply to the new**[**Notifications**](<https://support.nepton.com/hc/en-gb/articles/32259026029213>)**feature**.  
Can add/edit/delete notifications |  Persons with this permission can add, edit and delete notifications for _all_ users. _Note: This permission relates to the old Communication service, not the new Notifications feature. The Communication service must be enabled for deployment this permission to have any effect._  
**Work hours**  
Can edit own personal entries | Persons with this permission can edit their own events. Note: there may be more specific permissions that override this permission for certain event types e.g. types that hold sensitive information like sick leave (see below).  
Can edit own event requests | Persons with this permission can add/edit their own event requests.  
Can edit attachments in own events |  Persons with this permission can edit/delete files attached to their own events. _Note: attachment support must be enabled for deployment._  
Can edit own approved events with no end time | If a person's unfinished/open-ended event (e.g. a sick leave when the end date is not known yet) gets approved by a supervisor, persons with this permission can edit the event until it's closed. Note: Editing is not just the end date/time field but whatever their normal event editing permissions allow.  
Can edit projects on own work events with no end time | Allows users to edit project details on their ongoing (open) events. Only works with activities in work category.  
Only works with ongoing activities.  
Project notes are still editable after stopping the activity.  
Can approve personal events | Persons with this permission can approve their own events.   
Gives the right to define compensation for absences (unpaid, reduced salary, paid) when creating or editing an event.  
Can review subordinates entries | Persons with this permission can _view_(not edit) their subordinate's events.  
Can view attachments in subordinates' events | Persons with this permission can  _view_(not edit) their subordinate's event attachments.  
Can edit and approve subordinates entries | Persons with this permission can view, edit, delete and approve subordinates' events. It also grants the permission to edit work day length, work week length, permitted work times and expected work times. The permission gives the right to define compensation for absences (unpaid, reduced salary, paid) of the subordinate's entry. It also gives right to accept event requests made by subordinates.  
Can edit attachments in subordinates' events | Persons with this permission can view, edit and delete their subordinate's event attachments.  
Can view everyone in presence view | Persons with this permission can view all other persons in the presence report (Worktime > Reports).  
Can view everyone in dining reports | Persons with this permission can view all other persons in the dining reports.  
Can edit correction events |  Persons with this permission can create/edit/delete Correction event types intended for adjusting salary compensation. This applies to the person's own Correction events and their subordinates Correction events. _Note: Correction type supplements must be configured in Worktime settings._  
**Work shifts**  
Can review all users' work shifts |  Persons with this permission can view planned work shifts for _all_ persons from the "Work shifts" reporting pages. _Note: Work shift planning must be enabled for deployment._  
**Sick leave**  
Can view subordinates sick leave compensation | Persons with this permission can view the Compensation field (e.g. Paid, unpaid) for their subordinate's sick leave events.  
Can view medical certificates of subordinates | Persons with this permission can view the medical certificate field (e.g. received, not received) for their subordinate's sick leave events.  
Can edit information about own medical certificate | Persons with this permission can edit the Medical certificate field (Received, not received etc.) for their _own_ sick leave events.  
Can edit subordinates medical certificates | Persons with this permission can edit the Medical certificate field (Received, not received etc.) for their _subordinate's_ sick leave events.  
Can edit own sick leave compensation | Persons with this permission can _view and edit_ the Compensation field (e.g. Paid, unpaid) on their _own_ sick leave events.  
Can edit subordinates sick leave compensation | Persons with this permission can _view and edit_ the Compensation field (e.g. Paid, unpaid) on their _subordinate's_ sick leave events.  
Can edit own reason code | Persons with this permission can _view and edit_ the sick leave reason code for their _own_ sick leave events.  
Can edit subordinates reason codes | Persons with this permission can _view and edit_ the sick leave reason code for their _subordinate's_ sick leave events.  
**Projects**  
Can report EU/ELY-centre project hours for managed projects | Persons with this permission can take EU/ELY-centre project report for their managed projects.  
Can create missing projects via terminal barcode reader | Persons with this permission can start an event with an attached project that will be automatically created if it does not already exist, using barcode readers with Nepton Flexim terminals.  
Can report sick leave and absence hours for managed projects | Project manager can report sick leaves and absence hours for managed projects. This option can be ticked active in report options.  
### High-level permissions
Title | Description  
---|---  
**Work hours**  
Can view events of all personnel | Persons with this permission can  _view_ (not edit) the events of _all_ persons in calendars and reports.  
Can view attachments in all events | Persons with this permission can  _view_ attached files in all persons' events.  
Can edit and approve all users events | Persons with this permission can create, edit and approve _all_ persons' events. It also grants the permission to approve event requests and set absence compensation (paid, reduced pay, unpaid). Grants the permission to edit work day length, work week length, permitted work times and expected work times.  
Can edit attachments in all events | Persons with this permission can  _view and_ _edit_ attached files in all persons' events.  
Can lock event dates |  Persons with this permission can lock event/calendar dates. Locked dates won't allow events to be added/edited or deleted unless the person doing the edit also has permission to unlock the dates. For the person to lock their _own_ calendar dates requires the medium level permission "Can approve personal events" (or higher equivalent permission) to also be set. For the person to lock events for other persons, they need permission to review and edit their calendars e.g. using "Can review subordinates entries" (or higher equivalent permission). ![](https://support.nepton.com/hc/article_attachments/19335314109597)  
Can unlock locked dates | Persons with this permission can unlock event/calendar dates that have been locked (for which persons depends on their other permissions, see previous permission for more details).  
Can administer annual leaves and their balances |  Persons with this permission can create/edit/delete events that change annual leave/holiday such as Annual leave earning reset and Annual leave earning change. _Note: To add these event types through the calendar they must also be activated in "Worktime settings > Work hours > Event types"_  
  
Can review all users annual leave reports | Persons with this permission can view all users (regardless of other permissions) in the annual leave reports.  
Can administer balances |  Persons with this permission can create/edit/delete events that change accrual values such as bank, balance etc. This includes all accruals except Annual leave which has a separate permission (see above). _Note: To add these event types through the calendar they must also be activated in "Worktime settings > Work hours > Event types"._  
Can define exceptions to own work obligation | Persons with this permission can change their own work day and work week obligations (lengths).  
Can set exceptions to own permitted work times | Persons with this permission can change their own permitted work times. Working outside of permitted work times is unpaid.  
Can edit all users dining events | Persons with this permission can view and edit the dining events for _all_ users.  
Can edit approved events | Persons with this permission can edit an event once it has been approved. They can only edit approved events from other persons if they have permission to view and edit their events in the first place.  
Can view external identifier of events | Persons with this permission can view external identifier of events.  
Can edit external identifier of events | Persons with this permission can edit external identifier of events.  
Can view salary information of all personnel | If displaying payslips is enabled in the calendar view, persons with this permission can view the payslips for all persons.   
**Shifts**  
Can edit shifts via API | Persons with this permission can create and edit shifts via API.  
**Sick Leave**  
Can view sick leave compensation of all personnel | Persons with this permission can view compensation (paid, unpaid...) of sick leaves for all persons.  
Can view medical certificates of all personnel | Persons with this permission can view medical certificate details (received, not received...) of sick leaves for all persons.  
Can edit sick leave compensation of all personnel | Persons with this permission can edit compensation (paid, unpaid...) of sick leaves for all persons.  
Can edit medical certificates of all personnel | Persons with this permission can edit medical certificate details (received, not received...) of sick leaves for all persons.  
**Projects**  
Can manage projects and project relations | Persons with this permission can add/edit/delete projects in the project administration, as well as add project managers to projects.  
Can report project events for all persons | Persons with this permission can report project events for _all_ persons.  
**Administration**  
Can manage persons' settings and projects | Persons with this permission can edit person settings, projects related to persons, and projects managed by the person.  
Can manage person groups | Persons with this permission can edit person group information, person group settings, persons related to the person group, and projects related to person groups.  
Can manage person setting groups | Persons with this permission can edit worktime setting group information, group settings. Note, also setting group members.  
Can manage Worktime roles | Persons with this permission can manage roles and permissions related to Worktime.**Important: this means that user effectively has all permissions listed on this page as they are able to set their own permissions and permissions of every other user.**  
Can take integration exports | Persons with this permission can use the "Administration > Integration" area to run imports and exports. **Important: this permission effectively grants persons ability to export and import data of any person(s).**
