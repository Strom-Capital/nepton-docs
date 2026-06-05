---
id: 360004861558
title: Worktime API in general
url: https://support.nepton.com/hc/en-gb/articles/360004861558-Worktime-API-in-general
locale: en-gb
category: Support
category_id: 360000446658
section: Worktime API
section_id: 360005706218
section_path:
- Integration
- API
- Worktime API
labels: []
promoted: false
updated_at: '2025-02-27T06:58:51Z'
edited_at: '2025-02-27T06:58:51Z'
---

# Worktime API in general

## Production API description
<https://time.nepton.com/WebService.php?WSDL>
Please also ensure that the necessary IP addresses are opened. Instructions [here](<https://support.nepton.com/hc/en-gb/articles/360009237257>).
Maximum POST request data size to worktime API is 128 MB. 
The Worktime API provides external systems access to certain features of Worktime. Guidance for individual topics is provided in the following articles:
  * [Authentication in Worktime API](<https://support.nepton.com/hc/articles/360019983978>)
  * [Events API](<https://support.nepton.com/hc/articles/360019840217>)
  * [Projects API](<https://support.nepton.com/hc/articles/360019840237>)
  * [Accruals API](<https://support.nepton.com/hc/articles/360019984338>)
  * [Worktime Integrations API](<https://support.nepton.com/hc/articles/360019840857>)
  * [Terminal Services API](<https://support.nepton.com/hc/articles/360019841037>)
  * [Response codes of Worktime API](<https://support.nepton.com/hc/articles/360019841477>)


Please note that:
  * The sent XML has to be valid XML
  * Used character encoding is UTF-8
  * Parameters used in the API call are **case-sensitive.** Make sure all upper case letters are used in a correct way when forming the call.


The best way to ensure the validity of XML is to use a SOAP library to handle requests and responses. For example [SoapClient](<https://www.php.net/manual/en/class.soapclient>) in PHP and [WCF Web Service Reference](<https://learn.microsoft.com/en-us/dotnet/core/additional-tools/wcf-web-service-reference-guide>) in .NET are viable options.
If you are generating XML without the help of an XML library, you need to keep in mind that the following characters need to be represented as entities:
Character | Entity  
---|---  
`&` | `&amp;`  
`<` | `&lt;`  
`>` | `&gt;`  
If you want to represent project name "Project & other work" in XML, it should be done the following way:
[code] 
    <Name>Project &amp; other work</Name>
[/code]
