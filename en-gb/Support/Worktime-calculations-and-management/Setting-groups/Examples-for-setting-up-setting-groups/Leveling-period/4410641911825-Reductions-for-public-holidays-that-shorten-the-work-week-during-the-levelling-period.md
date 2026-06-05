---
id: 4410641911825
title: Reductions for public holidays that shorten the work week during the levelling
  period
url: https://support.nepton.com/hc/en-gb/articles/4410641911825-Reductions-for-public-holidays-that-shorten-the-work-week-during-the-levelling-period
locale: en-gb
category: Support
category_id: 360000446658
section: Leveling period
section_id: 4410638658833
section_path:
- Worktime calculations and management
- Setting groups
- Examples for setting up setting groups
- Leveling period
labels: []
promoted: false
updated_at: '2025-07-03T11:09:16Z'
edited_at: '2025-07-03T11:09:16Z'
---

# Reductions for public holidays that shorten the work week during the levelling period

These instructions explain how public holidays falling within the levelling period are interpreted in work time calculations. Similar to other working time arragements, it is possible t o define how public holidays are treated when they fall within the levelling period. The settings for interpreting public holidays in the levelling period can be found under setting group settings **Work hours - > Accruals -> Levelling period hours -> Reductions to levelling period limits on public holidays**.
The interpretation of public holidays is usually already defined in working community settings, but if needed, it can be specified separately in the levelling period settings group under **Work hours - > Public holidays section**, with instructions available [here](<https://support.nepton.com/hc/en-gb/articles/360002558797>).
Public holidays that shorten the work week can be set to reduce the following levelling period limits:
  * Maximum regular working time
  * Maximum additional work
  * Maximum 50% overtime


![](https://support.nepton.com/hc/article_attachments/28583919038749)
More detailed instructions on configuring overtime calculation in the levelling period can be found [here](<https://support.nepton.com/hc/en-gb/articles/4410630282257>).
### Example 1
A two-week levelling period with the following limits:
  * Additional work is earned after a total of 75 hours
  * 50% overtime is earned after a total of 80 hours
  * 100% overtime is earned after a total of 100 hours
  * Hours are no longer compensated after a total of 300 hours


And the following public holiday reductions:
  * Maximum regular working time: 7,5 hours
  * Maximum additional work: 0,5 hours
  * Maximum 50% overtime: 2 hours


The levelling period includes two public holidays that shorten the workweek, for example, Good Friday and Easter Monday. The public holidays would reduce the levelling period limits as follows:
  * Additional work earned after: 60 hours, holiday reduction 2 x 7,5 hours
  * 50% overtime is earned after: 79 hours, holiday reduction 2 x 0,5 hours
  * 100% overtime is earned after: 96 hours, holiday reduction 2 x 2 hours


### Example 2
A two-week levelling period with the following limits on work days in period:
  * Average length of work day: 7,5 hours
  * Maximum additional work compensated per day: 0,5 hours
  * Maximum 50% overtime compensated per day: 2 hours
  * Maximum 100% overtime compensated per day: 10 hours


And the following public holiday reductions:
  * Maximum regular working time: 7,5 hours
  * Maximum additional work: 0,5 hours
  * Maximum 50% overtime: 2 hours


The limits for the entire two-week period would be:
  * Maximum regular working time: 75 hours
  * Maximum additional work: 5 hours
  * Maximum 50% overtime: 20 hours
  * Maximum 100% overtime: 100 hours


The levelling period includes two public holidays that shorten the work week, for example, Good Friday and Easter Monday. The public holidays would reduce the levelling period limits as follows:
  * Maximum regular working time: 60 hours, holiday reduction 2 x 7,5 hours
  * Maximum additional work: 4 hours, holiday reduction 2 x 0,5 hours
  * Maximum 50% overtime: 16 hours, holiday reduction 2 x 2 hours


### Example 3
If the outcome of Example 1 is to be aligned with Example 2, the public holiday reductions must be set as follows:
  * Maximum regular working time: 7,5 hours
  * Maximum additional work: 8 hours
  * Maximum 50% overtime: 10 hours


Then the public holidays would reduce the levelling period limits as follows:
  * Additional work earned after: 60 hours, holiday reduction 2 x 7,5 hours
  * 50% overtime earned after: 64 hours, holiday reduction 2 x 8 hours
  * 100% overtime earned after: 80 hours, holiday reduction 2 x 10 hours
