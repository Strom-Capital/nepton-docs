---
id: 360002558757
title: Lunch break settings
url: https://support.nepton.com/hc/en-gb/articles/360002558757-Lunch-break-settings
locale: en-gb
category: Support
category_id: 360000446658
section: Calculation settings
section_id: 360005872258
section_path:
- Worktime calculations and management
- Calculation settings
labels:
- ruoka
- lounas
- lounaan
- lounastauko
- lounaskirjaus
- työnantajan tarjoama lounas
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-07-30T08:47:44Z'
---

# Lunch break settings

**This article describes how to use the Lunch break setting under Working community settings.**
Lunch break settings can be defined at the Working community settings or Worktime roles. The definition can be found in Work hours - Lunch break.
If Planning is used, the Lunch break settings can be defined by Locations-basis, (under Planning) in which case they do not necessarily need to be defined at all in the Working community or Worktime roles settings. Help can be found [here](<https://support.nepton.com/hc/en-gb/articles/360015675918-Shift-planning-by-location>).
Configurations can also be made for user-specific settings. However, we recommend that you always make all configurations at the Working community or Worktime roles settings.
## Automatically set and subtract the default duration of a Lunch break from working time
If you want to set a default duration for a Lunch break, you can specify a length of the Lunch break for the default duration of the Lunch break, which is automatically deducted from the length of the working day if no meal break is recorded. This selection is made in the Assumed lunch break duration field.
Assumed lunch break definitions can also be different for the default duration if you want the duration to deviate from normal, for example on a specific day. In this case, select Exceptions.
Exceptions settings can specify exceptions to the automatic reduction of the Lunch break if the first Work event of the day (or an event similar to the Work event type) is started at a certain time or after a certain time.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4410084382225/mceclip2.png)
You can also set a threshold of how much payable work time should be earned on the day before assumed lunch is deducted. For example, if "Minimum work time before lunch is assumed" is set to 6:00 and the user records 5:59 hours of work, then no assumed lunch is created, if they record 6:00 of work with no manual lunch events, then assumed lunch will be deducted from the pay resulting in 5:30 of paid time (assuming there was a 0:30 assumed lunch break setting).
## Remove the default Lunch break duration setting and automatic deduction from working hours
The default duration of a Lunch break and the automatic reduction of working time can be deactivated by entering 0 minutes and Not set (in this case care must be taken that the configuration has not been made in a higher level, in which case it could be inherited).
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4406957063825/mceclip2.png)
## Increasing short lunches to set length
Stamps for short Lunch breaks can be extended to the desired length in Increase short lunches to length. In the lower field, it can also be specified that the zero length Lunch break stamps are extended to this same length. If it is set that zero-length lunches are not increased, an automatic Lunch break can be prevented by setting a zero-length Lunch break.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4410077862801/mceclip3.png)
The food break is not extended to the desired length if the amount of payable work/absence time does not exceed the value of "_Minimum work time before short lunches are increased in length_ ". For example, if this threshold is set to 6:00 with "Increase short lunches to length" set to 0:30, and the user has a 6:00 work event with a 10 minute overlapping lunch, the lunch break is not extended as they have only recorded 5:50 of payable work. If they record 6:10 of work with a 10 minute overlapping lunch break then the threshold is reached, the food break is extended by 20 minutes (from the end), and they earn 5:40 of paid work.
## Limiting lunch hour length
Stamps for long lunch breaks can be reduced to the desired length with "Reduce long lunches to length" setting. In this case, the lunch break will not exceed the desired length.
Note that this also affects the amount of work rises earned from lunch breaks.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4407852962449/mceclip2.png)
## Duration of paid lunch break
The duration of a paid lunch break determines the paid length of the lunch break. Excess time is not counted as normal working time and does not increase balance accumulation, for example.
![mceclip5.png](https://support.nepton.com/hc/article_attachments/4410069546897/mceclip5.png)
Lunch breaks with pay can also be configured to be earned after a certain threshold of paid work/absence on the day. This threshold can be reached after deductions in the work time are made as a result of Lunch break events, assumed lunches, and extended lunches. For example, if paid lunches are only earned after 6:00 of work time, and the user records a 6:00 work event of which 0:30 is assumed lunch, then no paid lunch is earned. If they mark 6:30 of work of which 0:30 is assumed lunch, then they reach the threshold and paid lunch is earned for the duration of the assumed/recorded lunch specified in "_Duration of paid lunch break_ "
## Default time of lunch break
The default time of the lunch break is displayed in the calendar view at the time of the food break, if no food break has been recorded.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4406964542737/mceclip3.png)
## Maximum amount of assumed lunch that contributes to accrual if worked
This setting allows you to specify how much a Lunch break event type can be used to accrue either balance, bank, flexible, overtime balance, or work time shortening leave.  
  
![mceclip4.png](https://support.nepton.com/hc/article_attachments/4406964780049/mceclip4.png)
## Assumed lunch calculated from event types
This setting allows you to specify from which event types the automatic lunch break will be deducted. The default settings are explained by event type directly in the view. The default configuration is used if the configuration is inherited from a higher level and no configuration has been made at the higher level. If you want to prioritize an event type during which the Assumed lunch break is set, it should be set as High Priority. No event type has a High Priority by default. The work type event type has Normal priority. Not earned means not being subtracted.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4406959544593/mceclip0.png)
Be sure to record all setting changes through the validity function so that any calculations based on previous settings do not go wrong.
