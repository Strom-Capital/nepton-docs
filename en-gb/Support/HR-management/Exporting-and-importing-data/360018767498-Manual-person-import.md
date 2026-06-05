---
id: 360018767498
title: Manual person import
url: https://support.nepton.com/hc/en-gb/articles/360018767498-Manual-person-import
locale: en-gb
category: Support
category_id: 360000446658
section: Exporting and importing data
section_id: 360004488578
section_path:
- HR management
- Exporting and importing data
labels:
- sisäänluku
promoted: false
updated_at: '2026-05-28T06:00:19Z'
edited_at: '2026-05-28T06:00:19Z'
---

# Manual person import

This article is about importing a single file containing information about persons into Nepton service. More information about different methods of importing persons and technical details of the file formats can be found [here](<https://support.nepton.com/hc/en-gb/articles/360003762577>).
Due to technical limitations, there are differences between the data fields supported by the person export and import. Please check the documentation carefully for the latest information.
### Accessing the feature
Person data can be selected to be manually imported to Nepton via Employees section. If you have a single import file containing data of persons in supported format, you can select to import it manually under **Employees** > **Persons** > **Import persons**. Person importing is usable only by persons in Administrator-role.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/12495710430109)
On first screen options to select a file are presented:
![mceclip8.png](https://support.nepton.com/hc/article_attachments/360018303077)
You can drag & drop the file using the file manager of your device (view depends on the operating system of your device):
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360018302557)
Alternatively you can click the Choose file button and open the file from your device (view depends on the operating system of your device):
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360018302737)
When you have selected the file, its name appears in the view:
![mceclip7.png](https://support.nepton.com/hc/article_attachments/360018359518)
If you chose a wrong file, you can remove the selection clicking the Remove icon next to the file name. You can then choose the correct file. Alternatively you can just choose a new file without removing the previous one and the previously selected file will not be imported - only one file can be imported at a time.
After you have selected the file, you need to provide details needed by service to interpret the values correctly:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360019137197)
### Choose file encoding
Option for choosing file encoding is only available when the file being imported is of CSV format. This option defines the character set used for the file being imported. Possible options are:
  * UTF-8
  * ISO-8859-1 


