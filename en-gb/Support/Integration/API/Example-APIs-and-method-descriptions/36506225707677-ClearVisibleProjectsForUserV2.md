---
id: 36506225707677
title: ClearVisibleProjectsForUserV2
url: https://support.nepton.com/hc/en-gb/articles/36506225707677-ClearVisibleProjectsForUserV2
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
edited_at: '2026-06-01T10:51:17Z'
---

# ClearVisibleProjectsForUserV2

## Interface overview
The web service allows you to remove all user-level project visibility from a specified person. This does not affect projects defined through a person group.
The WSDL schema of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). The interfaces are described in general [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The occurrences column in the description determines whether a piece of information is mandatory in the call or not. Occurrences 0 means that the information in question does not need to be passed in the call. Occurrences 1 means that the information must appear once in the call. Occurrences 0..n means that the information in question can appear any number of times in the call. Occurrences 1..n means that the information in question must appear in the data at least once, but can appear more often.
## Changes to previous version ([ClearVisibleProjectsForUser](<https://support.nepton.com/hc/en-gb/articles/6919474574237>))
V2-version adds the following field
Field | Description  
---|---  
PersonExternalIdentifier | Allows identification of a person using an external identifier  
## User identifiers
The target user can be identified by a unique Nepton ID, employee number, external identifier, or a username. One of these must be provided. The service returns an error if no username has been specified or no user matching the identifier was found.
## Data to send
LEVEL | FIELD NAME | FORMAT | OCCURRENCES | DESCRIPTION  
---|---|---|---|---  
0 | ParametersForClearVisibleProjectsForUserV2 | XML element | 1 | Root, below SOAP body  
1 | CallerAuthentication | XML element | 1 | Authentication details, see more [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>)  
1 | ClearVisibleProjectsForUserList | XML element | 1 |   
2 | ClearVisibleProjectForUser | XML element | 1..n |   
3 | UserId | integer | 0..1 | Target user's id  
3 | PersonnelNumber | string | 0..1 | Target user's personnel number  
3 | PersonExternalIdentifier | XML Element | 0..1 | NEW in V2 - Target user's external identifier  
4 | Identifier | string | 1 | Value of external identifier  
4 | FieldName | string | 1 |  Field name of external identifier. Supported values:
[code] 
    ExternalIdentifier1
[/code]  
### Response
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ReturnValueForClearVisibleProjectsForUserV2 | XML element | 1 | Root, below SOAP body  
1 | Responsecode | integer | 1 | General response code  
1 | ResponseString | string | 1 | General response message  
1 | ClearVisibleProjectsForUserResultList | XML element | 1..n | List of results for each handled row  
2 | ResponseCode | integer | 1 | Response code for a single row  
2 | ResponseString | string | 1 | Response message for a single row  
2 | UserId | integer | 1 | Target user's id  
2 | Username | string | 1 | Target user's username  
2 | PersonnelNumber | string | 1 | Target user's personnel number  
2 | PersonExternalIdentifier | XML element | 1 | NEW in V2 - Target user's external identifier  
3 | Identifier | string | 1 | Value of external identifier  
3 | FieldName | string | 1 |  Field name of external identifier. Supported values:
[code] 
    ExternalIdentifier1
[/code]  
### Example requests
#### Example with external identifier (new in V2)
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForClearVisibleProjectsForUserV2>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->  
          <ClearVisibleProjectsForUserList>  
            <ClearVisibleProjectForUser>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-12345<Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUser>  
            <ClearVisibleProjectForUser>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-67890<Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUser>  
          </ClearVisibleProjectsForUserList>  
        </tyo:ParametersForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
#### Example with personnel number
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForClearVisibleProjectsForUserV2>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->  
          <ClearVisibleProjectsForUserList>  
            <ClearVisibleProjectForUser>  
              <PersonnelNumber>12345</PersonnelNumber>  
            </ClearVisibleProjectForUser>  
          </ClearVisibleProjectsForUserList>  
        </tyo:ParametersForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
### Example response
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForClearVisibleProjectsForUserV2>  
          <ResponseCode>0</ResponseCode>  
          <ResponseString>No errors</ResponseString>  
          <ClearVisibleProjectsForUserResultList>  
            <ClearVisibleProjectForUserResult>  
              <ResponseCode>0</ResponseCode>  
              <ResponseString>No errors</ResponseString>  
              <UserId>1234</UserId>  
              <Username>matti.meikalainen</Username>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-12345</Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUserResult>  
          </ClearVisibleProjectsForUserResultList>  
        </tyo:ReturnValueForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
