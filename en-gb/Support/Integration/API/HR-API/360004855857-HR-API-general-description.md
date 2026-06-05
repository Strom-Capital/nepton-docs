---
id: 360004855857
title: HR API general description
url: https://support.nepton.com/hc/en-gb/articles/360004855857-HR-API-general-description
locale: en-gb
category: Support
category_id: 360000446658
section: HR API
section_id: 4406143245713
section_path:
- Integration
- API
- HR API
labels:
- henkilötietoliittymä
promoted: false
updated_at: '2025-02-27T07:05:34Z'
edited_at: '2025-02-27T07:05:34Z'
---

# HR API general description

## Production API description
<https://go.nepton.com/API/SOAPWebService.asmx>
Please also ensure that the necessary IP addresses are opened. Instructions [here](<https://support.nepton.com/hc/en-gb/articles/360009237257>).
The HR API provides external systems access to certain features and data from Nepton. The WSDL for the API can be found at <https://go.nepton.com/API/SOAPWebService.asmx?wsdl>.
Request are passed as a SOAP request using the POST method. The Content-Type HTTP header is required with value of "text/xml; charset=utf-8".
Guidance for individual topics is provided in the following articles:
  * [Authentication in HR API](<https://support.nepton.com/hc/en-gb/articles/4406441875089>)
  * [Responses and result codes of HR API](<https://support.nepton.com/hc/en-gb/articles/4406446686609>)
  * [Persons API](<https://support.nepton.com/hc/en-gb/articles/4406271660945>)
  * [Units API](<https://support.nepton.com/hc/en-gb/articles/4406271664273>)


Please note that:
  * The sent XML has to be valid XML
  * Used character encoding is UTF-8
  * API-calls are case-sensitive. Make sure you have typed all upper case letters in a correct way.


The best way to ensure the validity of XML is to use a SOAP library to handle requests and responses. For example [SoapClient](<https://www.php.net/manual/en/class.soapclient>) in PHP and [WCF Web Service Reference](<https://learn.microsoft.com/en-us/dotnet/core/additional-tools/wcf-web-service-reference-guide>) in .NET are viable options.
If you are generating XML without the help of an XML library, you need to keep in mind that the following characters need to be represented as entities:
Character | Entity  
---|---  
`&` | `&amp;`  
`<` | `&lt;`  
`>` | `&gt;`  
If you want to represent password "_HpR9cHN &f8C<_" in XML, it should be done the following way:
[code] 
    <UserPassword>HpR9cHN&amp;f8C&lt;</UserPassword>
[/code]
