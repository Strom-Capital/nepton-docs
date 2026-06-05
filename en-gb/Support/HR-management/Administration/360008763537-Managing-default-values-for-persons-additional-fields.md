---
id: 360008763537
title: Managing default values for persons additional fields
url: https://support.nepton.com/hc/en-gb/articles/360008763537-Managing-default-values-for-persons-additional-fields
locale: en-gb
category: Support
category_id: 360000446658
section: Administration
section_id: 360004488558
section_path:
- HR management
- Administration
labels: []
promoted: false
updated_at: '2024-08-23T10:03:02Z'
edited_at: '2020-11-12T08:24:33Z'
---

# Managing default values for persons additional fields

Setting a default for persons additional fields allows you to configure a value which will be used whenever a new person is created. This can be a big time saver if you have a piece of information that should always be the same for all persons, or you always want a particular starting value for all persons, or it is a value which is rarely different between persons in your organisation. This feature can also be used in conjunction with the person export if you wish a column to have a fixed value. More information about persons additional fields [here](<https://support.nepton.com/hc/en-gb/articles/360002430918>).
## How to set a default value
A default value can be configured for any persons additional fields which are not set to be unique for every person. You can view and edit currently configured defaults from Employees > Administration > Persons additional fields. 
You can set a default value when creating a new additional information field, or you can edit an existing field by clicking the pencil button to the left of its name. Simply enter the desired default value into the relevant column. The value you enter will be checked to ensure it is suitable, before saving.
**Please note** that default values only affect newly added persons and that setting or editing a default value for a field, does not automatically update any existing person. See the 'Mass update existing persons with a new default value' heading below, if you wish to update persons with a new default value. 
![Adding_new_info_type_default_value.PNG](https://support.nepton.com/hc/article_attachments/360008540678/Adding_new_info_type_default_value.PNG)
### An example
When a new person is added via Employees > Persons > Persons > Add person, or via the Person import feature, all person information fields having a default value set, are automatically filled. For instance, in the following screenshot 'First aid training completed' has a default value of "yes". This means that whenever a new person is added, a value of "yes" will be set for the 'First aid training completed' field for that person.
![info_type_values_default.PNG](https://support.nepton.com/hc/article_attachments/360008540658/info_type_values_default.PNG)
## Mass update existing persons with a new default value
When adding or changing a default value for a field, it is important to note that existing persons will not be updated with the new default. If you wish to set this new value for existing persons in your environment, this can be achieved by using the person import feature.
  1. Visit Employees tab
  2. Apply any filters you wish, to limit the persons you will update
  3. Click the 'Export to importable excel' button 
     * Depending on the number of persons in your environment, and your internet connection, this can take some time to generate and download.
  4. Open the excel and enable editing
  5. Remove all columns from the excel except for Username, and the field you wish to set the default value for 
     * Note that fields without any values set will automatically be hidden when the excel is opened. To find these, select all columns, right-click and choose 'Unhide'
  6. Add the new default you wish to set into every person's row
  7. Save your changes
  8. Return to Nepton, and visit Employees > Persons > Import persons
  9. Follow the instructions and check that the expected number of persons will be updated before clicking Import.


## Defaults and the person import
When adding persons using the person import via Employees > Import persons, or when persons are added by a scheduled person import, default field values will be used unless a value is provided in the import file.
As such, it is not necessary to include fields which have default values configured in an import file, unless you wish to set a different value than the default.
