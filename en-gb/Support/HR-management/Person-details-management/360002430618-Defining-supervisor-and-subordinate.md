---
id: 360002430618
title: Defining supervisor and subordinate
url: https://support.nepton.com/hc/en-gb/articles/360002430618-Defining-supervisor-and-subordinate
locale: en-gb
category: Support
category_id: 360000446658
section: Person details management
section_id: 360004485937
section_path:
- HR management
- Person details management
labels:
- NEPTONNEEDSREVIEW
- esihenkilö
- ensisijainen esimies
- supervisor
promoted: false
updated_at: '2026-11-06T10:36:08Z'
edited_at: '2026-11-04T14:25:09Z'
---

# Defining supervisor and subordinate

The supervisor-subordinate relationship is defined in the person's information on the employment side. If person B is added as a supervisor for person A, person A will appear as a subordinate in person B's information, without the information having to be saved in each person's information separately.
Adding or replacing a supervisor or a subordinate for a user requires a certain type of [role](<https://support.nepton.com/hc/en-gb/articles/360002425637>). A supervisor can only be a user with employee number.
Please note that supervisor only sees his own subordinates. If a supervisor should be able to see other supervisors subordinates, the supervisor needs to be set as a substitute this supervisor. Instructions can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002430678>).
## Defining a supervisor
A supervisor can be assigned to an employee as follows:
Open the Employees section and choose Persons > **Persons**.  
Open the desired person's information from the magnifying glass.  
From the menu, select **Organization > Supervisors > Add**. Start typing the name of the supervisor and select the desired person as the supervisor from the results.
You can add more than one supervisor to a person. If more than one supervisor is added to the person, the service will indicate who is the primary supervisor. However, it is important to note that only the primary supervisor receives messages about the sensitive actions of his subordinates, such as sick leave, vacation leave and annual leave.
Once you have selected the supervisors, select **Done**.
Always remember to save the changes from the **Save** button at the bottom of the page.
![](https://support.nepton.com/hc/article_attachments/29075242646813)
Supervisor information can also be updated for multiple employees at the same time. Instructions for mass import of supervisors can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002430658>).
Only the primary supervisor (and/or the primary supervisor's substitute) receives an email notification requesting approval for a subordinate's event request."
## Defining a subordinate
You can add a subordinate to a user through the person's information card in the **Employees** section. A person may have several subordinates. In order to add a subordinate, the subordinate must have an Employee Number.
A subordinate can be assigned to an employee as follows:
Open the **Employees** section and choose Persons > **Persons**.  
Open the desired person's information from the magnifying glass.  
From the menu, select **Organization > Subordinates > Add**. Start typing the name of the subordinate in the opening box and select the desired person as the subordinate from the results.
Once you have selected the subordinates, select **Done**.
Always remember to save the changes from the **Save** button at the bottom of the page.
![](https://support.nepton.com/hc/article_attachments/39953933181725)
## Updating or adding supervisor for multiple people at once
Supervisor information can be updated for multiple people at once by using an importable file. This example uses manual person import in .csv file format with UTF-8 encoding. More information about the different import options can be found [here](<https://support.nepton.com/hc/en-gb/articles/360003762577>).
  1. In the Employment section, select **Employees > Persons **and click the **Export to importable Excel -** button.
  2. Remove all columns from the Excel file except **Person number, Primary managers and Secondary managers**. The **First name** and **Last name** columns can also be kept if they make processing the file easier.
  3. If the person already has supervisors assigned (the supervisor’ person numbers), **do not** remove them from the data.
  4. Add the person number of the new supervisor to the Secondary supervisors column for each person. If the person already has supervisors, separate the new supervisor’s person number from the existing ones with the | character, without spaces.
  5. After the steps above, the Excel file should look as follows:  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/40416025959453)  

  6. Then save the file in **CSV UTF-8** format. 
  7. The file is now ready to be uploaded using the Import persons tool found on the Import Persons tab in the Employees section of the service (see [Manual import of people](<https://support.nepton.com/hc/en-gb/articles/360018767498>)). 
  8. Retrieve the data from your computer by dragging the file to the striped area or by clicking the Select file button.  
![](https://support.nepton.com/hc/article_attachments/40416025961501)
  9. Select UTF-8 as the file encoding and "Default" as the type of person import type. Finally, click the Import persons button. The service will indicate whether the import was successful or unsuccessful. If the import fails, the service will provide more detailed information about the error in the data.


It is recommended that you first test importing supervisor information for one person to ensure that the file format is correct and that the desired outcome is achieved. Make sure that at least one supervisor is assigned as the primary supervisor. Notifications about sensitive actions, such as sickness absence, balance and annual leave requests, are sent only to primary supervisors.
