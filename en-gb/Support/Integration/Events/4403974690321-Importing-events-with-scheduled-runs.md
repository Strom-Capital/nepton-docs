---
id: 4403974690321
title: Importing events with scheduled runs
url: https://support.nepton.com/hc/en-gb/articles/4403974690321-Importing-events-with-scheduled-runs
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
updated_at: '2026-01-19T05:19:27Z'
edited_at: '2025-06-05T11:04:28Z'
---

# Importing events with scheduled runs

Service can be read in files containing events on scheduled runs. The setup of the transfer and import contents are set up in similar manner than importing events using user interface.
With scheduled runs the available columns are a bit different and setup also includes setting up the scheduled transfers. Available column contents are described below. The setup of imported data is done as explained [here](<https://support.nepton.com/hc/en-gb/articles/360002868137>).
In the import settings you will define the event creator, who is used to create the events (look at the settings below). The edits based on the imported file are done with this person's information. When the import file rows are processed they are compared if the specific event is already created by this event creator set in the settings. If the persons events do not contain the event imported in the file it will be added to persons events. Events that are no longer part of the imported events, and are created by event creator, are removed from persons events.
The fill imported must always include all the events for the person and additions and deletions to persons events are performed based on the file. It means for example that a persons event is removed if it has earlier been transferred in the file, but no longer exists in the file. This way the import file always presents the real situation and events in the service are updated to match this. The source system must create the file always, also when it would only include deleted rows, which means an empty file.
If you are importing file in a format that it only included added and deleter rows, look at the instructions about Sympa - formatted import file in [here](<https://support.nepton.com/hc/en-gb/articles/360003736798>).
Import settings define how many days of history the import file contains. This setting allows the sended to not send the full history of the events, but rather only the amount of days into the history that is set in the settings.
Note that if import file has older events than what is set in "Amount of days to rewrite in the past" - setting, import will issue a warning if these events are set for persons that can not be found with the given personnel number.
Nepton reads in the file based on the configured settings. File is moved into archive folder if the folder is set. If archive folder is not set, then file is removed. In case there is an problem with the contents of the file, the file is kept in the original folder.
## Import file columns
The import file columns are described in the article about [importing events via user interface](<https://support.nepton.com/hc/en-gb/articles/360002868137>).
## Automating and scheduling imports
Event imports can be automated to repeat on a daily basis (or other time schedule) providing you have an SFTP server where Nepton can fetch the file from. Information about scheduling can be found [here.](<https://support.nepton.com/hc/en-gb/articles/10510800700573-Scheduling-worktime-import-export-integrations>)
The settings required to configure automated imports are described below. After these settings are done the schedule will run on the next day. The results of the run will be stored into the service log.
Setting name | Description  
---|---  
Person used to create event | The person who is marked as the creator of the imported events. **Note:** For each import, there must be a unique administrator-level user who performs the import. In this way, it can be ensured that if you want to delete imported events, they are only events imported by one user. So, for example, a user "Nepton Import" can be created with administrator-level rights and used only for one scheduled data import by specifying the Nepton Import user here.  
Import file name | You can use this setting in three ways:  

  * Exact filename - only file with given filename is imported
  * Filename with wildcard - imports all files that match given filter, can be for example: event_import*.csv
  * No filename given - all files in import folder will be imported

  
SFTP host address | Address of file server where to fetch the file. The server should be able to accept SFTP connections.  
SFTP username | Username to login to file server.  
Use public key authentication | Public keys can be configured for authentication  
SFTP password | Password to login to file server.  
SFTP relative directory path | The directory path where to find the files to import. This is relative to the default directory which is opened when first connecting to the file server e.g. absences/to-nepton/  
SFTP relative directory path for archiving | Once an import file is processed it is deleted so it doesn't get imported again. We recommend to archive the files by setting the archive folder e.g. absences/to-nepton/processed. Files will then be archived into separate folder for each month.  
Amount of days to rewrite in the past |  The setting determines how many past days are processed. Note: The transaction end date is used to see if it is among the transactions being processed. If there is a previously imported event from the past days that is no longer in the transfer file, it will be marked as deleted. In this way, events that have been imported into Nepton but then deleted from the source system can be deleted. This setting is zero by default if it is not set. The maximum amount is 120 days. Note: It is important that the "Person who is displayed as the creator of events" setting has a user who only creates events via import. So, for example, a user "Nepton Import" can be created that has maintenance rights and is only used for scheduled data import.  
Approve events on import | If "Yes" is selected, transactions will be accepted during import.  
When times not provided, use the default begin and end times |  If the selection is "Yes" and the event does not have a start or end time and the day does not have planned work shifts or expected work times, the default times set in the section Work hours > Display settings are used. If the selection is not given or the selection is "No" and the event does not have a start or end time and the day does not have planned work shifts or expected work times, the start time is 00:00 and the end time is 24:00.  
Import period rule #n |  These rules define on which _days_ the import is run. e.g.
  * _now_ = Triggers the import to run every day
  * _Monday_ = Triggers the import to run every Monday
  * _12 day_ = Triggers the import to run on the 12th day of every month
  * _second Wednesday of this month_ = Triggers the import to run on every second Wednesday of the month

Rules to trigger the import at specific _times_ are not supported and imports are processed during the morning (usually between 3am to 12pm).  
Date format |  Date format in the import file for fields that indicate a date. The default format is _Y-m-d_(for example 2021-08-04). [The format is defined in the same way as with PHP date function.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Time format |  Time format in the import file for fields that indicate a time. Default format is _H:i:s_ (for example. 15:30:00). [The format is defined in the same way as with PHP date function.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Date and time format |  Date and time format in the import file for fields that indicate date and time. Default format is _Y-m-d H:i:s_ (for example. 2021-08-25 15:30:00). [The format is defined in the same way as with PHP date function.](<https://www.php.net/manual/en/function.date.php#refsect1-function.date-parameters>)  
Character set |  Character set of the file, default is `UTF-8`. The following character sets are supported:
  * `UCS-4`
  * `UCS-4BE`
  * `UCS-4LE`
  * `UCS-2`
  * `UCS-2BE`
  * `UCS-2LE`
  * `UTF-32`
  * `UTF-32BE`
  * `UTF-32LE`
  * `UTF-16`
  * `UTF-16BE`
  * `UTF-16LE`
  * `UTF-8`
  * `UTF-7`
  * `UTF7-IMAP`
  * `ASCII`
  * `EUC-JP`
  * `SJIS`
  * `eucJP-win`
  * `EUC-JP-2004`
  * `SJIS-win`
  * `SJIS-Mobile#DOCOMO`
  * `SJIS-Mobile#KDDI`
  * `SJIS-Mobile#SOFTBANK`
  * `SJIS-mac`
  * `SJIS-2004`
  * `UTF-8-Mobile#DOCOMO`
  * `UTF-8-Mobile#KDDI-A`
  * `UTF-8-Mobile#KDDI-B`
  * `UTF-8-Mobile#SOFTBANK`
  * `CP932`
  * `CP51932`
  * `JIS`
  * `ISO-2022-JP`
  * `ISO-2022-JP-MS`
  * `GB18030`
  * `Windows-1252`
  * `Windows-1254`
  * `ISO-8859-1`
  * `ISO-8859-2`
  * `ISO-8859-3`
  * `ISO-8859-4`
  * `ISO-8859-5`
  * `ISO-8859-6`
  * `ISO-8859-7`
  * `ISO-8859-8`
  * `ISO-8859-9`
  * `ISO-8859-10`
  * `ISO-8859-13`
  * `ISO-8859-14`
  * `ISO-8859-15`
  * `ISO-8859-16`
  * `EUC-CN`
  * `CP936`
  * `HZ`
  * `EUC-TW`
  * `BIG-5`
  * `CP950`
  * `EUC-KR`
  * `UHC`
  * `ISO-2022-KR`
  * `Windows-1251`
  * `CP866`
  * `KOI8-R`
  * `KOI8-U`
  * `ArmSCII-8`
  * `CP850`
  * `JIS-ms`
  * `ISO-2022-JP-2004`
  * `ISO-2022-JP-MOBILE#KDDI`
  * `CP50220`
  * `CP50220raw`
  * `CP50221`
  * `CP50222`

  
CSV delimiter |  What character is used as a delimiter. Default value is `;` If comma is used as a delimiter, the following value should be used: `,`  
CSV enclosure |  What character is used as an enclosure. Default value is `"`  
  
If a column is enclosed in the following way, _"Tässä, on; esimerkki"_ , it would be interpreted as one column when CSV enclosure has been set to be `"`  
Skip rows with unknown person |  If the value is yes, lines with an unknown person will be skipped instead of marking the import as failed.  
Personnel numbers to skip |  Comma separated list of personnel numbers of persons that you want to skip in import. For example setting this to be "1234,5678,1995" means that events won't be imported for persons with personnel numbers 1234, 5678 or 1995.  
Event type codes to skip |  Comma separated list of event type codes that you want to skip in import. For example setting this to be "1234,5678,1995" means that event types with codes 1234, 5678 or 1995 won't be imported.  
Column order relevant to integration |  Yes/No. If import file contains a header row for columns, set this to be "No" as columns are detected from header row. If import file does not contain a header row, set this to be "Yes"  
if import file contains header, then set **The order of the columns matters** to value **No**. In this case each column name must match the column title defined in the settings. For eg: 
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4410731516945)
If import file does not contain header then set **The order of the columns matters** to value **Yes** then the file column order must match the setting created. For eg:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4410724962577)
Notes about import columns:
![](https://support.nepton.com/hc/article_attachments/27916326960541) | 
  * Event type ID = old way to refer to an event type, do not use in new implementations
  * Event type internal name = old way to refer to an event type, do not use in new implementations
  * **Customer defined event type code** = use this column in event imports to indicate the event type being imported (sick leave, year leave, etc.)
  * Absence type ID = old way to refer to an absence type, do not use in new implementations
  * Absence or sick leave paid until date/time and paid after date/time = columns can only be assigned a value for absence events that allow changing the compensation type

  
---|---
