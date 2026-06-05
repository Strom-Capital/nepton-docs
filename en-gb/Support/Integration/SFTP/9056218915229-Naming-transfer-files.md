---
id: 9056218915229
title: Naming transfer files
url: https://support.nepton.com/hc/en-gb/articles/9056218915229-Naming-transfer-files
locale: en-gb
category: Support
category_id: 360000446658
section: SFTP
section_id: 360001029457
section_path:
- Integration
- SFTP
labels: []
promoted: false
updated_at: '2024-09-05T07:40:27Z'
edited_at: '2023-05-23T08:19:36Z'
---

# Naming transfer files

Transfer files are used in SFTP-integrations to transfer file either to Nepton service or from Nepton to an external system. We recommend that the filename includes the type of the data, direction of transfer and date and time the transfer file has been created. In this way the transfer file can not be mixed up with other transfer files, and it helps with solving possible issues when the file for a certain type of transfer on a certain date can be easily identified. The file name must have the correct file extension at the end of the file, such as csv, xls or txt.
  
Recommended file format:
TypeOfData_DirectionOfTransfer_YYYYMMDD_HHmm.fileextension
For example:
A file in csv-format that sends person data to Nepton on 23:35 30.1.2023 could be:  
Persons_ToNepton_20230130_2335.csv
A file in txt-format that sends person data to Nepton on 23:35 30.1.2023 could be:  
Persons_ToNepton_20230130_2335.txt
