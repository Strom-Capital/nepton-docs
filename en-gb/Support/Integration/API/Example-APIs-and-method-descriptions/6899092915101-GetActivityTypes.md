---
id: 6899092915101
title: GetActivityTypes
url: https://support.nepton.com/hc/en-gb/articles/6899092915101-GetActivityTypes
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
edited_at: '2023-08-25T10:35:47Z'
---

# GetActivityTypes

## Overview of the interface  
Interface is used in retrieving event type information from Nepton.
Web service WSDL-schema is available publicly [here](<https://time.nepton.com/WebService.php?WSDL>). Interfaces are described generally [here](<https://support.nepton.com/hc/articles/360004861558>).
Occurrences - column in request description defines whether a field is mandatory in a request or not. 0 occurrences means that field is not mandatory in the request. 1 occurrence means that the field must be present in the request once. 0..n occurrences means that the request may contain any number of those fields or none at all. Occurrences 1..n means that the request may contain any number of those fields but there must be at least one instance of that field.
## Request data
LEVEL | FIELD NAME | TYPE | OCCURRENCES | DESCRIPTION  
---|---|---|---|---  
0 | ParametersForGetActivityTypes | XML element | 1 | Root element under SOAP body  
1 | CallerAuthentication | XML element |  | More information about authentication [here](<https://support.nepton.com/hc/articles/360004861558>)  
1 | FilterByIds | XML element | 0..1 | Filter by Nepton unique identifiers of event types  
2 | Id | integer | 0..n | Nepton unique identifier  
1 | FilterByInternalNames |  | 0..1 | Filter by event type internal names  
2 | InternalName | string | 0..n | Event type internal name  
### Request example
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForGetActivityTypes>  
          <CallerAuthentication / > <!-- Authentication is required but is omitted from this example -->  
          <FilterByIds>  
            <Id>1</Id>  
          </FilterByIds>  
          <FilterByInternalNames>  
            <InternalName>work</InternalName>  
          </FilterByInternalNames>  
        </tyo:ParametersForGetActivityTypes>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Response
LEVEL | FIELD NAME | TYPE | OCCURRENCES | SELITE  
---|---|---|---|---  
0 | ReturnValueForGetActivityTypes | XML element | 1 | Root element under SOAP body  
1 | ResponseCode | integer | 1 | Response code of handling the request. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).  
1 | ResponseString | string | 1 | Response description  
1 | ActivityTypeList | XML element | 1 | List of event type  
2 |  ActivityType |  XML element |  0..n | Element containing information of single event type  
3 |  Id |  integer |  1 |  Nepton identifier of event type  
3 |  InternalName |  string |  1 |  Internal name of event type  
3 |  TranslatedName | XML element | 0..n | Translated names for event type. The number of elements is the same as the number of supported languages in Nepton. See supported languages and their codes [here](<https://support.nepton.com/hc/en-gb/articles/6904407712413>).  
4 |  Locale | string | 1 | Language code for translation  
4 |  Name | string | 1 | Translation of event type name  
3 |  Code |  string |  0..1 |  Event type code  
3 |  Visible |  boolean |  0..1 |  true if event type is set as visible in Nepton, false if not  
3 |  CanAssignWorkIncrements |  boolean |  0..1 |  Can supplements be assigned for event type (true/false)  
3 |  CanHaveRelatedProjects |  boolean |  0..1 |  Can projects be targeted for event type (true/false)  
3 |  CategoryInternalName |  string |  0..1 |  Event type category internal name  
3 |  TranslatedCategoryName | XML element | 0..n | Translated names for event type category. The number of elements is the same as the number of supported languages in Nepton. See supported languages and their codes [here](<https://support.nepton.com/hc/en-gb/articles/6904407712413>).  
4 |  Locale | string |  1 |  Language code for translation  
4 |  Name | string |  1 |  Translation of event type category name  
3  |  BeginDateTimeInput |  string |  0..1 |  Setting for inserting begin time for event type Possible values: | **Value** | **Description**  
---|---  
mandatory | Mandatory  
  
optional | Optional  
  
disabled | Not in use  
  
3 |  EndDateTimeInput |  string |  0..1 |  Setting for inserting end time for event type. Options are same as with BeginDateTimeInput - element.  
### Response example
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForGetActivityTypes>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors</ResponseString>  
          <ActivityTypeList>  
            <ActivityType>  
              <Id>1</Id>  
              <InternalName>work</InternalName>  
              <TranslatedName>  
                <Locale>fi_FI</Locale>  
                <Name>työ</Name>  
              </TranslatedName>  
              <TranslatedName>  
                <Locale>en_US</Locale>  
                <Name>work</Name>  
              </TranslatedName>  
              <Code>456/w</Code>  
              <Visible>true</Visible>  
              <CanAssignWorkIncrements>true</CanAssignWorkIncrements>  
              <CanHaveRelatedProjects>true</CanHaveRelatedProjects>  
              <CategoryInternalName>test</CategoryInternalName>  
              <TranslatedCategoryName>  
                <Locale>fi_FI</Locale>  
                <Name>testausta</Name>  
              </TranslatedCategoryName>  
              <TranslatedCategoryName>  
                <Locale>en_US</Locale>  
                <Name>testing</Name>  
              </TranslatedCategoryName>  
              <BeginDateTimeInput>mandatory</BeginDateTimeInput>  
              <EndDateTimeInput>optional</EndDateTimeInput>  
            </ActivityType>  
          </ActivityTypeList>  
        </tyo:ReturnValueForGetActivityTypes>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
