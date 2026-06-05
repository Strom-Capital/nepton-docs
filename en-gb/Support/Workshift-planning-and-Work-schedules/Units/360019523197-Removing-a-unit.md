---
id: 360019523197
title: Removing a unit
url: https://support.nepton.com/hc/en-gb/articles/360019523197-Removing-a-unit
locale: en-gb
category: Support
category_id: 360000446658
section: Units
section_id: 360000708958
section_path:
- Workshift planning and Work schedules
- Units
labels:
- unit
- yksikkö
- remove unit
- yksikön poistaminen
promoted: false
updated_at: '2025-06-18T07:34:25Z'
edited_at: '2025-06-18T07:34:25Z'
---

# Removing a unit

## General
Units are used in many parts of Nepton service and removing a unit might have undesired effects. Please check all the related information mentioned in this guidance before removing a unit.
## Check locations
A unit should not be removed if there are any locations under it that have not been removed. You can check if there are any locations for the unit from Locations. Select Change Unit tab, select the unit from Unit Selection and click Continue. You should now see the locations of the unit. If there are locations for the unit, you should check for each location if the location is still needed. The locations are displayed as a hierarchy tree:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360019349497)
If you plan to remove a location, you should make sure no location under it is needed either. Existing locations under a location can be moved under another location by changing the category. However, locations cannot be moved to another unit, so if any of the locations are needed, the unit cannot be removed.
### Locations in workshift planning
If your working community is using [workshift planning](<https://support.nepton.com/hc/en-gb/sections/360000934137>), the location may be needed to group people to plan shifts for in [shift planning by location](<https://support.nepton.com/hc/en-gb/articles/360015675918>). You can check if there are people assigned to a location from Planning > select Change Unit > select the unit from Unit Selection > Continue > select the location from Location selection > Continue > select Locations tab > select Location Persons. If there are any persons under Location Persons heading, you should check if they should be assigned to another (unit and) location.
## Check Worktime projects
If a unit has locations created under it, there are corresponding projects automatically created to Worktime matching the names and codes of the units and locations (for locations the project code matches the calculation unit of location). These projects may be used like any other projects to target work to and the may have been assigned project managers - [see more information about Project management](<https://support.nepton.com/hc/en-gb/sections/360000707398>). When deleting a location, the corresponding project will also be deleted and it cannot be used to target work to. Also, after the project has been deleted any work targeted to it cannot be retrieved from Worktime using project reports. You can check if there is work targeted to a project using different reports under **Worktime > Projects > Reports**.
## Check persons in unit
You can check if the unit has been assigned for persons as their unit from **Employees > Units > select unit > Unit Persons**. Before removing persons in this view you should consider adding the persons to another unit. See [Add persons to the unit](<https://support.nepton.com/hc/en-gb/articles/360002595478>).
## Release the unit code for future use
We strongly recommend changing the code of the unit before removing the unit. You can use a format that would never be used for normal unit codes. For example, you could prefix the code with REMOVED_, e.g. REMOVED_1000.
## Removing unit
After resolving all the possible issues that might prevent removing the unit (see previous steps) and after you've renamed the unit code (see last step before this), you can remove the unit via **Employees > Units > select Unit > (check that you've selected the correct unit) > Additional functions > Remove**.
After removing the unit a message 'The unit has been deleted' is displayed. If at this point you notice you've pressed the Remove button accidentally or there is still some additional checks you've not done, you can click **Restore**. The unit will be restored to use.
