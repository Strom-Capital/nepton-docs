---
id: 360002489417
title: Common principles on implementing integrations
url: https://support.nepton.com/hc/en-gb/articles/360002489417-Common-principles-on-implementing-integrations
locale: en-gb
category: Support
category_id: 360000446658
section: General information on integrations
section_id: 360002325398
section_path:
- Integration
- General information on integrations
labels:
- NEPTONNEEDSREVIEW
- liittymäkuvaus
- ajastuspalvelut
- integraatio
- henkilötietoliittymä
- henkilöliittymä
promoted: false
updated_at: '2026-08-14T10:05:38Z'
edited_at: '2025-07-25T12:13:23Z'
---

# Common principles on implementing integrations

Integration refers to the method of transferring data either from Nepton to another system or from another system to Nepton. The available integration methods are:
[File-based SFTP transfer](<https://support.nepton.com/hc/en-gb/articles/360003762477>)
[Using an API](<https://support.nepton.com/hc/en-gb/articles/360004861518>)
The principle of file-based SFTP transfer is that the source system generates the data on a scheduled basis and uploads it to an SFTP server. The target system then retrieves and processes the data on a separate schedule. Typically, data is transferred during nighttime, with enough buffer time between generation and retrieval to ensure the source system has completed the file.
![](https://support.nepton.com/hc/article_attachments/29108382197021)
The API integration is based on requests, where the external system calls Nepton’s API to obtain the desired information. The capabilities available via Nepton’s API are described in the following articles:
  * [Worktime API](<https://support.nepton.com/hc/en-gb/articles/360004861558>)
  * [HR API](<https://support.nepton.com/hc/en-gb/articles/360004855857>)


![](https://support.nepton.com/hc/article_attachments/29108414553117)
File-based SFTP transfers are more schedule-oriented and often involve transferring a larger volume of data at once (e.g. importing new personnel and updating personal information). API integrations are used when data needs to be transferred quickly and made available in Nepton immediately (e.g. importing or exporting project data).
When implementing integrations, the following operational principles should be considered:
## Problem detection and resolution
[Potential issues should be anticipated and handled](<https://support.nepton.com/hc/en-gb/articles/9056347382813>) already during the integration implementation phase.
## Scheduling
Integrations operating through the SFTP server can be scheduled in Nepton. Learn more about:
  * [Scheduled task - Person import](<https://support.nepton.com/hc/en-gb/articles/360002489317>)
  * [Scheduled task - Person export](<https://support.nepton.com/hc/en-gb/articles/360002489357>)
  * [Scheduling worktime import/export integrations](<https://support.nepton.com/hc/en-gb/articles/10510800700573>)


Additionally, there are some near real-time integrations that run once per minute. These include integrations to phone exchange and presence systems such as:
  * [Elisa Ring (eIPKulva)](<https://support.nepton.com/hc/en-gb/articles/360004522538>)
  * [Mitel Aastra and Telia Merex](<https://support.nepton.com/hc/en-gb/articles/360013422917>)


## Identification of the person being transferred
An employee number can be assigned to the individual, which is used in all transfers. If multiple identifiers are in use, a system-specific identifier can be set in the person's Employees-section. This identifier will be used for transfers related to that specific system.
The code '0' (zero) is a special code used to exclude the individual’s data from being transferred. This code should be used as the identifier only when the person's data or events are not to be transferred.
## Integration user
A dedicated user account that only executes transfers must be created in Nepton. This user is granted the required permissions for the integration tasks.
To transfer personnel data, the user must have administrator rights.
To transfer worktime data, the following additional permissions may be required (depending on the type of data):
For exporting data:  
Can view events of all personnel
For importing data:  
Can edit and approve all users events  
Can lock event dates  
Can unlock locked dates  
Can administer balances  
Can edit approved events  
Can view external identifier of events  
Can edit external identifier of events
For transferring project data:  
Can manage projects and project relations  
Can manage persons' settings and projects
For modifying person groups, setting groups or worktime roles:  
Can manage person groups  
Can manage person setting groups  
Can manage worktime roles
