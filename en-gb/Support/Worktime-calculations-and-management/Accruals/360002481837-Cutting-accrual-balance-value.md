---
id: 360002481837
title: Cutting accrual balance value
url: https://support.nepton.com/hc/en-gb/articles/360002481837-Cutting-accrual-balance-value
locale: en-gb
category: Support
category_id: 360000446658
section: Accruals
section_id: 360000705197
section_path:
- Worktime calculations and management
- Accruals
labels:
- liukumarajat
- liukumaraja
- saldonylitys
promoted: false
updated_at: '2025-06-09T08:08:19Z'
edited_at: '2025-06-09T08:08:19Z'
---

# Cutting accrual balance value

It might be necessary to cut the value of accrual balance if you want to define a maximum and / or minimum amount (flexible hours) for the accrual value. The settings are made in the Worktime section in either the Working Community or Setting group level. Let's use balance as an example (the same settings can be found under all the accruals):
Navigate to**Worktime > Administration > Working community / Setting group settings > Work hours > Accruals > Calculation settings > Balance > Maximum negative / positive balance.**
![](https://support.nepton.com/hc/article_attachments/27987471843229)
If the settings are defined to take effect at the beginning of the day, the maximum and minimum amount of the balance value is limited before the working day balance calculation. In practice, the limitation is made on the value of the previous day's end balance.
If, on the other hand, the setting is made to apply to the end of the day, the limitation is made after the balance calculation for that day. In this case, information about the change in the balance on that day is lost, and the value at the end of the day cannot be retrieved, for example, for salary integration data.
## Setting a date for balance cut
By using the [validity function](<https://support.nepton.com/hc/en-gb/articles/360002559358>), the day on which the balance value is cut can be flexibly set through a setting exception. In this case, you can specify that the balance is always cut on a specific day, such as the first day of each month.
Open the validity tool. Click Add setting exception and enter the desired value and time of the cut in the Rule field.
Below is an example of a definition that would always cut the balance to zero hours on the first day of April each year at the beginning of the day:
![](https://support.nepton.com/hc/article_attachments/27987471844253)
Another example showing a setting that would cut the balance on several set days a year:
![](https://support.nepton.com/hc/article_attachments/27987471845021)
The date of the balance cut can be flexibly determined by various exception rules. For more information on exception rules and how to use them, see [Configure exceptions to settings](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
