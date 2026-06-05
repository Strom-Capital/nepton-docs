---
id: 360002557537
title: Add or copy a setting group
url: https://support.nepton.com/hc/en-gb/articles/360002557537-Add-or-copy-a-setting-group
locale: en-gb
category: Support
category_id: 360000446658
section: Setting groups
section_id: 360000707358
section_path:
- Worktime calculations and management
- Setting groups
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-04-14T10:02:23Z'
edited_at: '2026-04-14T10:02:20Z'
---

# Add or copy a setting group

New setting groups can be added or copied from **Worktime > Administration > Setting groups > Add setting group**. 
![](https://support.nepton.com/hc/article_attachments/35364810356893)
There are many ways to add a new setting group.
## Add manually
**Name** : Setting group can be given any name. The name is recommended to be descriptive of the setting groups settings regarding work time calculations, e.g. "Levelling period 40hrs".  
  
**Parent group** : If parent group is set, the setting group will be added as a child to the parent setting group. The new child setting group can have distinct settings that override the settings in the parent group. The selection must be empty if the group to be added is a parent group itself.  
  
**Code** : Setting group code can contain numbers and letters and is mandatory. Code is used in person imports in case the import handles setting group information.  
  
**Description:** A brief description on what kind of settings the setting group consists of.
![](https://support.nepton.com/hc/article_attachments/35364810358301)  
  
Adding the new setting group is finalized by clicking **Save** -button.
## Create from template
Setting groups can also be created based on existing groups or ready-made templates. We recommend that existing customers, however, create empty setting groups so that they always have all the desired settings. When using templates, it can be more difficult to get the desired interpretation of working hours when you cannot directly see what settings have been set.
### Basic templates
The service has ready-made templates for each environment, which have some TESs-compliant settings predefined. We recommend using templates only with the project manager during the service implementation phase!
When creating a new setting group from a template, you can choose whether to copy the subgroups of the selected template at the same time. This is done by selecting Copy subgroups. If this option is active, all groups that are subgroups of the settings group selected in Create from template will be copied as a subgroup when creating the setting group.
![](https://support.nepton.com/hc/article_attachments/35364810359581)
### Copy an existing setting group
It is also possible to copy an existing setting group from your environment. All setting groups created in the environment are displayed in the "create from template" menu under the subheading "Existing setting groups".
![](https://support.nepton.com/hc/article_attachments/35364810361117)
Unless the new settings group has a completely different parent group than the group being copied, it is recommended to create a new settings group from scratch and set it as a subgroup of the desired settings group instead of copying it.
### Copy from another customer environment
This option is only available if you have access to another client environment.
Use this option if you want to copy an existing setting group from another customer environment. You must know the system ID of that setting group to be able to copy it.
The system ID of a setting group is displayed in the setting group details. For more information, see [this article](<https://support.nepton.com/hc/en-gb/articles/360002558758>).
![](https://support.nepton.com/hc/article_attachments/35364836061213)  
If "Create from system identifier" is selected, "Create from system identifier" - field appears below the "Create from template" field. The system identifier of the other customer's setting group is inserted into the "Create from system identifier" input field. Note that if a setting group is copied from another customer environment, the system will not copy settings that are related to custom event and absence types, or settings that are related to integration rulesets.  
  
![20210107-support-add-setting-group-en-3.PNG](https://support.nepton.com/hc/article_attachments/360015672537)
