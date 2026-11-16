---
id: 26861716054045
title: Target servers for work time integrations
url: https://support.nepton.com/hc/en-gb/articles/26861716054045-Target-servers-for-work-time-integrations
locale: en-gb
category: Support
category_id: 360000446658
section: General information on integrations
section_id: 360002325398
section_path:
- Integration
- General information on integrations
labels: []
promoted: false
updated_at: '2026-08-14T11:43:40Z'
edited_at: '2026-01-10T08:11:31Z'
---

# Target servers for work time integrations

A separately defined target server must be defined for work time integrations. When the target server has been defined, the same target server can be used in multiple integrations, so you only need to specify the server information once.
Target servers can be managed in **Worktime > Administration > Working community settings > Integrations > Integration target servers**.
![](https://support.nepton.com/hc/article_attachments/30716510563613)
## Target server settings
A new target server is added by pressing "Add integration target server", which allows you to fill in the basic information for the target server:
![](https://support.nepton.com/hc/article_attachments/30716541074717)
The target server is given a name, an optional description, and its type is selected from the drop-down menu. The type can be either SFTP (Export), SFTP (Import) or webservice. The type is selected depending on the type of integration the target server is used for. Once this information has been added and "Save" has been pressed, this target server will appear in the target servers menu:
![](https://support.nepton.com/hc/article_attachments/30716541078557)
In the image above, a new target server called "Absences to Mepco" has been added. The more detailed information about the target server can be filled in by clicking on its name. Note: Each folder structure must have its own defined target server. This means that even if two different files are exported to the same SFTP server, if the target folder is different, separate target servers must be created for them. For example, if a salary export and an absence export were in use and being exported to the server in the folders FromNepton/Salaries and FromNepton/Absences, two target servers should be defined in Nepton.
![](https://support.nepton.com/hc/article_attachments/30716510569885)
Please see [Setting up SFTP data transfer](<https://support.nepton.com/hc/en-gb/articles/360003722778>) for general instructions regarding the server address, username, authentication (public key or password), and what kind of path structure the server should have.
If the target server is used for a real-time integration, the "Enable real-time sync (if supported)" setting must be set to Yes.
Once the target server information is specified, it can be selected as the target server for a scheduled export under "Schedules". The same target server can be used for multiple connections.
![](https://support.nepton.com/hc/article_attachments/30716541080733)
## Buffering real-time exports
Buffering allows the export data to be scheduled rather than being performed when events are saved or approved.
The main benefit of buffering is that downtime on the target server does not result in data not being transferred. Failed transfers are retried as long as they are in the buffer.
The buffer is configured by setting a schedule for the integration target server. In the schedule settings, you must select:
1\. Integration "SFTP file export"  
2\. The desired target server for the integration target server
![](https://support.nepton.com/hc/article_attachments/27169551827101)
You can read more about scheduling integrations [in this article](<https://support.nepton.com/hc/en-gb/articles/10510800700573>).
