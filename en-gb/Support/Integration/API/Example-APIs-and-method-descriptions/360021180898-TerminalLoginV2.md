---
id: 360021180898
title: TerminalLoginV2
url: https://support.nepton.com/hc/en-gb/articles/360021180898-TerminalLoginV2
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
edited_at: '2025-09-17T10:26:48Z'
---

# TerminalLoginV2

## Interface overview
The webservice is used to retrieve a person's current status from Nepton. The web service is designed to be used in terminal applications, to show for example the following user related information:
  * Ongoing event registration
  * Projects that can be registered for events
  * Which projects are used by default when starting a new event
  * Is registering a project for an event mandatory or not
  * Work supplements that can be registered for events
  * Default overtime target for work events
  * Event typess that can be registered
  * Person's accruals and their balances


Authentication in the web service differs from other web services in that a person who has successfully authenticated with a username and password can authenticate as another person based on a PIN code or RFID code. In the first step, the authenticated person must have the rights to view personal data. For example:
[code] 
    <CallerAuthentication>  
      <CustomerId>1234</CustomerId>  
      <Username>PäätelaiteKäyttäjä</Username>  
      <Password>KuvitteellinenSalasana123</Password>  
      <PinCode>1234</PinCode> <!-- Pin code given on terminal -->  
    </CallerAuthentication>
[/code]
If the person cannot be found with the provided PIN code or RFID code, authentication will fail.
The WSDL schema of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). The interfaces are described in general [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The occurrences column in the description determines whether a piece of information is mandatory in the call or not. Occurrences 0 means that the information in question does not need to be passed in the call. Occurrences 1 means that the information must appear once in the call. Occurrences 0..n means that the information in question can appear any number of times in the call. Occurrences 1..n means that the information in question must appear in the data at least once, but can appear more often.
## Changes from previous version ([TerminalLogin](<https://support.nepton.com/hc/articles/6887099778333>))
### Structural changes
**Old** | **New** | **Additional information**  
---|---|---
[code] 
    <tyo:ParametersForTerminalLogin>  
      ...  
    </tyo:ParametersForTerminalLogin>
[/code]  
| 
[code] 
    <tyo:ParametersForTerminalLoginV2>  
      ...  
    </tyo:ParametersForTerminalLoginV2>
[/code]
| The name of the call root element has changed.
[code] 
    <tyo:ReturnValueForTerminalLogin>  
      ...  
    </tyo:ReturnValueForTerminalLogin>
[/code]  
| 
[code] 
    <tyo:ReturnValueForTerminalLoginV2>  
      ...  
    </tyo:ReturnValueForTerminalLoginV2>
[/code]
| The name of the response root element has changed.
[code] 
    <OngoingActivity>  
      <BeginDateTime>2020-01-01 12:00:00</BeginDateTime>  
      <EndDateTime>2020-01-01 14:00:00</EndDateTime>  
      <ModifiedDateTime>2020-01-01 16:00:00</ModifiedDateTime>  
    </OngoingActivity>  
    
[/code]  
| 
[code] 
    <OngoingActivity>  
      <BeginDateTime>2020-01-01T12:00:00</BeginDateTime>  
      <EndDateTime>2020-01-01T14:00:00</EndDateTime>  
      <ModifiedDateTime>2020-01-01T16:00:00</ModifiedDateTime>  
    </OngoingActivity>
[/code]
| In the response, the date and time elements are now of type datetime, which slightly affects the date format (BeginDateTime, EndDateTime, ModifiedDateTime)  
### Obsolete elements
The following elements were previously in the response twice, first under the OngoingActivity element and the second time under the ActivityDetails element:
  * PlannedWorkCalculationUnit
  * PlannedWorkColor
  * PlannedWorkUseForWorkDayLengthCalculations
  * PlannedWorkCanBeCancelledUntil
  * PlannedWorkWorkTimeLimitOffsetStartInMins
  * PlannedWorkWorkTimeLimitOffsetEndInMins
  * PlannedWorkActivityGroupPublicInfo


From now on, these elements will only be found under the ActivityDetails element.
RelatedActivityId was already reported as deprecated in the previous version, but now this element has been technically removed from the response.
### New features and elements
  * The response contains the personnel number for the person in the event (UserPersonnelNumber element)
  * The response contains the personnel number for the approver of the event (ApproverPersonnelNumber element)
  * The response contains the external identifiers for the event (ExternalIdentifiers element)


## Sent Data
Level | Field name | Format | Occurences | Description  
---|---|---|---|---  
Root,  
below SOAP body | ParametersForTerminalLoginV2 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | More information about authentications [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>).  
### Call example
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForTerminalLoginV2>  
          <CallerAuthentication>  
            <CustomerId>1234</CustomerId>  
            <Username>PäätelaiteKäyttäjä</Username>  
            <Password>KuvitteellinenSalasana123</Password>  
            <RFID>2893789127981239</RFID> <!-- RFID code read on the terminal -->          
          </CallerAuthentication>  
        </tyo:ParametersForTerminalLoginV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Response
Level | Field name | Format | Occurences |  Description  
---|---|---|---|---  
| ReturnValueForTerminalLoginV2 | XML element | 1 | Root element,  
below SOAP body  
1 | ResponseCode | integer | 1 | Processing result code. Possible codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).  
1 | ResponseString | string | 0..1 | Code description  
1 | UserId | integer | 0..1 | Nepton ID of the authenticated person  
1 | CustomerId | integer | 0..1 | Deployment's worktime customer ID (from Nepton)  
1 | Username | string | 0..1 | The username of the authenticated person  
1 | FirstName | string | 0..1 | The first name of the authenticated person  
1 | LastName | string | 0..1 | The last name of the authenticated person  
1 | Locale | string | 0..1 | The language of the authenticated personhenkilön kieli. The possible values are: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
1 | AvailableProjects | XML element | 0..1 |  Projects that the person can add to events. Note: Although the project's activity status and start and end dates are returned, only projects that are active on the current day are returned.  
2 | Project | XML element | 0..n | Data of one project.  
3 | Id | integer | 0..1 | Project's unique Nepton identifier  
3 | Name | string | 1 | Project's name  
3 | Deleted | boolean | 0..1 | If the project is deleted (`true`) or not (`false`)  
3 | Active | boolean | 0..1 | If the project is active (`true`) or not (`false`)  
3 | Code | string | 0..1 | Project code  
3 | TypeInternalName | string | 0..1 | Project's internal name  
3 | Description | string | 0..1 | Project's description  
3 | StartDate | date | 0..1 | Project start date, format `YYYY-MM-DD`. Value can also be `nil`, for example: 
[code]
    <StartDate xsi:nil="true" />
