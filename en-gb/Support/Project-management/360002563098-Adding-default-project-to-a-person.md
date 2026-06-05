---
id: 360002563098
title: Adding default project to a person
url: https://support.nepton.com/hc/en-gb/articles/360002563098-Adding-default-project-to-a-person
locale: en-gb
category: Support
category_id: 360000446658
section: Project management
section_id: 360000707398
section_path:
- Project management
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-05-22T07:34:17Z'
edited_at: '2026-05-20T09:36:43Z'
---

# Adding default project to a person

A default project can be added to a person in the Employees section. The default project is automatically attached to an event when creating a new event. The project can be changed to another one before saving the event.
If default project has been set it is automatically added to all new events. Automation can not be defined based on event type or absence type.
Default project can only be one of the projects person has [visibility ](<https://support.nepton.com/hc/en-gb/articles/360006776758>)to either through person or person group settings, if not all projects are visible to everyone.
## Adding or changing default project to a single person
1\. Go to **Employees > Persons**. Choose the correct person by searching with their name. Open that person's details from the magnifying glass. ![](https://support.nepton.com/hc/article_attachments/36220871121053)
The default project is set in the **Person’s information** tab in the **organization** section. Start entering the project name in the field “Default project” and select the correct project from the search results. Click **save** at the bottom of the page to save the information.
![](https://support.nepton.com/hc/article_attachments/36220871121949)
The default project field does not have a validity function. A person can only have one default project at a time, and it is always valid for the past and future. Changing the default project to another does not change the entries already made, only new events created after the change are offered the new default project.
## Adding or changing default project to multiple persons at once
The default project can be edited for multiple people at once.
  1. Go to**Employees > Persons > Persons.**
  2. Select **Export to importable Excel**. Open the file. In Excel, you'll see a **Default Project** column.
  3. Leave only the people whose default project you want to change to the list (completely remove all other people (rows) from the file).
  4. Only leave the columns ‘Employee Number', 'First Name', 'Last Name' and 'Default Project' in the list.
  5. In the 'Default Project' column, write the code for the project you want to assign to the persons.
  6. Save the file (name does not matter).
  7. Choose **Employee > Persons > Import Persons**. Upload the file you saved.
  8. The information has now been updated.


With this method, other person information can also be edited at the same time. More information about person import can be found [here](<https://support.nepton.com/hc/en-gb/articles/360003762577>).
The update is valid for all columns from the moment the file is run.
An example file for updating default projects:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4414989045137)
