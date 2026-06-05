---
id: 36513332931869
title: RunIntegrationRulesetV3
url: https://support.nepton.com/hc/en-gb/articles/36513332931869-RunIntegrationRulesetV3
locale: en-gb
category: Support
category_id: 360000446658
section: Example APIs and method descriptions
section_id: 4410135708433
section_path:
- Integration
- API
- Example APIs and method descriptions
labels: []
promoted: false
updated_at: '2026-06-01T14:54:30Z'
edited_at: '2026-06-01T14:18:34Z'
---

# RunIntegrationRulesetV3

## API overview  
Nepton offers a SOAP-web service for running an integration ruleset. For the run a ruleset needs to be set. You can read more about rulesets [here](<https://support.nepton.com/hc/en-gb/articles/360002492278>) and instructions for setting up integration rulesets can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002489257>). 
The WSDL scheme of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). General description of the Worktime API can be found [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The "Occurrences" column in the description defines whether an information is mandatory in the web service call or not. Occurrences 0 means that that item is not required in the call. Occurrences 1 means that the item must be included in the call exactly one time. Occurrences 0...n means that any amount of the item can be included in the call. Occurrences 1...n means that the item must be present in the data at least once, but can occur multiple times.
## Changes to previous verson ([RunIntegrationRulesetV2](<https://support.nepton.com/hc/en-gb/articles/360014449458>))
### Rakenteelliset muutokset
**Old** | **New** | **Description**  
---|---|---
[code] 
    <tyo:ParametersForRunIntegrationRulesetV2>
      ...
    </tyo:ParametersForRunIntegrationRulesetV2>
[/code]  
| 
[code]
    <tyo:ParametersForRunIntegrationRulesetV3>
    ...
    </tyo:ParametersForRunIntegrationRulesetV3>
[/code]
| Name of root element in request has changed
[code] 
    <tyo:ReturnValueForRunIntegrationRuleset>
      ...
    </tyo:ReturnValueForRunIntegrationRuleset
[/code]  
| 
[code]
    <tyo:ReturnValueForRunIntegrationRulesetV3>
    ...
    </tyo:ReturnValueForRunIntegrationRulesetV3>
[/code]
| Name of root element in response has changed  
### New features and elements
  * Possibility to filter persons with person's external identifiers
    * PersonExternalIdentifier-element added to request
      * PersonExternalIdentifier contains Identifier- ja FieldName-fields


## Limitations
  * Persons with the personnel number 0 are not included in the data
  * The data can be requested for maximum timespan of two years
  * Forming the data can take tens of minutes depending on the size of the request data. The client application time limit is recommended to have a high value. The time that it takes to create the data can be checked by forming the data via user interface. More instructions about running the integrations through user interface is [here](<https://support.nepton.com/hc/en-gb/articles/360002492898>).


## Information to send
Level | Field name | Format | Occurrences | Description  
---|---|---|---|---  
Root, under the  
SOAP body | ParametersForRunIntegrationRulesetV3 | XML-element | 1 |   
1 | CallerAuthentication | XML-element | 1 | More info about authentication [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>).  
1 | IntegrationRulesetName | string | 1 | Name of the ruleset  
1 | FilterPeriodBeginDate | date | 1 | Starting date for fetching data. Format `YYYY-MM-DD`  
1 | FilterPeriodEndDate | date | 1 | End date for fetching data. Muoto `YYYY-MM-DD`  
1 | FilterByUsers | XML-element | 0..1 |  Persons to whom the ruleset is run. If no filter is set, the ruleset is run for all persons. Different person identifiers can be used in a single call, for example if some persons should be identified by personnel number and some by user name.  
2 | UserId | integer | 0..n | Internal identifier of person  
2 | Username | string | 0..n | User name of person  
2 | PersonnelNumber | string | 0..n | Personnel number of person  
2 | PersonExternalIdentifier | XML-elementti | 0..n | Person's external identifier info  
3 | Identifier | merkkijono | 1 | Person's external identifier value  
3 | FieldName | merkkijono | 1 | Person's external identifier field name  
2 | SocialSecurityNumber | string | 0..n | Social security number of person  
1 | ReturnFormat | string | 0..1 |  Format of the export file, if omitted or the value is `formatDefinedInRulesetSettings`, the format used is the one set in the ruleset "Export format" - setting. [See list of supported file formats here.](<https://support.nepton.com/hc/en-gb/articles/15468480461085>)  
### Example call
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForRunIntegrationRulesetV3>
          <CallerAuthentication /> <!-- Authentication is required, but omitted in this example -->
          <IntegrationRulesetName>?</IntegrationRulesetName>
          <FilterPeriodBeginDate>?</FilterPeriodBeginDate>
          <FilterPeriodEndDate>?</FilterPeriodEndDate>
          <FilterByUsers> <!-- All 4 persons are retrieved, 2 matches with usernames and 2 matches with personnel numbers -->
            <Username>Matti Meikäläinen</Username>
            <Username>Maija Mehiläinen</Username>
            <PersonnelNumber>9001</PersonnelNumber>
            <PersonnelNumber>9002</PersonnelNumber>
            <PersonExternalIdentifier>
              <Identifier>EMP-12345</Identifier>
              <FieldName>ExternalIdentifier1</FieldName>
            </PersonExternalIdentifier>
            <PersonExternalIdentifier>
              <Identifier>EMP-67890</Identifier>
              <FieldName>ExternalIdentifier1</FieldName>
            </PersonExternalIdentifier>
          </FilterByUsers>
          <ReturnFormat>formatDefinedInRulesetSettings</ReturnFormat>
        </tyo:ParametersForRunIntegrationRulesetV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Response
Level | Field name | Format | Occurrences | Description  
---|---|---|---|---  
Root, under the SOAP body | ReturnValueForRunIntegrationRulesetV3 | XML-element | 1 |   
1 | ResponseCode | integer | 1 | Response code for the handling of the requested date. List of possible codes is [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).   
1 | ResponseString | string | 1 | Description of response code  
1 | Output | string | 0..1 |  Contents of the requested data. If the data is not in text form, it will be base64 encoded.  This occurs in following cases:
  * The data is split into several files. Content is a base64 encoded ZIP file. More information about splitting the data is [here](<https://support.nepton.com/hc/en-gb/articles/360006255458>).
  * The data format is not always text. For example in Swgi-format the content is a base64 encoded XSLX file.

  
### Response example
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ReturnValueForRunIntegrationRulesetV3>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <Output>909;Käyttäjä Admin;2016-05-12;2016-05-12;8.00;100;;Year leave;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-10;2016-05-10;7.15;990;;Training;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-11;2016-05-11;9.15;999;;Work;;;;;;;;;</Output>
        </tyo:ReturnValueForRunIntegrationRulesetV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