[/code]  
3 | EndDate | date | 0..1 | Project end date, format `YYYY-MM-DD`. Value can also be `nil`, for example:  

[code] 
    <EndDate xsi:nil="true" />
[/code]  
3 | ParentProjectId | integer | 0..1 | The Nepton identifier of the project's parent project. Value can also be `nil`, for example: 
[code]
    <ParentProjectId xsi:nil="true" />
[/code]  
3 | ParentProjectCode | string | 0..1 | The code of the project's parent project. Value can also be `nil`, for example: 
[code]
    <ParentProjectCode xsi:nil="true" />
[/code]  
3 | Left | integer | 0..1 | Data is not used  
3 | Right | integer | 0..1 | Data is not used  
3 | ChildProjects | XML element | 0..1 | Project's child projects. Data is not used  
1 | ProjectsToContinue | XML element | 0..1 | Projects to continue  
2 | ProjectToContinue | XML element | 0..n |   
3 | Id | integer | 0..1 | The project's unique identifier in Nepton  
3 | Duration | integer | 0..1 | Project duration in minutes. Data is not used.  
3 | Name | string | 0..1 | Project name  
3 | Code | string | 0..1 | Project code  
1 | OnGoingActivity | XML element | 0..1 | Information of ongoing event  
2 | Id | integer | 0..1 | The event's unique identifier in Nepton  
2 | UserId | integer | 0..1 | The person's unique identifier in Nepton.  
2 | UserFirstName | string | 0..1 | Person's first name.   
2 | UserLastName | string | 0..1 | Person's last name.   
2 | UserUsername | string | 0..1 |  Person's username.   
2 | UserPersonnelNumber | string | 0..1 |  Person's personnel number.   
2 | UserSocialSecurityNumber | string | 0..1 |  Person's social security number.   
2 | ActivityTypeId | integer | 0..1 | Event type's unique identifier in Nepton.  
2 | ActivityTypeName | string | 0..1 | Event type name.  
2 | ActivityTypeCategoryId | string | 0..1 | Event type category's unique Nepton identifier.  
2 | ActivityTypeCategoryName | string | 0..1 | Event type category name.  
2 | ApproverUserId | integer | 0..1 | Person who has approved the event. Reference by user ID.  
2 | ApproverFirstName | string | 0..1 | The first name of the person who has approved the event.  
2 | ApproverLastName | string | 0..1 | The last name of the person who has approved the event.  
2 | ApproverPersonnelNumber | string | 0..1 | The personnel number of the person who has approved the event.  
2 | BeginDateTime | dateTime | 0..1 | The start date and time of the event. Format is `YYYY-MM-DDTHH:MM:SS`, for example`2021-02-18T12:30:00`.  
2 | EndDateTime | dateTime | 0..1 | The end date and time of the event. Format is `YYYY-MM-DDTHH:MM:SS`, for example`2021-02-18T12:30:00`.  
2 | ModifiedDateTime | dateTime | 0..1 | The time the event was last modified. The format is `YYYY-MM-DDTHH:MM:SS`, for example `2021-02-18T12:30:00`.  
2 | ModifiedByUserId | integer | 0..1 |  User ID of the user who last modified the event.  
2 | ModifiedFromIp | string | 0..1 | The IP-address from where the event was last modified from.  
2 | Comment | string | 0..1 | Comments on the event.  
2 | IsClockedEvent | boolean | 0..1 | Is the event clocked (`true`) or not (`false`).  
2 | IsCreatedWithPinCode | boolean | 0..1 | Is the event clocked with PIN code (`true`) or not (`false`).  
2 | OvertimeBasePartTargetedTo | string | 0..1 | Overtime base part target for the event.  
2 | OvertimeIncrementPartTargetedTo | string | 0..1 | Overtime increment part target for the event.  
2 | RelatedProjects | XML element | 0..1 | Projects on the event.  
3 | ActivityToProjectRelation | XML element | 0..n |   
4 | Id | integer | 0..1 | Project unique identifier in Nepton  
4 | Duration | integer | 0..1 | Project duration in minutes.  
4 | Name | string | 0..1 | Project name  
4 | Code | string | 0..1 | Project code  
2 | WorkIncrements | XML element | 0..1 | Supplements on the event.  
3 | WorkIncrement | XML element | 0..n |   
4 | Index | integer | 1 | Supplement index  
4 | Value | decimal | 1 | Supplement value in minutes, units, or decimals.  
2 | ActivityDetails | XML element | 0..1 | Additional information on the event  
3 | AbsenceDetails | XML element | 0..1 | Additional information on the absence  
4 | CompensationTypeId | integer | 0..1 |  Absence compensation type identifier. Possible values:
  * `1` \- paid
  * `2` \- unpaid
  * `3` \- reduced pay

  
