---
id: 360002596797
title: Adding events in calendar view
url: https://support.nepton.com/hc/en-gb/articles/360002596797-Adding-events-in-calendar-view
locale: en-gb
category: Support
category_id: 360000446658
section: Event recording
section_id: 360000934997
section_path:
- Work events
- Event recording
labels:
- NEPTONNEEDSREVIEW
- kellottaminen
promoted: false
updated_at: '2026-02-27T08:58:41Z'
edited_at: '2026-02-27T08:58:41Z'
---

# Adding events in calendar view

Adding an event can be done in multiple ways. This article will walk you through adding an event in the calendar view.
You can either enter all the event details at once, or start the event with just the start time and later complete and end it.
## Starting an event
1\. Click on the date of the day you want to make an entry for. A new window will open next to the day, where you can see the day's information and add new events. Click **Add event**.
![](https://support.nepton.com/hc/article_attachments/30001021673117)
  
2\. The **Add Event** button will open a new pop-up window:
![](https://support.nepton.com/hc/article_attachments/30001021675933)
3\. The [default event type](<https://support.nepton.com/hc/en-gb/articles/360002558717>) is Work, unless otherwise specified. The event type to be recorded is selected from the drop-down menu using the arrow. The event types are divided into three categories; Work, Absence and administrative events. Administrative events are only visible to the administrator or another person who has been granted sufficient access rights.
![](https://support.nepton.com/hc/article_attachments/34216683314205)
4\. By default, the event times are 08:00-16:00, unless[ otherwise specified](<https://support.nepton.com/hc/en-gb/articles/360008777997>). The event can be started with just the start time, leaving the end time blank, in which case the event will roll as active until it is stopped, or it can be given an end time as well. By clicking on the green arrow next to the start time, the current time will be the start time of the event. If there is an event for the day already, Nepton suggest the end time of the previous event to the new event.
5\. It is also possible to write a comment for the event in the Note field. Additionally, depending on the settings, project allocation, overtime target, and possible supplements and attachments can be added to the event.
6\. Save the entry from the **Save** -button, after which it is visible in the calendar.
## Using Quick Events
If quick start buttons have been defined in the service, a specific event type can be started directly from such a button. Quick starts appear in the calendar and table view when you click on the date of the desired day and a window opens next to it:
![](https://support.nepton.com/hc/article_attachments/30001021679133)
Quick starts can have predefined content, so the event can already have everything you need (such as project allocation, overtime target) ready. Therefore, event registration is faster when you just start the event. The quick start event starts in real time if you press the 'Start' button highlighted with an arrow, or the event editing window can be opened from the + sign in front of it if you want to make changes to the predefined content, or if you want to start the event in a time other than real time.
## Targeting work to project
The service allows you to enable work allocation to projects. Project is the service's generic name for an object, but projects can be used to target work for customers, orders, cost centers, and so on. The interpreted work time is targeted for the project on the event, and it is available in reporting and integrations.
An event can be targeted to one or more projects. The project targeting can specify the amount of work done either as a percentage or in hours. If no information is set, all worked time interpreted from the event is targeted to the project in question. It is also possible to record two or more projects, each with 100% project targeting. Please note that events can only be targeted to the lowest-level projects.
Internal and public notes can be written to projects. Notes set for projects are displayed in the user interface and in the Hours by Person report in project reporting. The Note field of the event is also displayed in the report in question.
Notes can be used, for example, to describe the content of the work or to record the billing basis for the work. The note fields of project lines are visible to everyone and their visibility cannot be specified. Notes can be fetched using rule sets in integrations.
![](https://support.nepton.com/hc/article_attachments/34216683318557)
When targeting work to project, the projects that have been used most frequently in the last two months are displayed as a shortcut. This two-month time window is based on the day for which the event and the project targeting to it are performed. For example:
A Work event is created and the project targeting is Project A for the current day.
The most frequently used projects are displayed in a two-month time window, counting backwards from the current day.
The most frequently used projects are arranged so that the most frequently used ones appear first in the list. If there are more than 20 most frequently used projects, only the 20 most frequently used projects are displayed as a shortcut. All projects can be browsed or searched regardless of whether a project is displayed as a shortcut or not.
![](https://support.nepton.com/hc/article_attachments/34216677155869)
## Overtime target
Depending on the rights and settings, it may be possible to choose overtime target for an event. The overtime target is selected under "Overtime". Clicking this opens a menu from which you can select the desired target for the event.
![](https://support.nepton.com/hc/article_attachments/34216683319709)
## Adding a supplement
[Supplements ](<https://support.nepton.com/hc/en-gb/articles/360002559637>)can also be added to an event. Supplements are allowances that are manually added to an event. The supplements drop-down menu opens a search for all available supplements. The supplement shows the unit for entering the value (euros, pieces, decimal, integer), a comment field, and a date field, based on supplement settings.
![](https://support.nepton.com/hc/article_attachments/34265729301405)
## Adding an attachment
Attachments can also be added to the event. This function is used especially with the travel invoice event. We do not recommend saving medical certificates to Nepton. The attachment can be uploaded from the device to Nepton under the "Attachments" heading.
![](https://support.nepton.com/hc/article_attachments/34265729306525)
Once an attachment has been added to an event, it is shown in calendar view with paperclip icon:
![](https://support.nepton.com/hc/article_attachments/34265729309085)
**Attachment restrictions**
File size:
Maximum attachment size: 2 MB  
Maximum number of attachments per event: 20  
Maximum total attachment size per event: 8 MB
**File format**
Supported file formats are:
  * Excel
  * Html
  * Image
  * Pdf
  * Power Point
  * Text
  * Word
  * Zip


## Finishing an event
1\. In the calendar view or table view, click on an unfinished event and select Stop from the pop-up window or alternatively Edit, which allows you to select the end time in the window that opens.
![](https://support.nepton.com/hc/article_attachments/30000994856605)
Different worktime roles can be defined with different [rights](<https://support.nepton.com/hc/en-gb/articles/360002554338-Worktime-roles>) in Nepton. All functions in this article might not be in use in your environment in Nepton. Please contact your company Nepton administrator if you are not sure your company's practices.
