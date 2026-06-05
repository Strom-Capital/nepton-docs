---
id: 360003737078
title: Project import
url: https://support.nepton.com/hc/en-gb/articles/360003737078-Project-import
locale: en-gb
category: Support
category_id: 360000446658
section: Projects
section_id: 360001075297
section_path:
- Integration
- Projects
labels: []
promoted: false
updated_at: '2024-08-23T10:04:37Z'
edited_at: '2024-01-12T12:36:46Z'
---

# Project import

Projects can be easily imported from other services with scheduled or manual import. This can be used for example to import new projects, change project information or end projects.
At the bottom of this article is an example file for project import.
## Scheduled import
File containing project information can be scheduled for Nepton to fetch from SFTP server or API. More information can be found in [Scheduled project import](<https://support.nepton.com/hc/en-gb/articles/360002492518>) article.
## Manual import
For manual project import, person doing the import needs to have both "Administrator" role and "Kaikki oikeudet" (all permissions) role for Worktime roles.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/8613159607325)
Instructions for adding a person: [Add person](<https://support.nepton.com/hc/en-gb/articles/360002427618>)
Instructions for worktime roles: [Assigning roles](<https://support.nepton.com/hc/en-gb/articles/360002553397>)
## Preparing data to import
  * Use this article's example file as a template.
  * Mandatory fields are project name, project code and visibility in a terminal (A, B and H - columns)
  * Do not remove empty columns. Leave columns empty for fields you do not have information. 
  * After filling the information, remove three top rows from the file (rows 1-3, including A-column's orange text, ’Individual value’ and ’Project Code’).
  * Save file in CSV format - CSV UTF-8 (Comma delimited) (*.csv).


## Importing manual file
1\. Go to **Worktime > Administration > Working community settings > Integration > Project import**
2\. Select import file from your computer by clicking Choose file. Locate the previously saved CSV file. Select **Run****.**
![](https://support.nepton.com/hc/article_attachments/15494080007325)
If import was successful, it is shown on light blue background in import history. Magnifier icon can be clicked to open import log.
![](https://support.nepton.com/hc/article_attachments/15494080018333)
If import file contains projects that have not changed, they will be marked as skipped projects in the import log.
If import was not successful, it is shown on red background in import history. Exclamation mark icon can be clicked to open import log where errors are shown. Once the errors have been fixed, file can be imported again.
![](https://support.nepton.com/hc/article_attachments/15494073246749)
3\. Project import is now complete and changes to projects have been done.
4\. Information about the import can also be found in the service log in Employees section. Go to **Employees > Administration > Service log**. Each import is shown as an own row in the log. Detailed information about the import can be viewed by clicking the icon on the left of each row. Icon is green if import was successful and red if it failed.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/8614024562461)
Imported projects are created to the service automatically. If the project already existed in the service, it's information was updated.
Project that has a parent project can not be updated as a root project.
## Import fields
Field to import | Description  
---|---  
Project Code |  Project code. If a project with this code is not found in the service, new project will be created with this code. If a project with this code is found in the service, that project will be updated.  
Project Name |  Project name. Mandatory field.  
Project Description |  Project description. Can be empty.  
Project Start date |  Project start date, can be empty. Format YYYY-MM-DD. **Note: 1.1.1970 and earlier dates are not visible in the user interface**  
Project End date |  Project end date, can be empty. Format YYYY-MM-DD.  
Parent project code |  Code of parent project, can be empty. The project imported for this row will be set below the project that is set here.  
ProjectTypeName |  Project type. If empty, default value is 'Projektit' (project_work).  
Show on terminals |  Is project shown in terminals. '1' means yes, '0' means no.  
External Identifier |  External identifier. If project with external identifier is found, the project is updated. External identifier is used to identify project before project code. Can be set empty.   
Project Managers |  Project manager employee numbers. Multiple employee numbers can be separated with "|" character. For example, "001 | 002 | 003". Can be set empty.   
User Groups |  Project's visibility to user groups. User group codes are used as values. Multiple user group codes can be separated with "|" character. For example, "001 | 002 | 003". Can be set empty.   
Users |  Project's visibility to users. Employee numbers are used as values. Multiple employee numbers can be separated with "|" character. For example, "001 | 002 | 003". Can be set empty.  
## Project code and external identifier in import
Project code is mandatory in import data but external identifier is not. Project can be identified by code or by external identifier. If external identifier is found in the service and in import data, relevant project is updated. It is shown in the import log which identifier was used to update project. If no external identifier is set, project code is used for identification. Good to know about identifiers:
  * If service has multiple projects with the same project code and no external identifiers are used for identification, project with that code is skipped during import because it is not possible to know which project is meant to be updated. For this reason it is recommended to use unique project codes.
  * If service has multiple projects with the same project code and this project is set as a parent project during import, imported project is skipped because it is not possible to know which project is meant to be set as its parent project. For this reason it is recommended to use unique project codes.
  * It is possible to change project code during import if project is identified with external identifier. It is recommended to check that no duplicate project codes are present in the service after update.


## Project managers, users groups and users in import
Project managers, user groups and users are non-mandatory fields in import data.
  * If non-mandatory fields for project managers, user groups or users are left empty, by default they are ignored during import.
  * If these fields have values, new values are set for project. All the values which are not present in import data are removed. For example, project has currently project manager with employee number 123. Project managers with employee numbers 321 and 322 are imported for that project. Project manager 123 is removed because it is not present in import data.
  * Empty cell for these fields can only remove values if it's set to do so with setting **Administration > Working community settings > Integrations > Project import > Empty cell removes...** For example, project has 10 project managers. Value "Yes" is set for "Empty cell removes project managers from project" setting and the cell in import data is empty. All the project managers are removed from project.


![](https://support.nepton.com/hc/article_attachments/15737740295837)
