---
id: 360005968797
title: SetVisibleProjectsForUserV2
url: https://support.nepton.com/hc/en-gb/articles/360005968797-SetVisibleProjectsForUserV2
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
edited_at: '2026-06-01T14:40:22Z'
---

# SetVisibleProjectsForUserV2

A newer version of this method exists. If you are currently using this method, we recommend that you will look at the instructions of the next method for changes required to update to the next version. You can find the instructions for the next version [here](<https://support.nepton.com/hc/en-gb/articles/36513542448925>)
## Interface overview
The interface sets the projects that are visible for user when registering events.
The WSDL schema of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). The interfaces are described in general [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The occurrences column in the description determines whether a piece of information is mandatory in the call or not. Occurrences 0 means that the information in question does not need to be passed in the call. Occurrences 1 means that the information must appear once in the call. Occurrences 0..n means that the information in question can appear any number of times in the call. Occurrences 1..n means that the information in question must appear in the data at least once, but can appear more often.
## Changes from the previous version ([SetVisibleProjectsForUser](<https://support.nepton.com/knowledge/articles/6885147716893>))
### Structural changes
**Old** | **New** | **Additional info**  
---|---|---
[code] 
    <tyo:ParametersForSetVisibleProjectsForUser>  
      ...  
    </tyo:ParametersForSetVisibleProjectsForUser>
[/code]  
| 
[code]
    <tyo:ParametersForSetVisibleProjectsForUserV2>  
    ...  
    </tyo:ParametersForSetVisibleProjectsForUserV2>
[/code]
| Root element name changed in call
[code] 
    <tyo:ReturnValueForSetVisibleProjectsForUser>  
      ...  
    </tyo:ReturnValueForSetVisibleProjectsForUser>
[/code]  
| 
[code]
    <tyo:ReturnValueForSetVisibleProjectsForUserV2>  
    ...  
    </tyo:ReturnValueForSetVisibleProjectsForUserV2>
[/code]
| Root element name changed in response
[code] 
    <SetVisibleProjectsForUserList>  
      <SetVisibleProjectForUser>  
        ...  
      </SetVisibleProjectForUser>  
    </SetVisibleProjectsForUserList>
[/code]  
| 
[code]
    <SetVisibleProjectsForUserListV2>  
      <SetVisibleProjectForUserV2>  
        ...  
      </SetVisibleProjectForUserV2>  
    </SetVisibleProjectsForUserListV2>
[/code]
| In call SetVisibleProjectsForUserList-element and below it SetVisibleProjectsForUser element names have changed
[code] 
    <SetVisibleProjectsForUserResultList>  
      <SetVisibleProjectsForUserResult>  
        ...  
      </SetVisibleProjectsForUserResul>  
    </SetVisibleProjectsForUserResultList>
[/code]  
| 
[code]
    <SetVisibleProjectsForUserV2ResultList>  
      <SetVisibleProjectsForUserV2Result>  
        ...  
      </SetVisibleProjectsForUserV2Resul>  
    </SetVisibleProjectsForUserV2ResultList>
[/code]
| In response SetVisibleProjectsForUserResultList-element and below it setVisibleProjectsForUserResult-element names have changed  
### New features and elements
  * Projects can be referenced using the project's external identifier.
    * Added ProjectIdentifier-element to the call
  * Project's external identifier is included in the response
    * Added ProjectIndentifier-element to the response


## Sent Data
Level | Field name | Format | Occurences | Description  
---|---|---|---|---  
0 | ParametersForSetVisibleProjectsForUserV2 | XML element | 1 | Root, below SOAP body  
1 | CallerAuthentication | XML element | 1 | Authentication details. More information about authentication [here.](<https://support.nepton.com/hc/en-gb/articles/360019983978>)  
1 | SetVisibleProjectsForUserListV2 | XML element | 1 | List of project visibility settings for one user, so a list of SetVisibleProjectForUserV2-elements  
2 | SetVisibleProjectForUserV2 | XML element | 1..n | Setting the visibility of one project for one person.  
3 | ProjectId | unsignedIntt | 0..1 | Unique project identifier provided by Nepton  
3 | ProjectCode | string | 0..1 | Project code  
3 | ProjectIdentifier | XML element | 0..1 | Project identifier  
4 | Identifier | string | 1 | Project identifier string  
4 | IdentifierType | string | 1 | Project identifier type. Can be either `ProjectCode` or `ExternalIdentifier`  
3 | UserId | unsignedInt | 0..1 | Unique personal identifier provided by Nepton  
3 | Username | string | 0..1 | Person's username  
3 | PersonnelNumber | string | 0..1 | Person's personnel number  
3 | ProjectVisible | boolean | 1 | Can person see project (`true`) or not (`false`)  
### Call example
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
        <soapenv:Body>  
          <tyo:ParametersForSetVisibleProjectsForUserV2>  
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <SetVisibleProjectsForUserListV2>  
            <SetVisibleProjectForUserV2>  
              <ProjectIdentifier>  
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>  
                <IdentifierType>ExternalIdentifier</IdentifierType>  
              </ProjectIdentifier>  
              <PersonnelNumber>9001</PersonnelNumber>  
              <ProjectVisible>true</ProjectVisible>  
            </SetVisibleProjectForUserV2>  
          </SetVisibleProjectsForUserListV2>  
        </tyo:ParametersForSetVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Response
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForSetVisibleProjectsForUserV2 | XML element | 1 |   
1 | ResponseCode | integer | 1 | Response code of handling the request. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).  
1 | ResponseString | string | 1 | Code description  
1 | SetVisibleProjectsForUserV2ResultList | XML element | 1 |   
2 | SetVisibleProjectsForUserV2Result | XML element | 0..n | Result for setting project visibility for user  
3 | ResponseCode | integer | 1 | Response code. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).  
3 | ResponseString | string | 1 | Response code description  
3 | ProjectId | unsignedInt | 0..1 |  The unique project identifier provided by Nepton. The value can also be `null`, for example:
[code] 
    <ProjectId xsi:nil="true" />
