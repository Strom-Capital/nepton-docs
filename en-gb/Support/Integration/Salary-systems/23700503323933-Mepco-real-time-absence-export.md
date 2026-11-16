---
id: 23700503323933
title: Mepco real time absence export
url: https://support.nepton.com/hc/en-gb/articles/23700503323933-Mepco-real-time-absence-export
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
updated_at: '2026-07-01T06:52:45Z'
edited_at: '2026-07-01T06:52:44Z'
---

# Mepco real time absence export

With the Mepco Absence Export integration, absences are added to the export buffer in real time as they are recorded in Nepton. The data in the buffer is transferred to Mepco at selected intervals. The integration uses Mepco's deletion and addition entries ("P" and "U"). When editing an absence, both will be sent.
## Good to know
  * Employees with employee number 0 are not included in the data.
  * The integration only handles absences. Please note this when creating integration rulesets. For example, work events are not processed, but an event type that has the behavior of "absence" is included (i.e. the integration handles events with activitytypecategoryid = '2').
  * If an absence is started in the calendar without an end time, the integration will not process it. The integration will process the absence event when it is ended with a specified end time.
  * When recording an absence, only that event is processed and exported to the SFTP server. Other events from the same day are not included in the data.
  * An absence is only transferred if it is new, deleted, or has been changed in a way that affects the information being transferred. Check the export file data below to see which information is being transferred. For example, adding a comment to an absence event does not create new data.
  * **If only approved events are to be moved, you must add isApproved = 'Y' to the integration rule.**  

  * An absence can be recorded even if there are problems with the integration. For example, an incorrect integration rule or a problem with the SFTP server will not prevent the absence from being recorded. The user will be warned about the error.
  * For each absence event and rule set, a separate file is created and transferred to the SFTP server. If the same absence event forms data in two different rule sets, two different files are created.
  * A deleted absence or a previous version of a modified absence is marked with a "P" in the data.
  * A new event or the latest version of a modified absence event is created with "U" in the data.
  * Editing an absence creates two lines. The first line contains the version of the absence before editing with the tag “P”. The second line contains the updated version of the absence with the tag “U”. The first and second lines are created in separate files.
  * It is possible to define multiple rule sets for an integration. If multiple rule sets are defined, recording an event may take slightly longer.  
If absences are deleted from a person's calendar via mass actions, the deleted rows are created in a single file, even if there are multiple absence events. When copying absence events, a separate file is created for each event.


