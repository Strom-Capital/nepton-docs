---
id: 360002558717
title: Default event types and assumed event types
url: https://support.nepton.com/hc/en-gb/articles/360002558717-Default-event-types-and-assumed-event-types
locale: en-gb
category: Support
category_id: 360000446658
section: Event types and absence types
section_id: 360005841257
section_path:
- Work events
- Event types and absence types
labels:
- automaattinen tapahtuma
- automaattikirjaus
- automaatti
- oletustyöaika
- oletus
- oletustapahtuma
- etukäteisleimaus
- ennakkoleima
- automaattileimaus
- työajan automatisointi
- työajan automaattinen täyttö
promoted: false
updated_at: '2026-08-14T08:06:02Z'
edited_at: '2026-01-02T08:37:59Z'
---

# Default event types and assumed event types

The service can be used to define what kind of assumed, i.e. automatic, events are created in different situations.
Default event types can be defined in the Work Time section in either the Working Community Settings or Setting Groups level settings in **Work time > Administration > Working community / Setting group settings > Work hours > Event types. **The configuration can also be done at person level (**Work Time > Administration > Persons**). However, we do not recommend making configurations on person level, as managing them is challenging.
Configurations can be made for two different functions:
![](https://support.nepton.com/hc/article_attachments/32927233128349)
**1\. Default event type when creating a new event**  
Specifies which event type is displayed by default when a new event is recorded. If this settings has not been set, the default event type is Work. This default event type is also mobile quick start event type in addition to the Lunch Break. Read [this article](<https://support.nepton.com/hc/en-gb/articles/360009193677-How-to-edit-mobile-start-page->) for more instructions on how to customize your mobile view quick start.
**2\. Assumed event type on empty work days**  
Defines which event type is created in the person's worktime calendar on days, when the person has a work obligation (length of working day) but the person has not recorded any events. NOTE: The assumed event type can't be automatically formed on public holidays, even if the day has work obligation. The automatic event is created with start and end times defined in the [Rendering Options](<https://support.nepton.com/hc/en-gb/articles/360008777997>). If nothing is specified in the rendering options, an automatic event will occur between 8:00 and 16:00.
The assumed event type on empty business days can be used in the following situations, for example:
  * Individuals who do the same task at the same time every day. In this case, the person does not have to make entries manually, but they are automatically added to the person's calendar.
  * Individuals whose work time isn't monitored, but all work done needs to be reported.
  * Individuals who work part-time in such a way that they have full-day absences during the week and the day of absence varies. In this case, it can be set that an 'Part-time off' event, for example, is added to the days not worked automatically. More about part-time options [here](<https://support.nepton.com/hc/en-gb/articles/360002559018>).


In case a different assumed event type is needed for certain days, an exceptional setting can made:
![](https://support.nepton.com/hc/article_attachments/32927171527453)
In this example. on Saturdays and Sundays Remote Work is the assumed event type. More about exceptional entries [here](<https://support.nepton.com/hc/en-gb/articles/360002560618>). NOTE: The assumed event types can't be automatically formed on public holidays, not even using exceptional settings.
It is also possible to use planned work shift as the base for default event type:
![](https://support.nepton.com/hc/article_attachments/32927233133469)
In this case, the default event is created with work shift begin and end times and the planned event type is used as the event type. Setting exceptions can also be used to specify that the assumed event type only comes from certain types of shifts. The determination can be made based on the shift alias or the planned event type.
If the **Assumed Event Type on empty work days** is set from the start of a person's work contract, some sort of entry must be made in the calendar (such as work or balance reset) to start the calculations. In other words, if you want the assumed event type on empty working days to be valid from 15.5.2024, you can for example, enter work from 08:00 to 08:00, and the default event types are now entered for empty work days, from this day onwards.
We recommend that you perform all configurations in all situations through the [validity control function](<https://support.nepton.com/hc/en-gb/articles/360002559358-Using-the-validity-control-in-Worktime>).
