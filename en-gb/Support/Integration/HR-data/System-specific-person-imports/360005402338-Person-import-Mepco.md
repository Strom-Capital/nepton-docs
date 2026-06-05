---
id: 360005402338
title: 'Person import - Mepco '
url: https://support.nepton.com/hc/en-gb/articles/360005402338-Person-import-Mepco
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels:
- S365
promoted: false
updated_at: '2023-09-26T12:38:59Z'
edited_at: '2023-09-26T12:37:58Z'
---

# Person import - Mepco 

This article describes the default fields for the Mepco person import in CSV format, which will be used when the file doesn't contain a header row. If the header row is included in the file or it has been defined into the [scheduled task settings](<https://support.nepton.com/hc/en-gb/articles/360002489317>), the file will be imported based on the content and the ordering of the header row ignoring the table below. Also [other file types](<https://support.nepton.com/hc/en-gb/articles/360003762577#h_01F1J435S3DJ9B4MSK8Y4FV9CS>) are supported, in which case the field table below will not be used. Default import without the header row will be done according rules of [person import without validity information](<https://support.nepton.com/hc/en-gb/articles/360015741097>).
## Import fields
Field | Import Column Index | Mapped to Nepton Field  
---|---|---  
Username | 1 | Username  
First name | 2 | First name  
Last name | 3 | Last name  
Employee number | 4 | Employee number  
Email | 5 | Email  
**_Not imported_** | 6 | **_Not imported_**  
Contract start date | 7 | Employment start date  
Contract end date | 8 | Employment end date  
Worktime calculation group | 9 | Worktime setting group  
Supervisor | 10 | Primary supervisor