## Settings
**1\. Defining persons' IDs**
Persons' IDs can be defined in **Employees > Person's information > Identifiers**.
![](https://support.nepton.com/hc/article_attachments/27239544683421)
If the person's Mepco ID has not been set, employee number will be used.
**2\. Adding a target server**
If there is no target server for the integration yet, add it in the Working Community settings under **Integrations > Target servers**. See [Target servers for work time exports](<https://support.nepton.com/hc/en-gb/articles/26861716054045>) for general instructions on how to add a target server and set the SFTP settings.
SFTP settings for the target server must specify at least the SFTP server address, SFTP username, and SFTP password (or public key authentication).
**3\. Integration settings**
In order to enable the integration, a rule set must be defined to generate the absence data. In the export options, select Accountor Mepco HRM (Absence or Annual leave) as the export format.![](https://support.nepton.com/hc/article_attachments/27239590003101)
Select the target server for the integration, that you added in step 2.
![](https://support.nepton.com/hc/article_attachments/27239544684701)
The exact timestamp _[timestamp-ms]_ must be added to the export file name, like in the example below. If a timestamp is not used, each file will have the same name and they will overwrite each other.
![](https://support.nepton.com/hc/article_attachments/27239590004125)
In **Worktime > Administration > Working community settings > Integrations > Accountor Mepco HRM** you can find general settings for what's included in the export data, with further instructions [here](<https://support.nepton.com/hc/en-gb/articles/360003473498-Mepco-Salary-data>). 
![](https://support.nepton.com/hc/article_attachments/27240087000349)
**4\. Export options**
In the Integration ruleset section, the rules for the data to be extracted are defined. Below the integration rules is the Export options section.
The settings under Export file splitting are usually not used in real-time export, as the file is split into parts depending on how the data is grouped when it is transferred from the buffer to the server. Absences recorded in Nepton are transferred to the buffer in real time according to the rule set. When absences are transferred from the buffer to the server according to a schedule, files are created according to the file name, for example, with the file name “absences_[yyyyymmdd].csv” one file would be created on the server, containing all absences transferred to the buffer on that day. If, on the other hand, the file name was “absences_[timestamp-ms].csv”, each absence would be created in the buffer as its own file, because the timestamps are based on milliseconds.
If, in addition to the timestamp-based file splitting, you also want to use the settings in the “export file splitting” section, it is possible to specify that the file is split based on other basis, for example, payment group information.
It should be noted that each individual real-time transfer extracts a very small amount of data. With most grouping criteria, this small amount of data is no longer divided into smaller parts, but the transfer still consists of only one file. However, the specified grouping criterion (e.g. payment group) would be appended to the file name. This definition would also be retrieved for manually initiated transfers, which would likely result in multiple files due to the larger amount of data.  
![](https://support.nepton.com/hc/article_attachments/37273294592157)
**5\. Export scheduling to the target server**
Finally, you need to set the export schedule for the target server buffer. You can read more about this in the article [Target servers for worktime exports](<https://support.nepton.com/hc/en-gb/articles/26861716054045#h_01JSK5VK4NMRKM5R7TP1B6ATE1>).
## File format
The transfer file is UTF-8 formatted text data separated by semicolons (`;`) . There is no maximum length for the fields. in order for Mepco to receive the data, the same columns and settings are defined in Mepco. 
The data transfer can also be done with just one project target.
## Export data fields
Column | Field | Ruleset field name | Format | Description  
---|---|---|---|---  
A | Employee number | _Automatically added, not replacable_ | string | Person's Mepco ID / employee number.  
B | Absence start date | StartDateTime | date | The start date of the absence.  
C | Absence end date | EndDateTime | date | The end date of the absence.  
D | Person's name | _Automatically added, not replacable_ | string | Person's last and first names.  
E | Project code 1 | ProjectCode1 | string | Can be overridden in a rule set with field `OverrideProjectCode1`  
F | Project code 2 | ProjectCode2 | string | Can be overridden in a rule set with field `OverrideProjectCode2`  
G | Project code 3 | ProjectCode3 | string | Can be overridden in a rule set with field `OverrideProjectCode3`  
H | Project code 4 | ProjectCode4 | string | Can be overridden in a rule set with field `OverrideProjectCode4`  
I | Project code 5 | ProjectCode5 | string | Can be overridden in a rule set with field `OverrideProjectCode5`  
J | Salary code | SalaryCode | string | Can be overridden in a rule set with field `OverrideSalaryCode`  
K | Amount | Amount | decimal | The length of the absence, can be in hours or days. The decimal separator is a period (`.`).  
L | Row type | _Automatically added, not replacable_ | string |  Defines, whether the data is to be deleted or added in Mepco. Deletion: `P` Addition: `U`  
The data below shows a modified absence. A 6-hour absence has been modified to 8 hours. A deletion line ("P") is created from the previous version and an addition line ("U") is created from the new version.
[code]
    1918;2024-12-12;2024-12-12;Meikäläinen Matti;1001;;;;;123;6.00;P
    1918;2024-12-12;2024-12-12;Meikäläinen Matti;1001;;;;;123;8.00;U
[/code]
## Performing integration when recording an event
In the example below, an absence has been copied for five days in the calendar view.
![](https://support.nepton.com/hc/article_attachments/25944857514013)
When saving, each event creates its own file on the SFTP server, containing the data generated by the rule set. Please note that it is important to specify an exact timestamp [timestamp-ms] in the event name so that the files do not overwrite each other.
![](https://support.nepton.com/hc/article_attachments/25944857515805)
## Performing integration manually
The integration can be performed manually in**Worktime > Administration > Integrations > Accountor Mepco HRM absence export**. This may be necessary, for example, when you want to completely rerun or delete data for a certain period. 
Row and file type can be selected from the Context dropdown. For example, option "Deleted" creates deletion file with "P" rows.
The example below uses a previously created rule set "Populus absences". The integration rule is mandatory.![](https://support.nepton.com/hc/article_attachments/27239544686493)
## Overriding row type in integration rule
Sometimes it may be necessary to skip the generation of "P" or "U" rows when processing certain types of absences. To do this, three different variables can be used in the integration rule:
  1. :integrationContext - context, in which the integration is being executed ("P" or "U")
  2. :integrationContextForDeletedOrEditedActivities - Generation of row "P"
  3. :integrationContextForNewActivities - Generation of row "U"


The example below describes in a simplified way how only the addition markings "U" are created for paternity leave, but the deletion marking "P" is not created in connection with deletion or editing.
[code]
    SELECT *, SUM(Amount) AS OverrideAmount, 
    MIN(SalaryRenderingDate) As OverrideStartDatetime, 
    MAX(SalaryRenderingDate) AS OverrideEndDatetime,
    CASE 
    WHEN AbsenceTypeId = 11 THEN 'KERTAUS' -- Kertausharjoitukset
    WHEN AbsenceTypeId = 3 THEN 'ISYYSVAPAA' -- Isyysvapaa
    ELSE
    'MUU VAPAA'
    END AS OverrideSalaryCode
    FROM UserSalaryData 
    WHERE CompensationType = 'BasicTime'
    AND 
    AbsenceTypeId IS NOT NULL 
    AND 
    (AbsenceTypeId != 3 OR :integrationContext != :integrationContextForDeletedOrEditedActivities) -- Lähetä ainostaan U-rivit isyysvapaalle
    AND isApproved = 'Y' -- Lähetä ainoastaan hyväksytyt tapahtumat
    GROUP BY ActivityId
[/code]
When a new paternity leave is added to the calendar, a file that includes the paternity leave with the addition mark "U" is created. If the paternity leave is edited, new file is created with the addition mark "U", but the previous version of the absence is not created with the deletion mark "P". If the paternity leave is deleted completely, no file is created.
If any other absence is added to the calendar, it will be processed according to the normal operating procedure of the integration.
## Partial and current day sick leaves rule condition
When a sick leave for the current day or part of a day is recorded, two separate basictime rows are created in the database table, one of which contains the information "istimeborrowedfrombalance = 'Y'" and "isapproved = 'Y'". This causes a situation where an unapproved sick leave is unnecessarily transferred to the export buffer and further to Mepco. This situation can arise for part-day sick leaves as well as sick leaves that are recorded for the current day.
For this reason, the condition istimeborrowedfrombalance = 'N' should be added to the rule so that sick leaves for the current day or part of a day are not transferred prematurely and unnecessarily before they are approved.
## Problem situations
### Adding and deleting absences from Mepco
If you want to delete a larger number of absences entered in Mepco at once during a certain period, you can do so by performing a manual integration. Manual integration can also be used in the same way to add absences.
### Setting changes
It is not recommended to make settings changes that affect the payroll data afterwards. For example, changing the length of the working day in the calendar view can also change the paid absence days. When making such changes, the integration is not run and any previously imported information about the absences will remain in Mepco. In such a situation, the following should be done:
  * Delete the previously created absence in Mepco.
  * Delete the current absence from Nepton. This will send a "P" line, which has no equivalent in Mepco.
  * Add the absence again. This will create a "U" line, forming the data using the current settings.
