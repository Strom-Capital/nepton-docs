---
id: 360005783318
title: EnsureProjectsExistV2
url: https://support.nepton.com/hc/en-gb/articles/360005783318-EnsureProjectsExistV2
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
edited_at: '2026-06-01T11:17:29Z'
---

# EnsureProjectsExistV2

A newer version of this method exists. If you are currently using this method, we recommend that you will look at the instructions of the next method for changes required to update to the next version. You can find the instructions for the next version [here](<https://support.nepton.com/hc/en-gb/articles/13106403486109>)
## Overview of interface
Web service is used in updating the list of projects provided in the request into Nepton. If the project exists in Nepton, its information will be updated. Project to update will be identified by either its Nepton identifier (Id), the identifier defined in ExistingIdentifier-element or with project code (Code).
Web service WSDL-schema is available publicly [here](<https://time.nepton.com/WebService.php?WSDL>). Interfaces are described generally [here](<https://support.nepton.com/hc/articles/360004861558>).
Occurrences - column in request description defines whether a field is mandatory in a request or not. 0 occurrences means that field is not mandatory in the request. 1 occurrence means that the field must be present in the request once. 0..n occurrences means that the request may contain any number of those fields or none at all. Occurrences 1..n means that the request may contain any number of those fields but there must be at least one instance of that field.
## Changes to earlier version ([EnsureProjectsExist](<https://support.nepton.com/hc/articles/6880677487005-EnsureProjectsExist>))
### Structural changes
**Old** | **New** | **Information**  
---|---|---
[code] 
    <tyo:ParametersForEnsureProjectsExist>
      ...
    </tyo:ParametersForEnsureProjectsExist>
[/code]  
| 
[code]
    <tyo:ParametersForEnsureProjectsExistV2>
      ...
    </tyo:ParametersForEnsureProjectsExistV2>
[/code]
| Root element name in request has changed
[code] 
    <tyo:ReturnValueForEnsureProjectsExist>
      ...
    </tyo:ReturnValueForEnsureProjectsExist>
[/code]  
| 
[code]
    <tyo:ReturnValueForEnsureProjectsExistV2>
    ...
    </tyo:ReturnValueForEnsureProjectsExistV2>
[/code]
| Root element name in response has changed  
### New properties and elements
  * Existing project can be referred to with an external identifier in addition to project's Nepton identifier or code
    * ExistingProjectIdentifier-element added to request
  * External identifier can be created for the project to insert/update
    * ExternalIdentifier-element added to request


## Request data
Level | Field name | Type | Occurrences | Description  
---|---|---|---|---  
Root, under SOAP body | ParametersForEnsureProjectsExistV2 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | More information about authentication [here](<https://support.nepton.com/hc/articles/360004861558>)  
1 | ProjectList | XML element | 1 | List of projects  
2 | Project | XML element | 1..n | Information for a project. Information about common element content can be seen [here](<https://support.nepton.com/hc/articles/360004861558>).  
3 | ExistingProjectIdentifier | XML element | 0..1 | Identifier for fetching existing project identifier. If project is found, its information will be updated, otherwise a new project will be created. The identifier given in this element is not saved into project information.  
4 | Identifier | string | 1 | Value of project identifier.  
4 | IdentifierType | string | 1 |  Project identifier type. Can be either
  * `ProjectCode` \- project code
  * `ExternalIdentifier` \- project external identifier

Read more about project code and external identifier [here](<https://support.nepton.com/hc/articles/360006768998>).  
3 | Id | unsignedInt | 0..1 | Nepton unique identifier for project. Define only if you want Nepton to identify the existing project based in this information.  
3 | ExternalIdentifier | XML element | 0..n | Identifier from an external system which is saved as the project's external identifier.  
4 | Identifier | string | 1 | Value of project identifier.  
4 | IdentifierType | string | 1 |  Project identifier type. At the moment only supported value is 
  * `ExternalIdentifier` \- project external identifier

Read more about external identifier [here](<https://support.nepton.com/hc/articles/360006768998>).  
3 | Name | string | 1 | Project name  
3 | Deleted | boolean | 0..1 | Is project deleted or not. Deleted projects are saved in the database, but restoring them is not possible via this API.  
3 | Active | boolean | 0..1 |  If set to `true`, project end date will be removed. If set to `false`, project end date will be set as the previous day of the request. If `EndDate` field has a value, this field will be ignored.  
3 | Code | string | 0..1 | Project code. If ID or ExistingIdentifier - elements are not defined in the request, identifying existing project will be attempted by the value of this field.  
3 | TypeInternalName | string | 0..1 | Project type internal identifier. Must be set when creating a project. If now separate project types are set, value is `project_work`  
3 | Description | string | 0..1 | Project description  
3 | StartDate | date | 0..1 |  Project begin date. Project can't be targeted in events or have its hours reported before this date. Value can also be `null`, for example:  

[code] 
    <StartDate xsi:nil="true" />
[/code]  
3 | EndDate | date | 0..1 |  Project start date. Project can't be targeted in events or have its hours reported after this date. Value can also be `null`, for example:  

[code] 
    <EndDate xsi:nil="true" />
[/code]  
3 | ParentProjectId | unsignedInt | 0..1 |  Nepton unique identifier for the parent project of the project. Value can also be `null`, for example:  

[code] 
    <ParentProjectId xsi:nil="true" />
[/code]  
3 | ParentProjectCode | string | 0..1 |  Project code for the parent project of the project. Value can also be `null`, for example:  

[code] 
    <ParentProjectCode xsi:nil="true" />
[/code]  
3 | ParentProjectIdentifier | XML element | 0..1 |  Identifier for the parent project of the project. Value can also be `null`, for example:  

[code] 
    <ParentProjectIdentifier xsi:nil="true" />
[/code]  
4 | Identifier | string | 1 | Identifier for the parent project  
4 | IdentifierType | string | 1 | Parent project identifier type. Can be either  
`ProjectCode` or `ExternalIdentifier`  
3 | Left | unsignedInt | 0..1 | Not used  
3 | Right | unsignedInt | 0..1 | Not used  
3 | ChildProjects | XML element | 0..n | Not used  
### Example request
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForEnsureProjectsExistV2>
          <CallerAuthentication /> <!-- Authentication is required but is omitted from this example -->
          <ProjectList>
            <Project>
              <ExistingProjectIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ExistingProjectIdentifier>
              <ExternalIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ExternalIdentifier>
              <Name>Projekti X</Name>
              <Code>1000/9001</Code>
              <TypeInternalName>project_work</TypeInternalName>
              <Description>Lorem ipsum primis venenatis justo mollis fringilla lectus sociosqu nostra, vehicula nunc massa sodales habitasse duis</Description>
              <StartDate>2001-01-01</StartDate>
              <EndDate xsi:nil="true" />
              <ParentProjectIdentifier>
                <Identifier>45453ddd-f167-408b-9e75-6c419755caf8</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ParentProjectIdentifier>
            </Project>
          </ProjectList>
        </tyo:ParametersForEnsureProjectsExistV2>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Response
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Root, under SOAP body | ReturnValueForEnsureProjectsExistV2 | XML element | 1 |   
1 | ResponseCode | integer | 1 | Response code of handling the request. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).  
1 | ResponseString | string | 1 | Response description  
1 | EnsureProjectsExistResultList | XML element | 1 |   
2 | EnsureProjectsExistResult | XML element | 0..n | Result of handling a project  
3 | ResponseCode | integer | 1 | Response code of handling the project. List of response codes can be found [here](<https://support.nepton.com/hc/en-gb/articles/360019841477>).  
3 | ResponseString | integer | 1 | Response description  
3 | ProjectId | unsignedInt | 1 |  Nepton unique identifier for handled project. Can also be `null`, for example:  

[code] 
    <ProjectId xsi:nil="true" />
[/code]
In error situations `null` is returned if request did not provide a unique Nepton identifier for the project.  
3 | ProjectIdentifier | XML element | 1 | Identifier that was sent in the`ExistingProjectIdentifier` field.  
4 | Identifier | string | 1 | Value of the project identifier  
4 | IdentifierType | string | 1 |  Project identifier type. Can be either
  * `ProjectCode` \- project code
  * `ExternalIdentifier` \- project external identifier

Read more about project code and external identifier [here](<https://support.nepton.com/hc/articles/360006768998>).  
### Example response
[code]
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForEnsureProjectsExistV2>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <EnsureProjectsExistResultList>
            <EnsureProjectsExistResult>
              <ResponseCode>1000</ResponseCode>
              <ResponseString>All clear. No errors.</ResponseString>
              <ProjectId>76254</ProjectId>
              <ProjectIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ProjectIdentifier>
            </EnsureProjectsExistResult>
          </EnsureProjectsExistResultList>
        </tyo:ReturnValueForEnsureProjectsExistV2>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
