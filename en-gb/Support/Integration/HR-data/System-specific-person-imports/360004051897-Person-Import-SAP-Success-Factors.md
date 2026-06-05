---
id: 360004051897
title: Person Import - SAP Success Factors
url: https://support.nepton.com/hc/en-gb/articles/360004051897-Person-Import-SAP-Success-Factors
locale: en-gb
category: Support
category_id: 360000446658
section: System specific person imports
section_id: 7976634441629
section_path:
- Integration
- HR data
- System specific person imports
labels: []
promoted: false
updated_at: '2023-09-14T12:16:45Z'
edited_at: '2023-08-31T07:03:31Z'
---

# Person Import - SAP Success Factors

Not to be confused with the similarly named [SAP](<https://support.nepton.com/hc/en-gb/articles/360005404298>) mapping. This import mapping is specifically designed for the SAP Success Factors source system. It extends the general import rules with special business logic and data identifiers.  
This mapping is primarily intended for XML file format and therefore does not have a column order defined. This makes node names mandatory (or column headers if using file types other than XML).
## Fields
Below is a list of the special identifiers and behaviours of fields related to this import mapping. Additional person information fields can be imported using the [general](<https://support.nepton.com/hc/fi/articles/360003762577>) import documentation.
Identifier | Mapped to Nepton Field | Description  
---|---|---  
person_id_external | Henkilönumero | Employee number  
surrogate_id | Käyttäjätunnus | Username  
first_name | Etunimi | First name(s)  
last_name | Sukunimi | Last name  
business_email_address | Sähköposti | Email  
business_phone_number | Puhelin | Phone number  
emp_start_date | Työsuhteen alkupäivä | Work relationship start date  
emp_end_date | Työsuhteen loppupäivä | Work relationship end date  
emp_status | Henkilö poistettu / Tili aktiivinen | Values: A,P,F,U,D -> In use Values: R,S,T,O -> Deleted  
company_code | Yksikkö | Unit  
manager_person_id_external | Ensisijainen esimies | Primary supervisor  
grouping_code segment_code business_area_code department_code business_unit_code team_code group_code sub_team_code | Person group code fields |  Used to define users person group(s) and the person group hierarchy. Any number of listed fields can be used. For more information, please see the **Person group fields (Codes and names)** heading below.  
grouping_name segment_name business_area_name department_name business_unit_name team_name group_name sub_team_name | Person group name fields | Used to define users worktime user groups and the user group hierarchy. Any number of listed fields can be used. For more information, please see the **Person group fields (Codes and names)** heading below.  
## Business Logic
  * **Import data may contain multiple user elements/rows per person  
** However, only one will be imported per import 
    * Element/row to be imported will be selected based on value in "emp_status"-field, having highest priority 
      * The priority is from highest to lowest: A,P,F,U,D,R,S,T,O
      * If more than one row has same priority, the first occurrence will be selected
  * **Extend working contract length  
** check details [here](<https://support.nepton.com/hc/en-gb/articles/13129687045789>)


## Person group fields (Codes and names)
Used for setting a persons' person group and importing the person group hierarchy
**Two ways for importing**
  * **Using two fields and pipe separators**
    * **Codes field** contains pipe (|) character separated list of person group codes. Last rightmost code is the code of persons' person group and codes left from that defined the person group hierarchy
    * **Names field** works the same way as codes field but it contains the names of the person groups. Names field usage is optional and additional information to the codes. In case only codes are defined, new groups will have code as name
  * **Using multiple fields and no separators**
    * The order of the fields matters, not the names of the fields
    * Last rightmost field is the code/name of persons' person group and codes/names left from that defined the person group hierarchy


  * **If user group hierarchy defined in import doesn't exist it will be created**
    * If first leftmost group defined in import doesn't exist, it will be created as a root user group 
      * Groups after first leftmost group in import, will be created under it, unless matching existing groups are found, in which case existing groups with members are moved to new position in the hierarchy
    * If first leftmost group defined in import exists, hierarchy defined in import will be created under it in case it doesn't exist