[UTF-8](<https://en.wikipedia.org/wiki/UTF-8>) is a way of encoding Unicode character set, [ISO-8859-1](<https://en.wikipedia.org/wiki/ISO/IEC_8859-1>) is limited to common characters used in European languages. In general, the program or service you are creating the file with should provide the information about the encoding. If you choose a wrong encoding, latin characters with diacritics or characters for non-latin characters will probably appear incorrect.
### Person import type 
Person import type specifies the way the file contents are interpreted in Nepton. In general, Nepton recommends using the **Default** import type. It supports the most widest range of Nepton person information fields. More information about available fields for Default type are available [here](<https://support.nepton.com/hc/en-gb/articles/360015933397>). Other types are for integrating with specific external systems or other special purposes. See linked pages below for each type for more information. All possible options are:
  * [Default](<https://support.nepton.com/hc/en-gb/articles/360015933397>)
  * [Extend working contract dates](<https://support.nepton.com/hc/en-gb/articles/360007538657>)
  * [Kieku (new accounts)](<https://support.nepton.com/hc/en-gb/articles/360005399958>)
  * [Kieku (worktime rules)](<https://support.nepton.com/hc/en-gb/articles/360005401578>)
  * [Mepco](<https://support.nepton.com/hc/en-gb/articles/360005402338>)
  * [SAP](<https://support.nepton.com/hc/en-gb/articles/360005404298>)
  * [SAP SuccessFactors](<https://support.nepton.com/hc/en-gb/articles/360004051897>)
  * [Sympa](<https://support.nepton.com/hc/en-gb/articles/360003733858>)
  * [Sympa HR Integration API](<https://support.nepton.com/hc/en-gb/articles/360014650697>)


After you have selected the person import type, Nepton service will automatically do a preliminary analysis of the import file and present its results below the options. You can still choose the next option for changing the handling of the empty values in import file. 
### Person identifier
The person identifier refers to the personal data used to determine whether the imported person already exists in the system. If a person with the same identifier is found, their information will be updated with the imported data.  
  
When the value “Default” is used, the system selects the first of the following personal data fields that has a value in the imported data: Nepton Id, External identifier 1, Username, Employee number.  
  
Tip: When you select a value other than “Default,” you can update these identifiers—External Identifier 1, Username, and Employee number—using the imported data, except for the identifier you have chosen as the person identifier.
### Empty values in import file
By default in manual person import, the fields that are empty in import file do not change existing field values. Using that option any existing values in Nepton service for persons being imported are preserved for all fields that have empty values in the import file.
Using option "Delete existing field values (Strict)" will force any existing values in Nepton service for persons being imported to be deleted from service if there are empty values in the import file for these fields.
### Preliminary analysis
After you have selected the person import type, Nepton service will automatically do a preliminary analysis of the import file and present its results below the options:
![mceclip5.png](https://support.nepton.com/hc/article_attachments/360018614978)
If there are specific problems in one or several fields in the import file, warnings for these are presented here in yellow colour. For example:
![mceclip4.png](https://support.nepton.com/hc/article_attachments/360018577337)
These warnings indicate that certain fields cannot be imported to Nepton using the file. However, if no information about one or several persons can be imported, error messages for these are presented in red colour. For example:
![mceclip6.png](https://support.nepton.com/hc/article_attachments/360018577897)
### Starting import
When you have reviewed the preliminary analysis and accept its results and there is at least some contents to be imported, you can start importing using the Import persons button:
![mceclip12.png](https://support.nepton.com/hc/article_attachments/360018640398)
If you chose the option that empty values will delete existing field values, you are required to confirm your choice after selecting the Import persons button.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360018614458)
After you select Confirm choice, the file contents will be imported to Nepton. If you select Cancel import, you can still change your selections.
### Results
When the import operation has finished, the results for each imported entry are presented:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360018592857)
If there are problems but at least some information was successfully imported, warnings are presented in yellow:
![mceclip3.png](https://support.nepton.com/hc/article_attachments/360018593937)
If no information for one or more persons could be imported, error messages are presented in red:
![mceclip4.png](https://support.nepton.com/hc/article_attachments/360018631658)
### Examples
#### Mass import supervisor information
There is a separate guidance page [here](<https://support.nepton.com/hc/en-gb/articles/360002430658>) with detailed information on how to import supervisor information using a spreadsheet program.
#### Add only new persons with mandatory information
An example of a CSV file to import initial [mandatory information](<https://support.nepton.com/hc/en-gb/articles/360018575177>) for new persons added to the system:
[code]
    First name;Last name;Service usage language;Role
    Hope;Hopeful;English;Employee
    Dana;Dannerø;Danish;Supervisor
    Matti;Meikäläinen;Finnish;Employee
    Wojciech;Kozłowski;Polish;Employee
    Sven;Svensson;Swedish;Employee
    Ülle;Võsu;Estonian;Employee
    Jakob;Hansen;Norwegian;Employee
[/code]
As neither username nor employee number field is provided, the above will always add the persons as new to Nepton system even if persons with similar information were previously saved in the system.
#### Update worktime setting group codes for a number of persons
An example of an Excel file to update new worktime setting group codes for a group of people listed by their employee numbers:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360018644638)
The above will search for persons with employee numbers 101, 104, 106, 147 and 159 saved in Nepton and, if found, update their Worktime setting group code to be C100. As not all mandatory information is not provided, no new person will be added if person with the employee number given is not found. 
#### Import empty values
An example of importing empty values for fields in CSV format. Persons are identified with the Username given. The field
[code]
    Username;Employee number;Additional administrative information;Role
    Hope Hopeful;101;;Employee
    Dana Dannerø;102;;Supervisor
    Matti Meikäläinen;104;;Employee
    Wojciech Kozłowski;106;;Employee
    Sven Svensson;147;Sven;;Employee
    Ülle Võsu;159;Ülle;Võsu;;Employee
    Øyvind Thorsen;168;;Supervisor
[/code]
If this import file is imported with default option "Do not change existing field values (Safe)", any existing additional administrative information will still be found in Nepton after import. However, if the Additional administrative information field needs to be cleared for these persons, the option "Delete existing field values (Strict)" must be selected in the import options.
