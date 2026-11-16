---
id: 360002489357
title: Scheduled task - person export
url: https://support.nepton.com/hc/en-gb/articles/360002489357-Scheduled-task-person-export
locale: en-gb
category: Support
category_id: 360000446658
section: HR data
section_id: 360001070377
section_path:
- Integration
- HR data
labels:
- henkilöstönvienti
promoted: false
updated_at: '2026-11-06T13:05:52Z'
edited_at: '2026-11-06T13:05:52Z'
---

# Scheduled task - person export

The person export feature allows you to export personnel data (aka HR data). This can be done [manually to Excel file](<https://support.nepton.com/hc/en-gb/articles/360002430478>), or automatically to a CSV or JSON formatted file on a schedule. This article explains how you can export persons data directly to an external system using a scheduled export in Nepton.
Scheduled export supports exporting data in CSV or JSON format.
You can create a scheduled export task by clicking **Add Task** in section **Employees – Administration – Scheduled tasks**. After clicking “Add Task” a form will appear where you can define a scheduled task.
Initially, only the basic details for any task are visible. When you've selected the type "Export persons" for the task, an option to select transport method will appear. More options will appear according to your selections.
Form’s field descriptions are listed below:
  * **General information**
    * **Name:** Select the desired name for the task, for example "Person export from Nepton". This text has no technical impact on the operation.
    * **Description:** You can optionally select a more detailed description you want for the task. This text does not have a technical effect on the functionality, and it won’t be shown anywhere else than in administering the scheduled tasks.
    * **Type:** Export persons
    * **Run as administrator:** In this field you can select the person account from which the transfer will be performed, and which will be shown in the logs and listing. The user selected for this must be an administrator. We recommend that an entirely new person account will be created for this (i.e. “Person export account”). We do not recommend a real person to be selected for this because it could create confusion about whether persons’ data is exported manually or using a scheduled task.
    * **Transport method:** The transport can be performed to an external server using SFTP transport or using a REST API service.
  * **Person data**
    * **Export format:** Choose the format which matches the system you are exporting to (E.g. Visma Nova). If there is not a premade format for your target system or it is known that the target system supports the default format, then choose the ["Default" format](<https://support.nepton.com/hc/articles/4405423095953>).
    * **Encoding:** Select the character encoding for the exported data and file. Possible options are:
      * UTF-8
      * ISO-8859-1 
[UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) is a way of encoding Unicode character set, [ISO-8859-1](<https://en.wikipedia.org/wiki/ISO/IEC_8859-1>) is limited to common characters used in European languages. Character encoding is only selectable for CSV data format – files in JSON data format are always sent in UTF-8 encoding. In general, the program or service you are creating the file for should provide the information about the encoding needed. If you choose a wrong encoding, latin characters with diacritics or characters for non-latin characters will probably appear incorrect in the external system.
    * **Include persons with integration identifier/ employee number zero:** Select “Yes” if you want to include all persons in the export file, select "No" to exclude persons without employee number or with employee number zero “0”. Setting this to "No" gives you the possibility to prevent special accounts, for example, to be exported by simply setting the employee number to 0. This option is not supported by Visma Nova export format - it will always include all persons.
    * **Data format:** CSV for [comma-separated values formatted file](<https://en.wikipedia.org/wiki/Comma-separated_values>) or JSON for [JSON formatted](<https://en.wikipedia.org/wiki/JSON>) file. The CSV data contents depends on selected export format, see Export format above. File exported for Visma Nova system is always in CSV format. Fields included in JSON data format files are listed in [Export persons - JSON data format](<https://support.nepton.com/hc/articles/7982660700189>). When using the CSV format, you can also utilize the settings **Escape illegal CSV export values** and **Quote character for illegal CSV export values**. These settings determine whether prohibited characters found in the data should be enclosed (protected) by a selected quotation mark. If the chosen quotation mark itself appears within the data, it is doubled, and the entire content of the field is enclosed in quotation marks.
    * **File name format:** Name of the export file without the .csv or .json extension - the extension will be added automatically. This option is available for SFTP transport method only.
    * **Include header row in CSV:** Select “Yes” if you want to include the fields’ names in the export file otherwise select “No”. This option is available for CSV data format only.
    * **Select data to send:** Select "All persons" to export all data for all persons each time the task is run. Select "Persons with changes" to export all data for persons that have any information changed since the last time the task was run. This option is available for JSON data format only.
  * **File server (SFTP)** \- These options are shown for the SFTP transport format.
    * **Server address:** Set the host server address where the exported data is transferred to.
    * **Port:** Set the port of the host server used in transfer (most common value for SFTP servers is 22).
    * **Username:** Set the username for the host server used in transfer.
    * **Password:** Set the password for the username. Note that HTML code (e.g., **<** followed by text) is not valid for password.
    * **Working folder:** You can optionally set a specific folder in the host server where the exported data is transferred to. Folder can only be under the default folder for the username, e.g employees/fromNepton
  * **REST API** \- These options are shown for the REST API transport format.
    * **REST API address:** Set the URL of the REST API service providing the API access to transfer the person data to.
    * **Authentication type:** Set the authentication according to the requirements of the REST API service: 
        * **No authentication:** The service does not require any type of authentication for access.
        * **Basic HTTP authentication:** The service requires a basic authentication via username and password. Set the username and password for the REST API in **parameter** settings using 'username' and 'password' for the parameter **Name** fields and their respective values in the **Value** fields.
        * **OAuth 2.0 (Basic HTTP Authentication):** The service requires use of a separate authorization service using OAuth 2.0 protocol. Set the required **authorization server address** value. Set the username and password for the _authorization server_ in **parameter** settings using 'username' and 'password' for the parameter **Name** fields and their respective values in the **Value** fields.
        * **Token authorization:** The service authenticates using a specific key. Set the required key as **parameter** with **Name** 'apikey' and the key value as **Value** for the parameter.
    * **Parameters 1 - 4:** See above for parameters required by the authentication. You can also specify additional HTTP parameters required by the REST API service here.
  * **Schedule**
    * **Run:** These options determine when the task should be scheduled to run.
      * **Only manually** : If there should not be any automatic scheduling of the task, pick this option. The task will only run if the **Execute now** button is selected after saving the task.
      * **Once** : The task is scheduled to run one time only. Select the date & time to run in the **At date & time** field.
      * **When data changes** : The task is run immediately when any person data is edited. In addition a daily run is required because values can change due to their validity periods. If you pick this scheduling option, the **Select data to send** field should usually have the value _Persons with changes_ selected. This option is only available for the JSON data format.
      * **Hourly:** The task is run every hour at the minute of the hour set in the **Minute of the hour** field. E.g. if the minute of the hour is 30, the task is run on 0:30, 1:30, 2:30 etc.
      * **Daily:** The task is run every day at the time set in the **At time** field.
      * **Weekly:** The task is run on weekdays set in the **On weekday(s)** only. Set the time to run in the **At time** field.
      * **Monthly:** The task is run on selected months and days of the months set in **Month(s)** and **Day(s)** fields. For **Day(s)** field there are options by the day numbers or the last day of the month. Set the time to run in the **At time** field.
    * **Active:** Select the time period for when the scheduling is active for tasks scheduled to run regularly. The task is run according to other scheduling options, but not before the **From** date and time or after **To** date and time. The **From** field defaults to be active immediately. The **To** field is optional.


When you have set the necessary settings select **Save**. The service will indicate that the changes were saved after all fields have been correctly filled in.  
  
Person data export can be done manually using the options at the bottom of the page. First, choose if you wish to transfer all person data from the entire history, or enter a desired date after which changes will be transferred. In addition, you enter a reason for running the manual export of person data.
![](https://support.nepton.com/hc/article_attachments/35209947985565)
Once these fields are filled in, click **Execute now** , which will cause the export of person data to be performed immediately.
