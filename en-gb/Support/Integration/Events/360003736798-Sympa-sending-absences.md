---
id: 360003736798
title: Sympa sending absences
url: https://support.nepton.com/hc/en-gb/articles/360003736798-Sympa-sending-absences
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
updated_at: '2025-08-25T11:20:38Z'
edited_at: '2025-06-03T07:25:04Z'
---

# Sympa sending absences

Absences from Sympa can be imported to the service. A csv-file must be created on the SFTP server. Creation timestamp must be in the file name. Timestamp is added to the end of the file name. This ensures that the previous file will not be overwritten for example when receiving end is not run according the import schedule.
The file is saved in UTF-8 encoding. Records are separated by semicolons (`;`). The line feed character is a UNIX line feed character `LF`. By default, this line break consists of almost all information systems.
The data does not contain a title row. In the data, one absence and its validity periods are presented on one row. The absence file must be generated from Sympa so that only new absences (type uusi) and/or deleted absences (type poisto) that have been created since the last absence import are present on the file as their own rows. The setting "Amount of days to rewrite in the past" has no effect when using Sympa absence import, as all the absences on the file are handled according to their type (poisto/uusi).
Rows in the file are processed in _sequential_ order. For example if the first row inserts a new absence on Jan 1st and then the second row removes an absence on Jan 1st, then it will remove the absence it had just created. For this reason, if the import data is spread across multiple files you should ensure that users don't exist in multiple files at the same time, or if they do, that those files are in the correct order (we process the files from the SFTP server in the _chronological_ order they were created in).
## Configuration
**1\. Setting person identifiers**
Person's identifier can be set by editing person's employee number in **Employees** \- **Person's information** \- **Identifiers**
![mceclip0.png](https://support.nepton.com/hc/article_attachments/22448508792477)
**2\. Setting event start and end times**
Events created by the Sympa import will be created with the dates specified in the file import and the times as specified in the Worktime settings (Worktime > Administration > Working community settings/Setting groups-Setting group settings > Work hours > Rendering options > Work hour event default start time/Work hour event default end time). 08:00 - 16:00 will be used if no times are specified.
Note: if [expected work times](<https://support.nepton.com/hc/en-gb/articles/360002558617>) are in use, events will be created based on the times of the expected work times.
**3\. Setting absence / holiday codes and SFTP settings**
Absence / holiday codes and SFTP settings can be configured in **Worktime > Administration > Working community settings/Setting groups-Setting group settings > Integrations > Sympa**. If an event type has multiple possible codes, these can be set separated by a comma.
Note that SFTP settings are only available in working community settings.
### Import schedule
The schedules for the automatic import can be defined in **Work time > Administration > Working community settings > Integrations > Schedules**. You can read more about the schedules in [this article](<https://support.nepton.com/hc/en-gb/articles/10510800700573>)
### Importing start and end times
It is possible to import the start and end times with the 7th column being the start time and the 8th column being the end time. To enable importing or partial day absences, the following needs to be set in **Worktime > Administration > Working community settings > Integrations > Sympa**:
![sympa-absence-import-settings.png](https://support.nepton.com/hc/article_attachments/11161885698205)
#### Event start and end times with partial day absences
If the start/end times are present in the import file, the will be used as the start/end times.
## File format
If the imported file has more than 6 columns, the import will ignore the extra ones. If the
Below is a description of the data and their additional information.
Column | Data | Description  
---|---|---  
1 | Employee number | Employee number  
2 | Absence / holiday code | The codes are defined in the service UI under Sympa settings. If code does not exists then absence is created as holiday.  
3 | Type |  Whether the row is a deletion or a new row. Accepts the following values:
  * `uusi` or `false`
  * `poisto` or `true`

Type 'uusi' will create the absence. Type 'poisto' will remove the absence.  
4 | Vacation period | This is only present in holidays, in absences it is empty. Saved as description. Please surround the column in quotes if there is a risk the value could contain semi-colons.  
5 | Start date | Absence start date, format `DD.MM.YYYY`  
6 | End date | Absence end date, format `DD.MM.YYYY`  
7 | Start time | Optional field, absence start time, format `HH:MM`  
8 | End time | Optional field, absence end time, format `HH:MM`  
Example of the file can be seen below:
[code] 
    445;101;uusi;;02.05.2016;04.05.2016;  
    445;103;uusi;;03.05.2016;06.05.2016;08:00;16:00  
    445;101;poisto;;02.05.2016;03.05.2016;  
    445;200;uusi;"vacation period, something something";01.06.2016;28.06.2016  
    445;200;uusi;"vacation period, something something. Wrong dates on previous one";06.06.2016;02.07.2016  
    445;200;poisto;"vacation period, something something";01.06.2016;28.06.2016
[/code]
