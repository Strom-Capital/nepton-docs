---
id: 36510325765533
title: InsertActivitiesV5
url: https://support.nepton.com/hc/en-gb/articles/36510325765533-InsertActivitiesV5
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
edited_at: '2026-06-01T13:24:43Z'
---

# InsertActivitiesV5

## Overview of interface
Interface is used in adding event information to Nepton.
Web service WSDL-schema is available publicly [here](<https://time.nepton.com/WebService.php?WSDL>). Interfaces are described generally [here](<https://support.nepton.com/hc/articles/360004861558>).
Occurrences - column in request description defines whether a field is mandatory in a request or not. 0 occurrences means that field is not mandatory in the request. 1 occurrence means that the field must be present in the request once. 0..n occurrences means that the request may contain any number of those fields or none at all. Occurrences 1..n means that the request may contain any number of those fields but there must be at least one instance of that field.
## Changes to earlier version ([InsertActivitiesV4](<https://support.nepton.com/hc/en-gb/articles/27550371952925>))
### New properties and elements
  * Event person can be identified by person's external identifier
    * UserPersonExternalIdentifier-element added to request
  * Person who has approved an event can be identied by approving person's external identifier
    * ApproverUserPersonExternalIdentifier-element added to request
  * UserPersonExternalIdentifier and ApproverUserPersonExternalIdentifier contain Identifier- and FieldName-fields


## Person references
In creating an event it is mandatory to have information about the person the event belongs to and a non-mandatory information about the person who has approved the event. Both of these person informations can be referred to with one of these identifiers: Nepton unique person id, username, social security number or personnelnumber. If approver of event is set, the event will be marked as approved. See request data - table for more information about elements used in providing event data.
## Request Data
**LEVEL** | **FIELD NAME** | **TYPE** | **OCCURRENCES** | **DESCRIPTION**  
---|---|---|---|---  
0 | ParametersForInsertActivitiesV5 | XML element | 1 | Root, under SOAP body  
1 | CallerAuthentication | XML element | 1 | More information about authentication [here](<https://support.nepton.com/hc/articles/360004861558>)  
1 | ActivityList | XML element | 1 | List of events to send  
2 | Activity | XML element | 1..n | Event to be added  
3 | UserId | integer | 0..1 | Person the event will be added to. Referenced by Nepton identifier  
3 | UserUsername | string | 0..1 | Person the event will be added to. Referenced by username  
3 | UserSocialSecurityNumber | string | 0..1 | Person the event will be added to. Referenced by social security number  
3 | UserPersonnelNumber | string | 0..1 | Person the event will be added to. Referenced by personnel number  
3 | UserPersonExternalIdentifier | XML element | 0..1 | Person the event will be added to. Referenced by external identifier.  
4 | Identifier | string | 1 | Person's external identifier value.  
4 | FieldName | string | 1 |  Person's external identifier field name. Supported values:
[code] 
    ExternalIdentifier1
[/code]  
3 | ActivityTypeId | integer | 0..1 |  **Note!** Please use the ActivityTypeCode field, ActivityTypeId is used by older implementions. Event type for the event. Referenced by Nepton identifier.  If neither of ActivityTypeId or ActivityTypeCode are provided in the request, event will be created as Work.  
3 | ActivityTypeCode | string | 0..1 |  Event type for the event. Referenced by event type code. If several event types have the same code, the first event type found will be added for the event. If neither of ActivityTypeId or ActivityTypeCode are provided in the request, event will be created as Work.  
3 | BeginDateTime | dateTime | 1..1 |  Event begin date and time. Format is `YYYY-MM-DDTHH:MM:SS` , for example `2021-02-18T12:30:00` . Mandatory  
3 | EndDateTime | dateTime | 0..1 |  Event end date and time. Format is `YYYY-MM-DDTHH:MM:SS` , for example `2021-02-18T12:30:00` . If information is not provided or it is empty, event will be created without an end time.  
3 | ApproverUserId | integer | 0..1 | Person who has approved the event. Reference by unique user identifier (can be seen in the user profile URL)  
![](https://support.nepton.com/hc/article_attachments/36511098147357)  
3 | ApproverUsername | string | 0..1 | Person who has approved the event. Reference by username  
3 | ApproverUserSocialSecurityNumber | string | 0..1 | Person who has approved the event. Reference by social security number  
3 | ApproverUserPersonnelNumber | string | 0..1 | Person who has approved the event. Reference by personnel number  
3 | ApproverUserPersonExternalIdentifier | XML element | 0..1 | Person who has approved the event. Referenced by external identifier.  
4 | Identifier | string | 1 | Approver person's external identifier value.  
4 | FieldName | string | 1 |  Approver person's external identifier field name. Supported values:
[code] 
    ExternalIdentifier1
[/code]  
3 | Comment | string | 0..1 | Event notes.  
3 | IsClockedEvent | boolean | 0..1 | Is event to be added clocked ( `true` ) or not ( `false` ).  
3 | IsCreatedWithPinCode | boolean | 0..1 | Is event to be added created with PIN-code ( `true` ) or not ( `false` ).  
3 | OvertimeBasePartTargetedTo | string | 0..1 | Overtime base part target for the event to be added.  
3 | OvertimeIncrementPartTargetedTo | string | 0..1 | Overtime increment part target for the event to be added.  
3 | ResetValue | decimal | 0..1 | The amount in minutes, or the amount in days if the accural is a day based accrual, to set when inserting accrual reset events  
3 | ChangeValue | decimal | 0..1 | The amount in minutes, or the amount in days if the accural is a day based accrual, to set when inserting accrual change events  
3 | RelatedProjects | XML element | 0..1 | Projects that the event targets. This element must contain ActivityToProjectRelation - elements for each of the project that is linked to the event (see more from the next row).  
4 | ActivityToProjectRelation | XML element | 0..n | Information about a single project to be added for the event.  
5 | Id | integer | 0..1 | Unique Nepton identifier of the project. Either Id or Code must be provided for the project relation.  
5 | Duration | integer | 0..1 | Project duration in minutes.  
5 | Name | string | 0..1 | Project name. Information is not used.  
5 | Code | string | 0..1 | Project code. Either Id or Code must be provided for the project relation.  
3 | WorkIncrements | XML element | 0..1 | Supplements to be added for the event.  
4 | WorkIncrement | XML element | 0..n |   
5 | Index | integer | 1 | Index of the supplement  
5 | Value | decimal | 1 | Supplement value in minutes, pieces or decimals.  
3 | ExternalIdentifiers | XML element | 0..1 | External identifiers for the event  
4 | ExternalIdentifier | XML element | 1..n | External identifier to be set for the event  
5 | Identifier | string | 1 | External identifier  
5 | IdentifierType | string | 1 | Type of external identifier. Only supported type at the moment is `External` .  
3 | ActivityDetails | XML element | 0..1 | Element which contains event type specific details such as sick leave or absence details. More info about these described in rows below.  
4 | AbsenceDetails | XML element | 0..1 |  If event type is of absence type, its details can be sent as child elements of AbsenceDetails - element. AbsenseDetails - element must be a child of ActivityDetails - element. If AbsenceDetails - fields have not been defined, default values for absence type and event type will be used. If compensation or accrual of vacation days is not set, they are defined automatically the same way as is in event editing form in the user interface of Nepton service. User permissions function the same way as in user interfaces permissions for "Add/Edit event" - page.  
5 | AbsenceTypeId | Int | 0..1 | Identifier for absence type to be used. Absence type identifiers can be found in Nepton user interface from Settings > Work hours > Absence types.  
5 | AbsenceTypeName | String | 0..1 | Alternative method of providing absence type based on its name or translation, e.g. "Ammattiyhdistystoiminta". It is recommended to use primarily AbsenceTypeId -field, if possible.  
5 | CompensationTypeId | Int | 0..1 | Absence compensation type identifier  
1 = paid,  
2 = unpaid,  
3 = reduced salary  
5 | CompensationTypeName | string | 0..1 | Alternative method of providing absence compensation type by name or translation, e.g. "palkallinen", "paid", "palkaton", "unpaid", "vähennetty palkka", "reduced salary"  
5 | EarnsVacationDays | bool | 0..1 | Does absence accrue vacation days (true/false)  
4 | SickLeaveDetails | XML element | 0..1 |  If event type is sick leave, details can be sent as child elements in SickLeaveDetails - element. SickLeaveDetails - element must be a child of ActivityDetails - element. If sick leave details are not provided, by default details are used from "Sick" - sick leave type. If compensation or accrual of vacation days is not set, they are defined automatically the same way as is in event editing form in the user interface of Nepton service. User permissions function the same way as in user interfaces permissions for "Add/Edit event" - page.  
5 | SickLeaveTypeId | Int | 0..1 | Sick leave type identifier:  
1=Sick,  
2=Child sick,  
3=Accident at work,  
4=Accident while commuting,  
5=Accident in free time  
5 | SickLeaveTypeName | String | 0..1 |  Alternative method of providing sick leave type based on its name or translation. It is recommended to use primarily SickLeaveTypeId -field, if possible.  
5 | MedicalCertificateGiven | bool | 0..1 | Is medical certificate given? (true/false)  
5 | SupervisorsPermission | bool | 0..1 | Does sick leave have permission of supervisor? (true/false)  
5 | ReasonCode | String | 0..1 | Reason code  
5 | CompensationTypeId | Int | 0..1 | Identifier for sick leave compensation type  
1 = paid,  
2 = unpaid,  
3 = reduced salary  
5 | CompensationTypeName | string | 0..1 | Alternative method of providing sick leave compensation type by name or translation e.g. "palkallinen", "paid", "palkaton", "unpaid", "vähennetty palkka", "reduced salary"  
5 | EarnsVacationDays | Bool | 0..1 | Does sick leave accrue vacation days? (true/false)  
4 | PlannedWorkDetails | XML element | 0 | Not in use. Better suport for different kind of details in planned work and their grouping will be enabled in future versions.  
### Example request
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV5>
          <CallerAuthentication /><!-- Authentication is required but is omitted from this example -->
          <ActivityList>
            <Activity>
              <UserPersonExternalIdentifier>
                <Identifier>EMP-12345</Identifier>
                <FieldName>ExternalIdentifier1</FieldName>
              </UserPersonExternalIdentifier>
              <ActivityTypeCode>201</ActivityTypeCode>
              <BeginDateTime>2021-01-19T08:00:00</BeginDateTime>
              <ApproverUserPersonExternalIdentifier>
                <Identifier>MGR-67890</Identifier>
                <FieldName>ExternalIdentifier1</FieldName>
              <ApproverUserPersonExternalIdentifier>
              <Comment>Hard work</Comment>
              <IsClockedEvent>true</IsClockedEvent>
              <ExternalIdentifiers>
                <ExternalIdentifier>
                  <Identifier>27ae3e08-bfa0-11eb-8529-0242ac130003</Identifier>
                  <IdentifierType>External</IdentifierType>
                </ExternalIdentifier>
              </ExternalIdentifiers>
              <RelatedProjects>
                <ActivityToProjectRelation>
                  <Id>1234567890</Id><!-- Refers to a project with Nepton internal identifier 1234567890 -->
                  <Duration>120</Duration>
                </ActivityToProjectRelation>
                <ActivityToProjectRelation>
                  <Code>ExampleProjectCode</Code><!-- Refers to a project with code ExampleProjectCode -->
                  <Duration>60</Duration>
                </ActivityToProjectRelation>
              </RelatedProjects>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
### Example request absence/sick leave
AbsenceDetails - element of absence events and SickLeaveDetails - element of sick leaves must be children of ActivityDetails - element like in the examples below:
#### Absence
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV5>
          <CallerAuthentication /><!-- Authentication is required but is omitted from this example -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>4</ActivityTypeCode>
              <BeginDateTime>2024-01-19T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-19T16:00:00</EndDateTime>
              <ApproverUserPersonnelNumber>9999</ApproverUserPersonnelNumber>
              <ActivityDetails>
                <AbsenceDetails>
                  <AbsenceTypeId>8</AbsenceTypeId>
                  <CompensationTypeId>1</CompensationTypeId>
                  <EarnsVacationDays>true</EarnsVacationDays>
                </AbsenceDetails>
              </ActivityDetails>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
#### Sick leave
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV5>
          <CallerAuthentication /><!-- Authentication is required but is omitted from this example -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>2</ActivityTypeCode>
              <BeginDateTime>2024-01-22T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-22T16:00:00</EndDateTime>
              <ApproverUserPersonnelNumber>9999</ApproverUserPersonnelNumber>
              <ActivityDetails>
                <SickLeaveDetails>
                  <SickLeaveTypeId>3</SickLeaveTypeId>
                  <MedicalCertificateGiven>true</MedicalCertificateGiven>
                  <SupervisorsPermission>true</SupervisorsPermission>
                  <ReasonCode>12345</ReasonCode>
                  <CompensationTypeId>1</CompensationTypeId>
                  <EarnsVacationDays>true</EarnsVacationDays>
                </SickLeaveDetails>
              </ActivityDetails>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
    
[/code]
### Example request accrual reset/change
Setting the balance to +1:00 with a balance reset
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV5>
          <CallerAuthentication /><!-- Authentication is required but is omitted from this example -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>12</ActivityTypeCode>
              <ResetValue>60</ResetValue>
              <BeginDateTime>2024-01-22T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-22T08:00:00</EndDateTime>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
    
[/code]
Deducting 1h from the balance with a balance change
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV5>
          <CallerAuthentication /><!-- Authentication is required but is omitted from this example -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>13</ActivityTypeCode>
              <ChangeValue>-60</ChangeValue>
              <BeginDateTime>2024-01-22T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-22T08:00:00</EndDateTime>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
### Response
**LEVEL** | **FIELD NAME** | **TYPE** | **OCCURRENCES** | **DESCRIPTION**  
---|---|---|---|---  
0 | ReturnValueForInsertActivitiesV5 | XML element | 1 | Root element under SOAP body  
1 | ResponseCode | integer | 1 | Response code of handling the request. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).  
1 | ResponseString | string | 1 | Response description  
1 | ActivityList | XML element | 1 |   
1 | ActivityList | XML element | 0..1 | Events that were added  
2 | Activity | XML element | 0..n | Added event  
3 | Id | integer | 0..1 | Unique Nepton identifier of added event  
3 | ExternalIdentifiers | XML element | 0..1 | External identifiers of added event. In error situations primarily `ExternalIdentifiers` is returned and secondarily  `ExistingExternalIdentifier` is returned .  
4 | ExternalIdentifier | XML element | 1..n |   
5 | Identifier | string | 1 | External identifier  
5 | IdentifierType | string | 1 | Type of external identifier. Only supported type at the moment is `External` .  
3 | Success | boolean | 1 | Was event added successfully ( `true` ) or not ( `false` ).  
3 | ErrorCode | integer | 0..1 | If adding event was not successful, reason code for the error. List of possible codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>)  
3 | ErrorMessage | string | 0..1 | If adding event was not succesful, reason description for the error.  
### Example response
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForInsertActivitiesV5>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <ActivityList>
            <Activity>
              <Id>12345678</Id>
              <ExternalIdentifiers>
                <ExternalIdentifier>
                  <Identifier>27ae3e08-bfa0-11eb-8529-0242ac130003</Identifier>
                  <IdentifierType>External</IdentifierType>
                </ExternalIdentifier>
              </ExternalIdentifiers>
              <Success>true</Success>
            </Activity>
          </ActivityList>
        </tyo:ReturnValueForInsertActivitiesV5>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
