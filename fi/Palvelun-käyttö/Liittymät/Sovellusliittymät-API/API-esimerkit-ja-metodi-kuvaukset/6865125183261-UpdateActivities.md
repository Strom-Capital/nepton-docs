---
id: 6865125183261
title: UpdateActivities
url: https://support.nepton.com/hc/fi/articles/6865125183261-UpdateActivities
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: API esimerkit ja metodi-kuvaukset
section_id: 4410135708433
section_path:
- Liittymät
- Sovellusliittymät (API)
- API esimerkit ja metodi-kuvaukset
labels: []
promoted: false
updated_at: '2026-06-01T14:44:17Z'
edited_at: '2022-09-30T06:09:16Z'
---

# UpdateActivities

# UpdateActivities
Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme, että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/6865441448861>)
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatietojen päivittämiseen Neptonissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Huom! Jos jotain tapahtuman tietoa ei ole kutsussa, tietoa ei nollata. Tieto jätetään päivittämättä. 
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Käyttäjäviittaukset
Tapahtuman henkilö ja tapahtuman hyväksynyt henkilö voidaan asettaa kutsussa. Henkilöön voi viitata jollain seuraavista tunnisteista: Käyttäjän yksilöllinen Nepton ID, käyttäjänimi, käyttäjän henkilötunnus, tai käyttäjän henkilönumero. Kaikki näihin liittyvät kentät voi jättää pois mikäli näihin ei ole tarkoitus tehdä muutoksia. Jos halutaan poistaa taphtuman hyväksyntä ja hyväksynyt henkilö, niin käytettävään tunnistekenttään täytyy antaa tyhjä arvo (nil). Katso lähetettävät tiedot -taulukosta tarkemmat tiedot elementeistä, joissa tiedot tulisi antaa.
## Lähetettävät tiedot
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
0 |  ParametersForUpdateActivities |  XML element |  1 |  Juurielementti,  
SOAP body:n alla  
1 |  CallerAuthentication |  XML element |  1 |  Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 |  ActivityList |  XML element |  1 |  Lista päivitettävistä tapahtumista  
2 |  Activity |  XML element |  1..n |  Päivitettävä tapahtuma  
3 |  ActivityId |  integer |  0..1 |  Päivitettävä tapahtuma. Viittaus yksilöllisen Nepton tunnisteen perusteella.   
3 |  UserId |  integer |  0..1 |  Tapahtuman henkilö. Viittaus käyttäjän Nepton tunnisteen perusteella.  
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
###  Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForUpdateActivities>  
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <ActivityList>  
            <Activity>  
              <ActivityId>2</ActivityId><!-- Päivitettävän tapahtuman Nepton tunniste -->  
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
        </tyo:ParametersForUpdateActivities>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
##  Vastaus
**TASO** |  **KENTÄN NIMI** |  **MUOTO** |  **ESIINTYMISKERRAT** |  **SELITE**  
---|---|---|---|---  
0 |  ReturnValueForUpdateActivities |  XML element |  1 |  Juurielementti,  
SOAP body:n alla  
1 |  ResponseCode |  integer |  1 |  Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 |  ResponseString |  string |  1 |  Koodin kuvaus  
1 |  ActivityList |  XML element |  1 |   
1 |  ActivityList |  XML element |  0..1 |  Päivitetyt tapahtumat  
2 |  Activity |  XML element |  0..n |  Päivitetty tapahtuma  
3 |  Id |  integer |  0..1 |  Päivitetyn tapahtuman yksilöllinen Nepton-tunniste.  
3 |  Success |  boolean |  1 |  Onnistuiko tapahtuman muokkaus (  `true` ) vai ei (  `false` ).  
3 |  ErrorCode |  integer |  0..1 |  Jos tapahtuman päivitys ei onnistunut, syyn virhekoodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
3 |  ErrorMessage |  string |  0..1 |  Jos tapahtuman päivitys ei onnistunut, syyn selite.  
###  Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:ns1="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForUpdateActivities>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <ActivityList>  
            <Activity>  
              <Id>12345678</Id>  
              <Success>true</Success>  
            </Activity>  
          </ActivityList>  
        </ns1:ReturnValueForUpdateActivities>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
