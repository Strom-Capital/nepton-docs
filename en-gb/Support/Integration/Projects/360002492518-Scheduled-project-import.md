---
id: 360002492518
title: Scheduled project import
url: https://support.nepton.com/hc/en-gb/articles/360002492518-Scheduled-project-import
locale: en-gb
category: Support
category_id: 360000446658
section: Projects
section_id: 360001075297
section_path:
- Integration
- Projects
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2023-09-11T12:28:52Z'
edited_at: '2023-09-11T12:28:52Z'
---

# Scheduled project import

  
Projects can be imported and updated to the service on a scheduled basis either via the API interface or via file upload. 
## Importing projects by file upload
When using file upload, import of projects is defined in the menu **Working time - > Administration -> Work community settings -> Integrations -> Import of projects**. The transfer uses a file that Nepton retrieves from the SFTP server, and the SFTP server information is specified in this menu to Nepton. The file must contain the columns described [in this article](<https://support.nepton.com/hc/en-gb/articles/360003737078-Project-import>).
  
Please note when defining the file upload; If Public key authentication is on, an asymmetric RSA key pair is used to log in to the SFTP server instead of a password. In this case, no password is set. The public part of the key pair is requested from the customer's IT supplier and delivered to the SFTP server administrator. If the administrator of the SFTP server is Nepton, the public part of the key pair is delivered to Nepton's customer service. 
Projektien import can set on an automatic schedule. The schedules are defined in menu
**Working time > Administration -> Work community settings -> Integrations -> Schedules**
More about the schedules [in this article](<https://support.nepton.com/hc/en-gb/articles/10510800700573>)
##    
Importing projects using the API interface
You can find a more detailed description of the projects API [in this article](<You%20can%20find%20a%20more%20detailed%20description%20of%20the%20projects%20API%20in%20this%20article.>).
