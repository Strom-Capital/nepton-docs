---
id: 6919474574237
title: ClearVisibleProjectsForUser
url: https://support.nepton.com/hc/en-gb/articles/6919474574237-ClearVisibleProjectsForUser
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
edited_at: '2026-06-01T11:16:12Z'
---

# ClearVisibleProjectsForUser

A newer version of this method exists. If you are currently using this method, we recommend that you will look at the instructions of the next method for changes required to update to the next version. You can find the instructions for the next version [here](<https://support.nepton.com/hc/articles/36506225707677>)
## Interface overview
The web service allows you to remove all user-level project visibility from a specified person. This does not affect projects defined through a person group.
The WSDL schema of the web service is publicly available [here](<https://time.nepton.com/WebService.php?WSDL>). The interfaces are described in general [here](<https://support.nepton.com/hc/en-gb/articles/360004861558>).
The occurrences column in the description determines whether a piece of information is mandatory in the call or not. Occurrences 0 means that the information in question does not need to be passed in the call. Occurrences 1 means that the information must appear once in the call. Occurrences 0..n means that the information in question can appear any number of times in the call. Occurrences 1..n means that the information in question must appear in the data at least once, but can appear more often.
## User identifiers
The target user can be identified by a unique Nepton ID, employee number, or a username. One of these must be provided. The service returns an error if no username has been specified or no user matching the identifier was found.
## Data to be sent
LEVEL | FIELD NAME | FORMAT | OCCURRENCES | DESCRIPTION  
---|---|---|---|---  
0 | ParametersForClearVisibleProjectsForUser | XML element |  | Root,  
below SOAP body  
1 | CallerAuthentication | XML element | 1 | Authentication details. See more [here](<https://support.nepton.com/hc/en-gb/articles/360019983978>).  
1 | ClearVisibleProjectsForUserList | XML element | 1 |   
2 | ClearVisibleProjectForUser | XML element | 1..n |   
3 | UserId | integer | 0..1 | Target user's Nepton ID.  
3 | PersonnelNumber | string | 0..1 | Target user's personnel number.  
3 | UserName | string | 0..1 | Target user's username.  
### Call example
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForClearVisibleProjectsForUser>
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->
          <ClearVisibleProjectsForUserList>
            <ClearVisibleProjectForUser>
              <PersonnelNumber>54236</PersonnelNumber>
            </ClearVisibleProjectForUser>
          </ClearVisibleProjectsForUserList>
        </tyo:ParametersForClearVisibleProjectsForUser>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
