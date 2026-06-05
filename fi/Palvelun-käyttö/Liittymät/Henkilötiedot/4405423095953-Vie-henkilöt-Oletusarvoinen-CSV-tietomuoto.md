---
id: 4405423095953
title: Vie henkilöt - Oletusarvoinen CSV-tietomuoto
url: https://support.nepton.com/hc/fi/articles/4405423095953-Vie-henkil%C3%B6t-Oletusarvoinen-CSV-tietomuoto
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötiedot
section_id: 360001070377
section_path:
- Liittymät
- Henkilötiedot
labels: []
promoted: false
updated_at: '2024-03-04T08:43:34Z'
edited_at: '2024-03-04T08:43:33Z'
---

# Vie henkilöt - Oletusarvoinen CSV-tietomuoto

Henkilötietoja on mahdollista viedä Neptonista ulkoiseen palveluun. Tässä artikkelissa kuvataan Oletus-muotoisen henkilötietojen viennin määritykset. Tarkemman kuvauksen henkilötietojen viennistä löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489357>).  

## Kentät CSV-muotoisessa henkilöviennin tiedostossa
**Sarakejärjestys** | **Sarakkeen otsikko** | **Kentän nimi** | **Sisällön muoto** | **Voidaan käyttää henkilön yksilöintiin**  
---|---|---|---|---  
1 | Esimiesten henkilönumerolista | Esimiehet | Esimiesten henkilönumerot eroteltuina pystyviivalla (|), ensisijainen esimies ensimmäisenä |   
2 | Käyttöoikeustaso | Rooli | Henkilön määritelty rooli:  
| Työntekijä  
---  
Esimies  
Yksikön johtaja  
Palkkahallinto  
Henkilöstöhallinto  
Ylläpitäjä  
3 | Member of units | Yksiköt | Henkilön yksiköiden nimet pystyviivalla (|) eroteltuina |   
4 | Kokonimi | Koko nimi | Henkilön koko nimi muodossa  
sukunimi, etunimi |   
5 | Tili aktiivinen | Käyttäjätili käytössä |  1: Käyttäjätili on käytössä (viennissä ovat mukana vain käytössä olevat tilit) |   
6 | User Setting Group | Työajan asetusryhmä | Henkilön työajan asetusryhmän koodi |   
7 | Toimi | Ammattinimike | Tekstisisältö |   
8 | Työskentelyalue | Työskentelyalue | Tekstisisältö |   
9 | Uusi henkilö |  |  0 (Tämä on asiakasspesifi kenttä, aina 0 (nolla). |   
10 | Language | Palvelun käyttökieli | Henkilön valitsema palvelun käyttökieli englanniksi:  
| **Käyttökieli** | **Arvo**  
---|---  
englanti | English  
puola | Polish  
ruotsi | Swedish  
suomi | Finnish  
tanska | Danish  
viro | Estonian  
norja | Norwegian  
11 | BIC | BIC | BIC-koodi |   
12 | Ensisijainen tehtävä | Ensisijainen tehtävä | Henkilön ensisijaisen tehtävän nimi |   
13 | Etunimi | Etunimi | Tekstisisältö |   
14 | Henkilönumero | Henkilönumero | Tekstisisältö | X  
15 | Henkilötunnus | Henkilötunnus | Suomalainen henkilötunnus |   
16 | IntegrationIdAastra | Aastra | Tekstisisältö |   
17 | IntegrationIdHeeros | Heeros | Tekstisisältö |   
18 | IntegrationIdDLSoftware | DL Software | Tekstisisältö |   
19 | IntegrationIdeIP_Kulva | Elisa Ring | Tekstisisältö |   
20 | IntegrationIdEmce | Emce | Tekstisisältö |   
21 | IntegrationIdFivaldi | Fivaldi | Tekstisisältö |   
22 | IntegrationIdHogia | Hogia | Tekstisisältö |   
23 | IntegrationIdIFS | IFS | Tekstisisältö |   
24 | IntegrationIdKieku | Kieku | Tekstisisältö |   
25 | IntegrationIdLessor5 | Lessor-5 | Tekstisisältö |   
26 | IntegrationIdLiksa | Liksa | Tekstisisältö |   
27 | IntegrationIdMepco | Mepco | Tekstisisältö |   
28 | IntegrationIdOscar | Oscar | Tekstisisältö |   
29 | IntegrationIdPersonecF | Personec F | Tekstisisältö |   
30 | IntegrationIdPersonecW | Personec W | Tekstisisältö |   
31 | IntegrationIdProCountor | ProCountor | Tekstisisältö |   
32 | IntegrationIdScala | Scala | Tekstisisältö |   
33 | IntegrationIdSedab | Sedab | Tekstisisältö |   
34 | IntegrationIdSonet | Sonet | Tekstisisältö |   
35 | IntegrationIdTikon | Tikon | Tekstisisältö |   
36 | IntegrationIdVisma | Visma | Tekstisisältö |   
37 | Katuosoite | Katuosoite | Tekstisisältö |   
38 | Kaupunki | Postitoimipaikka | Tekstisisältö |   
39 | Kirjautumistunnus | Käyttäjätunnus | Tekstisisältö | X  
40 | Koeajan päättymispäivä | Koeajan päättymispäivä | Päiväys muodossa PP.KK.VVVV |   
41 | Kotisivu | Verkkosivu | Tekstisisältö |   
42 | Lisätietoa | Hallinnon lisätieto | Tekstisisältö |   
43 | Lähiomaisen puh | Lähiomaisen puhelinnumero | Puhelinnumero |   
44 | Lähionmainen | Lähiomainen | Tekstisisältö |   
45 | MicrosoftAxHourlyCost | Microsoft AX -tuntihinta | Desimaaliluku (pilkku , desimaalierottimena) |   
46 | Oletuskalleusluokka | Oletuskustannuspaikka | Tekstisisältö |   
47 | Oletuslaskentayksikkö | Oletusprojekti | Oletusprojektin koodi |   
48 | Postinumero | Postinumero | Tekstisisältö |   
49 | Puhelinnumero | Puhelinnumero | Puhelinnumero |   
50 | Raportin lisätieto | Raporteilla näkyvä lisätieto | Tekstisisältö |   
51 | RFID | RFID-tunniste | Tekstisisältö |   
52 | Sukunimi | Sukunimi | Tekstisisältö |   
53 | Syy työsopimuksen päättymiseen | Työsuhteen päättymissyy | Tekstisisältö |   
54 | Sähköpostiosoite | Sähköposti | Sähköpostiosoite |   
55 | Tilinumero | IBAN | IBAN-muotoinen tilinumero |   
56 | Työsopimuksen aloitus pvm | Työsuhteen alkupäivä | Päiväys muodossa PP.KK.VVVV |   
57 | Työsopimuksen lopetus pvm | Työsuhteen päättymispäivä | Päiväys muodossa PP.KK.VVVV |   
58 | Työsopimuksen tuntipalkka | Tuntipalkka | Desimaaliluku (pilkku , desimaalierottimena) |   
59 | Veronumero | Veronumero | 12-numeroinen suomalainen veronumero |   
60 | Voimassa alkaen | Voimassa alkaen | (tyhjä kenttä, voidaan täyttää tarvittaessa [henkilöiden tuontiin](<https://support.nepton.com/hc/fi/articles/360015754117>)) |   
61, 62, ... | Kaikki [henkilön lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) |  | Muotoilu valitun kentän tyypin mukaan |   
61/viimeinen | Worktime permission groups | Työajan roolit | Työajan roolien nimet eroteltuina pystyviivalla (|) |   
## Tietomuodon yksityiskohdat
  * Vienti CSV-tiedostojen oletusmuodossa sisältää 61 vakiokenttää.
  * Lisäksi kaikki [henkilön lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) ovat mukana viennissä.
  * Kentän, joka ei ole käytössä tai jonka arvo on tyhjä, arvo vientitiedostossa on tyhjä.
  * Käytettävä erotinmerkki kenttien välissä CSV-tiedostossa on puolipiste (;).
  * Rivinvaihto on Windowsin vakiorivinvaihto (CR+LF 0x0D 0x0A).
  * Ensimmäinen rivi vientitiedostossa sisältää yllä luetellut sarakkeiden otsikot.
  * Käyttäjätunnus ja henkilönumero ovat molemmat yksilöllisiä työyhteisössä ja niitä voidaan käyttää henkilön yksilöintiin.
  * Päivämääräkentät käyttävät muotoa PP.KK.VVVV (päivä, kuukausi ja vuosi pisteillä (.) eroteltuina)
  * Mahdolliset päivämäärä ja aika -tyyppiset [lisätietokentät](<https://support.nepton.com/hc/fi/articles/360002430918>) käyttävät muotoa PP.KK.VVVV TT:MM (päivä, kuukausi ja vuosi pisteillä (.) eroteltuina, välilyönti, tunnit ja minuutit kaksoispisteellä (:) eroteltuina).
  * Desimaalilukukentät käyttävät pilkkua (,) desimaalierottimena.
  * Kentät, joissa yhdistetään useita arvoja, käyttävät pystyviivaa (|) kunkin arvon erottamiseen toisistaan.


## Esimerkkitiedosto
[code] 
    Esimiesten henkilönumerolista;Käyttöoikeustaso;Yksiköt;Kokonimi;Tili aktiivinen;User Setting Group;Toimi;Työskentelyalue;Uusi henkilö;Language;BIC;Ensisijainen tehtävä;Etunimi;Henkilönumero;Henkilötunnus;IntegrationIdAastra;IntegrationIdHeeros;IntegrationIdDLSoftware;IntegrationIdeIP_Kulva;IntegrationIdEmce;IntegrationIdFivaldi;IntegrationIdHogia;IntegrationIdIFS;IntegrationIdKieku;IntegrationIdLessor5;IntegrationIdLiksa;IntegrationIdMepco;IntegrationIdOscar;IntegrationIdPersonecF;IntegrationIdPersonecW;IntegrationIdProCountor;IntegrationIdScala;IntegrationIdSedab;IntegrationIdSonet;IntegrationIdTikon;IntegrationIdVisma;Katuosoite;Kaupunki;kirjautumistunnus;Koeajan päättymispäivä;Kotisivu;Lisätietoa;Lähiomaisen puh;Lähionmainen;MicrosoftAxHourlyCost;Oletuskalleusluokka;Oletuslaskentayksikkö;Postinumero;Puhelinnumero;Raportin lisätieto;RFID;Sukunimi;Syy työsopimuksen päättymiseen;Sähköpostiosoite;Tilinumero;Työsopimuksen aloitus pvm;Työsopimuksen lopetus pvm;Työsopimuksen tuntipalkka;Veronummero;Voimassa alkaen;CustomBIC;CustomBool;CustomDate;CustomDateTime;CustomDouble;CustomDropDown;CustomEMail;CustomInt;CustomMultipleLines;CustomPhone;CustomPinCode;CustomTaxNumber;CustomText;Worktime permission groups;  
    00585205|2|3;Työntekijä;Main|Branch;Meikäläinen, Janita Olga Fatima;1;A1001;Ammatti;Alue;0;Finnish;HIBKUSH1XXX;Primary task;Janita Olga Fatima;585206;111111A112D;Aastra code;Heeros code;DL code;Elisa code;Emce code;Fivaldi code;Hogia code;IFS code;Kieku code;Lessor-5 code;;Mepco code;Oscar code;Personec F code;Personec W code;;Scala code;Sedab code;Sonet code;Tikon code;Visma code;Katu 11 D;KAUPUNKI;Janita Meikäläinen;31.03.2022;https://www.pa.ge/;Additional information for administrative purposes;048512951516;Anja Meikäläinen;11,25;90;B;12345;05505156066;Additional information shown on reports;angn893623n3n8tu;Meikäläinen;Määräaikainen työsuhde päättyy;janita.meikalainen@yritys.fi;GB79ABBY09012603367219;01.12.2021;31.01.2023;58;012345678901;;LOYDGBC1XXX;1;08.01.2023;10.12.2022 12:51;5,5;1;custom.email@compa.ny;5;Text2;+358585157189769;2544;123456789012;Text;Omien tietojen katseluoikeus, alaisten muokkausoikeus;  
    1|;Esimies;Main;Leader, PK;1;;;;0;English;;;PK;3;;;;;;;;;;;;;;;;;;;;;;;;;PK Leader;;;;;;;;;;;;;Leader;;testaddress@testtest.fi;;;;;;;;0;;;;;;;;;;;;;  
    1|;Esimies;Main;Leader, Other;1;;;;0;English;;;Other;2;;;;;;;;;;;;;;;;;;;;;;;;;Other Leader;;;;;;;;;;;;;Leader;;testaddress@testtest.fi;;;;23,62;;;;0;;;;;;;;;;;;;
[/code]
