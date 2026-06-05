---
id: 360004861518
title: Nepton API description
url: https://support.nepton.com/hc/en-gb/articles/360004861518-Nepton-API-description
locale: en-gb
category: Support
category_id: 360000446658
section: API
section_id: 360000921798
section_path:
- Integration
- API
labels:
- liittymäkuvaus
promoted: false
updated_at: '2025-09-08T07:26:22Z'
edited_at: '2025-09-08T07:26:22Z'
---

# Nepton API description

When there is a need to transfer data between Nepton and another service, the Nepton Application Program Interface (API) is an excellent alternative to an SFTP integration. Integrations can, in other words, be implemented by using Nepton API.
The requesting system can make service requests to Nepton API at any point. The requesting system is defined by the customer. A third party can also be involved in implementing the requesting system. API requests can be created in different applications or, for example, onto a server where they are run by scripts as needed. The implementation of the API usage is up to the customer to decide. This article and other API related articles help the customer or a third party to set up the API interface.
![](https://support.nepton.com/hc/article_attachments/13831592826269)
Nepton API is utilized, for example, when importing projects and events to Nepton and in these imports the additions and changes relayed from the customer's system are immediately updated into Nepton. 
Nepton has two API endpoints to which requests can be sent. The other one is [HR API](<https://support.nepton.com/hc/en-gb/articles/360004855857-HR-API-general-description>) including
  * Personnel information


and the [Worktime API](<https://support.nepton.com/hc/en-gb/articles/360004861558-Worktime-API-in-general>) including
  * Absences
  * Worktime events
  * Projects, cost centers, work orders which are treated like Projects in Nepton.


## Deployment of Nepton API
When forming the API calls, bear in mind that the parameters are case-sensitive. All upper case letters must be the same way as they are in our instructions.
1\. The Worktime API (worktime events, absences and projects) needs to use **CustomerId** in the request, which can be obtained from a Nepton contact or customer service. The authentication for worktime API is described [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>).
2\. The HR API usage requires a **DeploymentId** and a **Webservicepassword** , which can be obtained from a Nepton contact or customer service. HR API is described [here](<https://support.nepton.com/hc/en-gb/articles/360004855857>).
3\. The API requests are authenticated. Authentication requires user login information and changes made via the API are seen as this user's actions. For this purpose and to ensure information security, for each API implementation a **user account** needs to be created. This account is seen the log when, for example, one needs to investigate a certain API request. This account is not used for any other purpose in Nepton other than the API. Minimum access to Nepton is recommended for this account for security reasons. For example, if the API implementation does not utilize HR data, then minimum role for accessing the HR data should be granted.
## API deployment for data exports
When exporting, for example, **projects** or **events** from Nepton, in addition to the settings above, [integration rulesets](<https://support.nepton.com/hc/en-gb/articles/360002492278-Rulesets-in-general>) which define the content of the exports, are needed.
Nepton API is included in all Nepton service levels.
