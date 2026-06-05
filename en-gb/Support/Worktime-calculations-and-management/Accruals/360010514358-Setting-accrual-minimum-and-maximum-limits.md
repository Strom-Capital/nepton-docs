---
id: 360010514358
title: Setting accrual minimum and maximum limits
url: https://support.nepton.com/hc/en-gb/articles/360010514358-Setting-accrual-minimum-and-maximum-limits
locale: en-gb
category: Support
category_id: 360000446658
section: Accruals
section_id: 360000705197
section_path:
- Worktime calculations and management
- Accruals
labels:
- maksimisaldo
- saldoleikkuri
promoted: false
updated_at: '2026-02-12T11:12:24Z'
edited_at: '2026-02-12T11:12:24Z'
---

# Setting accrual minimum and maximum limits

This article guides you through on how to set minimum and maximum limits to accruals, and how these limits behave.
Please note, if there is a minimum or a maximum limit for accrual, the real accrual value is not shown on the calendar, when the limit has been reached. However, when using the maximum limit, it is possible to direct the hours exceeding it directly to, for example, salary or other accrual.
## Setting minimum and maximum limits for accrual
This article uses balance accrual as an example, but the same limits can be set for any accrual. Balance limits can be set either to working community or setting group level. The setting can be found in **Worktime > Administration > Working community / Setting group settings > Work hours > Accruals** **> Balance > Limits and adjustments.** Minimum limit is set with setting "maximum negative balance at the beginning/end of the day" and maximum limit is set with the setting "Maksimum positive/negative balance at the beginning/end of the day".
![](https://support.nepton.com/hc/article_attachments/25465114675101)
In exceptional situations balance maximum/minimum limits can also be set in Person's settings: **Worktime > Persons > Person's settings > Work hours > Accruals > Calculation settings: Balance > Maximum positive/negative balance at the beginning/end of the day**. This can be necessary in situations where exceptional limits to balance are temporary and concern only few people. It is highly recommended to document any changes made in person's settings, so they are easy to trace later.
Please note, that all changes should be done using the [validity tool.](<https://support.nepton.com/hc/en-gb/articles/360002559358>)
## Behavior of negative and positive limits
The settings regarding behavior of balance limits can be used to direct what happens when the set limit has been reached.
![](https://support.nepton.com/hc/article_attachments/25465662169885)
### Handling of the portion exceeding the negative balance limit
By default, the behavior of negative balance limit is "the limit can be exceeded i.e. warning only". This means, that when the negative balance limit is reached, a yellow [warning triangle](<https://support.nepton.com/hc/en-gb/articles/360002560618>) will show in the user's calendar. The hours can still go over the limit. 
The setting can also be set to "The limit cannot be exceeded". In this case calculations stop, when the limit has been reached, and the total accrual value cannot be lower. Note: In this case, the real accrual value is not shown on the calendar, the cut hours can be seen in report "Managerial balance changes". The same also applies to the maximum limit if the setting "limit cannot be exceeded" is used.
If the setting is "The limit cannot be exceeded" and the limit is reached, no regular time will be formed in the calendar to be borrowed from the accrual, because nothing can be borrowed from the accrual anymore.
#### Transferring negative excess hours to salary or another accrual
It is possible to specify that hours exceeding the negative balance limit are deducted from salary or some other accrual. This is done in the "Behaviour of the negative balance limit" setting with the option: "Transfer excess to: accrual X". If the setting is set to Transfer excess to salary, Compensationtype = 'UnpaidOverMinAccrualLimit' will appear for the day the limit is exceeded, and this can be added to salary rules to be picked up and a negative value moved to salary, therefore reducing the salary to be paid.
#### Example 1. The negative balance limit is reached in the middle of the workday
For example, it has been selected that hours exceeding the balance limit are transferred to the bank accrual and the negative balance limit has been set to 40 hours. The balance of the person in the example image reaches the negative balance limit on Wednesday, January 21, when -40 hours are reached from the balance limit when borrowing the day's regular working hours. 5,5 hours can be borrowed from the balance, after which its limit is reached and the final obligation for the working day, i.e. 2 hours, is subtracted from the bank accrual.
![](https://support.nepton.com/hc/article_attachments/33598735994141)
If the amount exceeding the limit is deducted from another accrual, a warning triangle will appear in the calendar, indicating which accrual the limited hours have been transferred to.
![](https://support.nepton.com/hc/article_attachments/33598735998237)
For negative balance limit, there is also a setting to manage how it behaves in terms of future accrual leaves. The options are the same as above, the limit can either be exceeded with a warning, or it can not be exceeded.
### Handling of the portion exceeding the positive balance limit
By default, the behavior of positive balance limit is "the limit can be exceeded i.e. warning only". This means, that when the negative balance limit is reached, a yellow [warning triangle](<https://support.nepton.com/hc/en-gb/articles/360002560618>) will show in the user's calendar. The hours can still go over the limit. 
The setting can also be set to "The limit cannot be exceeded". In this case calculations stop, when the limit has been reached, and the total accrual value cannot be greater. Note: In this case, the real accrual value is not shown on the calendar, the cut hours can be seen in report "Managerial balance changes". The same also applies to the maximum limit if the setting "limit cannot be exceeded" is used.
#### Transferring positive excess hours to another accrual
The setting "**Behaviour of the maximum positive balance limits"** can be used to direct hours exceeding the limit to another accrual or salary.
![](https://support.nepton.com/hc/article_attachments/25465123298333)  
  

#### Example 1: An event with overtime targeting the balance, but accrual has exceeded its maximum limit
In this example, the behaviour of the maximum positive balance limits has been set to "transfer excess to: Salary". The maximum balance limit is 40 hours.
![](https://support.nepton.com/hc/article_attachments/25465123299613)
On Tuesday the balance is 38h, and the person has logged 11h30min worktime with overtime to balance. Out of these hours 7h30min is regular time, and as the overtime target is balance, the exceeding hours are going into balance, until it reaches it's limit. After the limit has been reached, the rest is being paid in salary. The overtime breakdown in calendar shows where the hours are being targeted at:
![](https://support.nepton.com/hc/article_attachments/25465114683037)
By clicking on the arrows the breakdown shows further details on how the overtime has been divided and percentages. In this example the first 30 min is additional work targeted to balance, and then daily 50% overtime for 1h, so 2 hours has been moved to balance. At this stage the balance maximum limit has been reached, and the rest, 1 hour of daily 50% and 1h30min of daily 100% is being paid in salary. By default a yellow warning triangle will also appear to calendar to inform of the maximum limit being reached.
#### Example 2: Limiting an accrual maximum balance on a specific date and paying the excess as salary
Limits can also be configured on arbitrary dates (e.g. at the end of some agreed holiday period) so in the instance where there might not be any overtime on the day to convert, the time is exportable using the integration rulesets as compensation type "PayOverAccrualLimit" (in UserSalaryData). This includes automatically cut accrual hours due to limits. In order to get this compensationtype to show in usersalarydata, the setting "behaviour of the maximum positive balance limits" must be set to "transfer excess to: Salary"![](https://support.nepton.com/hc/article_attachments/22288697441821)  
The example above shows 10 hours of bank being paid due to the maximum bank limit of 0:00 being applied on 31.12.
