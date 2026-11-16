---
id: 28022676814109
title: SD Worx difference data
url: https://support.nepton.com/hc/en-gb/articles/28022676814109-SD-Worx-difference-data
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels: []
promoted: false
updated_at: '2026-08-21T09:27:47Z'
edited_at: '2026-08-21T09:27:46Z'
---

# SD Worx difference data

SD Worx (Difference) integration can be taken into use if SD Worx (salary data) is also in use.
SD Worx (Difference) integration makes sure that any changes to past payment periods are exported to salary system. When a change to a past payment period is done in Nepton, it moves to the buffer in real time. Changes made to current or future payment periods are not added to the export buffer in real time, they must be exported either manually or automatically using an integration schedule. When a change is made to a past payment period, the difference between the event before the edit and after the edit, is added to the export buffer.
## Good to know
  * Employees with employee number 0 are not included in the data.
  * An event can be recorded in a past payment period even if there are problems with the integration. For example, an incorrect integration rule or a problem with the SFTP server will not prevent the event from being recorded. The user will be warned about the error.
  * It is possible to define multiple rule sets for an integration. If multiple rule sets are defined, recording an event may take slightly longer.


## Settings
### Payment groups
See [Payment groups](<https://support.nepton.com/hc/en-gb/articles/4406602996625>) for general instructions on how to add and configure payment groups.
A payment group must be configured with payment periods and each payment period must have an approval deadline. When the approval deadline has passed, the payment period is in the past, and any edits made to events within that period will be sent to the export buffer in real time as the difference between the events before the change and after the change.
### Integration settings
**1\. Defining persons' IDs**
Persons' IDs can be defined in **Employees > Person's information > Identifiers**.
![sdworx-integration-id.png](https://support.nepton.com/hc/article_attachments/28022676809373)
If the person's SD Worx ID has not been set, the employee number will be used.
**2\. Adding a target server**
If there is no target server for the integration yet, add it in the Working Community settings under **Integrations > Target servers**. See [Target servers for work time exports](<https://support.nepton.com/hc/en-gb/articles/26861716054045>) for general instructions on how to add a target server and set the SFTP settings.
SFTP settings for the target server must specify at least the SFTP server address, SFTP username, and SFTP password (or public key authentication).
**3\. Integration settings**
In order to enable the integration, a rule set must be defined to generate the data. In the export options, select SD Worx (Difference) as the export format. SD Worx (Difference) must have it's own separate rule set.![sdworx-integration-ruleset-format.png](https://support.nepton.com/hc/article_attachments/28022676810653)
Select the target server for the integration, that you added in step 2.
![sdworx-integration-ruleset-target-server.png](https://support.nepton.com/hc/article_attachments/28022672556829)
The exact timestamp _[timestamp-ms]_ must be added to the export file name, like in the example below. If a timestamp is not used, each file will have the same name and they will overwrite each other.
![](https://support.nepton.com/hc/article_attachments/28022676812061)
**4\. Export scheduling to the target server**
Finally, you need to set the export schedule for the target server buffer. You can read more about this in the article [Target servers for worktime exports](<https://support.nepton.com/hc/en-gb/articles/26861716054045#h_01JSK5VK4NMRKM5R7TP1B6ATE1>).
## File format
The transfer file is ISO-8859-1 formatted text data separated by semicolons (`;`). The line feed is `LF`. There is one blank line at the end of the transfer file.
## Export data fields
Column | Field | Ruleset field name | Format | Description  
---|---|---|---|---  
A | Business ID | _Automatically added_ | string | Business ID. Can be overridden in a rule set with field `SDWorxDifferenceBusinessId`.  
B | Employee number | _Automatically added_ | string | Person's SD Worx ID / employee number.  
C | Payment group code | _Automatically added_ | string | Payment group code. Can be overridden in a rule set with field `SDWorxDifferencePaymentGroupCode`.  
D | Work contract start date | _Automatically added_ | string | Work contract start date, in format `DD.MM.YYYY`. Can be overridden in a rule set with field `SDWorxDifferenceWorkRelationshipStartDate`.  
E | Salary code | SalaryCode | string | Can be overridden in a rule set with field `OverrideSalaryCode`  
F | Amount, hours | "Amount" field if UnitType is 'H' or 'S', otherwise empty | decimal | Amount of hours with accuracy of 2 decimals. , as decimal separator. This field contains information if field is output as hours.  
G | Amount, days | "Amount" field if UnitType is 'J', otherwise empty | decimal | Amount of days with accuracy of 2 decimals. , as decimal separator. This field contains information if field is output as days.  
H | Amount, decimal / units | "Amount" field if UnitType is 'U' or 'D', otherwise empty | decimal | Amount with accuracy of 2 decimals. , as decimal separator. This field contains information if field is output as decimal or units.  
I | Start date | StartDateTime | string | Format DD.MM.YYYY  
J | End date | EndDateTime | string | Format DD.MM.YYYY  
K | Amount, currency | "Amount" field if UnitType is 'C', otherwise empty | decimal | Amount of currency with accuracy of 2 decimals. , as decimal separator. This field contains information if field is outputted as currency.  
The data below shows an example of exporting an 8-hour work event excluding lunch
[code]
    1234567-1;219354;10;01.01.2025;1000;3,50;;;02.06.2025;05.06.2025;  
    1234567-1;219354;10;01.01.2025;1000;4,00;;;05.06.2025;05.06.2025;
[/code]
## Problem situations
### Setting changes
It is not recommended to make settings changes that affect the payroll data afterwards. For example, changing the length of the working day in the calendar view can also change the amount paid. When making such changes, the integration is not run and any previously imported information about the event will remain in SD Worx. In such a situation, the following should be done:
  * Delete the event from Nepton. This will send a file containing the difference which should be deleted.
  * Delete all the data for the event in SD Worx. There may be multiple rows depending on rule set configuration.
  * Add the event again.
