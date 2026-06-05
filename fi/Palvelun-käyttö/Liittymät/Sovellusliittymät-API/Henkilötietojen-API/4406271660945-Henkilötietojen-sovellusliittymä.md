---
id: 4406271660945
title: Henkilötietojen sovellusliittymä
url: https://support.nepton.com/hc/fi/articles/4406271660945-Henkil%C3%B6tietojen-sovellusliittym%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen API
section_id: 4406143245713
section_path:
- Liittymät
- Sovellusliittymät (API)
- Henkilötietojen API
labels: []
promoted: false
updated_at: '2026-05-28T07:28:03Z'
edited_at: '2026-05-26T07:48:04Z'
---

# Henkilötietojen sovellusliittymä

Tämä artikkeli kuvaa [henkilötietojen sovellusliittymien](<https://support.nepton.com/hc/sections/4406143245713>) toiminnot henkilötietojen käsittelemiseksi.  
## Tuo henkilöitä CSV-muotoisena
Funktion nimi: "**ImportUsersFromCSVV2** " - Tämä toiminto mahdollistaa yhden tai useamman henkilön tietojen tuonnin sovellusliittymän kautta CSV-muotoisena. Henkilöt, joita ei vielä ole Neptonissa, lisätään ja jo olemassaolevat päivitetään päivitetään annetuilla tiedoilla.
Jos käytät edelleen funktion vanhaa "**ImportUsersFromCSV** "-versiota, suosittelemme uuden version käyttöön siirtymistä.
Katso [henkilötuonnin](<https://support.nepton.com/hc/articles/360003762577>) ohjeista tarkemmat tiedot.
### Pyynnön kentät
Username | Nepton-palveluun tallennetun henkilön käyttäjätunnus. Henkilötuonnin oikeudet lisätä ja muokata tietoja ovat samat kuin tämän henkilön.  
  
Suosittelemme perustamaan testausta ja automaattista käyttöä varten erilliset henkilötiedot, joita ei käytetä muihin tarkoituksiin. Ks. [ohjetta henkilön lisäämiseksi](<https://support.nepton.com/hc/articles/360002427618>).  
---|---  
UserPassword | Username-kentässä mainitun henkilön salasana.  
DeploymentId | Numeerinen tunnus, jolla työyhteisösi on tunnistettavissa. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
WebServicePassword | Salasana, joka liittyy työyhteisön tietoihin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
IgnoreEmptyValues |  Mahdolliset arvot kentälle ovat "1" tai "0" **1** : tyhjä arvo tuontitiedostossa ei vaikuta olemassaolevaan tietoon Nepton-palvelussa **0** : tyhjä arvo tuontitiedostossa poistaa olemassaolevan arvon Nepton-palvelussa Lisätietoja [täällä](<https://support.nepton.com/hc/articles/360018767498#EmptyValues>).  
ImportType |  Kertoo henkilötuonnin tyypin. Yleisesti ottaen Nepton suosittelee käyttämään **Oletus** -tuontityyppiä. Ks. [Henkilötuonnin tyypistä](<https://support.nepton.com/hc/articles/360018767498#ImportType>) lisätietoja. Mahdolliset arvot ovat: 0: Oletus. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
1: Kieku (uudet tilit). Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
2: Mepco. Tällä muodolla on ennalta määritetty sarakejärjestys.  
3: Kieku (työaikasäännöt). Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
4: SAP. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
5: Sympa. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
6: SAP SuccessFactors. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
8: Jatka työsopimusten päiväyksiä. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
9: Sympa HR Integraatio API. Tällä muodolla ei ole ennalta määritettyä sarakejärjestystä.  
IdentifierFieldName |  Henkilötietokentän nimi, jonka perusteella etsitään löytyykö tuotava henkilö jo olemassa olevista henkilöistä. Jos henkilö samalla henkilötietokentän arvolla löytyy, päivitetään tämän henkilön tietoja tuotavalla tiedolla. Kentän sallitut arvot ovat: "Nepton-tunniste", "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero". Jos tätä kenttää ei kutsussa määritetä, käytetään henkilön tunnistamiseen ensimmäistä näistä henkilötiedoista, jolle löytyy arvo tuotavista henkilötiedoista: Nepton-tunniste, Ulkoinen tunniste 1, Käyttäjätunnus, Henkilönumero. Jos määrität kentän arvon, voit päivittää tuotavan aineiston avulla näitä tunnisteita, "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero", lukuunottamatta tunnistetta jonka olet valinnut henkilön tunnisteeksi. **HUOM** : Tätä kenttää ei ole pakko määrittää, mutta tämän käyttö on suositeltua. **HUOM** : Vanha "ImportUsersFromXML"-versio funktiosta ei tuo tätä kenttää.  
ImportColumnNames | Putkimerkillä "|" eroteltu lista sarakkeita, jotka tuodaan. Tätä parametria ei tarvita, jos importdata elementti sisältää otsikon tai jos importTypellä on ennalta määritetty sarakejärjestys  
ImportEncoding | Sen merkistökoodauksen nimi, jota käytetään tuontitiedostossa, esim. utf-8. Lisätietoja [täällä](<https://support.nepton.com/hc/articles/360018767498#Encoding>).  
ImportData | Tuotavat tiedot merkkijonomuodossa. Varmista, että tiedot on HTML-koodattu.  
### Vastauskentät
ResultCode | Tarkista virhekoodi [täältä](<https://support.nepton.com/hc/articles/4406446686609#ResultCodes>)  
---|---  
ResultMessage | Kenttä sisältää vastausviestin. Vastausviesti "Import Successful" tarkoittaa, että tuonti onnistui eikä siinä ilmennyt ongelmia. Jos tuonti ei onnistunut, tässä kentässä ilmoitetaan syy epäonnistumiselle.  
ResultBreakdown | Tämä on listaus tuonnin tuloksista.  
### CSV-muoto
Tietosisältö on CSV-tiedosto UTF-8- tai ISO-8859-1-merkistökoodauksella. Kentät on eroteltu puolipistemerkein (';'). Rivinvaihtoerottimena toimii joko Windows-tyylinen \r\n tai UNIX-tyylinen \n.
Tiedot yhdelle henkilölle tuodaan yhdellä rivillä. Kenttien järjestys on sama kuin rajapintakutsun ImportColumnNames-kentässä tai taulukon ensimmäisellä rivillä luetelluissa otsikoissa. Pyynnön perusteella lisätään uudet henkilötiedot automaattisesti ja olemassaolevat henkilötiedot päivitetään. Kaikki Nepton-palvelun yleiset ja asiakaskohtaiset kentät voidaan tuoda tietosisällössä.
Käytettävissä olevat kentät riippuvat määritellystä henkilötuonnin tyypistä. Käytettävissä olevat henkilötuonnin tyypit löytyvät [täältä](<https://support.nepton.com/hc/articles/360018767498#ImportType>).
## Tuo henkilöitä XML-muotoisena
Funktion nimi: "**ImportUsersFromXMLV2** " - Tämä toiminto mahdollistaa yhden tai useamman henkilön tietojen tuonnin sovellusliittymän kautta XML-muotoisena. Henkilöt, joita ei vielä ole Neptonissa, lisätään ja jo olemassaolevat päivitetään päivitetään annetuilla tiedoilla.
Jos käytät edelleen funktion vanhaa "**ImportUsersFromXML** "-versiota, suosittelemme uuden version käyttöön siirtymistä.
Katso [henkilötuonnin](<https://support.nepton.com/hc/articles/360003762577>) ohjeista tarkemmat tiedot.
### Pyynnön kentät
Username | Nepton-palveluun tallennetun henkilön käyttäjätunnus. Henkilötuonnin oikeudet lisätä ja muokata tietoja ovat samat kuin tämän henkilön.  
  
Suosittelemme perustamaan testausta ja automaattista käyttöä varten erilliset henkilötiedot, joita ei käytetä muihin tarkoituksiin. Ks. [ohjetta henkilön lisäämiseksi](<https://support.nepton.com/hc/articles/360002427618>).  
---|---  
UserPassword | Username-kentässä mainitun henkilön salasana.  
DeploymentId | Numeerinen tunnus, jolla työyhteisösi on tunnistettavissa. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
WebServicePassword | Salasana, joka liittyy työyhteisön tietoihin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
IgnoreEmptyValues |  Mahdolliset arvot kentälle ovat "1" tai "0" **1** : tyhjä arvo tuontitiedostossa ei vaikuta olemassaolevaan tietoon Nepton-palvelussa **0** : tyhjä arvo tuontitiedostossa poistaa olemassaolevan arvon Nepton-palvelussa Lisätietoja [täällä](<https://support.nepton.com/hc/articles/360018767498#EmptyValues>).  
ImportType |  Kertoo henkilötuonnin tyypin. Yleisesti ottaen Nepton suosittelee käyttämään **Oletus** -tuontityyppiä. Ks. [Henkilötuonnin tyypistä](<https://support.nepton.com/hc/articles/360018767498#ImportType>) lisätietoja. Mahdolliset arvot ovat: 0: Oletus  
1: Kieku (uudet tilit)  
2: Mepco  
3: Kieku (työaikasäännöt)  
4: SAP  
5: Sympa  
6: SAP SuccessFactors  
8: Jatka työsopimusten päiväyksiä  
9: Sympa HR Integraatio API  
IdentifierFieldName |  Henkilötietokentän nimi, jonka perusteella etsitään löytyykö tuotava henkilö jo olemassa olevista henkilöistä. Jos henkilö samalla henkilötietokentän arvolla löytyy, päivitetään tämän henkilön tietoja tuotavalla tiedolla. Kentän sallitut arvot ovat: "Nepton-tunniste", "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero". Jos tätä kenttää ei kutsussa määritetä, käytetään henkilön tunnistamiseen ensimmäistä näistä henkilötiedoista, jolle löytyy arvo tuotavista henkilötiedoista: Nepton-tunniste, Ulkoinen tunniste 1, Käyttäjätunnus, Henkilönumero. Jos määrität kentän arvon, voit päivittää tuotavan aineiston avulla näitä tunnisteita, "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero", lukuunottamatta tunnistetta jonka olet valinnut henkilön tunnisteeksi. **HUOM** : Tätä kenttää ei ole pakko määrittää, mutta tämän käyttö on suositeltua. **HUOM** : Vanha "ImportUsersFromXML"-versio funktiosta ei tuo tätä kenttää.  
ImportNodeNames |  Putkimerkillä "|" eroteltu lista sarakkeita, jotka tuodaan. Allaolevassa esimerkissä ImportNodeNames = "First_name|Last_name|Username|Email" Huomaa, että <MuuKentta> ei ole mukana ImportNodeNames-listassa, joten sitä ei tuoda.
[code] 
    <Persons>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>1</Last_name>
            <Username>Käyttäjä 1</Username>
            <Email>testikayttaja1@testi.fi</Email>
            <MuuKentta>Tätä kenttää ei pidä tuoda henkilötuonnissa</MuuKentta>
        </ImportUserData>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>2</Last_name>
            <Username>Käyttäjä 2</Username>
            <Email>testikayttaja2@testi.fi</Email>
            <MuuKentta>Tätä kenttää ei pidä tuoda henkilötuonnissa</MuuKentta>
        </ImportUserData>
    </Persons>
[/code]  
SeparatorNodeName |  XML-solmun nimi, joka erottaa jokaisen henkilön tiedot tuontitiedostossa.  
**Huom!** Isojen ja pienten kirjainten erot ovat merkitysellisiä. Allaolevassa esimerkissä SeparatorNodeName = "**ImportUserData"**
[code] 
    <Persons>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>1</Last_name>
            <Username>Käyttäjä 1</Username>
            <Email>testikayttaja1@testi.fi</Email>
        </ImportUserData>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>2</Last_name>
            <Username>Käyttäjä 2</Username>
            <Email>testikayttaja2@testi.fi</Email>
        </ImportUserData>
    </Persons>
[/code]  
ImportEncoding | Sen merkistökoodauksen nimi, jota käytetään tuontitiedostossa, esim. utf-8. Lisätietoja [täällä](<https://support.nepton.com/hc/articles/360018767498#Encoding>).  
ImportData |  Tuotava XML-data HTML-koodatussa merkkijonomuodossa. Lisätietoja sisällön muodosta löytyy [täältä](<https://support.nepton.com/hc/articles/360003762577>). Luettelo käytettävissä olevista kentistä löytyy [täältä](<https://support.nepton.com/hc/articles/360015933397>). Tuotavat tiedot XML-muodossa ImportData-elementin sisällä voivat olla esimerkiksi seuraavanlaiset:
[code] 
    <Persons>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>1</Last_name>
            <Username>Käyttäjä 1</Username>
            <Email>testikayttaja1@testi.fi</Email>
        </ImportUserData>
        <ImportUserData>
            <First_name>Käyttäjä</First_name>
            <Last_name>2</Last_name>
            <Username>Käyttäjä 2</Username>
            <Email>testikayttaja2@testi.fi</Email>
        </ImportUserData>
    </Persons>
[/code]
Koska kenttä lähetetään HTML-koodattuna, ImportData-elementin tekstimuotoinen sisältö tuotavassa tiedostossa olisi
[code] 
    &lt;Persons&gt;
        &lt;ImportUserData&gt;
            &lt;First_name&gt;Käyttäjä&lt;/First_name&gt;
            &lt;Last_name&gt;1&lt;/Last_name&gt;
            &lt;Username&gt;Käyttäjä 1&lt;/Username&gt;
            &lt;Email&gt;testikayttaja1@testi.fi&lt;/Email&gt;
        &lt;/ImportUserData&gt;
        &lt;ImportUserData&gt;
            &lt;First_name&gt;Käyttäjä&lt;/First_name&gt;
            &lt;Last_name&gt;2&lt;/Last_name&gt;
            &lt;Username&gt;Käyttäjä 2&lt;/Username&gt;
            &lt;Email&gt;testikayttaja2@testi.fi&lt;/Email&gt;
        &lt;/ImportUserData&gt;
    &lt;/Persons&gt;
[/code]  
### Vastauskentät
ResultCode | Tarkista virhekoodi [täältä](<https://support.nepton.com/hc/articles/4406446686609#ResultCodes>)  
---|---  
ResultMessage | Kenttä sisältää vastausviestin. Vastausviesti "Import Successful" tarkoittaa, että tuonti onnistui eikä siinä ilmennyt ongelmia. Jos tuonti ei onnistunut, tässä kentässä ilmoitetaan syy epäonnistumiselle.  
ResultBreakdown | Tämä on listaus tuonnin tuloksista.  
### Esimerkki
Tässä on esimerkki ImportUsersFromXML-SOAP-viestistä:
  * Metodi: POST
  * Yhteysosoite: https://go.nepton.com/API/SOAPWebService.asmx
  * Otsikot:
    * Content-Type: text/xml; charset=utf-8
  * Sisältö:
[code] <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <ImportUsersFromXML xmlns="http://tempuri.org/">
              <Username>Integration Account</Username>
              <UserPassword>e8bc7c00-17c8-4802-8962-c77e1071116c</UserPassword>
              <UserPassword>string</UserPassword>
              <DeploymentId>285057</DeploymentId>
              <WebServicePassword>060b20fe-cd2a-4629-bdc5-7b896a1cebc6</WebServicePassword>
              <IgnoreEmptyValues>false</IgnoreEmptyValues>
              <ImportType>0</ImportType>
              <IdentifierFieldName>Ulkoinen tunniste 1</IdentifierFieldName> 
              <ImportNodeNames>First_name|Last_name|Username|Email</ImportNodeNames>
              <SeparatorNodeName>ImportUserData</SeparatorNodeName>
              <ImportEncoding>utf-8</ImportEncoding>
              <ImportData>&lt;Persons&gt;
            &lt;ImportUserData&gt;
                &lt;First_name&gt;Käyttäjä&lt;/First_name&gt;
                &lt;Last_name&gt;1&lt;/Last_name&gt;
                &lt;Username&gt;Käyttäjä 1&lt;/Username&gt;
                &lt;Email&gt;testkayttaja1@testi.fi&lt;/Email&gt;
            &lt;/ImportUserData&gt;
            &lt;ImportUserData&gt;
                &lt;First_name&gt;Käyttäjä&lt;/First_name&gt;
                &lt;Last_name&gt;2&lt;/Last_name&gt;
                &lt;Username&gt;Käyttäjä 2&lt;/Username&gt;
                &lt;Email&gt;testikayttaja2@testi.fi&lt;/Email&gt;
            &lt;/ImportUserData&gt;
        &lt;/Persons&gt;</ImportData>
            </ImportUsersFromXML>
          </soap:Body>
        </soap:Envelope>
        
[/code]


## Hae henkilön työsopimukset
Funktion nimi "**GetUserWorkingContractsByUserNameAndDates** " - Tämä toiminto palauttaa henkilön aktiivisten työsopimusten perustiedot annetulla aikavälillä. Huomaa, että jos annetulla aikavälillä ei ole aktiivisia työsopimuksia, vastausviesti on tyhjä.
### Pyynnön kentät
UserName | Sen henkilön käyttäjätunnus, jonka työsopimukset haetaan  
---|---  
BeginDate | Työsopimusten hakuaikavälin ensimmäinen päivä  
EndDate | Työsopimusten hakuaikavälin viimeinen päivä  
WebServicePassword | Salasana, joka liittyy työyhteisön tietoihin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
DeploymentID | Numeerinen tunnus, jolla työyhteisösi on tunnistettavissa. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
### Vastauskentät
ID | Työsopimuksen tunnus  
---|---  
UserFullName | Henkilön koko nimi  
UserStreetAddress | Henkilön katuosoite  
UserPostalCode | Henkilön postinumero  
UserCity | Henkilön postitoimipaikka  
UserTelePhoneNumber | Henkilön puhelinnumero  
UserBankAccountNumber | Henkilön pankkitilin numero  
MonthSalary | Henkilön kuukausipalkka (tiedot tähän kenttään palautetaan työsopimusdokumentista)  
HourlyWage | Henkilön tuntipalkka (tiedot tähän kenttään palautetaan työsopimusdokumentista)  
WeekHours | Henkilön viikoittainen minimi- ja maksimityöaika tunteina  
WorkArea | Henkilön työalue (tiedot tähän kenttään palautetaan työsopimusdokumentista)  
ContractStartDate | Henkilön työsopimuksen alkamispäivä  
ContractEndDate | Henkilön työsopimuksen päättymispäivä  
WorkTask | Henkilön työtehtävä (tiedot tähän kenttään palautetaan työsopimusdokumentista)  
Customer | (Tätä kenttää ei käytetä)  
SocialSecurityNumber | Henkilön henkilötunnus  
UserEmail | Henkilön sähköpostiosoite  
## Lisää dokumentti
Funktion nimi "**InsertDocument** " - Tämä toiminto lisää dokumentin henkilölle ja palauttaa tuloksena tallennetun dokumentin tunnuksen. Toiminto on ensisijaisesti tarkoitettu järjestelmäkäyttöä varten. Asiakkaat voivat pyytää asiakaspalvelusta henkilön tunnisteen henkilölle, jonka he ovat määritelleet Neptoniin. Tämä vaaditaan ModifiedBy-kenttää varten.
### Pyynnön kentät
Name | Dokumentin nimi  
---|---  
Filename | Dokumentin tiedostonimi  
ModifiedBy | Sen henkilön tunniste, joka tekee muutoksia henkilön dokumenttiin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
Description | Dokumentin kuvaus  
DocumentTypeID |  Dokumentin tyyppitunniste. Mahdolliset arvot ovat 1, 2, 5, 6, 7, 8 tai 9 1 Työsopimus  
2 Työsopimusliite  
5 Työtodistus  
6 Palkkakuitti  
7 Provisioliite  
8 Käyttäjädokumentti  
9 Tapahtumaliite  
DocumentStatusID | Dokumentin tilatunniste. Jos olet lisäämässä työsopimusdokumenttia, aseta tähän "1", muutoin "4".  
DocumentFileTypeID |  Dokumentin tiedostotunniste. Mahdolliset arvot ovat 1, 3, 4, 5, 6, 7, 8, 9, 10 tai 11 1 Täytettävä lomake (HTML)  
3 PDF-tiedosto  
4 Valmis HTML-tiedosto  
5 Word-asiakirja (.doc)  
6 Excel-tiedosto (.xls)  
7 Muu  
8 PowerPoint (.pptx)  
9 Zip-tiedosto (.zip,.rar)  
10 Kuvatiedosto (.gif,.jpeg, .jpg, .png)  
11 Tekstitiedosto (.txt)  
DocumentData | Dokumentin sisältö (Base64Binary-muodossa)  
EmployeeNumber | Sen henkilön henkilönumero, jolle dokumentti lisätään  
DeploymentID | Numeerinen tunnus, jolla työyhteisösi on tunnistettavissa. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
WebServicePassword | Salasana, joka liittyy työyhteisön tietoihin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.  
OverrideDocumentBySameFilename |  Mahdolliset arvot ovat True tai False. **True** : Jos samalla tiedostonimellä (Filename) on jo olemassa dokumentti, poista vanha dokumentti ja lisää uusi. **False** : Jos samalla tiedostonimellä (Filename) on jo olemassa dokumentti, älä korvaa vanhaa tiedostoa.  
### Vastauskentät
ErrorMessage | Jos web-palvelu ei onnistu lisäämään dokumenttia, tässä kentässä palautetaan syy epäonnistumiseen.  
---|---  
IntegerValue | Jos web-palvelu lisäsi tai muokkasi tiedostoa onnistuneesti, tämä kenttä sisältää dokumentin tunnisteen.  
## Vanhentunut - Hae henkilöiden lukumäärä nimellä
Tämä on vanhentunut toiminto, joka tullaan poistamaan. Jos käytätte tätä toimintoa, siirtykää käyttämään muita tapoja.
Tätä osiota ei ole käännetty suomeksi.
Full function name "**GetCountOfUsersByFirstAndLastNames** "
It was originally used to determine whether a person exists within Nepton. It returns a count of persons based on the given first and last names.
### Request fields
FirstName | First name for which we need the total person count  
---|---  
LastName | Last name for which we need the total person count  
WebServicePassword | Password unique to the customer deployment (Provided by Nepton)  
DeploymentID | The unique customer deployment identifier (Provided by Nepton)  
### Response fields
GetCountOfUsersByFirstAndLastNamesResult | A numeric value showing persons' count e.g 0 or 2  
---|---  
## Vanhentunut - Hae henkilön perustiedot
Tämä on vanhentunut toiminto, joka tullaan poistamaan. Jos käytätte tätä toimintoa, siirtykää käyttämään muita tapoja.
Tätä osiota ei ole käännetty suomeksi.
Full function name "**GetUsersBasicInfoByFirstAndLastName** " - This legacy function returns a persons' basic information based on the requested First and last names. Until a new more capable function is created to replace this, it is recommended to use the [person export](<https://support.nepton.com/hc/articles/360002430478>) for exporting person information instead.
### Request fields
WebServiceCaller > CallerUsername | Username of the person calling web service  
---|---  
WebServiceCaller > CallerPassword | Password of the person calling web service  
WebServiceCaller > WRMDeploymentId | The unique customer deployment identifier (Provided by Nepton)  
WebServiceCaller > WebServicePassword | Password unique to the customer deployment (Provided by Nepton)  
TargetFirstNames | List of first names (need to in same amount as last names)  
TargetLastNames | List of last names (need to in same amount as first names)  
### Response fields
ErrorCode |  Error code can return the following values: Empty / Unknown_Errors / No_Error / Invalid_Password / Invalid_DeploymentId / AccessDenied / InvalidParameters / NotSupported / NotFound / DeploymentSettingsNotFound / CollectionContainsErrors / EncodingFailure / NotRecognised / IntegrationNotRecognizedReturnedUserId / AccessDenied_DueTo_RequestIPIsNotInWhiteList  
---|---  
BasicUserInfo > ErrorCode | Same as ErrorCode parameter above  
BasicUserInfo > Username | Person username  
BasicUserInfo > EmployeeNumber | Person employee number  
BasicUserInfo > UserId | Person id  
BasicUserInfo > FirstName | Person first name  
BasicUserInfo > LastName | Person last name
