---
id: 25397332335773
title: Best practices for ruleset modifications
url: https://support.nepton.com/hc/en-gb/articles/25397332335773-Best-practices-for-ruleset-modifications
locale: en-gb
category: Support
category_id: 360000446658
section: Rulesets
section_id: 360000827378
section_path:
- Integration
- Rulesets
labels:
- liittymät
- työajan liittymät
- poimintasäännöt
- sääntöjoukot
- rulesets
promoted: false
updated_at: '2025-03-27T13:22:18Z'
edited_at: '2025-03-27T13:22:18Z'
---

# Best practices for ruleset modifications

This article describes how to manage rule sets correctly. The article provides tips that facilitate change management and the rapid implementation of a previous rule set, if for some reason you do not want to implement the new rule set as is. This article only touches rulesets for data extracted from Nepton (e.g. salary data, absences, holidays, PowerBI). Rulesets are generally built as high as possible in the setting group structure in Nepton: either at the Working Community settings level or in the highest setting groups. You can access rule sets via **Worktime > Administration > Working Community Settings > Integrations: Integration ruleset** or **Worktime > Administration > Setting groups, select the setting group you wanted and its settings > Integrations: Integration ruleset.**
## Changing a ruleset and keeping old ruleset rule in history
When changing a ruleset rule, it is important to note that the old rule, which has already been found to be working, is left "retained" in the history.
  1. Select the desired rule along the path mentioned above and copy the old rule in its entirety using the CTRL C key combination.
  2. Go to the rule validity function field from the button that looks like a calendar icon on the right side of the ruleset rule box  
  
![](https://support.nepton.com/hc/article_attachments/25559426027293)
  3. The Validity tool function opens a new view showing the currently valid rule. Set the **Valid to** date for the old rule (this should be either at the end of the month or at the end of the payroll period, so that the rule does not change in the middle of the payroll period). It is important that the validity of the old rule ends before the new rule starts. If the validity periods overlap, Nepton follows the validity period of the old rule.
  4. Press the **"Add"** button to add its own line for the new rule.
  5. Paste the old rule you copied in step 1 into the view that opens (for example, with the CTRL V key combination). Also make the desired changes to the rule here, if you are making changes in the user interface. If you are using another application to change the rule, paste the changed, new rule into this field directly from the other application.
  6. Set the **Valid from** date for the new rule. This date must be the day following the end date of the old rule, if the intention is that there will be no break between the old and new rules.  
  
![](https://support.nepton.com/hc/article_attachments/26177499481629)  
  

  7. Add a comment at the top of the new rule that contains a detailed description of **what** changes were made, **when** , at **whose request** , and **who** made the change. You can add a comment to a rule by using two dashes (--) at the beginning of the line, this prevents the comment from affecting the extraction rule itself. See an example of adding a comment below.  
  
![](https://support.nepton.com/hc/article_attachments/26177437803037)  
  

  8. When you are satisfied with the changes you have made, finally press the **Save** button in the validity function window to apply the changes you have made.
  9. After making the changes, it is also essential to test that the desired changes work correctly. You can test the new rule in its entirety by running the application in preview mode for selected test or example persons. Instructions for running working time applications can be found in our support service [here](<https://support.nepton.com/hc/en-gb/articles/360002492898-Worktime-integrations>)
