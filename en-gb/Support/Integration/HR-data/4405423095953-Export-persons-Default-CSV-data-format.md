---
id: 4405423095953
title: Export persons - Default CSV data format
url: https://support.nepton.com/hc/en-gb/articles/4405423095953-Export-persons-Default-CSV-data-format
locale: en-gb
category: Support
category_id: 360000446658
section: HR data
section_id: 360001070377
section_path:
- Integration
- HR data
labels: []
promoted: false
updated_at: '2024-03-04T08:43:34Z'
edited_at: '2024-03-04T08:42:53Z'
---

# Export persons - Default CSV data format

Person data can be exported from Nepton into an external service. This article describes Default format person export fields. A detailed description about person export can be found [here](<https://support.nepton.com/hc/articles/360002489357>).
## Fields in person export file in CSV format
**Column order** | **Column title** | **Field name** | **Format of contents** | **Can be used to identify person**  
---|---|---|---|---  
1 | Esimiesten henkilönumerolista | Supervisors | Employee numbers of the supervisors separated by pipe (|) character, primary supervisor first |   
2 | Käyttöoikeustaso | Role | Designated role of person (in Finnish)  
| **Role** | **Field value**  
---|---  
Employee | Työntekijä  
Supervisor | Esimies  
Unit Manager | Yksikön johtaja  
Salary Management | Palkkahallinto  
HR Management | Henkilöstöhallinto  
Administrator | Ylläpitäjä  
3 | Member of units | Units | Names of units of the person separated by pipe (|) |   
4 | Kokonimi | Full name | Full name of the person in the format  
Last name, First name |   
5 | Tili aktiivinen | User account enabled |  1: User account is enabled (disabled accounts are not exported in scheduled exports) |   
6 | User Setting Group | Worktime setting group | Code of the setting group of the person |   
7 | Toimi | Job title | Text contents |   
8 | Työskentelyalue | Work area | Text contents |   
9 | Uusi henkilö |  |  0 A customer specific field, always 0 (zero). |   
10 | Language | Service usage language | Selected service usage language of the person in English (Danish, English, Estonian, Norwegian, Finnish, Polish or Swedish) |   
11 | BIC | BIC | BIC code |   
12 | Ensisijainen tehtävä | Primary task | Name of the selected primary task of the person |   
13 | Etunimi | First name | Text contents |   
14 | Henkilönumero | Employee number | Text contents  | X  
15 | Henkilötunnus | Personal identity code | Finnish personal identity code |   
16 | IntegrationIdAastra | Aastra | Text contents |   
17 | IntegrationIdHeeros | Heeros | Text contents |   
18 | IntegrationIdDLSoftware | DL Software | Text contents |   
19 | IntegrationIdeIP_Kulva | Elisa Ring | Text contents |   
20 | IntegrationIdEmce | Emce | Text contents |   
21 | IntegrationIdFivaldi | Fivaldi | Text contents |   
22 | IntegrationIdHogia | Hogia | Text contents |   
23 | IntegrationIdIFS | IFS | Text contents |   
24 | IntegrationIdKieku | Kieku | Text contents |   
25 | IntegrationIdLessor5 | Lessor-5 | Text contents |   
26 | IntegrationIdLiksa | Liksa | Text contents |   
27 | IntegrationIdMepco | Mepco | Text contents |   
28 | IntegrationIdOscar | Oscar | Text contents |   
29 | IntegrationIdPersonecF | Personec F | Text contents |   
30 | IntegrationIdPersonecW | Personec W | Text contents |   
31 | IntegrationIdProCountor | ProCountor | Text contents |   
32 | IntegrationIdScala | Scala | Text contents |   
33 | IntegrationIdSedab | Sedab | Text contents |   
34 | IntegrationIdSonet | Sonet | Text contents |   
35 | IntegrationIdTikon | Tikon | Text contents |   
36 | IntegrationIdVisma | Visma | Text contents |   
37 | Katuosoite | Street address | Text contents |   
38 | Kaupunki | City | Text contents |   
39 | kirjautumistunnus | Username | Text contents | X  
40 | Koeajan päättymispäivä | Trial period end date | Date in format DD.MM.YYYY |   
41 | Kotisivu | Web page | Text contents |   
42 | Lisätietoa | Additional administrative information | Text contents |   
43 | Lähiomaisen puh | Next of kin phone number | Telephone number |   
44 | Lähionmainen | Next of kin | Text contents |   
45 | MicrosoftAxHourlyCost | Microsoft AX hourly cost | Decimal number (comma , as decimal separator) |   
46 | Oletuskalleusluokka | Default cost group | Text contents |   
47 | Oletuslaskentayksikkö | Default project | Code of the default project |   
48 | Postinumero | Postcode | Text contents |   
49 | Puhelinnumero | Phone number | Telephone number |   
50 | Raportin lisätieto | Additional information for reports | Text contents |   
51 | RFID | RFID tag identifier | Text contents |   
52 | Sukunimi | Last name | Text contents |   
53 | Syy työsopimuksen päättymiseen | Reason for ending employment | Text contents |   
54 | Sähköpostiosoite | Email | E-mail address |   
55 | Tilinumero | IBAN | IBAN formatted bank account number |   
56 | Työsopimuksen aloitus pvm | Employment start date | Date in format DD.MM.YYYY |   
57 | Työsopimuksen lopetus pvm | Employment end date | Date in format DD.MM.YYYY |   
58 | Työsopimuksen tuntipalkka | Hourly wage | Decimal number (comma , as decimal separator) |   
59 | Veronummero | Tax number | 12-digit Finnish tax number |   
60 | Voimassa alkaen | Valid from date | (empty field, can be filled for [person import](<https://support.nepton.com/hc/en-gb/articles/360015754117>), if necessary) |   
61, ... | All [persons additional fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) |  | Formatted according to selected field type |   
Last | Worktime permission groups | Worktime roles | Worktime role names separated by pipe (|) character |   
## Data format details
  * Default CSV format contains 61 standard fields.
  * In addition, all the [persons additional fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) are included in the export.
  * If the fields are not in use or not set yet the value in the export file will be empty.
  * The separator character used between fields in CSV file is semicolon (;).
  * Line separator is standard Windows line separator (CR+LF 0x0D 0x0A).
  * The first row of the export file includes the column titles listed in the table above.
  * Username and employee number are both unique fields within the working community and can be used to identify the person.
  * Date fields are using the format DD.MM.YYYY - day, month and year separated by dots (.)
  * Possible [additional fields](<https://support.nepton.com/hc/en-gb/articles/360002430918>) of type Date and time are using the format DD.MM.YYYY HH:MM - day, month and year separated by dots (.), a space, hours and minutes separated by colon (:)
  * Decimal number fields are using comma (,) as decimal separator.
  * Fields combining multiple values are using pipe (|) separating each value.


## Example file
[code] 
    Esimiesten henkilönumerolista;Käyttöoikeustaso;Yksiköt;Kokonimi;Tili aktiivinen;User Setting Group;Toimi;Työskentelyalue;Uusi henkilö;Language;BIC;Ensisijainen tehtävä;Etunimi;Henkilönumero;Henkilötunnus;IntegrationIdAastra;IntegrationIdHeeros;IntegrationIdDLSoftware;IntegrationIdeIP_Kulva;IntegrationIdEmce;IntegrationIdFivaldi;IntegrationIdHogia;IntegrationIdIFS;IntegrationIdKieku;IntegrationIdLessor5;IntegrationIdLiksa;IntegrationIdMepco;IntegrationIdOscar;IntegrationIdPersonecF;IntegrationIdPersonecW;IntegrationIdProCountor;IntegrationIdScala;IntegrationIdSedab;IntegrationIdSonet;IntegrationIdTikon;IntegrationIdVisma;Katuosoite;Kaupunki;kirjautumistunnus;Koeajan päättymispäivä;Kotisivu;Lisätietoa;Lähiomaisen puh;Lähionmainen;MicrosoftAxHourlyCost;Oletuskalleusluokka;Oletuslaskentayksikkö;Postinumero;Puhelinnumero;Raportin lisätieto;RFID;Sukunimi;Syy työsopimuksen päättymiseen;Sähköpostiosoite;Tilinumero;Työsopimuksen aloitus pvm;Työsopimuksen lopetus pvm;Työsopimuksen tuntipalkka;Veronummero;Voimassa alkaen;CustomBIC;CustomBool;CustomDate;CustomDateTime;CustomDouble;CustomDropDown;CustomEMail;CustomInt;CustomMultipleLines;CustomPhone;CustomPinCode;CustomTaxNumber;CustomText;Worktime permission groups;  
    00585205|2|3;Työntekijä;Main|Branch;Meikäläinen, Janita Olga Fatima;1;A1001;Ammatti;Alue;0;Finnish;HIBKUSH1XXX;Primary task;Janita Olga Fatima;585206;111111A112D;Aastra code;Heeros code;DL code;Elisa code;Emce code;Fivaldi code;Hogia code;IFS code;Kieku code;Lessor-5 code;;Mepco code;Oscar code;Personec F code;Personec W code;;Scala code;Sedab code;Sonet code;Tikon code;Visma code;Katu 11 D;KAUPUNKI;Janita Meikäläinen;31.03.2022;https://www.pa.ge/;Additional information for administrative purposes;048512951516;Anja Meikäläinen;11,25;90;B;12345;05505156066;Additional information shown on reports;angn893623n3n8tu;Meikäläinen;Määräaikainen työsuhde päättyy;janita.meikalainen@yritys.fi;GB79ABBY09012603367219;01.12.2021;31.01.2023;58;012345678901;;LOYDGBC1XXX;1;08.01.2023;10.12.2022 12:51;5,5;1;custom.email@compa.ny;5;Text2;+358585157189769;2544;123456789012;Text;Omien tietojen katseluoikeus, alaisten muokkausoikeus;  
    1|;Esimies;Main;Leader, PK;1;;;;0;English;;;PK;3;;;;;;;;;;;;;;;;;;;;;;;;;PK Leader;;;;;;;;;;;;;Leader;;testaddress@testtest.fi;;;;;;;;0;;;;;;;;;;;;;  
    1|;Esimies;Main;Leader, Other;1;;;;0;English;;;Other;2;;;;;;;;;;;;;;;;;;;;;;;;;Other Leader;;;;;;;;;;;;;Leader;;testaddress@testtest.fi;;;;23,62;;;;0;;;;;;;;;;;;;
[/code]
