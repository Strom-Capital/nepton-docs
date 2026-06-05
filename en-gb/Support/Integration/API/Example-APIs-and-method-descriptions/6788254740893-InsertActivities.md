---
id: 6788254740893
title: InsertActivities
url: https://support.nepton.com/hc/en-gb/articles/6788254740893-InsertActivities
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
edited_at: '2022-10-26T05:31:56Z'
---

# InsertActivities

This article has not been translated yet.
Huom! Tästä metodista on uudempi versio. Tämä vanhentunut versio tullaan poistamaan tulevaisuudessa. Mikäli käytät tätä versiota, niin katso seuraavan version ohjeesta rajapinnan muutokset. Seuraavan version löydät [täältä](<https://support.nepton.com/hc/en-gb/articles/6788513921565>)
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatietojen lisäämiseen Neptonissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Käyttäjäviittaukset
Tapahtuman luonnissa on pakollinen tieto henkilöstä sekä ei-pakollinen tieto tapahtuman hyväksyneestä henkilöstä. Kumpaankin henkilötietoon voi viitata käyttäen tunnisteena jotain seuraavista: Neptonin yksilöllinen käyttäjä ID, käyttäjänimi, käyttäjän henkilötunnus, tai käyttäjän henkilönumero. Jos hyväksyvä henkilö määritetään niin tapahtuma merkitään samalla myös hyväksytyksi. Katso lähetettävät tiedot -taulukosta tarkemmat tiedot elementeistä, joissa henkilöiden tunnisteet tulisi ilmoittaa.
## Lähetettävät tiedot
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
0 |  ParametersForInsertActivities |  XML element |  1 |  SOAP body:n alla oleva juurielementti  
1 |  CallerAuthentication |  XML element |  1 |  Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 |  ActivityList |  XML element |  1 |  Lista lisättävistä / päivitettävistä tapahtumista  
2 |  Activity |  XML element |  1..n |  Lisättävä / päivitettävä tapahtuma  
3 |  UserId |  integer |  0..1 |  Henkilö, jolle tapahtuma lisätään. Henkilön määritys käyttäjän Nepton tunnisteella  
3 |  UserUsername |  string |  0..1 |  Henkilö, jolle tapahtuma lisätään. Henkilön määritys käyttäjänimen perusteella  
3 |  UserSocialSecurityNumber |  string |  0..1 |  Henkilö, jolle tapahtuma lisätään. Henkilön määritys henkilötunnuksen perusteella  
3 |  UserPersonnelNumber |  string |  0..1 |  Henkilö, jolle tapahtuma lisätään. Henkilön määritys henkilönumeron perusteella  
3 |  ActivityTypeId |  integer |  0..1 |  Tapahtumatyypin Nepton-tunniste. Jos tietoa ei anneta kutsussa, tapahtuma luodaan Työ-tapahtumana.  
3 |  BeginDateTime |  dateTime |  1..1 |  Tapahtuman alkamispäivä ja -aika. Muotona on  `VVVV-KK-PPTHH:MM:SS` , esimerkiksi  `2021-02-18T12:30:00` . Pakollinen  
3 |  EndDateTime |  dateTime |  0..1 |  Tapahtuman päättymispäivä ja -aika. Muotona on  `VVVV-KK-PPTHH:MM:SS` , esimerkiksi  `2021-02-18T12:30:00` . Jos tietoa ei anneta tai se on tyhjä, tapahtuma luodaan ilman päättymisaikaa.  
3 |  ApproverUserId |  integer |  0..1 |  Tapahtuman hyväksynyt henkilö. Henkilön määritys Nepton-tunnisteen perusteella  
3 |  ApproverUsername |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Henkilön määritys käyttäjänimen perusteella  
3 |  ApproverUserSocialSecurityNumber |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Henkilön määritys henkilötunnuksen perusteella  
3 |  ApproverUserPersonnelNumber |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Henkilön määritys henkilönumeron perusteella  
3 |  Comment |  string |  0..1 |  Tapahtumalle kirjattavat huomiot.  
3 |  IsClockedEvent |  boolean |  0..1 |  Onko lisättävä/päivitettävä tapahtuma kellotettu (  `true` ) vai ei (  `false` ).  
3 |  IsCreatedWithPinCode |  boolean |  0..1 |  Onko lisättävä/päivitettävä tapahtuma kellotettu PIN-koodilla (  `true` ) vai ei (  `false` ).  
3 |  OvertimeBasePartTargetedTo |  string |  0..1 |  Ylityön perusosan kohdenne lisättävällä/päivitettävällä tapahtumalla.  
3 |  OvertimeIncrementPartTargetedTo |  string |  0..1 |  Ylityön korotusosan kohdenne lisättävällä/päivitettävällä tapahtumalla.  
3 |  RelatedProjects |  XML element |  0..1 |  Tapahtumalle kirjattavat projektit. Tämän elementin sisään laitetaan ActivityToProjectRelation - elementtejä jokaista tapahtuman projektilinkitystä kohden (ks. lisää seuraavasta kohdasta).  
4 |  ActivityToProjectRelation |  XML element |  0..n |  Tapahtumaan lisättävän projektimerkinnän tiedot. Katso lisätietoja ja esimerkki [tästä.](<https://support.nepton.com/hc/fi/articles/360019840217-Tapahtumien-API#ActivityToProjectRelation>)  
5 |  Id |  integer |  0..1 |  Projektin yksilöllinen tunniste Neptonissa. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
5 |  Duration |  integer |  0..1 |  Projektin kesto minuutteina  
5 |  Name |  string |  0..1 |  Projektin nimi. Tietoa ei käytetä.  
5 |  Code |  string |  0..1 |  Projektin koodi. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
3 |  WorkIncrements |  XML element |  0..1 |  Tapahtumalle kirjattavat työlisät.  
4 |  WorkIncrement |  XML element |  0..n |   
5 |  Index |  integer |  1 |  Työlisän indeksi  
5 |  Value |  decimal |  1 |  Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
###  Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForInsertActivities>  
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <ActivityList>  
            <Activity>  
              <UserPersonnelNumber>9001</UserPersonnelNumber>  
              <ActivityTypeId>2</ActivityTypeId>  
              <BeginDateTime>2021-01-19T08:00:00</BeginDateTime>  
              <ApproverUserPersonnelNumber>9999</ApproverUserPersonnelNumber>  
              <Comment>Kovaa työtä</Comment>  
              <IsClockedEvent>true</IsClockedEvent>  
              <ExternalIdentifiers>  
                <ExternalIdentifier>  
                  <Identifier>27ae3e08-bfa0-11eb-8529-0242ac130003</Identifier>  
                    <IdentifierType>External</IdentifierType>  
                </ExternalIdentifier>  
              </ExternalIdentifiers>  
              <RelatedProjects>  
                <ActivityToProjectRelation>  
                  <Id>1234567890</Id><!-- Viittaa projektiin jonka Neptonin sisäinen tunniste on 1234567890 -->  
                  <Duration>120</Duration>  
                </ActivityToProjectRelation>  
                <ActivityToProjectRelation>  
                  <Code>ExampleProjectCode</Code><!-- Viittaa projektiin jonka koodi on ExampleProjectCode -->  
                  <Duration>60</Duration>  
                </ActivityToProjectRelation>  
              </RelatedProjects>  
            </Activity>  
          </ActivityList>  
        </tyo:ParametersForInsertActivities>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
  
Vastaus
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
0 |  ReturnValueForInsertActivities |  XML element |  1 |  SOAP body:n alla oleva juurielementti  
1 |  ResponseCode |  integer |  1 |  Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 |  ResponseString |  string |  1 |  Koodin kuvaus  
1 |  ActivityList |  XML element |  1 |   
1 |  ActivityList |  XML element |  0..1 |  Lisätyt / päivitetyt tapahtumat  
2 |  Activity |  XML element |  0..n |  Lisätty / päivitetty tapahtuma  
3 |  Id |  integer |  0..1 |  Lisätyn / päivitetyn tapahtuman yksilöllinen Nepton-tunniste.  
5 |  Identifier |  string |  1 |  Ulkoinen tunniste  
5 |  IdentifierType |  string |  1 |  Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on  `External` .  
3 |  Success |  boolean |  1 |  Onnistuiko tapahtuman lisäys (  `true` ) vai ei (  `false` ).  
3 |  ErrorCode |  integer |  0..1 |  Jos tapahtuman lisäys tai päivitys ei onnistunut, syyn virhekoodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
3 |  ErrorMessage |  string |  0..1 |  Jos tapahtuman lisäys tai päivitys ei onnistunut, syyn selite.  
###  Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns1="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForInsertActivities>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <ActivityList>  
            <Activity>  
              <Id>12345678</Id>  
              <Success>true</Success>  
            </Activity>  
          </ActivityList>  
        </ns1:ReturnValueForInsertActivities>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
