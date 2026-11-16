---
id: 9056347382813
title: Detecting and resolving integration problems
url: https://support.nepton.com/hc/en-gb/articles/9056347382813-Detecting-and-resolving-integration-problems
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
edited_at: '2023-02-01T08:17:36Z'
---

# Detecting and resolving integration problems

When integrating with Nepton, ensure that possible problems will be detected and resolved. This is especially important when integration is synchronizing data between external system and Nepton by sending only the changes in the data instead of sending all the data including non-changed data periodically. In these types of integrations, the data will get out of sync potentially permanently unless the potential problems are detected and resolved.
To ensure this we recommend to:
  1. Identify and agree the ways potential problems will be detected.
  2. Agree how to resolve the detected problems.


To help with these goals Nepton provides tooling and related process examples. These tools are:
  * [Service log](<https://support.nepton.com/hc/fi/articles/360002575478>)
    * Logs detected integration related problems
  * Nepton API responses 
    * Contains information about problems API call encounter 
      * [HR API result codes](<https://support.nepton.com/hc/en-gb/articles/4406446686609>)
      * [Worktime API result codes](<https://support.nepton.com/hc/en-gb/articles/360019841477>)


## Using service log in integration problem handling
Integration related problems detected by Nepton can be found in the service log. Here are some examples of how service log can be used in process of detecting and resolving the integration problems.
### Example 1
  1. Customer detects an integration problem during regular routine service log check.
  2. Log details tell that there is a problem in the integration file content sent nightly to Nepton, so the customer fixes the data in the HR system where the data is being sent from.
  3. The corrected data will be sent to Nepton automatically the next night.


### Example 2
  1. Customer detects an integration problem during regular routine service log check.
  2. Log details show that one of the calls to Nepton API adding a new project failed because of a missing project name.
  3. The customer asks the person responsible for the project to fill in the project name and save the changes to get the changes re-sent to Nepton.


## Using API call results in integration problem handling
The Nepton API call responses tells the caller if the API call was successful. If the call was not successful, the response describes what the detected problems were.
### Ensuring data doesn't get out of sync
On integrations implemented using Nepton API it is more common to sync only the changes in the data between Nepton and external system. In these cases, if problems occur, to avoid the systems getting out of sync it is important to ensure there is a way to re-send the data. Examples of ways to ensure data can be synchronized after possible API call fail:
  * Resaving the data in originating system to trigger resending of data
  * Capability of triggering a resynching of all the data including unchanged data
  * Periodical scheduled resynching of all the data including unchanged data


Here is an example of how API call response can be used in the process of detecting and resolving potential integration problems.
  1. The sending system gets a response from Nepton API that tells that adding a project to Nepton failed.
  2. The sending system informs designated person at customer about the problem by email containing the problem details from the API response.
  3. The person who got the email instructs how to correct projects details causing the problem and resave the changes to get the changes re-sent to Nepton.


It is also good to notice that the failed API calls are also shown in the [Service log.](<https://support.nepton.com/hc/fi/articles/360002575478>)
Additional info:
[HR API result codes](<https://support.nepton.com/hc/en-gb/articles/4406446686609>)
[Worktime API result codes](<https://support.nepton.com/hc/en-gb/articles/360019841477>)
## Integration problem handling using other methods
In addition to the integration problem detection Nepton can offer by provided tooling, it is important to notice that often additional integration problem detection is needed. For example:
  * In case external system fails on connecting Nepton API for a reason or another, Nepton can't know about the failed API call attempt
  * In case there are problems on creating the data to be transferred to Nepton, Nepton can't be aware of the problems
