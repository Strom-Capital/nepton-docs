---
id: 360002868137
title: Importing events via the file upload interface
url: https://support.nepton.com/hc/en-gb/articles/360002868137-Importing-events-via-the-file-upload-interface
locale: en-gb
category: Support
category_id: 360000446658
section: Events
section_id: 360001061298
section_path:
- Integration
- Events
labels:
- lomat
- vuosiloma
- tapahtumien tuonti
- tapahtumatuonti
- vuosilomaoikeus
- lomaoikeus
- vuosilomasaldo
- lomapäivä
- lomatuonti
- esikatselu
promoted: false
updated_at: '2026-10-16T11:43:45Z'
edited_at: '2026-10-16T11:43:44Z'
---

# Importing events via the file upload interface

This article describes importing events via file upload with a selectable structure during import. There are other ways to import events from the interface, which are described [here](<https://support.nepton.com/hc/fi/articles/4404767615249>).
This article covers the **Import Events function in the Tools menu and the required configurations for it.** At the end of the article, there is an example file attached for importing events.
Event import is done via **Worktime** > **Tools** > **Import Events**. The import settings must be configured before uploading the first file via the interface or via scheduled import.
This import method always uses settings from Event import #1.
## Manual event import (Tools)
### General information about the file
  * Data can be read into the service with or without a header row. The column headers can have any names. The content of the columns is defined in Nepton during the event import process.
  * Events are imported for persons who have a employee number in the service.
  * Each event’s data must be on a single row in the file.
  * If the file contains more than 10,000 rows, it is recommended to split it into several files.
  * If a project is set as mandatory for event recording, the file must include the project information for the event.
  * Format the columns as text in Excel before importing to ensure the data remains correct.
  * The Event Import function allows importing using the following file types: CSV, XLSX, XLS, ODS.


## Steps for importing data (Tools)
### Define event type codes for the events to be imported
With event import, the event type is created according to the code transferred in the file. The code can be any that describes the event to be imported, e.g. for a Balance set event, use code SA. The event type codes (Tapahtumatyyppien koodit) are set by selecting **Worktime > Working community settings > Integrations > Event import #1.**
**NOTE!** The event type code must always be set specifically in the **Event import #1 settings.**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4406377927185)
For example, if the codes are set as in the example above and the import file contains event type code "4", the event will be imported as annual leave (Vuosiloma). The code "3" in the file would be imported to Nepton as weekly rest (Viikkovapaa).
If several codes are needed to create the same event type, the codes can be sent separated by a comma, e.g. 1, 4. If a code itself needs to include a comma, it must be enclosed in quotation marks, e.g. "1,2".
### Create the file with the correct columns and content
An example file is available for download as an Excel file at the end of this guide.
![](https://support.nepton.com/hc/article_attachments/34356002237341)
### Data contents of the transfer file
The following data contents can be imported for an event. During the import, you can select which column contains which data content. For this reason, the column header in the file does not need to match the name of the data content being imported, and a header row is not required. Below are the different data contents and their formats. The file must contain all data marked as mandatory.
Please note that at least one of the three start time data fields must be present in the file. For most event types, the end time is also required in the file.
Data to import | Description  
---|---  
Employee number (Personnel number) | **Mandatory field.**  
Event type code |  **Mandatory field.** The event type codes used for import are set by selecting **Worktime > Working community settings > Integrations** **> Event import** #1 (or another event import if several are in use) **> Event type codes.** This should not be confused with the Event type settings under Working hours. ![mceclip0.png](https://support.nepton.com/hc/article_attachments/4406377927185) For example, if the codes are set as in the example above and the import file contains event type code "4", the event will be imported as annual leave. If several codes are needed to create the same event type, the codes can be sent separated by a comma, e.g. 1, 4. If a code itself needs to include a comma, it must be enclosed in quotation marks, e.g. "1,2".  
Absence type code | If an absence is being created, this field defines the absence type code. Absence type codes are set in the community settings under **Integrations > Event import** **#1** (or another event import if several are in use) **> Absence type codes.**  
Start date and time / End date and time | The event’s start/end date and time, for example 2020-01-01 13:00:00. Times are processed as the user’s local time and displayed as imported.  
Start date and time UTC /   
End date and time UTC | The event’s start/end date and time, for example 2020-01-01 13:00:00. Times are processed in the UTC time zone and converted to the Helsinki time zone.  
Start date / End date | The event’s start/end date, 2020-01-01 or 01.01.2020.  
Start time / End time | The event’s start/end time in 24-hour format, e.g. 16:00:00, 16:00 or 1600. Times are processed as the user’s local time and displayed as imported.  
Description | Description.  
External identifier |  The event’s external identifier. If an existing event is found with this external identifier, the event’s data will be updated. Note! The external identifier is intended to be set by the integration user when the event is imported from an external system.  
Project code #_n_ | Up to 6 projects per event can be imported using different columns: first project code, second project code, etc. Project codes are set in project management. If no project is specified for the event, the default project of the target person is used.  
Work supplement #_n_ | A work supplement can be attached to the event using Work supplement codes (1 work supplement per column), which are set in the Supplements settings. The value of the work supplement is imported for the event, e.g. 1h/pcs/€, depending on the work supplement type settings.  
Set accrual value (hours as decimals) | Sets the accrual value. The value is given in hours as decimals. The event type must be a set accrual value type.  
Set accrual value (HH:MM) | Sets the accrual value. The value is given in HH:MM format. The event type must be a set accrual value type.  
Set accrual value (days) | Sets the accrual value. The value is given in days. The event type must be a set accrual value type.  
Change accrual value (+hours as decimals) | Increases or decreases the accrual value. The change is given in hours as decimals. The event type must be a change accrual value type.  
Change accrual value (+HH:MM) | Increases or decreases the accrual value. The change is given in HH:MM format. The event type must be a change accrual value type.  
Change accrual value (+days) | Increases or decreases the accrual value. The change is given in days. The event type must be a change accrual value type.  
Absence or sick leave paid until date/time |  Creates the event as two separate events, of which
  * The first starts at the event start time specified in the row and ends at the absence/sick leave paid until date/time specified in the row. The event is created as paid.
  * The second starts at the absence/sick leave paid until date/time specified in the row and ends at the event end time specified in the row. The event is created as unpaid.

This field can only be set for sick leaves and absences for which the paid status can be changed.  
Absence or sick leave paid after date/time |  Creates the event as two separate events, of which
  * The first starts at the event start time specified in the row and ends at the absence/sick leave paid after date/time specified in the row. The event is created as unpaid.
  * The second starts at the absence/sick leave paid after date/time specified in the row and ends at the event end time specified in the row. The event is created as paid.

This field can only be set for sick leaves and absences for which the paid status can be changed.  
### Import the events
To import events, select **Worktime > Tools > Import Events.**
![](https://support.nepton.com/hc/article_attachments/34355996380573)
  * Select the **file** from your device.
  * If necessary, select whether the first row is a **header**. By default, this is automatic.


![](https://support.nepton.com/hc/article_attachments/34355996382109)
  * At this stage, you can define whether to **approve the imported events.**


![](https://support.nepton.com/hc/article_attachments/34356002243869)
  * In the **import preview** , define the **data content** for each column. If some columns are unnecessary for the import, you can skip them by selecting **ignore column**. Data in ignored columns will not be imported.


![](https://support.nepton.com/hc/article_attachments/34355996384413)
  * The service checks the file and highlights invalid columns in red. You can see the error description in a column by clicking the invalid column with your mouse.


![](https://support.nepton.com/hc/article_attachments/34355996389021)
  * When no errors are found in the data to be imported, the service will return a message:


![](https://support.nepton.com/hc/article_attachments/34356002246685)
  * The service will notify that the events have been imported.


![](https://support.nepton.com/hc/article_attachments/34355996390429)
## Examples of importing annual leave balances
### Changing annual leave balance (on top of existing annual leave balance)
A change to the currently available annual leave balance for a person is imported to the service for the day from which the change should take effect. The change increases or decreases the annual leave days available to the person. 
![](https://support.nepton.com/hc/article_attachments/34355996391965)
When the file is read into the service, the content for each column is selected from the dropdown menus. Cells are shown in green when the content format matches the selected column. Event import is described earlier in this guide in section 3. 
![](https://support.nepton.com/hc/article_attachments/34356002251677)
The example file contains only one person for clarity. As a result, for the person with employee number (= personnel number) 2, an event is created for Annual leave accrual change on 31/03/2022. This annual leave balance is available from 01/04/2022 onwards, including any previous annual leave balance the person may have had. 
### Setting annual leave balance (replacing the existing annual leave balance)
The annual leave entitlement earned by a person in the previous holiday accrual year should be set for the same holiday accrual year. This way, the person will have these annual leave days available from 1st of April onwards. Leave entitlements can be imported into the service using a file as shown in the example below. 
![](https://support.nepton.com/hc/article_attachments/34356002253469)
When the file is read into the service, the content for each column is selected from the dropdown menus. Cells are shown in green when the content format matches the selected column. Event import is described earlier in this guide in section 3. 
![](https://support.nepton.com/hc/article_attachments/34356002253981)
The example file contains only one person for clarity. As a result, for the person with employee number 2, an event is created for Annual leave accrual set on 31/03/2022. This annual leave balance is available from 01/04/2022 onwards and will replace any previous annual leave balance the person may have had.