[/code]
In error situations, the value is not returned if it was not provided in the query.  
3 | ProjectCode | string | 0..1 |  Project's code. The value can also be `null`, for example:
[code] 
    <ProjectCode xsi:nil="true" />
[/code]
In error situations, the value is not returned if it was not provided in the query.  
3 | ProjectIdentifier | XML element | 0..1 | Project identifier. The value is not returned if it is not provided in the query.  
4 | Identifier | string | 1 | Project identifier string  
4 | IdentifierType | string | 1 |  Project identifier type. Can be either `ProjectCode` tai `ExternalIdentifier` The value is not returned if it is not provided in the query.  
3 | UserId | unsignedInt | 0..1 |  The unique identifier of the person given by Nepton. The value can also be `null`, for example:
[code] 
    <UserId xsi:nil="true" />
[/code]
The value is not returned if it is not provided in the query.  
3 | Username | string | 0..1 |  Person's username. The value can also be `null`, for example:
[code] 
    <Username xsi:nil="true" />
[/code]
The value is not returned if it is not provided in the query.  
3 | PersonnelNumber | string | 0..1 |  Person's personnel number. The value can also be `null`, for example:
[code] 
    <PersonnelNumber xsi:nil="true" />
[/code]
The value is not returned if it is not provided in the query.  
### Response example
[code]
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForSetVisibleProjectsForUserV2>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <SetVisibleProjectsForUserV2ResultList>  
            <SetVisibleProjectsForUserV2Result>  
              <ResponseCode>1000</ResponseCode>  
              <ResponseString>All clear. No errors.</ResponseString>  
              <ProjectId>76254</ProjectId>  
              <ProjectCode>1000/9001</ProjectCode>  
              <ProjectIdentifier>  
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>  
                <IdentifierType>ExternalIdentifier</IdentifierType>  
              </ProjectIdentifier>  
              <UserId>1234</UserId>  
              <Username>matti.meikäläinen</Username>  
              <PersonnelNumber>9001</PersonnelNumber>  
            </SetVisibleProjectsForUserV2Result>  
          </SetVisibleProjectsForUserV2ResultList>  
        </ns1:ReturnValueForSetVisibleProjectsForUserV2>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
