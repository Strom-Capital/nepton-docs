---
id: 360019776498
title: Updating or setting a setting group for several people at once
url: https://support.nepton.com/hc/en-gb/articles/360019776498-Updating-or-setting-a-setting-group-for-several-people-at-once
locale: en-gb
category: Support
category_id: 360000446658
section: Person details management
section_id: 360004485937
section_path:
- HR management
- Person details management
labels:
- sisäänluku
- massamuutos
promoted: false
updated_at: '2026-11-06T11:24:37Z'
edited_at: '2026-11-06T11:24:37Z'
---

# Updating or setting a setting group for several people at once

If you want to move people in bulk to another settings group, there are several different ways to do this. This article describes all the options and the details related to them.
See also the instructions for updating or setting an individual person's settings group [in this article.](<https://support.nepton.com/hc/en-gb/articles/360002557357>)
## Moving persons to a setting group from the current day onwards
### In the setting group settings
Go to **Worktime > Administration > Setting groups > Setting group: Select the correct settings group > Action: Setting group members.**
Then select the checkbox in front of the name of each person you want to move to this setting group.
![](https://support.nepton.com/hc/article_attachments/40465779003549)
Select **Save** at the bottom of the page.  
  
With this method, the people are moved to the setting group starting on the day the save is made.
### As a mass import
Select **Employees > Persons > Persons. **Select **Export to importable Excel**. Open the Excel file that is downloaded. In Excel, you will see the column 'Worktime setting group'. Leave only the people whose settings group you want to change in the list (remove all other people from the file completely). Leave only the columns 'Employee number', 'First name', 'Last name' and 'Worktime setting group' in the list. In the 'Working time settings group' column, enter the code of the settings group to which you want to move the people. Save the file (the name does not matter).
Example image of the file contents:
![](https://support.nepton.com/hc/article_attachments/40465746302109)
Select **Employees > Persons > Import persons**. Upload the file you saved.  
  
With this method, the people are moved to the relevant settings group starting on the day the save (running the file) is made. With this method, other information about people can also be edited in bulk at the same time, if desired. In that case, leave in the file the columns you want to update. For all columns, the update takes effect from the time the file is imported.
## Moving persons to a setting group from any date onwards
People can also be moved to a setting group so that you can select the date from which the change is valid from. This change can be made in bulk or individually for each person through the [validity function.](<https://support.nepton.com/hc/en-gb/articles/360002559358>)
### As a mass import with valid from
Editing the setting group for several people so that the setting group's effective date is in the past or future is done in the same way as in the previous example, but the 'Valid from' field is also included in the Excel file being transferred.
Example image of the file contents:
![](https://support.nepton.com/hc/article_attachments/40465746302877)
