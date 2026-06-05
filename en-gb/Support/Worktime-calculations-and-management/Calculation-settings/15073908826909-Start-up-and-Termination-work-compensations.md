---
id: 15073908826909
title: Start-up and Termination work compensations
url: https://support.nepton.com/hc/en-gb/articles/15073908826909-Start-up-and-Termination-work-compensations
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
edited_at: '2025-05-23T09:22:34Z'
---

# Start-up and Termination work compensations

## Overview
The Start-up and termination work features can be taken into use when Nepton's work shift Planning is in use.
The service can be configured to compensate the employee for work done before the normal shift begin time (Start-up work) and for work done after the normal shift end time (Termination work). 
The purpose of Start-up work is to pay the employees for extra time they spend working before the shifts normal begin time. Sometimes this is recorded as work from a terminal and other times the worker was already working before reaching a terminal to start work (e.g. a mine entrance after changing/briefing rooms).
The purpose of Termination work (aka Washing/Clean-up work) is to pay the employees for extra time they spend after the shifts normal end time. The clocking might be done before they reach the exit, or they might be clocked hours after the shift is scheduled to end.
Example of what a work week might look like with Start-up- & Termination work:
![](https://support.nepton.com/hc/article_attachments/19036101973149)
Note! If start-up or termination work is earned from an event type, the time earned from the event type before the start of a shift and after the end of a shift is limited according to the maximum time that can be earned. Time earned will be limited even if permitted work times are not used.
If start-up or termination work should not be earned from an event type, that can be defined in settings. It is also possible to specify that start-up or termination work is not earned from an event type in situations where a specific overtime target has been defined for the event.
## Start-up and Termination work configuration
The Start-up and Termination work setting can be defined in the **Worktime > Administration > Working community / Setting group settings > Work Hours > Start-up and Termination work** section.
Both minimum amount to earn and maximum amount that earns need to be configured to earn Start-up work or Termination work.
### Start-up work
![](https://support.nepton.com/hc/article_attachments/26899608375965)
  * **Minimum time worked before the shift start to earn start-up work**  
The amount of time that the employee must  _at least_ have worked before the shift begin time to earn start-up work. e.g. if the employee works 29 minutes before the normal shift begin time, no start-up work is earned in this example (see images above).
  * **Maximum time that can be earned before the shift**  
The amount of time that the employee can _at most_ work before the shift begin time and still earn start-up work. e.g. if the employee works 1:30 before the normal shift begin time, only 1 hour of start-up work is earned and 30 minutes is uncompensated in this example (see images above).
  * **Fixed compensation**  
A fixed amount of compensation to pay if:  

    * The employee has worked _at least_ the minimum amount of time required before the normal shift begin time, or
    * The maximum deficit hasn't been exceeded. If the maximum deficit is 30 minutes and work is started 15 minutes late, fixed compensation is paid. If work is started 31 minutes late, fixed compensation is not earned.
  * **Earn fixed compensation without shift** If the setting is set to yes, a fixed amount of start-up work is earned also on days where there is no planned work shift.
  * **Maximum deficit at the beginning of the shift to earn fixed compensation**  
How many minutes late can you start the shift and still earn the fixed compensation for start-up work.
  * **Override event overtime base part target**  
Sets the overtime base part target for start-up work, which overrides the target set in the event.
  * **Override event overtime increment part target**  
Sets the overtime increment part target for start-up work, which overrides the target set in the event.
  * **Start-up work shortens threshold for earning 100% weekly overtime**  
If the setting is on, earned start-up work reduces the threshold for earning 100% weekly overtime. If for example the maximum amount of weekly 50% overtime is 8 hours and there have been 2 hours of start-up work during the week, weekly 100% overtime is earned after 6 hours of weekly 50% overtime have been earned.
  * **Limited by permitted work times**


**Start-up work earned from event type**  
Here you can set which event types you can earn start-up work from. By default, start-up work is not earned from any event type.
**Start-up work earned from event type and overtime target**  
Here you can set which event type and overtime target combinations you can earn start-up work from. For example:
\- If "work" event type should earn start-up work in all cases except when the event overtime target is "overtime -salary", it can be configured as shown in the image above.  
\- If an event type should earn start-up work only when the overtime target of the event is "hour-to-hour - salary", you should add a setting value for this combination with value "Yes".
### Termination work
![](https://support.nepton.com/hc/article_attachments/26899608377501)
  * **Minimum time worked after the shift end to earn termination work**  
The amount of time that the employee must _at least_ have worked after the shift end time to earn termination work. e.g. if the employee works 29 minutes after the shift end time, no termination work is earned in this example (see images above).
  * **Maximum time that can be earned after the shift**  
The amount of time that the employee can at most work after the shift end time and still earn termination work. e.g. if the employee works 1:30 after the shift end time, only 1 hour of termination work is earned and 30 minutes is uncompensated in this example (see images above).
  * **Maximum deficit at the end of the shift that can be filled**  
The minimum amount of time before the normal shift end time that can be filled in with termination work. e.g. if the employee clocks out at 15:29 then the remaining 31 minutes are not filled in this case. However if the employee clocks out at 15:30 then the remaining 30 minutes are filled in with termination work in this case (see images above).
  * **Fixed compensation**  
A fixed amount of compensation to pay if: 
    * The employee has worked _at least_ the minimum amount of time required after the shift end time, or
    * The maximum deficit hasn't been exceeded. If the maximum deficit is 30 minutes and work is ended 15 minutes early, fixed compensation is paid. If work is ended 31 minutes late, fixed compensation is not earned.
  * **Earn fixed compensation without shift** If the setting is set to yes, a fixed amount of termination work is earned also on days where there is no planned work shift.
  * **Maximum deficit at the end of the shift to earn fixed compensation**  
How many minutes early can you end the shift and still earn the fixed compensation for termination work.
  * **Override event overtime base part target**  
Sets the overtime base part target for termination work, which overrides the target set in the event.
  * **Override event overtime increment part target**  
Sets the overtime increment part target for termination work, which overrides the target set in the event.
  * **Termination work shortens threshold for earning 100% weekly overtime**  
If the setting is on, earned termination work reduces the threshold for earning 100% weekly overtime. If for example the maximum amount of weekly 50% overtime is 8 hours and there have been 2 hours of termination work during the week, weekly 100% overtime is earned after 6 hours of weekly 50% overtime have been earned.
  * **Limited by permitted work times**


**Termination work earned from event type**  
Here you can set which event types you can earn termination work from. By default, termination work is not earned from any event type.
**Termination work earned from event type and overtime target**  
Here you can set which event type and overtime target combinations you can earn termination work from. For example:
\- If "work" event type should earn termination work in all cases except when the event overtime target is "overtime -salary", it can be configured as shown in the image above.  
\- If an event type should earn termination work only when the overtime target of the event is "hour-to-hour - salary", you should add a setting value for this combination with value "Yes".
## Work rises
Work rises can be configured to earn from Start-up & Termination work under **Worktime > Administration > Working community settings > Work Hours > Work rises > Compensation types that earn work rise** section or in the **Worktime > Administration > Setting groups > Compensation types that earn work rise** section, respectively.
## Reporting
Start-up and Termination work are be reported on in the **Realized Work Hours** report under the **Total hours worked** , **time equal to to work** and **average time equal to work** columns. They are also reported on in the **Hours by salary type, by hours** report.
