---
id: 360019983978
title: Authentication in Worktime API
url: https://support.nepton.com/hc/en-gb/articles/360019983978-Authentication-in-Worktime-API
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime API
section_id: 360005706218
section_path:
- Integration
- API
- Worktime API
labels:
- Työajan API
promoted: false
updated_at: '2025-02-27T07:06:26Z'
edited_at: '2025-02-27T07:06:26Z'
---

# Authentication in Worktime API

All [Worktime API](<https://support.nepton.com/hc/articles/360004861558>) messages require authentication with a person account to Nepton service. The access rights for the API are the same that the person has in Nepton service. For regular use we recommend setting up a dedicated person account with a username and a password for the API use in Nepton service. See [guidance for setting up a person](<https://support.nepton.com/hc/articles/360002427618>). To authenticate a CallerAuthentication element must be supplied in the call as an SOAP element.
## CallerAuthentication
The CallerAuthentication element provides means for authentication. Values for the following fields should be provided:
  * CustomerId - A numeric value identifying the working community. You need to contact Nepton to get a value for the customer identifier.
  * Username - The username of the authenticating person account. A dedicated person account for the API is recommended.
  * Password - The password of the authenticating person account. **ATTN: Password can not end with &-character. It breaks the XML-message.**


Other fields listed in the API description of CallerAuthentication are for internal use only.
### Example
[code] 
    <CallerAuthentication>  
      <CustomerId>xxxxxxxxx</CustomerId>  
      <Username>xxxxxxxxx</Username>  
      <Password>xxxxxxxxx</Password>  
    </CallerAuthentication>
[/code]
API-calls are case-sensitive. When forming an API-call, make sure all the upper case letters are in their correct places to make the call work.
