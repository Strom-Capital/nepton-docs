---
id: 360002558617
title: Expected work times
url: https://support.nepton.com/hc/en-gb/articles/360002558617-Expected-work-times
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
- oletustyöaika
- oletustyöajat
promoted: false
updated_at: '2026-03-13T10:55:21Z'
edited_at: '2026-03-13T10:55:21Z'
---

# Expected work times

Expected work times determine the hours when overtime can be formed, for example in situations where a person leaves for sick leave in the middle of the day, or if work has been done before the start of the actual work hours. In the worktime calculations, regular working hours fall inside the expected work times. The worked time that is outside expected work times is interpreted with the overtime settings. The excess time is compensated based on the [overtime target](<https://support.nepton.com/hc/en-gb/articles/360002481617-Event-overtime-targeting>) on the event.
## Setting up Expected work times
Expected work times can be defined in Worktime section either on working community or setting group level: Worktime > Administration > Working community / setting group settings > Work hours > Expected work times. Please note, that all setting changes should be made using [validity control](<https://support.nepton.com/hc/en-gb/articles/360002559358-Using-the-validity-control-in-Worktime>).
In order to turn the expected work times on, first set 'Yes' to the setting 'Use expected working times'. After this you can define the expected work times for each day individually, Mon-Sun. It is possible to set two values for each day. This might be necessary when work is done overnight. 
In the example below the excepted work times have been set from 8am to 4pm from Monday to Friday.
![](https://support.nepton.com/hc/article_attachments/19949811109533)
If expected work hours are in use, they can be seen in the person's calendar view when clicking on the date:  
![](https://support.nepton.com/hc/article_attachments/19949843379485)
### Setting expected times for one person for one day
Sometimes it is necessary to modify the expected working hours in a certain situation. Exceptional expected working hours for a day can be set for a single person. This can be done in the person's calendar view, when clicking on the correct date. After that, click on the expected work times. This opens a new window where you can define exceptional expected work hours for the day in question, to apply only to the person in question.
## Expected work times and overtime interpretation
Now that the settings are set, a person can earn overtime even if regular work hours aren't filled. Below are examples of situations where expected work hours are set to 8-16:
![](https://support.nepton.com/hc/article_attachments/19949811113501)
Tuesday 4.6. Work has been done from 6am to 3pm. Overtime target is "overtime to salary". Because the expected work times start at 8am, the first two hours are interpreted as overtime. Regular working time starts at 8am. As the work was finished at 3pm, the regular working hours haven't been filled, but are one hour short. Therefore that one hour is borrowed from balance at the end of the day.
![](https://support.nepton.com/hc/article_attachments/19949811116061)
Wednesday 5.6. The work done is the same as previous day, but this time the overtime target is "hour to hour - balance". Therefore no overtime is formed, but at the end of the day one hour is added to balance as work exceeds regular time by one hour.
![](https://support.nepton.com/hc/article_attachments/19949811117597)
Thursday 6.6. Work has been started at 7am with the overtime target "overtime to salary". During the day the person has got sick, and started sick leave at 12pm. As expected work times begin at 8, the first hour is counted as overtime.
![](https://support.nepton.com/hc/article_attachments/19949843392797)
Without expected work hours the week in question would look like this, overtime would not be earned before regular working hours are full:
![](https://support.nepton.com/hc/article_attachments/19949811122333)
