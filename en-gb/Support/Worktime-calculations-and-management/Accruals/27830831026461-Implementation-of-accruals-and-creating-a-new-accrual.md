---
id: 27830831026461
title: Implementation of accruals and creating a new accrual
url: https://support.nepton.com/hc/en-gb/articles/27830831026461-Implementation-of-accruals-and-creating-a-new-accrual
locale: en-gb
category: Support
category_id: 360000446658
section: Accruals
section_id: 360000705197
section_path:
- Worktime calculations and management
- Accruals
labels:
- Työaikapankki
- Pankki
- Saldo
- Liukumasaldo
- työajan lyhennys
- jousto
- kertymät
- joustosaldo
- bank
- balance
- lomarahavapaa
- tasoittumisjakso
promoted: false
updated_at: '2026-02-20T10:17:37Z'
edited_at: '2026-02-20T10:17:25Z'
---

# Implementation of accruals and creating a new accrual

In Nepton, it is possible to set up different accruals either on the working community or setting group level. Custom accruals can also be created for each customer. Accruals can be used to, for example, target work that exceeds regular working hours or other compensation that is not paid in salary. Accrual settings can be found in the Worktime section under **Worktime > Administration > Working Community / Setting Group Settings > Work Hours > Accruals**.
## Standard accruals
The following accruals are available as standard in the service: balance, bank, annual absence, flexible bank, flexible work hours balance, holiday pay leave, levelling period hours, overtime, savings leave, weekly rest and work time shortening leave. By default, all accruals are set to off, and they can be activated for the desired setting group level with setting "Accruals in use":
![](https://support.nepton.com/hc/article_attachments/27832742401821)
When the accrual has been enabled at the desired setting group level, the desired settings are defined for it in "Calculation settings". The same settings open for each accrual when you click on the accrual name. As an exception, standard accruals: balance, bank, flexible work hours balance, flexible bank, holiday pay leave, overtime, savings leave and weekly rest do not have an earnings table or earnings settings rules. This is because the nature of accruals is not one that is earned at certain intervals. When a new custom accrual is created, all possible settings appear for this accrual, including an earnings table. If you do not want the accrual to be earned, leave the earnings table and earnings settings blank.
![](https://support.nepton.com/hc/article_attachments/27832742402845)
Accrual settings are opened up in [this article](<https://support.nepton.com/hc/en-gb/articles/360005073918>).
## Custom accruals
In addition to the standard accruals, you can create your own, custom accruals in the service. This can be done in the Working community level settings under **Work hours > Accruals: Add accrual** (below Calculation settings).
![](https://support.nepton.com/hc/article_attachments/27832736432541)
### Accrual name and code
When the button is pressed, a new window opens, where you can give the accrual a name and code. The code is needed for possible integrations.
The names of custom accruals determine their position in the calendar view and in the settings. Accruals are displayed in alphabetical order based on their name. The original order of custom accruals in the calendar view (and in the settings) is preserved even if the name of a custom accrual is changed later. If an English name is also given when creating an accrual, the English name determines the order.
![](https://support.nepton.com/hc/article_attachments/27832742406301)
Next to the Name field is the "Other languages" button, which you can click to provide a translation for the accrual, so that if a user uses Nepton in another language, they would see the accrual name in the language version assigned to it. For example, an accrual that is named "Testikertymä" in Finnish and "Test accrual" in English would appear as "test accrual" to users who use Nepton in English. If no translation has been provided for the language in which the user uses Nepton, the accrual will be displayed with its original name.
![](https://support.nepton.com/hc/article_attachments/27832742407965)
### Accrual settings
The accrual is created by pressing the "Save" button after the information has been filled in. After saving, the new accrual will appear in the accrual list shown above. The accrual settings can be opened by clicking on the accrual name. The settings are made as needed, for example, you can set whether the accrual is accumulated in hours and minutes or in days. All accrual settings are opened in more detail [here](<https://support.nepton.com/hc/en-gb/articles/360005073918>).
### Accrual related event types
When a new accrual is created, three related event types automatically appear; accrual leave, accrual reset, and accrual change. You can find these in the working community and setting group settings under **Work hours > Event types**:  
![](https://support.nepton.com/hc/article_attachments/27942829002781)
They can be activated for those settings groups that use that accrual.
**Accrual leave** event type is used to mark absence days when the regular working hours should be deducted from that accrual.
**Accrual reset** event type can be used only by users with sufficient [rights](<https://support.nepton.com/hc/en-gb/articles/360002554338>). This event type is used to set the accrual value to a certain value on a certain day. Accrual resets are interpreted at the beginning of the day.
**Accrual change** event type can be used only by users with sufficient [rights](<https://support.nepton.com/hc/en-gb/articles/360002554338>). This event type is used to add or subtract value from the accrual. Accrual changes are interpreted at the end of the day.
### Using the accrual
If the settings specify that the accrual is visible in the calendar, it will appear in the person's calendar view on its own row starting from the day the accrual is enabled in the person's settings group:
![](https://support.nepton.com/hc/article_attachments/27942832172573)
In the example image above, "Test accrual" has been enabled since 4.6. The starting value is 00:00. When the accrual is enabled, it can be used to [target hours exceeding regular working hours](<https://support.nepton.com/hc/en-gb/articles/360002481617>), and accrual leave can be taken into use.