4 | CompensationTypeName | string | 0..1 | Absence compensation type name  
4 | EarnsVacationDays | boolean | 0..1 | Does the absence accumulate annual holiday (`true`) or not (`false`)  
4 | AbsenceTypeId | integer | 0..1 | Absence identifier. Absence types can be found in Worktime > Working community settings > Work hours > Absence types.  
4 | AbsenceTypeName | string | 0..1 | Absence type name  
3 | PlannedWorkDetails | XML element | 0..1 | Additional details for planned work shift  
4 | PlannedWorkCalculationUnit | string | 0..1 | Calculation unit of the work shift location. Read more [here](<https://support.nepton.com/hc/en-gb/articles/360002575538>).  
4 | PlannedWorkColor | string | 0..1 | The color of the planning level of the work shift location. The color can be set in Shift Planning: Locations > Select planning level > Planning level settings > Planning level color.  
4 | PlannedWorkUseForWorkDayLengthCalculations | boolean | 0..1 | Does workday length come from shift (`true`) or not (`false`)  
4 | PlannedWorkCanBeCancelledUntil | string | 0..1 | Date and time, until which the shift need can be cancelled. Format is `VVVV-KK-PPTHH:MM:SS`, for example `2021-02-18T12:30:00`.  
4 | PlannedWorkWorkTimeLimitOffsetStartInMins | integer | 0..1 |  The time offset in minutes for the allowed work start time from the work shift. The value is added to the event start time used to set the allowed work start time. A value of zero sets the allowed work start time as the event start time.  
4 | PlannedWorkWorkTimeLimitOffsetEndInMins | integer | 0..1 |  The time offset in minutes for the allowed work end time from the work shift. The value is added to the event end time used to set the allowed work end time. A value of zero sets the allowed work end time as the event end time.  
4 | AssumedLunchInMinutes | integer | 0..1 | The length of the assumed lunch break from work shift in minutes.  
4 | PlannedWorkActivityGroupPublicInfo | string | 0..1 | Public information given to shift group information  
3 | SickLeaveDetails | XML element | 0..1 | Sick leave details  
4 | CompensationTypeId | integer | 0..1 |  Identifier of the sick leave compensation type. Possible values:
  * `1` \- paid
  * `2` \- unpaid
  * `3` \- reduced pay

  
4 | CompensationTypeName | string | 0..1 | Sick leave compensation type name  
4 | EarnsVacationDays | boolean | 0..1 | Does absence earn vacation days (`true`) or not (`false`)  
4 | SickLeaveTypeId | integer | 0..1 |  Identifier of the sick leave type. Possible values:
  * `1` \- sick
  * `2` \- sick child
  * `3` \- work accident
  * `4` \- work travel accident
  * `5` \- leisure time accident

  
4 | SickLeaveTypeName | string | 0..1 | Sick leave type name  
4 | MedicalCertificateGiven | boolean | 0..1 | If medical certificate has been given (`true`) or not (`false`)  
4 | SupervisorsPermission | boolean | 0..1 | If supervisor has approved the sick leave instead of medical certificate (`true`) or not (`false`)  
4 | ReasonCode | string | 0..1 | Reason code for sick leave  
2 | ExternalIdentifiers | XML element | 0..1 | External identifiers for the event  
3 | ExternalIdentifier | XML element | 1..n | External identifier for the event  
4 | Identifier | string | 1 | External identifier  
4 | IdentifierType | string | 1 | External identifier type. At the moment the only supported type is `External`  
2 | IsDeleted | boolean | 0..1 | Is the event deleted (`true`) or not (`false`)  
1 | ProjectMandatory | boolean | 0..1 | Is it mandatory to add project to an event (`true`) or not (`false`)  
1 | WorkIncrementsForUser | XML element | 0..1 | Supplements that can be added to events  
2 | WorkIncrement | XML element | 0..n |   
3 | Index | integer | 0..1 | Supplement indexi. Information is needed to record supplements.  
3 | Name | string | 0..1 |  Supplement name  
3 | UsedUnit | XML element | 0..1 | Supplement unit. Returns one of the following values: 
  * `minutes`
  * `decimal`
  * `units`

  
1 | DiningIncrements | XML element | 0..1 | Supplements for the latest dining event.   
2 | ActivityId | integer | 1 | Nepton identifier for a dining event  
2 | WorkIncrement | XML element | 0..n |   
3 | Index | integer | 1 | Supplement index  
3 | Value | decimal | 1 | Supplement value  
1 | DefaultOvertimeBasePartTargetedTo | string | 0..1 | Default overtime base part target  
1 | DefaultOvertimeIncrementPartTargetedTo | string | 0..1 | Default overtime increment part target  
1 | ActivityTypes | XML element | 0..1 | List of events that the user can add via terminals  
2 | ActivityType | XML element | 0..n |   
3 | Id | integer | 1 | Nepton identifier for an event type  
3 | InternalName | string | 1 | Event type internal identifier  
3 | TranslatedName | XML element | 0..n | Translated name for an event type  
4 | Locale | string | 1 | Language. Possible values are: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
4 | Name | string | 1 | Event type name  
3 | Code | string | 0..1 | Event type code  
3 | Visible | boolean | 0..1 | is event type visible or not. Data is not used.  
3 | CanAssignWorkIncrements | boolean | 0..1 | Can supplements be added to the event type (`true`) or not (`false`)  
3 | CanHaveRelatedProjects | boolean | 0..1 | Can projects be added to the event type (`true`) or not (`false`)  
3 | CategoryInternalName | string | 1 | Event type category's internal identifier in Nepton  
3 | TranslatedCategoryName | XML element | 0..n | Event type category translated name  
4 | Locale | string | 1 | Language. Possible values are: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
4 | Name | string | 1 | Event type category name  
3 | BeginDateTimeInput | string | 0..1 | Event type to be started start time input. Possible values are: 
  * `disabled` \- Not allowed
  * `optional` \- Allowed
  * `mandatory` \- Start time is mandatory

  
3 | EndDateTimeInput | string | 0..1 | Event type to be ended start time input Possible values are: 
  * `disabled` \- Not allowed
  * `optional` \- Allowed
  * `mandatory` \- Start time is mandatory

  
1 | AccrualList | XML element | 0..1 | List of accruals and their values  
2 | Accrual | XML element | 0..n |   
3 | InternalName | string | 1 | Name used as an identifier for the accrual  
3 | Name | string | 1 | Accrual name  
3 | Amount | string | 1 | Accrual value in hours and minutes, for example `-02:43`  
3 | ChangeAmount | string | 0..1 | How much the value of the accrual has changed on the current day. Value in hours and minutes, for example `+00:30`  
1 | CurrentDateTimeUTC | dateTime | 1 | The current time in the UTC time zone. Format is `YYYY-MM-DDTHH:MM:SS`, for example`2021-02-18T12:30:00`.  
### Response example
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForTerminalLoginV2>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <UserId>123456</UserId>  
          <CustomerId>1234</CustomerId>  
          <Username>matti.meikäläinen</Username>  
          <FirstName>Matti</FirstName>  
          <LastName>Meikäläinen</LastName>  
          <Locale>fi_FI</Locale>  
          <AvailableProjects>  
            <Project>  
              <Id>9001</Id>  
              <Name>Asiakaspalvelu</Name>  
              <Deleted>false</Deleted>  
              <Active>true</Active>  
              <Code>ASPA01</Code>  
              <TypeInternalName>project_work</TypeInternalName>  
              <Description>Asiakaspalvelutyö</Description>  
              <StartDate xsi:nil="true" />  
              <EndDate xsi:nil="true" />  
              <ParentProjectId xsi:nil="true" />  
              <ParentProjectCode xsi:nil="true" />  
            </Project>  
          </AvailableProjects>  
          <ProjectsToContinue>  
            <ProjectToContinue>  
              <Id>9001</Id>  
              <Name>Asiakaspalvelu</Name>  
              <Code>ASPA01</Code>  
            </ProjectToContinue>  
          </ProjectsToContinue>  
          <OnGoingActivity>  
            <Id>12345678</Id>  
            <UserId>123456</UserId>  
            <UserFirstName>Maija</UserFirstName>  
            <UserLastName>Meikäläinen</UserLastName>  
            <UserUsername>maija.meikäläinen</UserUsername>  
            <UserPersonnelNumber>1111</UserPersonnelNumber>  
            <ActivityTypeId>1</ActivityTypeId>  
            <ActivityTypeName>Työ</ActivityTypeName>  
            <ActivityTypeCategoryId>1</ActivityTypeCategoryId>  
            <ActivityTypeCategoryName>Työ</ActivityTypeCategoryName>  
            <BeginDateTime>2021-01-19T09:12:23</BeginDateTime>  
            <ModifiedDateTime>2021-01-19T09:12:23</ModifiedDateTime>  
            <ModifiedByUserId>123456</ModifiedByUserId>  
            <ModifiedFromIp>127.0.0.1</ModifiedFromIp>  
            <IsClockedEvent>true</IsClockedEvent>  
            <IsCreatedWithPinCode>false</IsCreatedWithPinCode>  
            <OvertimeBasePartTargetedTo>balance</OvertimeBasePartTargetedTo>  
            <OvertimeIncrementPartTargetedTo>uncompensated</OvertimeIncrementPartTargetedTo>  
            <RelatedProjects>  
              <ActivityToProjectRelation>  
                <Id>9001</Id>  
                <Duration>333</Duration>  
                <Name>Asiakaspalvelu</Name>  
                <Code>ASPA01</Code>  
              </ActivityToProjectRelation>  
            </RelatedProjects>  
            <IsDeleted>false</IsDeleted>  
          </OnGoingActivity>  
          <ProjectMandatory>true</ProjectMandatory>  
          <DefaultOvertimeBasePartTargetedTo>balance</DefaultOvertimeBasePartTargetedTo>  
          <DefaultOvertimeIncrementPartTargetedTo>uncompensated</DefaultOvertimeIncrementPartTargetedTo>  
          <ActivityTypes>  
            <ActivityType>  
              <Id>1</Id>  
              <InternalName>Work</InternalName>  
              <TranslatedName>  
                <Locale>fi_FI</Locale>  
                <Name>Työ</Name>  
              </TranslatedName>  
              <TranslatedName>  
                <Locale>en_US</Locale>  
                <Name>Work</Name>  
              </TranslatedName>  
              <CanAssignWorkIncrements>true</CanAssignWorkIncrements>  
              <CanHaveRelatedProjects>true</CanHaveRelatedProjects>  
              <CategoryInternalName>work</CategoryInternalName>  
              <TranslatedCategoryName>  
                <Locale>fi_FI</Locale>  
                <Name>Työ</Name>  
              </TranslatedCategoryName>  
              <TranslatedCategoryName>  
                <Locale>en_US</Locale>  
                <Name>Work</Name>  
              </TranslatedCategoryName>  
              <BeginDateTimeInput>disabled</BeginDateTimeInput>  
              <EndDateTimeInput>disabled</EndDateTimeInput>  
            </ActivityType>  
          </ActivityTypes>  
          <AccrualList>  
            <Accrual>  
              <InternalName>balance</InternalName>  
              <Name>Saldo</Name>  
              <Amount>13:05</Amount>  
            </Accrual>  
          </AccrualList>  
          <CurrentDateTimeUTC>2021-01-20T14:45:11</CurrentDateTimeUTC>  
        </ns1:ReturnValueForTerminalLoginV2>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
