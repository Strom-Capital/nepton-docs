---
id: 360002559358
title: Using the validity control in Worktime
url: https://support.nepton.com/hc/en-gb/articles/360002559358-Using-the-validity-control-in-Worktime
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels: []
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-03-21T08:52:43Z'
---

# Using the validity control in Worktime

The validity control allows more control over when the value of a setting changes. It also makes it possible to preserve past setting values so that historical data is not changed.
Validity control of rule set rules
The validity control determines the date of the export period from which the rule in question is valid.
For example, a rule that takes effect on April 1, 2025 will not generate events for the data for export period before April 1, 2025.
It is always a good idea to make setting changes using the validity control so that any previous setting history is preserved, and the corresponding calculation does not go wrong due to changing new settings.
The validity control opens from the calendar button associated with the setting.
![Validity1.png](https://support.nepton.com/hc/article_attachments/360010772757)
The example image above is from the Length of work day settings, under Worktime - Administration - Setting groups - Setting group: Desired setting group - Function: Setting group settings - Work hours - Length of work day.
Pressing the validity control marked in green in the image opens a view with information about the current length of work day, as well as possible previous lengths and their validity periods.
![Validity2.png](https://support.nepton.com/hc/article_attachments/360010846898)
The validity control allows you to edit both historical and future calculation settings by changing the validity dates for that value.
In the example in the image, the length of the work day on Monday is to be shortened from 1 September 2016 to 6 hours. This can be done as follows:
  1. Set the end date to 8 hours on August 31, 2016 in Valid to
  2. Add setting value
  3. Set the value to 6 hours and set the Valid from date on September 1, 2016
  4. Click Save to save the changes at the bottom of the window


You can also leave the date value blank, affecting past or future calculations without a start or end time. Such a need may be, for example, if:
  * The value has been valid from the beginning and it is desired that the value has a retroactive effect on the calculation OR there is no need to set an end date for the value, it is valid until further notice.


If necessary, you can clear the existing date value by clicking the date under Valid from and selecting Clear Date in the calendar window that opens.
Please note that the settings will no longer need to be saved again from the Save button on the main page. Saving in the change window is sufficient.
## Defining setting exceptions
For separate instructions on defining setting exceptions that open in the Exceptions section, see [Configure exceptions to settings](<https://support.nepton.com/hc/en-gb/articles/360002560677>).
If a setting has setting exceptions, it is denoted with a yellow star.
The following setting has setting exceptions:
![](https://support.nepton.com/hc/article_attachments/13532530234781)
The following setting doesn't have setting exceptions:
![](https://support.nepton.com/hc/article_attachments/13532528721181)
## Historic values in setting validity
If a setting has historic values in its validity, it is denoted with a blue icon:
![](https://support.nepton.com/hc/article_attachments/13532500387357)
If a setting has both historic values in its validity and setting exceptions, it is shown with the following icon:
![](https://support.nepton.com/hc/article_attachments/13532524177565)
