---
id: 6865441448861
title: UpdateActivitiesV2
url: https://support.nepton.com/hc/en-gb/articles/6865441448861-UpdateActivitiesV2
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
edited_at: '2022-09-30T06:00:04Z'
---

# UpdateActivitiesV2

This article has not been translated yet.
Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme, että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/articles/6865760767645>).
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatietojen päivittämiseen Neptonissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Huom! Jos jotain tapahtuman tietoa ei ole pyynnössä, tietoa ei nollata. Tieto jätetään päivittämättä. 
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen pyynnössä vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää pyynnössä. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä pyynnössä yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä pyynnössä minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([UpdateActivities](<https://support.nepton.com/hc/fi/articles/6865125183261>))
### Rakenteelliset muutokset
**Vanha** | **Uusi** | **Lisätiedot**  
---|---|---
[code] 
    <tyo:ParametersForUpdateActivities>  
      ...  
    </ns1:ParametersForUpdateActivities>
[/code]  
| 
[code] 
    <tyo:ParametersForUpdateActivitiesV2>  
      ...  
    </tyo:ParametersForUpdateActivitiesV2>
[/code]
| Pyynnön juurielementin nimi vaihtunut
[code] 
    <tyo:ReturnValueForUpdateActivities>  
      ...  
    </tyo:ReturnValueForUpdateActivities>
[/code]  
| 
[code] 
    <tyo:ReturnValueForUpdateActivitiesV2>  
      ...  
    </tyo:ReturnValueForUpdateActivitiesV2>
[/code]
| Vastauksen juurielementin nimi vaihtunut  
### Uudet omainaisuudet ja elementit
  * Tapahtumalle voi asettaa ulkoisia tunnisteita ja ulkoisen tunnisteen näkee myös vastauksessa 
    * ExternalIdentifiers-elementti lisätty kutsuun
    * ExternalIdentifiers-elementti lisätty vastaukseen
  * Muokattavaan tapahtumaan voi nyt viitata Nepton tunnisteella tai ulkoisella tunnisteella
    * ExistingExternalIdentifier-elementti lisätty kutsuun


## Käyttäjäviittaukset
Tapahtuman henkilö ja tapahtuman hyväksynyt henkilö voidaan asettaa kutsussa. Henkilöön voi viitata jollain seuraavista tunnisteista: Käyttäjän yksilöllinen Nepton ID, käyttäjänimi, käyttäjän henkilötunnus, tai käyttäjän henkilönumero. Kaikki näihin liittyvät kentät voi jättää pois mikäli näihin ei ole tarkoitus tehdä muutoksia. Jos halutaan poistaa tapahtuman hyväksyntä ja hyväksynyt henkilö, niin tunnistekenttään täytyy antaa tyhjä arvo (nil). Katso lähetettävät tiedot -taulukosta tarkemmat tiedot elementeissä, joissa tiedot tulisi antaa.
## Lähetettävät tiedot
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
|  ParametersForUpdateActivitiesV2 |  XML element |  1 |  Juuri,  
SOAP body:n alla  
1 |  CallerAuthentication |  XML element |  1 |  Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 |  ActivityList |  XML element |  1 |  Lista päivitettävistä tapahtumista  
2 |  Activity |  XML element |  1..n |  Päivitettävä tapahtuma  
3 |  ActivityId |  integer |  0..1 |  Päivitettävä tapahtuma. Viittaus yksilöllisen Nepton tunnisteen perusteella. Joko tämä tai ulkoinen tunniste on pakko ilmoittaa  
3 |  ExistingExternalIdentifier |  XML element |  0..1 |  Päivitettävän tapahtuma. Viittaus ulkoisen tunnisteen perusteella. Joko tämä tai Nepton tunniste on ilmoitettava  
4 |  Identifier |  string |  1 |  Ulkoinen tunniste  
4 |  IdentifierType |  string |  1 |  Ulkoisen tunnisteen tyyppi. Tällä hetkellä ainoa tuettu tyyppi on  `External`  
3 |  UserId |  integer |  0..1 |  Tapahtuman henkilö. Viittaus Nepton tunnisteen perusteella.  
3 |  UserUsername |  string |  0..1 |  Tapahtuman henkilö. Viittaus käyttäjänimen perusteella.  
3 |  UserSocialSecurityNumber |  string |  0..1 |  Tapahtuman henkilö. Viittaus henkilötunnuksen perusteella.  
3 |  UserPersonnelNumber |  string |  0..1 |  Tapahtuman henkilö. Viittaus henkilönumeron perusteella.  
3 |  ActivityTypeId |  integer |  0..1 |  Tapahtumatyyppi yksilöllisen Nepton tunnisteen perusteella. Voidaan jättää pois, jos ei haluta muuttaa tapahtumatyyppiä  
3 |  BeginDateTime |  dateTime |  0..1 |  Tapahtuman alkamispäivä ja -aika. Muotona on  `VVVV-KK-PPTHH:MM:SS` , esimerkiksi  `2021-02-18T12:30:00` .  
3 |  EndDateTime |  dateTime |  0..1 |  Tapahtuman päättymispäivä ja -aika. Muotona on  `VVVV-KK-PPTHH:MM:SS` , esimerkiksi  `2021-02-18T12:30:00` . Jos tietoa ei anneta kutsussa, tapahtuman päättymisaikaa ei päivitetä. Tyhjän (  `nil` ) arvon antaminen poistaa tapahtuman päättymisajan.  
3 |  ApproverUserId |  integer |  0..1 |  Tapahtuman hyväksynyt henkilö. Viittaus Nepton tunnisteen perusteella  
3 |  ApproverUsername |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Viittaus käyttäjänimen perusteella  
3 |  ApproverUserSocialSecurityNumber |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Viittaus henkilötunnuksen perusteella  
3 |  ApproverUserPersonnelNumber |  string |  0..1 |  Tapahtuman hyväksynyt henkilö. Viittaus henkilötunnuksen perusteella  
3 |  Comment |  string |  0..1 |  Tapahtumalle kirjattavat huomiot.  
3 |  IsClockedEvent |  boolean |  0..1 |  Onko päivitettävä tapahtuma kellotettu (  `true` ) vai ei (  `false` ).  
3 |  IsCreatedWithPinCode |  boolean |  0..1 |  Onko päivitettävä tapahtuma kellotettu PIN-koodilla (  `true` ) vai ei (  `false` ).  
3 |  OvertimeBasePartTargetedTo |  string |  0..1 |  Ylityön perusosan kohdenne päivitettävällä tapahtumalla.  
3 |  OvertimeIncrementPartTargetedTo |  string |  0..1 |  Ylityön korotusosan kohdenne päivitettävällä tapahtumalla.  
3 |  RelatedProjects |  XML element |  0..1 |  Tapahtumalle kirjattavat projektit. Tämän elementin sisään laitetaan ActivityToProjectRelation - elementtejä jokaista tapahtuman projektilinkitystä kohden (kts. lisää seuraavasta kohdasta).  
4 |  ActivityToProjectRelation |  XML element |  0..n |  Tapahtumaan lisättävän projektimerkinnän tiedot. Katso lisätietoja ja esimerkki [tästä.](<https://support.nepton.com/hc/fi/articles/360019840217-Tapahtumien-API#ActivityToProjectRelation>)  
5 |  Id |  integer |  0..1 |  Projektin yksilöllinen tunniste Neptonissa. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa. Projekteja on mahdollista hake API:n kautta. Lue lisää tästä --todo--  
5 |  Duration |  integer |  0..1 |  Projektin kesto minuutteina  
5 |  Name |  string |  0..1 |  Projektin nimi. Tietoa ei käytetä.  
5 |  Code |  string |  0..1 |  Projektin koodi. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
3 |  WorkIncrements |  XML element |  0..1 |  Tapahtumalle kirjattavat työlisät.  
4 |  WorkIncrement |  XML element |  0..n |   
5 |  Index |  integer |  1 |  Työlisän indeksi  
5 |  Value |  decimal |  1 |  Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
3 |  SetDeleted |  boolean |  0..1 |  Merkitäänkö tapahtuma poistetuksi? (true/false)  
3 |  ExternalIdentifiers |  XML element |  0..1 |  Tapahtumalle asetettavat ulkoiset tunnisteet  
4 |  ExternalIdentifier |  XML element |  1..n |  Tapahtumalle asetettava ulkoinen tunniste  
5 |  Identifier |  string |  1 |  Ulkoinen tunniste  
5 |  IdentifierType |  string |  1 |  Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on  `External` .  
###  Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForUpdateActivitiesV2>  
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <ActivityList>  
            <Activity>  
              <ExistingExternalIdentifier>  
                <Identifier>27ae3e08-bfa0-11eb-8529-0242ac130003</Identifier>   
                <IdentifierType>External</IdentifierType>  
              </ExistingExternalIdentifier>  
              <EndDateTime>2021-01-19T16:00:00</EndDateTime>  
              <ApproverUserId xsi:nil="true" /><!-- Tapahtuman hyväksyjän ja hyväksynnän poisto -->  
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
        </tyo:ParametersForUpdateActivitiesV2>  
      </soapenv:Body>  
    </soapenv:Envelope>  
      
    
[/code]
##  Vastaus
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
0 |  ReturnValueForUpdateActivitiesV2 |  XML element |  1 |  Juurielementti,  
SOAP body:n alla  
1 |  ResponseCode |  integer |  1 |  Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 |  ResponseString |  string |  1 |  Koodin kuvaus  
1 |  ActivityList |  XML element |  1 |   
1 |  ActivityList |  XML element |  0..1 |  Päivitetyt tapahtumat  
2 |  Activity |  XML element |  0..n |  Päivitetty tapahtuma  
3 |  Id |  integer |  0..1 |  Päivitetyn tapahtuman yksilöllinen Nepton-tunniste.  
3 |  ExternalIdentifiers |  XML element |  0..1 |  Päivitetyn tapahtuman ulkoiset tunnisteet. Virhetilanteissa ensisijaisesti palautetaan kutsussa ollut  `ExternalIdentifiers` ja toisisjaisesti kutsussa ollut  `ExistingExternalIdentifier` .  
4 |  ExternalIdentifier |  XML element |  1..n |  Päivitetyn tapahtuman ulkoinen tunniste  
5 |  Identifier |  string |  1 |  Ulkoinen tunniste  
5 |  IdentifierType |  string |  1 |  Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on  `External` .  
3 |  Success |  boolean |  1 |  Onnistuiko tapahtuman muokkaus (  `true` ) vai ei (  `false` ).  
3 |  ErrorCode |  integer |  0..1 |  Jos tapahtuman päivitys ei onnistunut, syyn virhekoodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
3 |  ErrorMessage |  string |  0..1 |  Jos tapahtuman päivitys ei onnistunut, syyn selite.  
###  Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <tyo:ReturnValueForUpdateActivitiesV2>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <ActivityList>  
            <Activity>  
              <Id>12345678</Id>  
              <ExternalIdentifiers>  
                <ExternalIdentifier>  
                  <Identifier>27ae3e08-bfa0-11eb-8529-0242ac130003</Identifier>  
                  <IdentifierType>External</IdentifierType>  
                </ExternalIdentifier>  
              </ExternalIdentifiers>  
              <Success>true</Success>  
            </Activity>  
          </ActivityList>  
        </tyo:ReturnValueForUpdateActivitiesV2>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
