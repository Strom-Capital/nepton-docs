---
id: 5080867698717
title: Reset keyword in person import
url: https://support.nepton.com/hc/en-gb/articles/5080867698717-Reset-keyword-in-person-import
locale: en-gb
category: Support
category_id: 360000446658
section: HR data
section_id: 360001070377
section_path:
- Integration
- HR data
labels:
- Reset
- Nolla keyword
- Nolla
- Reset keyword
- tyhjä kenttä
- tyhjä arvo
promoted: false
updated_at: '2023-02-13T06:50:16Z'
edited_at: '2023-02-13T06:49:40Z'
---

# Reset keyword in person import

Emptying the person information field can be ensured using the **RESET or NOLLA** keyword in the fields where it is [supported](<https://support.nepton.com/hc/en-gb/articles/360015933397>). Person import has two options to handle empty values in person import: 1)**Safe** (if a field value is empty then do not change existing values) 2)**Strict** (if a field value is empty then delete existing value of the field). All person import types and empty values mode and the RESET keyword behavior is described below.
## Person import types and empty value modes
**Person import types** | **Empty value mode**  
---|---  
Manual import ([/wrm/admin/personimport.aspx](<https://go.nepton.com/wrm/admin/personimport.aspx>)) |  Either of the following option can be selected from the drop down **Empty values in import file.**
  * Do not change existing field values (**Safe**)
  * Delete existing field values (**Strict**)

  
Person import (SFTP) - Scheduled task | Empty value mode is always set to "Delete existing field values (**Strict**)"  
Person import (REST API) - Scheduled task | Empty value mode is always set to "Delete existing field values (**Strict**)"  
Person import - Soap web service method **ImportUsersFromCSV** [/api/soapwebservice.asmx?wsdl](<https://go.nepton.com/api/soapwebservice.asmx?wsdl>) |  This method has a parameter named **ignoreEmptyValues** which set empty value mode for the person import. ignoreEmptyValues = **True** means "do not change existing field values (**Safe**)" ignoreEmptyValues = **False** means "delete existing field values (**Strict**)"  
Person import - Soap web service method **ImportUsersFromXML** [/api/soapwebservice.asmx?wsdl](<https://go.nepton.com/api/soapwebservice.asmx?wsdl>) |  This method has a parameter named **ignoreEmptyValues** which set empty value mode for the person import. ignoreEmptyValues = **True** means "do not change existing field values (**Safe**)" ignoreEmptyValues = **False** means "delete existing field values (**Strict**)"  
## Empty value mode details
**Empty value mode** | **Description**  
---|---  
Do not change existing field values (**Safe**) **Note** : "Do not change existing field values (Safe)" is also known as ignore empty values in our system | 
  * If a field value is empty string "", it is ignored and not imported
  * If a field value is set to RESET then it is imported and its value is emptied
  * If a multi value field contains RESET then all its values are removed e.g units (a person can have multiple units)
  * If the Password field for a person contains RESET then a random password is generated when inserting a new person

  
Delete existing field values (**Strict**) | 
  * If a field value is empty string "", it is imported and its value is emptied
  * If a field value is set to RESET then its value is imported and set to empty string
  * If a multi value field contains RESET then all its values are removed e.g units (a person can have multiple units)
  * If the Password field for a person contains RESET then a random password is generated when inserting a new person
