---
id: 36673036993565
title: HRX and Nepton Integration Guide
url: https://support.nepton.com/hc/en-gb/articles/36673036993565-HRX-and-Nepton-Integration-Guide
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels: []
promoted: false
updated_at: '2026-06-18T09:29:23Z'
edited_at: '2026-06-08T12:43:02Z'
---

# HRX and Nepton Integration Guide

This article explains what it means to set up the integration between HRX and Nepton.  
It provides details about the data that must be configured in HRX, including where it needs to be set up, to ensure the integration works seamlessly with Nepton.
When HRX is in use, HRX is the master of HR data.  

## Fields Imported from HRX
**Field** | **Master** | **Description**  
---|---|---  
External identifier 1 |  **Mandatory field.** Created in HRX | The primary identifier for a person, provided by HRX. This is the join key between the two systems and must be unique and stable.  
First name |  **Mandatory field.** Created in HRX | Person first name  
Last name |  **Mandatory field.** Created in HRX | Person last name  
Email | Created in HRX | Person email address  
Unit | Created in HRX |  HRX supports multiple levels in its organizational structure, and each customer must decide which level(s) they want to use. Once the organizational structure has been agreed upon, the corresponding units must be created in Nepton using the exact same names. HRX will then use these names during the person import synchronization process. For instance, if we have organization structure like Level 1 > Level 2 > Level 3 > Level 4 For unit: 
  * If a customer chooses**Level 2** as the Nepton unit level, the corresponding Level 2 units must first be created in Nepton. Once this is done, HRX will send the Level 2 value in the unit field for each person during synchronization.
  * If a customer chooses**Level 3** as the Nepton unit level, the corresponding Level 3 units must first be created in Nepton. Once this is done, HRX will send the Level 3 value in the unit field for each person during synchronization.

  
RFID  | Created in HRX | The RFID tag value used for terminal identification.  
Primary supervisor | Created in HRX | Currently, we only support updating the primary supervisor using the **employee number**. HRX provides employee number in this field.  
Nepton HR role | Roles are builtin in Nepton. Nepton has provided roles list to HRX. | Hard-coded in HRX specifically for Nepton. This is fixed by configuration on the HRX side and not normally changed per person.  
Nepton Worktime role | Created in Nepton. Nepton has provided roles list to HRX. | Dynamic. HRX maintains a manually editable list of valid Worktime roles, which is then mapped per person.  
Contract start date | Created in HRX | Mapped from the HRX field "Konserniin tulopäivä" (start date of the first work contract)  
Contract end date | Created in HRX | HRX sends end date value of the latest work contract (based on dates, not based on creation order). HRX sends the date as empty if the latest contract is open-ended.  
Contract type | Created in HRX | Contract type  
Person group code path in hierarchy | Created in HRX | Person group code path in hierarchy - The hierarchy is maintained in HRX as part of the organizational structure and is imported into Nepton as part of the person data.  
Person group name path in hierarchy | Created in HRX | Person group name path in hierarchy - The hierarchy is maintained in HRX as part of the organizational structure and is imported into Nepton as part of the person data.  
Work time percentage | Created in HRX | The person's contracted work time as a percentage. HRX has support for this and send this value to Nepton.  
Worktime setting group | Created in Nepton. Groups will also be created in HRX manually. | Hierarchy managed in Nepton. Groups will be created in HRX manually. The current value is set in HRX and pushed to Nepton daily. Note that this is a daily synchronisation rather than a real-time event, so changes will only be visible in Nepton after the next daily sync.  
Active  | Created in HRX | Whether the person is currently active in HRX. Inactive persons should be deactivated in Nepton accordingly. Person is not obliterated, it is only marked inactive.  
> **Important:** Any field that is not listed above is not kept in sync from HRX. For migrating customers, those fields are cleared in Nepton.
