---
id: 360002492898
title: Worktime integrations
url: https://support.nepton.com/hc/en-gb/articles/360002492898-Worktime-integrations
locale: en-gb
category: Support
category_id: 360000446658
section: General information on integrations
section_id: 360002325398
section_path:
- Integration
- General information on integrations
labels:
- liittymä
- sääntöjoukko
- liittymät
- integraatio
- liittymäaineisto
- manuaalinen
- palkkaliittymä
- palkka-ajo
- vakiomuotoinen
promoted: false
updated_at: '2026-08-14T12:38:50Z'
edited_at: '2026-08-14T12:38:50Z'
---

# Worktime integrations

[Standard integrations](<https://support.nepton.com/hc/en-gb/articles/360002494538>) have been implemented between Nepton's work time records and other services. These integrations can be created as data files downloadable from the service, scheduled file transfers, or by using web service APIs. You can read more about the integrations [here](<https://support.nepton.com/hc/en-gb/articles/360002489417>).
## Uploading standard format data in the user interface
Navigate to **Worktime** **> Administration > Integrations > Desired payroll system.**
![](https://support.nepton.com/hc/article_attachments/38369792737565)
  1. Select the time range
  2. Select the levelling period time range if necessary
  3. Select the **Ruleset** that defines the data to be extracted. It is not recommended to extract data without a selected ruleset, as this would prevent modifying the generated content. Integrations should be extracted using rulesets. You can read more about rule sets [here](<https://support.nepton.com/hc/en-gb/articles/360002492278>).
  4. Configure additional extraction settings:  

     * Approved events are those that have been authorized - for example, a supervisor has approved the event. (The option 'Export only approved events' can be selected when no ruleset is selected. When a Ruleset is chosen, the extraction rules must define whether the events to be transferred must be approved.)
     * Lock events until the export end date means the dates will be locked up until the end of the selected time range. Note: If no data is generated based on the selections, the dates will not be locked.
     * Email report to the following email addresses: The file will be sent to the selected email address. This field is optional. The email addresses used in the last transfer will be saved and used as default for the next one.
     * Send export data by SFTP: The file will be sent to the SFTP server defined either in the integration or in the selected ruleset settings. This field is optional.
       * SFTP settings must already be configured
       * If target server has been set, it will automatically be used. This can be changed in the setting "Integration target server".
       * If a ruleset hasn't been chosen, the integration's SFTP settings are used.
       * If a ruleset if selected, that ruleset's SFTP settings are used.
       * Send export data by web service: Web service settings must be configured. This option must be selected when transferring data, for example, to Netvisor or from Nepton to another system via interface.
  5. Integration target server. Comes from integration settings or ruleset by default, if nothing else set here.
  6. Preview: Use this mode to perform a test run for review purposes only (no data will be transferred).
  7. Select the persons whose data will be included in the file.
