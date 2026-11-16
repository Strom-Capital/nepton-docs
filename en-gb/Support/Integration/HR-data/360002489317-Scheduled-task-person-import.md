---
id: 360002489317
title: Scheduled task - person import
url: https://support.nepton.com/hc/en-gb/articles/360002489317-Scheduled-task-person-import
locale: en-gb
category: Support
category_id: 360000446658
section: HR data
section_id: 360001070377
section_path:
- Integration
- HR data
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-09-21T11:19:04Z'
edited_at: '2026-09-21T11:19:04Z'
---

# Scheduled task - person import

Persons can be added manually one by one or as a mass with manual person import. In this article we tell how persons can be added with scheduled persons import. Settings can be found in **Employees > Administration > Scheduled tasks**. When you start defining a new scheduled task choose **Add Task**. Now you can define a new task. Below you can see field descriptions. The selection of needed fields will vary and depends on selected task type (import persons), file type and person import type.
### General information
**Type:** Import persons  
**Name:** Choose a name for the task, like "Person import from Mepco". This text has no technical effect on the import. We recommend to always use a time stamp on the file name, in case there is a disruption in scheduled imports the files can be retroactively be read in in the right order.  
**Description:** Write a description for the task. This text has no technical effect on the import and it is visible here in task management only.  
**Run as administrator:** Here you choose with which user will run the task and is shown in the listing. The selected user needs to have administrative permissions. We recommend that you add new user for this (for example "Mepco Admin") instead of using a real-life user. This way you avoid any confusion whether this import is manually run or a scheduled task.
### Person data
**Person import type:** Here you choose which form the import should be. This defines how data will be imported and what kind of data structure and content are supported. Please find more detailed information of supported person import types [here](<https://support.nepton.com/hc/en-gb/sections/7976634441629-System-specific-person-imports>).  
**Encoding:** Choose encoding for the import. Essential for Scandic letter coding.  
**File type:** Choose type for the import file. The supported file types are [CSV](<https://fi.wikipedia.org/wiki/CSV>), [XML](<https://en.wikipedia.org/wiki/XML>), [Excel](<https://fi.wikipedia.org/wiki/Microsoft_Excel>) (XLS or XLSX) and [JSON](<https://fi.wikipedia.org/wiki/JSON>).  
**Person identifier:** The person identifier refers to the personal data used to determine whether the imported person already exists in the system. If a person with the same identifier is found, their information will be updated with the imported data.  
When the value “Default” is used, the system selects the first of the following personal data fields that has a value in the imported data: Nepton Id, External identifier 1, Username, Employee number.  
Tip: When you select a value other than “Default,” you can update these identifiers—External Identifier 1, Username, and Employee number—using the imported data, except for the identifier you have chosen as the person identifier.  
**Header row:** This optional setting is used with CSV-files. Please check are there person information field names on the first row of the imported data file. If you can see the field names in the file, then this header row setting will be left empty. If you cannot see the field names in the file, you need to list all required field names separated with pipe marking (|). This way you can use all [person import fields.](<https://support.nepton.com/hc/en-gb/articles/360015933397>)  
**Imported fields:** This optional setting is used with Excel-files. If there are columns which you don't want to be imported in the Excel-file, you simply choose only wanted field names by listing them to the header row separated with the pipe marking.
### File server (SFTP)
File server settings need to be set to all person import types, where Nepton collects the data from SFTP-server (currently all other person import types except Sympa HR Integraatio API -type).  
**Server address:** Write server name from where the file will be fetched.  
**Port:** Used port in import.  
**User name:** Write user name, which allows the file to be fetched from the SFTP server.  
**Password:** Write password, which allows the file to be fetched from the SFTP server. Note that HTML code (e.g., **<** followed by text) is not valid for password.  
**Working folder:** If there is a certain folder in SFTP server, where the data needs to be fetched, the name is marked here (picture below, example 1). Optional.  
**Archive folder:** Succesfully imported files are transferred to this folder in SFTP server. Nepton does not remove files from the archive folder.The user name used must have both read and write access to both the working folder and the archive folder.  
**File name filter:** Here you can indicate that only those files, which have text in it's name , that is marked in here, will be imported. For example importing only files which names include the text: sympa_persons (picture below,example 2). There should also be a time stamp in the file name to indicate when the file is created. This ensures that the previous file will not be overwritten for example when receiving end is not run according the import schedule.![mceclip4.png](https://support.nepton.com/hc/article_attachments/8828634919709)
### REST interface settings
Rest settings are defined for those person import types, which Nepton fetches data with http-protocol through API interface (currently person import Sympa HR Integration API).  
**REST API address:** The URL of the requested REST API service, to which you can add URL parameters after the address if necessary.  
**Authentication type:** Set authentication for REST API service according to your standards:
  * **No authentication:** No identification needed for access into service.
  * **Standard HTTP authentication:** Standard identification needed with user id and password. Set user id and password for REST API with **Parameter** settings using fields **Name** and **Value** and giving them appropriate values as described in the picture below.
  * **OAuth 2.0 (standard HTTP authentication):** Nepton requires a distinct authorization server which uses OAuth 2.0 -protocol. Set the required **authorization server address.** Then set user id and password in **Parameter** settings using fields **Name** and **Value** and giving them appropriate values as shown in the picture below.
  * **Token authorization:** Identification into service by using a special key for it. Set the required key into **Parameter** settings: **Name** field: "apikey" and **Value** field: the key value.


**Authorization server address:** If you chose "OAuth 2.0 (perus-HTTP-autentikointi)", here you will add the authentication server address, where you send the identification request.  
**Parametri 1 - Parametri 4:** Please check above the parameters, which are needed for different authentications. To these fields you can also add parameters which will be sent together with the interface request in the HTTP header information. Write the parameter name to the **Name** field and the value of the parameter to **Value field.**
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4409338812177)
 _**Invalid settings**_
If you change (scheduled task) the type, person import type, file type or authentication type and you have previously used fields which cannot be used with the new type, there will appear message "Invalid settings". Please check that the type is a correct one or empty the invalid field.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/8842031222173)
### Timing
These fields define when the data file will be imported and how it is repeated. We recommend to set the timing to the night time but also considering the regular maintenance times. Please check the times for Nepton maintenance work at the end of [Platform status](<https://support.nepton.com/hc/en-gb/articles/360006554777>) article. 
**Schedule:** These fields define when the task will be run. The visible timing settings will vary according to what option is selected in **Run** field (picture below).
  * **Only manually:** If you don't want to use the scheduled timing, choose this option. The task is run only if **Execute now** button is used. It will appear in lower right corner after you have saved the settings.
  * **Once** : The task will be run only once. Choose the time and date in **At date & time **field.
  * **Hourly:** The task will be run hourly and exactly on that minute which has been set in **Minute of the hour** field. For ex. 30 -> then the task is run 0:30, 1:30, 2:30...
  * **Daily:** The task will be run every day at the time which has been set **At time** field. 
  * **Weekly:** The task will be run only on those weekdays, that are chosen in **On weekday(s) field.** Set also time in **At time** field.
  * **Monthly:** The task will be run on those months and days and time, which have been chosen in **Month(s), Day(s) and At time -** fields.


**Active:** Optional. Choose an interval when this regularly run scheduled task will be active. The task will be run according to above set settings but never outside the hours/dates that have been set in **From** and**To** fields. Most common use for this is that the start time is set but not necessarily the end time because the scheduled task needs to be active all the time according to the scheduled settings.
**From** field's default setting is that it is active right away. **To** field is optional and has no default.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/8843800841629)
When all the settings have been set press **Save.** If all the settings are correctly set, you will get a notification about it. Please note that if any of the fields is incorrectly set or missing and you will get an error message, none of the settings are saved before you fix the invalid, pointed fields.
After you have successfully saved the task, you can test it by choosing **Execute now.**
The new scheduled task is also visible in the main menu **Employees > Administration > Scheduled tasks**.
Please note that scheduled imports may appear in the service logs with a slight delay. Although the import is triggered at the configured time (for example at 04:00), processing and updating the logs may take a few minutes. As a result, the import may appear in the user interface at 04:01 or 04:02. This is normal behaviour. If it is important for the import to appear as close as possible to a specific time in the UI, you can schedule it slightly earlier (for example at 03:58 or 03:59).
