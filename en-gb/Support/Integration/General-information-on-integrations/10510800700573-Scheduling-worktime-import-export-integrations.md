---
id: 10510800700573
title: Scheduling worktime import/export integrations
url: https://support.nepton.com/hc/en-gb/articles/10510800700573-Scheduling-worktime-import-export-integrations
locale: en-gb
category: Support
category_id: 360000446658
section: General information on integrations
section_id: 360002325398
section_path:
- Integration
- General information on integrations
labels: []
promoted: false
updated_at: '2026-08-14T10:05:38Z'
edited_at: '2025-03-31T07:08:32Z'
---

# Scheduling worktime import/export integrations

This article applies for integrations which can be found under Worktime. For integrations under other sections (e.g. Person import under Employees section) please review their guidance articles to see how automated schedules work.
## Introduction
The Integration scheduling settings area allows you to automate imports or exports to external systems to run on certain days and at certain times.
You can find the settings under _Worktime > Administration > Working community settings > Integration > Integration scheduling._ Schedules can only be defined at the working community level
Please refer to the guidance pages on specific integrations also when creating schedules, we have many different integrations to external systems that all work differently so can only give general advice here.
## Settings
You should configure the integration (and ruleset if applicable) you wish to schedule and fully save it and reload the page before attempting to configure schedules for it.
The schedule settings are checked every couple of minutes and will start any that need running so it is recommended only to use the history control when configuring _future_ setting changes otherwise you may accidentally end up triggering an integration whilst in the middle of changing settings.
![](https://support.nepton.com/hc/article_attachments/10920668909341)
**Schedule enabled from** is a mandatory field. The date and time can be set to the current moment if the schedule should be active right away but also setting the schedule to be active in the future. Configuring new schedules to be enabled from a date in the past will cause the scheduler to create jobs for those past dates (up to 3 days) so is not a typical use case. (Timezone: Europe/Helsinki)
Set the date and time into the validity field. It is not possible to save the new setting info without the time being there. Please note that the scheduled time setting has the save-button at the bottom of the page.
![](https://support.nepton.com/hc/article_attachments/20722982254877)
**Schedule enabled to** is an optional field. If there is no date set the schedule will just continue being active. (Timezone: Europe/Helsinki)
**Description** can freely be assigned to a schedule. The saved description text is show on the list of schedules to help you identify them easily.
**Integration** is a mandatory field. This defines which integration with an external system should be triggered when the schedule is run.
**Integration ruleset** allows defining a ruleset if the selected integration supports using a ruleset. Some integrations may explicitly require a ruleset. If the ruleset is selected the ruleset will also define the server settings where data is exported or where data is being imported depending whether selected integration was an export or import integration.
**Schedule type** is either daily or minutely. The options selectable here also depend on the selected integration since some integrations might only support the daily option.
**Minutely interval rule** is only available when the "minutely" schedule type is used, and allows defining the integration to run every x minutes. Schedules cannot be set to run more often than every 15 minutes. Clicking the wand icon opens a tool which allows picking a rule from examples.
**Daily interval rule** is only available when daily interval type is used and allows which days the integration is run. Clicking the magic wand icon will open a tool which allows picking a rule from a list of examples.
**Daily start time** is only available when daily interval type is used and allows defining the time of day when to execute the integration. There are no limitations for assigning the starting time of a schedule but if it is necessary to have the integration run as close to the target time as possible you should avoid setting the starting time during maintenance window or during the day when system is under high load. Information about the maintenance times can be found [here](<https://support.nepton.com/hc/en-gb/articles/360006554777>). (Timezone: Europe/Helsinki)
**Import/export period date start rule** and **import/export period date end rule** fields define the time period which is imported or exported. These options are not available for relevant integrations. Clicking the magic wand icon will open a tool which allows picking a rule from a list of examples.
**Email report to following addresses** Allows defining a comma separated list of email addresses which will receive a report for each scheduled run. Most integrations will include the imported/exported file as attachment in the email. The email is sent whether the run succeeded or failed. Note: the integration or ruleset does not necessarily need to be configured to interact with an external system if for example you just want to have a custom report delivered to your email address.
## Delayed or missed schedules
In some cases there might be a delay before the system starts running the scheduled integration e.g. due to [maintenance downtime](<https://support.nepton.com/hc/en-gb/articles/360006554777>). If an integration is delayed but it's still the date it was configured to run on the job will remain in status "Queued" and eventually be run.
If an integration cannot be started on the same day due to extended server maintenance or downtime we will show the missed jobs in the history table as failed. It is then up to you to decide if they are relevant and safe to re-run as every external system and configuration is different, it is impossible for us to know what the implications of running a schedule late is. We recommend checking the file status of any SFTP servers the integration may interact with, the synchronization state of any external systems we connect to, and the nature of the integration as some integrations sync everything every time so are typically safe to re-run whereas others might send only changes since the last sync, in which case it may be important to run them all in sequential order. See "Running and re-running schedules manually" for more information.
## Integrations running at the same time
It is impossible for us to know the implications of running the same integration concurrently, for example multiple jobs trying to read or write files on an SFTP server can easily lead to unpredictable results. If two or more integrations that read from or write to the same SFTP server within the same customer environment are triggered or scheduled to run simultaneously, we will ensure that one completes before starting the next.
Separate integration types that use the same resources should be configured so they are not going to interfere with one another when run. For example if one integration is reading files from an SFTP-server and another integration is writing files to the same SFTP-server then it is recommended that they are configured to use separate directories within the SFTP-server. Any approach that relies on start times is not guaranteed as it's possible there may be a delay in starting the job, like was described in "Delayed or missed schedules" section.
## History and status of the scheduled runs
**![](https://support.nepton.com/hc/article_attachments/11150026766749)**
On an opened schedule section there is a history table which displays all the past runs of the schedule and any in progress jobs along with any configuration errors detected with the schedule or integration.
The "Run now" button allows you to manually execute the integration in the schedule (see "Running and re-running schedules manually").
The table shows when the selected schedule was executed and was the result a success or a failure. For most integrations the export/import file is also available.
The "Status" column shows the following job states:
  * "Scheduled" - Represents an upcoming job that is scheduled to run at a particular time (see the scheduled column).
  * "In queue" - The job will start as soon as possible. The delay can be caused due to ongoing maintenance windows, multiple jobs from the same integration all starting at once, or an excessive number of jobs all scheduled to start at the same time.
  * "In progress" - The job is running now.
  * "Cancelled" - The job was cancelled and won't run at the scheduled time, this does not affect other future schedules.
  * "Finished" - The job has finished running and the log is now available.
  * "Missed start time" - For whatever reason we were unable to run the job at the time it was scheduled to run, if we cannot run it after a certain amount of time we deem it no longer safe to do and flag the job with this status.
  * "Timed out" - The job took longer than 6 hours to run so it has likely errored and we have flagged it as such. In the event it is still running and is taking a really long time, the status and log will eventually be corrected.


You can also see the status of all automatically run integrations through the service log (read more about it [here](<https://support.nepton.com/hc/en-gb/articles/360002575478>)).
## Running and re-running schedules manually
Once a schedule is configured it will start running automatically but in some instances you may need to manually run a schedule. Some important notes about manual run:
  * Manual run uses the same person as event creator if event creator setting is relevant for integration. For example setting "Person used to create event" for Event imports. Otherwise logged in user is shown as event creator.
  * The "Run now" button shown beneath the history control will trigger the configured integration as if it was scheduled to run at the present moment. Settings will be picked up relative to the current date meaning if you exporting data from 2 days ago then it is 2 days ago relative to the current date, not the date the schedule would normally run on.
  * The "Run again" button, shown when you view a specific schedule run log in the history table, has some important distinctions from the "Run now" button. This feature will attempt to run the schedule again as it was run _originally_. This means the settings will be used based on or relative to the date it originally ran. Also if the integration involved importing a file from an SFTP server then we will import our local copy of the exact same file that was imported originally instead of fetching the file from the SFTP server again. This is useful when imports were processed and archived but you need to run them again now some other data has been corrected. For exports they will be exported as normal.
