---
id: 360020751677
title: GetActivitiesV3
url: https://support.nepton.com/hc/fi/articles/360020751677-GetActivitiesV3
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: API esimerkit ja metodi-kuvaukset
section_id: 4410135708433
section_path:
- Liittymät
- Sovellusliittymät (API)
- API esimerkit ja metodi-kuvaukset
labels:
- v3
- getactivities
- getting activities
- gettingactivies
promoted: false
updated_at: '2026-09-01T07:31:20Z'
edited_at: '2026-09-01T07:30:47Z'
---

# GetActivitiesV3

Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/27551218873757>).
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatietojen noutoon Neptonista. Verkkopalvelu palauttaa tapahtumat myös deaktivoiduille (Neptonissa **Poista käyttäjätunnus** -toiminolla poistetuille) henkilöille kun kyselyyn sisällytetään käyttäjäsuodatus (esim. henkilönumero).
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([GetActivitiesV2](<https://support.nepton.com/hc/fi/articles/6580610511133>))
### Rakenteelliset muutokset
Vanha | Uusi | Lisätiedot  
---|---|---
[code] 
    <tyo:ParametersForGetActivitiesV2>
      ...
    </tyo:ParametersForGetActivitiesV2>
[/code]  
| 
[code]
    <tyo:ParametersForGetActivitiesV3>
      ...
    </tyoParametersForGetActivitiesV3>
[/code]
| Juurielementin nimi pyynnössä muuttunut
[code] 
    <tyo:ReturnValueForGetActivitiesV2>
      ...
    </tyo:ReturnValueForGetActivitiesV2>
[/code]  
| 
[code]
    <tyo:ParametersForGetActivitiesV3>
    ...
    </tyo:ParametersForGetActivitiesV3>
[/code]
| Juurielementin nimi vastauksessa muuttunut  
### Uudet ominaisuudet ja elementit
  * Tapahtumatyypin koodi lisätty rajapintavastaukseen
    * ActivityTypeCode-elementti lisätty vastaukseen


## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForGetActivitiesV3 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 | FilterByUserIds | XML element | 0..1 | Suodatus henkilöiden yksilöllisten Nepton-tunnisteiden mukaan.  
2 | UserId | integer | 1..n | Yhden henkilön yksilöllinen Nepton-tunniste.  
1 | FilterByUserNames | XML element | 0..1 | Suodatus henkilöiden käyttäjätunnuksien mukaan.  
2 | UserName | string | 1..n | Yhden henkilön käyttäjätunnus.  
1 | FilterByUserPersonnelNumbers | XML element | 0..1 | Suodatus henkilöiden henkilönumeroiden mukaan.  
2 | PersonnelNumber | string | 1..n | Yhden henkilön henkilönumero.  
1 | FilterByActivityTypeIds | XML element | 0..1 | Suodatus tapahtumatyyppien yksilöllisten Nepton-tunnisteiden mukaan.  
2 | ActivityTypeId | integer | 1..n |  Yhden tapahtumatyypin tunniste. ActvityTypeId:n saa tarkastettua SQL:ssä lisäämällä SELECT-osioon ActivityTypeId AS Aid. Tuo lisää viimeiseksi sarakkeen Aid, jossa ko. Id näkyy  
2 | ActivityTypeCode | string | 0..1 | Tapahtumatyypin koodi  
1 | FilterByExternalIdentifiers | XML element | 0..1 | Suodatus tapahtumien ulkoisten tunnisteiden mukaan.  
2 | ExternalIdentifier | XML element | 1..n | Yhden tapahtuman ulkoinen tunniste.  
3 | Identifier | string | 1 | Ulkoinen tunniste  
3 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Tällä hetkellä ainoa tuettu tyyppi on `External`  
1 | FilterPeriodBeginDateTime | dateTime | 0..1 | Suodatus tapahtumiin, jotka alkavat annetun päivämäärän ja ajan jälkeen. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
1 | FilterPeriodEndDateTime | dateTime | 0..1 | Suodatus tapahtumiin, jotka päättyvät ennen annettua päivämäärää ja aikaa. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
1 | FilterModifiedBeginDateTime | dateTime | 0..1 | Suodatus tapahtumiin, joita on viimeksi muutettu annetun päivämäärän ja ajan jälkeen. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
1 | FilterModifiedEndDateTime | dateTime | 0..1 | Suodatus tapahtumiin, joita on viimeksi muutettu ennen annettua päivämäärää ja aikaa. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
1 | FilterIsApproved | boolean | 0..1 | Suodatus tapahtumiin, jotka ovat hyväksyttyjä (`true`) tai eivät ole hyväksyttyjä (`false`).  
1 | IncludeDeleted | boolean | 0..1 | Sisällytetäänkö poistetut tapahtumat (`true`) vai ei (`false`). Poistettuja tapahtumia ei oletusarvoisesti sisällytetä.  
1 | OrderResultsFirstBy | string | 0..1 |  Tapahtumien ensisijainen lajittelukriteeri. Seuraavat arvot ovat tuettuja:
  * `ActivityId` \- Tapahtuman yksilöllinen tunniste Neptonissa
  * `ActivityBeginDatetime` \- Tapahtuman alkupäivä ja -aika
  * `ActivityEndDatetime` \- Tapahtuman päättymispäivä ja -aika
  * `UserId` \- Henkilön, jolla tapahtuma on, tunniste Neptonissa
  * `ActiviTytypeId` \- Tapahtumatyypin tunniste Neptonissa

  
1 | OrderResultsSecondBy | string | 0..1 | Tapahtumien toinen lajittelukriteeri. Tuetut kriteerit ovat samat kuin ensisijaisessa lajittelukriteerissä.  
1 | OrderResultsThirdBy | string | 0..1 | Tapahtumien kolmas lajittelukriteeri. Tuetut kriteerit ovat samat kuin ensisijaisessa lajittelukriteerissä.  
### Kyselyn esimerkki
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForGetActivitiesV3>
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois --> 
          <FilterByActivityTypeIds>
            <ActivityTypeId>1</ActivityTypeId>
          </FilterByActivityTypeIds>
          <FilterByExternalIdentifiers>
            <ExternalIdentifier>
              <Identifier>c2d816bc-bf67-11eb-8529-0242ac130003</Identifier>
              <IdentifierType>External</IdentifierType>
            </ExternalIdentifier>
            <ExternalIdentifier>
              <Identifier>4a700e90-c754-4d1d-ac9a-bfdc011fc2c1</Identifier>
              <IdentifierType>External</IdentifierType>
            </ExternalIdentifier>
          </FilterByExternalIdentifiers>
          <FilterPeriodBeginDateTime>2021-01-01T00:00:00</FilterPeriodBeginDateTime>
          <FilterPeriodEndDateTime>2021-01-31T23:59:59</FilterPeriodEndDateTime>
          <IncludeDeleted>false</IncludeDeleted>
          <OrderResultsFirstBy>ActivityBeginDatetime</OrderResultsFirstBy>
        </tyo:ParametersForGetActivitiesV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForGetActivitiesV3 | XML element | 1 |   
1 | ResponseCode | integer | 1 | Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 1 | Koodin kuvaus  
1 | ActivityList | XML element | 1 |   
2 | Activity | XML element | 0..n |   
3 | Id | integer | 0..1 | Tapahtuman yksilöllinen tunniste. Tapahtuman tunniste pysyy muuttumattomana vaikka tapahtumaa muokataan.  
3 | UserId | integer | 0..1 | Henkilön yksilöllinen tunniste Neptonissa. Kuuluu henkilölle, jolla tapahtuma on.  
3 | UserFirstName | string | 0..1 | Henkilön etunimi. Kuuluu henkilölle, jolla tapahtuma on.  
3 | UserLastName | string | 0..1 | Henkilön sukunimi. Kuuluu henkilölle, jolla tapahtuma on.  
3 | UserUsername | string | 0..1 | Henkilön käyttäjätunnus. Kuuluu henkilölle, jolla tapahtuma on.  
3 | UserPersonnelNumber | string | 0..1 | Henkilön henkilönumero. Kuuluu henkilölle, jolla tapahtuma on.  
3 | UserSocialSecurityNumber | string | 0..1 | Henkilön henkilötunnus. Kuuluu henkilölle, jolla tapahtuma on.  
3 | ActivityTypeId | integer | 0..1 | Tapahtumatyypin yksilöllinen tunniste Neptonissa.  
3 | ActivityTypeName | string | 0..1 | Tapahtumatyypin nimi.  
3 | ActivityTypeCategoryId | string | 0..1 | Tapahtumatyypin kategorian yksilöllinen tunniste Neptonissa.  
3 | ActivityTypeCategoryName | string | 0..1 | Tapahtumatyypin kategorian nimi.  
3 | ApproverUserId | integer | 0..1 | Tapahtuman hyväksyneen henkilön yksilöllinen tunniste Neptonissa.  
3 | ApproverFirstName | string | 0..1 | Tapahtuman hyväksyneen henkilön etunimi.  
3 | ApproverLastName | string | 0..1 | Tapahtuman hyväksyneen henkilön sukunimi.  
3 | ApproverPersonnelNumber | string | 0..1 | Tapahtuman hyväksyneen henkilön henkilönumero.  
3 | BeginDateTime | dateTime | 0..1 | Tapahtuman alkupäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
3 | EndDateTime | dateTime | 0..1 | Tapahtuman päättymispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
3 | ModifiedDateTime | dateTime | 0..1 | Aika milloin tapahtumaa on viimeksi muutettu. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
3 | ModifiedByUserId | integer | 0..1 | Tapahtumaa viimeksi muuttaneen henkilön tunniste Neptonissa.  
3 | ModifiedFromIp | string | 0..1 | IP-osoite mistä tapahtumaa on viimeksi muutettu. **EI ENÄÄ KÄYTÖSSÄ.**  
3 | Comment | string | 0..1 | Tapahtumalle kirjatut huomiot.  
3 | IsClockedEvent | boolean | 0..1 | Onko tapahtuma kellotettu (`true`) vai ei (`false`).  
3 | IsCreatedWithPinCode | boolean | 0..1 | Onko tapahtuma kellotettu PIN-koodilla (`true`) vai ei (`false`).  
3 | OvertimeBasePartTargetedTo | string | 0..1 | Ylityön perusosan kohdenne tapahtumalla.  
3 | OvertimeIncrementPartTargetedTo | string | 0..1 | Ylityön korotusosan kohdenne tapahtumalla.  
3 | RelatedProjects | XML element | 0..1 | Tapahtumalle kirjatut projektit.  
4 | ActivityToProjectRelation | XML element | 0..n |   
5 | Id | integer | 0..1 | Projektin yksilöllinen tunniste Neptonissa  
5 | Duration | integer | 0..1 | Projektin kesto minuutteina  
5 | Name | string | 0..1 | Projektin nimi  
5 | Code | string | 0..1 | Projektin koodi  
3 | WorkIncrements | XML element | 0..1 | Tapahtumalle kirjatut työlisät.  
4 | WorkIncrement | XML element | 0..n |   
5 | Index | integer | 1 | Työlisän indeksi  
5 | Value | decimal | 1 | Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
3 | ActivityDetails | XML element | 0..1 | Tapahtuman lisätiedot  
4 | AbsenceDetails | XML element | 0..1 | Poissaolotapahtuman lisätiedot  
5 | CompensationTypeId | integer | 0..1 |  Poissaolon korvaustyypin tunniste. Mahdolliset arvot:
  * `1` \- palkallinen
  * `2` \- palkaton
  * `3` \- vähennetty palkka

  
5 | CompensationTypeName | string | 0..1 | Poissaolon korvaustyypin nimi  
5 | EarnsVacationDays | boolean | 0..1 | Ansaitaanko poissaolosta vuosilomapäiviä (`true`) vai ei (`false`)  
5 | AbsenceTypeId | integer | 0..1 | Poissaolotyypin tunniste. Poissaolotyypit näkee Työajasta, Työyhteisön asetuksista: Työtunnis > Poissaolotyypit  
5 | AbsenceTypeName | string | 0..1 | Poissaolotyypin nimi  
4 | PlannedWorkDetails | XML element | 0..1 | Suunnitellun työvuoron lisätiedot  
5 | PlannedWorkCalculationUnit | string | 0..1 | Työvuoron toimipisteen laskentayksikkö. Lue toimipisteen lisäyksestä ja laskentayksiköstä [täällä](<https://support.nepton.com/hc/fi/articles/360002575538>).  
5 | PlannedWorkColor | string | 0..1 | Työvuoron toimipisteen suunnittelutason tunnusväri. Tunnusvärin voi asettaa Vuorosuunnittelussa: Toimipisteet > Valitse suunnittelutaso > Suunnittelutason asetukset > Suunnittelutason väri  
5 | PlannedWorkUseForWorkDayLengthCalculations | boolean | 0..1 | Tuleeko työpäivän pituus työvuorosta (`true`) vai ei (`false`)  
5 | PlannedWorkCanBeCancelledUntil | string | 0..1 | Päivämäärä ja aika, mihin asti varattu vuorotarve on mahdollista perua. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
5 | PlannedWorkWorkTimeLimitOffsetStartInMins | integer | 0..1 |  Työvuorosta tulevan sallitun työn aloitusajan aikasiirtymä minuutteina. Arvo lisätään tapahtuman alkuaikaan, jota käytetään sallitun työn aloitusajan asettamiseen. Nolla-arvo asettaa sallitun työn aloitusajan tapahtuman aloitusajaksi.  
5 | PlannedWorkWorkTimeLimitOffsetEndInMins | integer | 0..1 |  Työvuorosta tulevan sallitun työn lopetusajan aikasiirtymä minuutteina. Arvo lisätään tapahtuman loppuaikaan, jota käytetään sallitun työn lopetusajan asettamiseen. Nolla-arvo asettaa sallitun työn lopetusajan tapahtuman lopetusajaksi.  
5 | AssumedLunchInMinutes | integer | 0..1 | Työvuorosta tulevan oletetun ruokatauon pituus minuutteina  
5 | PlannedWorkActivityGroupPublicInfo | string | 0..1 | Työvuoron ryhmän tietoihin annettu julkinen tieto  
4 | SickLeaveDetails | XML element | 0..1 | Sairausloman lisätiedot  
5 | CompensationTypeId | integer | 0..1 |  Sairausloman korvaustyypin tunniste. Mahdolliset arvot:
  * `1` \- palkallinen
  * `2` \- palkaton
  * `3` \- vähennetty palkka

  
5 | CompensationTypeName | string | 0..1 | Sairausloman korvaustyypin nimi  
5 | EarnsVacationDays | boolean | 0..1 | Ansaitaanko poissaolosta vuosilomapäiviä (`true`) vai ei (`false`)  
5 | SickLeaveTypeId | integer | 0..1 |  Sairausloman tyypin tunniste. Mahdolliset arvot:
  * `1` \- sairas
  * `2` \- lapsi sairas
  * `3` \- työtapaturma
  * `4` \- työmatkatapaturma
  * `5` \- vapaa-ajan tapaturma

  
5 | SickLeaveTypeName | string | 0..1 | Sairausloman tyypin nimi  
5 | MedicalCertificateGiven | boolean | 0..1 | Onko lääkärintodistus luovutettu (`true`) vai ei (`false`)  
5 | SupervisorsPermission | boolean | 0..1 | Onko sairauslomalle esimiehen hyväksyntä lääkärintodistuksen sijaan (`true`) vai ei (`false`)  
5 | ReasonCode | string | 0..1 | Sairausloman syykoodi  
3 | ExternalIdentifiers | XML element | 0..1 | Tapahtuman ulkoiset tunnisteet  
4 | ExternalIdentifier | XML element | 1..n | Tapahtuman ulkoinen tunniste  
5 | Identifier | string | 1 | Ulkoinen tunniste  
5 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi  
3 | IsDeleted | boolean | 0..1 | Onko tapahtuma poistettu (`true`) vai ei (`false`)  
### Vastauksen esimerkki
[code]
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForGetActivitiesV3>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <ActivityList>
            <Activity>
              <Id>12345678</Id>
              <UserId>9001</UserId>
              <UserFirstName>Maija</UserFirstName>
              <UserLastName>Meikäläinen</UserLastName>
              <UserUsername>maija.meikäläinen</UserUsername>
              <UserPersonnelNumber>1111</UserPersonnelNumber>
              <ActivityTypeId>1</ActivityTypeId>
              <ActivityTypeName>Työ</ActivityTypeName>
              <ActivityTypeCategoryId>1</ActivityTypeCategoryId>
              <ActivityTypeCategoryName>Työ</ActivityTypeCategoryName>
              <BeginDateTime>2021-01-19T08:00:00</BeginDateTime>
              <EndDateTime>2021-01-19T16:00:00</EndDateTime>
              <ModifiedDateTime>2021-01-20T09:12:23</ModifiedDateTime>
              <ModifiedByUserId>9001</ModifiedByUserId>
              <ModifiedFromIp>127.0.0.1</ModifiedFromIp> EI ENÄÄ KÄYTÖSSÄ
              <Comment>Työtapahtuma</Comment>
              <IsClockedEvent>false</IsClockedEvent>
              <IsCreatedWithPinCode>false</IsCreatedWithPinCode>
              <OvertimeBasePartTargetedTo>salary</OvertimeBasePartTargetedTo>
              <OvertimeIncrementPartTargetedTo>salary</OvertimeIncrementPartTargetedTo>
              <RelatedProjects>
                <ActivityToProjectRelation>
                  <Id>12345</Id>
                  <Duration>450</Duration>
                  <Name>Asiakaspalvelu</Name>
                  <Code>ASPA</Code>
                </ActivityToProjectRelation>
              </RelatedProjects>
              <IsDeleted>false</IsDeleted>
            </Activity>
          </ActivityList>
        </tyo:ReturnValueForGetActivitiesV3>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
