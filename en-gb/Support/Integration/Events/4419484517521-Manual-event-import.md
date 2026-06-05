---
id: 4419484517521
title: Manual event import
url: https://support.nepton.com/hc/en-gb/articles/4419484517521-Manual-event-import
locale: en-gb
category: Support
category_id: 360000446658
section: Events
section_id: 360001061298
section_path:
- Integration
- Events
labels: []
promoted: false
updated_at: '2025-07-14T11:23:01Z'
edited_at: '2025-07-14T11:23:01Z'
---

# Manual event import

When importing work shifts, you should use scheduled event import or manual event import. You can read more about it [here](<https://support.nepton.com/hc/en-gb/articles/4403974690321>).
It is easy to import events into the service manually from Excel tables or other systems. There are two ways to import events, [Import Events from the Tools menu](<https://support.nepton.com/hc/en-gb/articles/360002868137>) or **Event Import #1-3** from the Integration menu. This article reviews the integration menu's event import functionality and the settings required for it. Attached at the end of the article is an example file for importing events.
Settings for importing events are made in the menu **Worktime - > Administration -> Working community settings -> Integrations -> Event import #1, #2, #3, #4 ... **. The settings for importing events must be done before downloading the first data from the UI (User Interface) or before the first scheduled download of the data. Manual import of events via the Integration menu requires the same settings as a scheduled download. In scheduled download, in addition to what is below, additional transfer settings must be defined. You can read about additional settings [here](<https://support.nepton.com/hc/en-gb/articles/4403974690321>).
In the data settings, you define how many days into the history the rows of the data are processed. These lines are processed in such a way that the material forms the events in the service that are not in the person's calendar. Events that have been removed from the data to be transferred are removed from the person's calendar. In this way, the absences presented in the calendar always contain the same information as in the transferred material. The source system must form the data to be transferred even when only deleted rows are to be forwarded in the data. Please note that in the settings for each event import, a separate person must be specified to be shown as the event importer. Learn more about who is shown as the event creator [here](<https://support.nepton.com/hc/en-gb/articles/4403974690321>).
# Data import steps
## Configure event import settings
The following information should be configured in the event import settings. **Worktime - > Administration -> Working community settings -> Integrations -> Event import #1-3**.
  * **Description**. In this field, informative text information is given about how the event import settings have been configured.


![mceclip1.png](https://support.nepton.com/hc/article_attachments/8936472780701)
  * **The person** who is shown as the event creator when importing events. If events have been previously imported as a user, e.g. Import User, and then a different user imports events from the same material, the events will be added to calendar as duplicates. Default is 'No one' and in that case currently logged in user is used.


![mceclip2.png](https://support.nepton.com/hc/article_attachments/8936490313117)
  * **Amount of days to rewrite in the past**. In this field, it is defined how long the period of time there are events in the data. If the setting is defined, importing events can also delete events. All those events within the defined time window are deleted, which are not in the material and are recorded by the person 'event creator'.


![mceclip3.png](https://support.nepton.com/hc/article_attachments/8936532440093)
  * **Approve events on import**. If the setting is turned on, the event creator set for the event is set as the event approver.


![mceclip4.png](https://support.nepton.com/hc/article_attachments/8936538152221)
  * Codes of event types added in the service. When importing events, the event type is created according to the code imported in the data. The event type codes are set by selecting **Worktime - > Administration -> Working community settings -> Integrations -> Event import #1-3**.**  
**


![mceclip6.png](https://support.nepton.com/hc/article_attachments/8938803779613)
For example, if the codes are set according to the example above and the event type code is set to "4" in the import file, the event will be imported as annual leave.
If several codes are needed to create the same event type, the codes can be sent separated by a comma, e.g. 1, 4. If a comma is needed in the code itself, it should be surrounded by apostrophes, e.g. "1,2".
Note that the validity control does not apply to codes used in event imports. For example, if code 4 is used for annual leave, the code 4 cannot be used to import any other event type in the past. All events imported with the code 4 are inserted into the calendar as annual leave.
  * If the import file contains a header row for columns, set Column order relevant to integration to No.   



![mceclip8.png](https://support.nepton.com/hc/article_attachments/8939262134941)
In this case, the name of each column header in the file must match the column header and field definition in the settings. For example:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/6452143067037)
  * If the import data does not contain column headers, set Column order relevant to integration to Yes.


![mceclip7.png](https://support.nepton.com/hc/article_attachments/8939078052381)
Select the column header field in the order in which the columns appear in the file. For example:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/6452158536733)
## Create the data with the right columns and contents
![mceclip0.png](https://support.nepton.com/hc/article_attachments/11614604061085)
## Data contents of integration
The following information contents can be imported to the event. When importing the data, you can choose column-by-column which data content the column contains. For this reason, the column header in the file does not have to match the header of the data content to be imported, and the header row is not mandatory. Below is a description of the different data contents and in what form the data should be in the column. The data must contain the information marked as mandatory.
Imported content | Description  
---|---  
Employee number | **Mandatory information.  
**  
Social security number | Social security number of the person related to events.  
Event type ID |  _Not recommended to use_. Information is not available for every event type.  
Event type internal name |  _Not recommended to use_. Information is not available for every event type.  
Customer defined event type code |  Mandatory information. The event type codes used in the import are set by choosing Worktime -> Administration -> Working community settings -> Integrations -> Event import #1 (or other event import if several are used) -> Event type codes.  ![mceclip6.png](https://support.nepton.com/hc/article_attachments/8938803779613) For example, if codes are set according to the example above and event type code is set to "4" in import file, event will be imported as annual leave. If several codes are needed to create the same event type, the codes can be sent separated by a comma, e.g. 1, 4. If a comma is needed in the code itself, it should be surrounded by apostrophes, e.g. "1,2".  
Absence type ID |  If an absence is created, the code of the absence type is defined in this field. Absence type codes are defined in the work community settings Integrations -> Event import #1 (or other event import, if several are used) -> Absence type codes.  
Start date and time / End date and time |  Event start/end date and time, for example. 2020-01-01 13:00:00. The times are processed in the user's local time and displayed as imported.  
Start date and time UTC /  
End date and time UTC |  Event start/end date and time, for example. 2020-01-01 13:00:00. The times are processed during the UTC time zone and converted to the Helsinki time zone.  
Start date / End date |  Event start/end date 2020-01-01 or 01.01.2020.  
Start time / End time |  Event start/end clock time in 24-hour format, for example 16:00:00, 16:00 or 1600. Times are processed in the user's local time and displayed as imported.  
Duration |  Event duration in decimals or HH:MM format, for example 4.5, 4,5 and 04:30 are all valid formats.  
Description | Description.  
External identifier |  The external identifier of the event. If an already existing event is found with the external identifier, the event information is updated. Note! The external identifier is intended to be set by the integration user when the event is imported from an external system.  
Project code #n | In connection with the import, 6 projects can be exported per transaction using different columns First project code, second project code, etc. Project codes are defined in project management. If no project is defined for the transaction, the target person's default project is used.  
Supplement #_n_ | Supplements can be attached to the event using the Supplement codes (1 Supplement per column), which are set in the Supplement settings. In connection with the import, the value of how much Supplement is to be recorded for the event is entered, e.g. 1h/pc/€, depending on the determination of the type of Supplement.  
Setting the accrual value (hours in decimals) |  Sets the accrual value, the value is given in hours as decimals. The event type must be the setting of an accrual value.  
Accrual value setting (HH:MM) |  Sets the accrual value, the value is given in HH:MM format. The event type must be the setting of an accrual value.  
Setting the accrual value (days) | Sets the accrual value, the value is given in days. The event type must be the setting of an accrual value.  
Change in accrual value (+hours in decimals) | Increases or decreases the value of the accumulation, the change is given in hours as decimals. The event type must be a change in the value of an accumulation.  
Change in accrual value (+HH:MM) | Increase or decrease the value of the accrual, the change is given in HH:MM format. The event type must be a change in the value of an accrual.  
Change in accrual value (+days) | Increase or decrease the value of the accrual, the change is given in days. The event type must be a change in the value of an accrual.  
Absence or sick leave paid until date/time |  Creates the event as two separate events:
  * The first one starts at event start time specified in the row and ends at absence / sick leave paid until date/time specified in the row. The event is created as a paid event.
  * The second one starts at absence / sick leave paid until date/time specified in the row and ends at event end time specified in the row. The event is created as an unpaid event.

The information can only be specified for sick leave and leave that allow changing the compensation type.  
Absence or sick leave paid after date/time |  Creates the event as two separate events:
  * The first one starts at event start time specified in the row and ends at absence / sick leave paid after date/time specified in the row. The event is created as an unpaid event.
  * The second one starts at absence / sick leave paid after date/time specified in the row and ends at event end time specified in the row. The event is created as a paid event.

The information can only be specified for sick leave and leave that allow changing the compensation type.  
## Import events
To import events, select **Worktime - > Administration -> Integrations -> Event import #1-3**.  
Note! When using manual import, you must login to Nepton with the same user as in scheduled import. Importing data with other user than import user could result in events disappearing from the current user's calendar.
![](https://support.nepton.com/hc/article_attachments/16005715362077)
  * Select a file from your device -> **Run**.
