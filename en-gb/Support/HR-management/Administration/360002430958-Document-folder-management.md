---
id: 360002430958
title: Document folder management
url: https://support.nepton.com/hc/en-gb/articles/360002430958-Document-folder-management
locale: en-gb
category: Support
category_id: 360000446658
section: Administration
section_id: 360004488558
section_path:
- HR management
- Administration
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-08-23T08:51:48Z'
edited_at: '2023-03-02T12:34:32Z'
---

# Document folder management

Document folders provide a convenient place to store additional information about personnel that is contained or archived in files. e.g. PDFs, Excels, Word documents, or any other file types.
By default, there are three document folders types; Work contracts, Salary slips, and Other documents.
Work contracts and Salary slips folder types are related to other features described below, and should not be removed if you are using them. However, removed folders can be returned at a later date.
  * **Work contracts folder** \- Required by the Online work contract features, for storing signed work contract PDFs and attached materials. The folder can also be used for storing any other working contract related materials. e.g. scanned copies of written contracts, etc.
  * **Salary slips folder** \- Required by the Salary advance request features, for storing approved requests as PDF. Can also be used for storing other manually created materials related to salaries.
  * **Other documents folder** \- A general-purpose folder for storing any other files related to a user


### Create or edit folders
The document folders are managed from the **Employees - > Administration page**, under the **Document folders** heading. From here you can adjust all aspects to the folders.
  * **Add a folder** \- To add a new folder, simply click the 'Add folder' button and fill the related fields. You can create as many folders as you feel necessary to organise your person information.  
An example of this can be seen in the screenshot below, called _Custom folder_.  
When adding a folder, the 'Type' dictates whether it is used by other features in the platform and the file types it permits. Please see the **Folder types, default folders and related features** heading above for more information.
  * **Remove a folder** \- Clicking the 'X' next to a folder, will mark it removed. Removed folders will no longer be accessible for anyone, but this can be reversed after clicking the 'Show deleted document folders' check box above the management panel.
  * **Edit a folder** \- By clicking the 'Pencil' icon next to a folder, you can edit its details. Here you can change its name, description, type, and permissions. Folders permissions dictate roles who have access to that folder for employees they also have permissions to.
  * **Change order** \- The arrow buttons beside the document folders, allow you to change the order in which they are displayed to end-users.  

Please note that changing a document folders 'Type' is not recommended after it has been created


![mceclip4.png](https://support.nepton.com/hc/article_attachments/360010972058/mceclip4.png)
## Viewing and editing a person's documents
### I can't see any document folders?
If your administrator has not yet configured any document folders, or you lack the permissions to view them for the person in question, then you will see a notification instead. If you think this is incorrect, please contact your administrator.
_Example: When no document folders are configured_
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360010897317/mceclip0.png)
### Person documents
If you have permissions to see a persons information, and permission to at least read one of the related document folders, it is possible to see the uploaded documents by visiting the person's information page and the Documents tab - **Employees - > Persons -> Person information**.
Depending on your folder permissions, you may then view, upload and even delete documents within each folder.
New documents can be uploaded either using the browse harddisk dialogue or by dragging and dropping the document to the intended folder.
![mceclip5.png](https://support.nepton.com/hc/article_attachments/360010972078/mceclip5.png)
### Document Permissions
Access to documents is restricted to individuals with authorized privileges, determined by both user role and document folder permissions. This chapter describes how document permissions are applied.
  * If document is not associated with any user, access to the document is based only on read permission granted to the folder for particular role.
  * Work contracts which are not associated with any user can only be read by Administrators, HR Management and Salary Management.
  * Persons holding the roles mentioned below are not able to access their own documents without employee role read access.


#### Permissions by Role
Below is a list of documents that can be accessed by different roles if read permission is set for their roles:
  * **Administrator, HR Management and Salary Management** \- All documents regardless of the user associated with the documents.
  * **Unit Manager** \- Documents which belong to users in the same unit as the Unit Manager.
  * **Supervisor** \- Documents of subordinates.
  * **Employee** \- Own documents.
