---
id: 360002559178
title: Hierarchy of calculation settings
url: https://support.nepton.com/hc/en-gb/articles/360002559178-Hierarchy-of-calculation-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- NEPTONNEEDSREVIEW
- hierarkiatasot
- asetushierarkia
- periytyminen
- periminen
promoted: false
updated_at: '2026-04-01T07:09:15Z'
edited_at: '2026-04-01T07:07:46Z'
---

# Hierarchy of calculation settings

The settings in the service work based on different setting levels, so that the setting levels have a hierarchy according to which the settings are inherited from top to bottom. The initial settings are already made during implementation, i.e. they are customized for your own working community and only need to be changed when necessary.
The hierarchy and inheritance of settings are described below.
## Settings in Working community level
The most common rules can be set in the working community level, aka the highest level, for all users. From here they are inherited downwards to setting groups and individual users. You can find these settings in **Worktime > Administration > Working community settings**.
## Settings in setting group level
Settings group settings can be used to make exceptions to working community settings. The setting groups are often made, for example, according to the different TES’ used, in which case each setting group has settings according to the TES. Usually, there is also one highest level setting group, for example 'Finland', where you can define rules that affect all users instead of using the working community level.
The settings made in a setting group apply to all its members, unless they have different settings on a lower level (user settings). Settings are inherited from the upper setting group level to the lower setting group, unless otherwise specified on a lower level. The setting group hierarchy is displayed in the setting group list with the lower setting groups indented below the upper. In the example image below you can see upper setting group level "Finland", under which is "7.5h monthly paid, from hour to hour to balance" and then below it three separate part-time setting groups (osa-aika 50%, 60%)".
![](https://support.nepton.com/hc/article_attachments/28386807397917)
In the example picture, the settings flow from the upper setting group to the Part-time groups, unless different settings have been defined in these setting groups. The setting group "8h monthly paid Mon-Sun" is on the same level as "7.5h monthly paid, hourly to balance" and the rest of the setting groups in the list, so the settings are not inherited from each other. The upper level of all these setting groups is Finland and then Working Community level. The settings group settings can be found in **Worktime > Administration > Settings groups > Function: Settings group settings**.
## Settings for persons
It is not recommended to make too many settings behind individual users as it is easier to manage settings from one location (setting group / working community level). Most settings should come from user's setting group. Settings should be made for a single user only in specific situations, such as a lower accrual limit or different annual leave calculations at the beginning of the employment or a temporarily agreed shorter work obligation. All settings must be made using [the validity tool.](<https://support.nepton.com/hc/en-gb/articles/360002559358>) User settings can be found in **Worktime > Administration > Persons > Function: Person settings**.
Inheriting settings according to the hierarchy described above works in practice so that when the service checks the settings, it first looks for a setting on the user level. If no setting is defined for the user level, the service switches to the setting group level. If there is no setting on the setting group level, the setting used comes from the working community level.
## Preventing inheriting
Inheritance can be prevented in many different ways, depending on the setting.
  * "Enabled" setting: Some settings have an "enabled" setting. This can be used to prevent settings from being inherited from a higher level by setting the "Enabled: No" in the actual setting group. For example: Allowed working hours are enabled at a higher setting group level, but you do not want them to be valid at a lower setting group level. In this case, you can specify that they are not enabled at that setting group level.  
![](https://support.nepton.com/hc/article_attachments/29757335523613)
  * Some settings have an option to select "Do not use parent group setting":  
![](https://support.nepton.com/hc/article_attachments/29757309896989)
  * A text field setting can be prevented from being inherited by storing an empty value in the field header. For example, if you want to prevent the name of a work rise from being inherited to a lower level, you can write some other text in the name field on the lower level, or save an empty field:  
![](https://support.nepton.com/hc/article_attachments/29757309898525)


The exception is integration rules (External Services), where inheritance is prevented by saving an empty value in all three fields: Description, Salary code, and Integration rule.
  * Inheritance of numeric fields can be prevented by clicking the cross icon that appears in the field. For example, inheritance of the length of work day can be prevented this way. In the example in the image, a cross is displayed for Monday, which can be clicked to prevent inheritance. Thursday shows what the setting looks like when inheritance is prevented.  
![](https://support.nepton.com/hc/article_attachments/29757309899421)


Please always use the [validity tool](<https://support.nepton.com/hc/en-gb/articles/360002559358>) when making changes in the settings.
If inheritance is prevented, the setting uses the default value in the service. The default value depends on which field is in question. The default value can be a numeric value (for example, the default working day length is 0 hours, unless otherwise specified), or it can mean that the setting is not valid at all. Several default values comply with the Working Time Act. Please note: Default value is not always 0.
## Exceptional settings inheritance
If a setting has been made on the top level with an exception rule, both of these are inherited to the setting groups below. Inheritance continues until something else is saved in the setting on one of the levels - that is, if something is saved in the main setting, the inheritance is broken, and the exception setting is also not inherited. Inheritance continues only as long as nothing is saved in the same setting on a lower level.
If only an exception setting has been made on the top level, this will be inherited downwards. If an exception setting has also been made on the bottom level, this will not prevent the exception from being inherited from the top level, but both exceptions (both the inheritable and the setting made at the setting group level itself) will be valid at the bottom level. Inheritance can only be prevented by giving the main setting a value, or by overriding the exception from the top level by setting the same exception with a different value at the bottom level.
