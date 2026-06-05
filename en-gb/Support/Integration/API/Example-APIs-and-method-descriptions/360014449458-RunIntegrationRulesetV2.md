---
id: 360014449458
title: RunIntegrationRulesetV2
url: https://support.nepton.com/hc/en-gb/articles/360014449458-RunIntegrationRulesetV2
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
updated_at: '2026-06-01T14:44:17Z'
edited_at: '2026-06-01T14:19:04Z'
---

# RunIntegrationRulesetV2

A newer version of this method exists. If you are currently using this method, we recommend that you will look at the instructions of the next method for changes required to update to the next version. You can find the instructions for the next version [here](<https://support.nepton.com/hc/en-gb/articles/36513332931869>)
## API overview
Nepton offers a SOAP-web service for running an integration ruleset. For the run a ruleset needs to be set. You can read more about rulesets [here](<https://support.nepton.com/hc/en-gb/articles/360002492278>) and instructions for setting up integration rulesets can be found [here](<https://support.nepton.com/hc/en-gb/articles/360002489257>). 
The WSDL scheme of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). General description of the Worktime API can be found [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The "Occurrences" column in the description defines whether an information is mandatory in the web service call or not. Occurrences 0 means that that item is not required in the call. Occurrences 1 means that the item must be included in the call exactly one time. Occurrences 0...n means that any amount of the item can be included in the call. Occurrences 1...n means that the item must be present in the data at least once, but can occur multiple times.
## Limitations
  * Persons with the personnel number 0 are not included in the data
  * The data can be requested for maximum timespan of two years
  * Forming the data can take tens of minutes depending on the size of the request data. The client application time limit is recommended to have a high value. The time that it takes to create the data can be checked by forming the data via user interface. More instructions about running the integrations through user interface is [here](<https://support.nepton.com/hc/en-gb/articles/360002492898>).


## Information to send
Level | Field name | Format | Occurrences | Description  
---|---|---|---|---  
Root, under the  
SOAP body | ParametersForRunIntegrationRulesetV2 | XML-element | 1 |   
1 | CallerAuthentication | XML-element | 1 | More info about authentication [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>).  
1 | IntegrationRulesetName | string | 1 | Name of the ruleset  
1 | FilterPeriodBeginDate | date | 1 | Starting date for fetching data. Format `YYYY-MM-DD`  
1 | FilterPeriodEndDate | date | 1 | End date for fetching data. Muoto `YYYY-MM-DD`  
1 | FilterByUsers | XML-element | 0..1 |  Persons to whom the ruleset is run. If no filter is set, the ruleset is run for all persons. Different person identifiers can be used in a single call, for example if some persons should be identified by personnel number and some by user name.  
2 | UserId | integer | 0..n | Internal identifier of person  
2 | Username | string | 0..n | User name of person  
2 | PersonnelNumber | string | 0..n | Personnel number of person  
2 | SocialSecurityNumber | string | 0..n | Social security number of person  
1 | ReturnFormat | string | 0..1 |  Format of the export file, if omitted or the value is `formatDefinedInRulesetSettings`, the format used is the one set in the ruleset "Export format" - setting. [See list of supported file formats here.](<https://support.nepton.com/hc/en-gb/articles/15468480461085>)  
### Example call
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForRunIntegrationRulesetV2>
          <CallerAuthentication /> <!-- Authentication is required, but omitted in this example -->
          <IntegrationRulesetName>?</IntegrationRulesetName>
          <FilterPeriodBeginDate>?</FilterPeriodBeginDate>
          <FilterPeriodEndDate>?</FilterPeriodEndDate>
          <FilterByUsers> <!-- All 4 persons are retrieved, 2 matches with usernames and 2 matches with personnel numbers -->
            <Username>Matti Meikäläinen</Username>
            <Username>Maija Mehiläinen</Username>
            <PersonnelNumber>9001</PersonnelNumber>
            <PersonnelNumber>9002</PersonnelNumber>
          </FilterByUsers>
          <ReturnFormat>formatDefinedInRulesetSettings</ReturnFormat>
        </tyo:ParametersForRunIntegrationRulesetV2>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Response
Level | Field name | Format | Occurrences | Description  
---|---|---|---|---  
Root, under the SOAP body | ReturnValueForRunIntegrationRulesetV2 | XML-element | 1 |   
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
        <tyo:ReturnValueForRunIntegrationRulesetV2>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <Output>909;Käyttäjä Admin;2016-05-12;2016-05-12;8.00;100;;Year leave;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-10;2016-05-10;7.15;990;;Training;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-11;2016-05-11;9.15;999;;Work;;;;;;;;;</Output>
        </tyo:ReturnValueForRunIntegrationRulesetV2>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
