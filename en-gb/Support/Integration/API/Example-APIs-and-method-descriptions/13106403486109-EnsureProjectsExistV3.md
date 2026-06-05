---
id: 13106403486109
title: EnsureProjectsExistV3
url: https://support.nepton.com/hc/en-gb/articles/13106403486109-EnsureProjectsExistV3
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
edited_at: '2026-06-01T11:41:14Z'
---

# EnsureProjectsExistV3

A newer version of this method exists. If you are currently using this method, we recommend that you will look at the instructions of the next method for changes required to update to the next version. You can find the instructions for the next version [here](<https://support.nepton.com/hc/en-gb/articles/36507754396573>)
## Overview of interface
Web service is used in updating the list of projects provided in the request into Nepton. If the project exists in Nepton, its information will be updated. Project to update will be identified by either its Nepton identifier (Id), the identifier defined in ExistingIdentifier-element or with project code (Code). Project managers for a project can be updated by providing a ProjectManagers - element under that project containing ProjectManager - elements for each project manager to update. ProjectManager - element identifies the project manager by either personnel number (PersonnelNumber), username (Username) or Nepton internal identifier for the user (UserId). Updating of project managers can be done so that the project managers provided in the request are added to Nepton in addition to project managers set earlier in Nepton (default) or updating will remove project managers set earlier in Nepton, if they are not provided in the request as project managers, by adding RemoveOthers - element with a value of `true` inside that projects ProjectManagers - element.
Web service WSDL-schema is available publicly [here](<https://time.nepton.com/WebService.php?WSDL>). Interfaces are described generally [here](<https://support.nepton.com/hc/articles/360004861558>).
Occurrences - column in request description defines whether a field is mandatory in a request or not. 0 occurrences means that field is not mandatory in the request. 1 occurrence means that the field must be present in the request once. 0..n occurrences means that the request may contain any number of those fields or none at all. Occurrences 1..n means that the request may contain any number of those fields but there must be at least one instance of that field.
## Changes to earlier version ([EnsureProjectsExistV2](<https://support.nepton.com/hc/articles/360005783318>))
### Structural changes
**Old** | **New** | **Information**  
---|---|---
[code] 
    <tyo:ParametersForEnsureProjectsExistV2>
      ...
    </tyo:ParametersForEnsureProjectsExistV2>
[/code]  
| 
[code]
    <tyo:ParametersForEnsureProjectsExistV3>
      ...
    </tyo:ParametersForEnsureProjectsExistV3>
[/code]
|  Root element name in request has changed
[code] 
    <tyo:ReturnValueForEnsureProjectsExistV2>
      ...
    </tyo:ReturnValueForEnsureProjectsExistV2>
[/code]  
| 
[code]
    <tyo:ReturnValueForEnsureProjectsExistV3>
    ...
    </tyo:ReturnValueForEnsureProjectsExistV3>
[/code]
|  Root element name in response has changed  
### New properties and elements
  * Project managers can be added for a project by providing them under that projects Project -element in a ProjectManagers - element
    * ProjectManagers - element added to request under Project
  * ProjectManagers - element can have RemoveOthers - element inside it, which defines whether the earlier project managers not present in the response will be removed as project managers for that project. This happens by setting the value of RemoveOthers - element to `true`.
    * RemoveOthers - element added to request under ProjectManagers.
  * ProjectManagers - element can have ProjectManager - elements inside it, which define the identifiers of the persons to be added as project managers to a project.
    * ProjectManager - element added to request under ProjectManagers.
      * UserId-, Username- and PersonnelNumber - elements added under ProjectManager.
  * ProjectManagers is also added to the response so that it returns the current project managers of that project.
    * ProjectManagers are added to the response only if project managers have been updated i.e. the request contained ProjectManagers - element.


### Removed properties and elements
  * Left and Right - elements that are not in use anymore removed from request


## Request data
LEVEL | FIELD NAME | TYPE | OCCURRENCES | DESCRIPTION  
---|---|---|---|---  
Root, under SOAP body | ParametersForEnsureProjectsExistV3 | XML element | 1 |   
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
4 | Identifier | string | 1 | Value of project identifier. Character limit 64 characters.  
4 | IdentifierType | string | 1 |  Project identifier type. At the moment only supported value is 
  * `ExternalIdentifier` \- project external identifier

Read more about external identifier [here](<https://support.nepton.com/hc/articles/360006768998>).  
3 | Name | string | 1 | Project name. Character limit 255 characters.  
3 | Deleted | boolean | 0..1 | Is project deleted or not. Deleted projects are saved in the database, but restoring them is not possible via this API.  
3 | Active | boolean | 0..1 |  If set to `true`, project end date will be removed. If set to `false`, project end date will be set as the previous day of the request. If `EndDate` field has a value, this field will be ignored.  
3 | Code | string | 0..1 | Project code. If ID or ExistingIdentifier - elements are not defined in the request, identifying existing project will be attempted by the value of this field. Character limit 255 characters.  
3 | TypeInternalName | string | 0..1 |  Project type internal identifier. Must be set when creating a project. If now separate project types are set, value is `project_work` Character limit 190 characters.  
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
3 | ChildProjects | XML element | 0..n | Not used  
3 | ProjectManagers | XML element | 0..1 | Project managers to be updated for the project  
4 | RemoveOthers | boolean | 0..1 | If set as `true`, removes existing project managers from the project if they are not set as project managers in the request  
4 | ProjectManager | XML element | 0..n | Project manager to be updated for the project  
5 | UserId | unsignedInt | 0..1 | Nepton unique user identifier of person  
5 | Username | string | 0..1 | Username of person  
5 | PersonnelNumber | string | 0..1 | Personnelnumber of person  
### Example request
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForEnsureProjectsExistV3>
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
              <ProjectManagers>
                <RemoveOthers>true</RemoveOthers>
                <ProjectManager>
                  <PersonnelNumber>27</PersonnelNumber>
                </ProjectManager>
                <ProjectManager>
                  <UserName>Example Username</PersonnelNumber>
                </ProjectManager>
              </ProjectManagers>
            </Project>
          </ProjectList>
        </tyo:ParametersForEnsureProjectsExistV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Response
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
Root, under SOAP body | ReturnValueForEnsureProjectsExistV3 | XML element | 1 |   
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
3 | ProjectManagers | XML element | 0..1 | Project project managers. Is returned only if ProjectManagers - element was present in the request.  
4 | ProjectManager | XML element | 0..n | Project project manager  
5 | UserId | unsignedInt | 0..1 | Nepton unique user identifier of person  
5 | Username | string | 0..1 | Username of person  
5 | PersonnelNumber | string | 0..1 | Personnelnumber of person  
### Example response
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForEnsureProjectsExistV3>
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
              <ProjectManagers>
                <ProjectManager>
                  <UserId>09876543210</UserId>
                  <UserName>Test User</UserName>
                  <PersonnelNumber>27</PersonnelNumber>
                </ProjectManager>
                <ProjectManager>
                  <UserId>1234567890</UserId>
                  <UserName>Example Username</PersonnelNumber>
                  <PersonnelNumber>1274</PersonnelNumber>
                </ProjectManager>
              </ProjectManagers>
            </EnsureProjectsExistResult>
          </EnsureProjectsExistResultList>
        </tyo:ReturnValueForEnsureProjectsExistV3>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
