---
id: 360002430918
title: Managing persons additional fields
url: https://support.nepton.com/hc/en-gb/articles/360002430918-Managing-persons-additional-fields
locale: en-gb
category: Support
category_id: 360000446658
section: Administration
section_id: 360004488558
section_path:
- HR management
- Administration
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-11-11T13:01:53Z'
edited_at: '2026-11-11T11:51:40Z'
---

# Managing persons additional fields

In the **Administration** tab of the **Employees** section, it is possible to add additional data fields that appear in the employees’ details. Additional data fields can be of different types, for example, date, text, or multiple-choice fields. For each field, different rights can be given on who can read or edit the field and whether the field is mandatory and what ‘s the default value. More about setting a default value [here](<https://support.nepton.com/hc/en-gb/articles/360008763537>).
## Adding a new additional field
1\. Go to **Employees** section.  
2\. Go to **Administration** and open **Persons additional fields.**  
3\. Choose **Add field.**  
![](https://support.nepton.com/hc/article_attachments/40580495816349)  
  
4\. Fill in the **name** of the field. The name should be unique and two fields can't have the same name.  
5\. Choose the **field type, units** where the field is shown, **permissions** and whether the field is **mandatory** or not. If the unit is left empty, the field is shown for persons in every unit.  
6\. Once you've added all the information, click **Save**.  
![](https://support.nepton.com/hc/article_attachments/40580495817501)
If you have more than one additional data field, you can use the arrows at the end of the row to change their order. Additional information fields can be modified from the pen symbol next to the row. The additional information field can be deleted from the cross button. Please note that in this case, the data stored in the field will also be deleted for the entire history.
![](https://support.nepton.com/hc/article_attachments/40580495818141)
## ​Using additional fields in online work contracts
Each additional information field can also be used in [online work contracts](<https://support.nepton.com/hc/en-gb/articles/360002590277>). If you want to include the additional Information field in the online work contract, you must specify an identifier in the contract’s identification field. This identifier can be used in an online work contract by specifying the identifier into the HTML code.
**Please note when using additional information fields in online contracts:**
\- The online contract identifier in the additional information field must always be unique. Two different fields cannot have the same name.  
\- The name and code of the drop-down menu options must be unique.  
![mceclip3.png](https://support.nepton.com/hc/article_attachments/360004657358)
## Managing default values for persons additional fields
Setting a default for persons additional fields allows you to configure a value which will be used whenever a new person is created. This can be a big time saver if you have a piece of information that should always be the same for all persons, or you always want a particular starting value for all persons. This feature can also be used in conjunction with the person export if you want a certain column to have a fixed value. 
### How to set a default value
A default value can be configured for any persons additional fields which are not set to be unique for every person. You can view and edit currently configured defaults from **Employees > Administration > Persons additional fields**. 
You can set a default value when creating a new additional information field, or you can edit an existing field by clicking the pencil button to the left of its name. Simply enter the desired default value into the relevant column. The value you enter will be checked to ensure it is suitable, before saving.
**Please note** that default values only affect newly added persons and that setting or editing a default value for a field, does not automatically update any existing person. See the 'Mass update existing persons with a new default value' heading below, if you wish to update persons with a new default value. 
![](https://support.nepton.com/hc/article_attachments/40582869202333)
### An example
When a new person is added via Employees > Persons > Persons > Add person, or via the Person import feature, all person information fields having a default value set, are automatically filled. For instance, in the following screenshot 'First aid training completed' has a default value of "yes". This means that whenever a new person is added, a value of "yes" will be set for the 'First aid training completed' field for that person.
![info_type_values_default.PNG](https://support.nepton.com/hc/article_attachments/40582869202973)
### Mass update existing persons with a new default value
When adding or changing a default value for a field, it is important to note that existing persons will not be updated with the new default. If you wish to set this new value for existing persons in your environment, this can be achieved by using the [person import feature](<https://support.nepton.com/hc/en-gb/articles/360018767498>) by updating person information in bulk as instructed [here](<https://support.nepton.com/hc/en-gb/articles/360019776498>).
### Defaults and the person import
When adding persons using the person import via Employees > Import persons, or when persons are added by a scheduled person import, default field values will be used unless a value is provided in the import file.
As such, it is not necessary to include fields which have default values configured in an import file, unless you wish to set a different value than the default.
