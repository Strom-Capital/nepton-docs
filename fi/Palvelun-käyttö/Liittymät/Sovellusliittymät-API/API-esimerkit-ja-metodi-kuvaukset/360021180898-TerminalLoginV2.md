---
id: 360021180898
title: TerminalLoginV2
url: https://support.nepton.com/hc/fi/articles/360021180898-TerminalLoginV2
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
edited_at: '2022-09-23T07:46:07Z'
---

# TerminalLoginV2

## Rajapinnan yleiskuvaus
Verkkopalveluita käytetään henkilön nykytilan hakemiseen Neptonista. Verkkopalvelu on suunniteltu käytettäväksi päätelaitesovelluksissa, esimerkiksi näyttämään seuraavat henkilöä koskevat tiedot:
  * Avoimena oleva tapahtumakirjaus
  * Projektit, joita voi tapahtumille kirjata
  * Mitä projekteja käytetään oletuksena uuden tapahtuman aloituksessa
  * Onko projektin kirjaaminen tapahtumalle pakollista vai ei
  * Tapahtumille kirjattavissa olevat työlisät
  * Ylityön oletuskohdenne työtapahtumilla
  * Kirjattavissa olevat tapahtumatyypit
  * Henkilön kertymät ja niiden saldot


Verkkopalvelun autentikoituminen eroaa muista verkkopalveluista sillä tavalla, että onnistuneesti käyttäjätunnuksella ja salasanalla autentikoitunut henkilö voi autentikoitua toisena henkilönä PIN-koodin tai RFID-koodin perusteella. Ensimmäisessä vaiheessa autentikoituneella henkilöllä täytyy olla oikeudet lukea henkilötietoja. Esimerkiksi:
[code] 
    <CallerAuthentication>  
      <CustomerId>1234</CustomerId>  
      <Username>PäätelaiteKäyttäjä</Username>  
      <Password>KuvitteellinenSalasana123</Password>  
      <PinCode>1234</PinCode> <!-- Päätelaitteella syötetty PIN-koodi -->  
    </CallerAuthentication>
[/code]
Jos annetulla PIN-koodilla tai RFID-koodilla ei löydy henkilöä, autentikoituminen epäonnistuu.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([TerminalLogin](<https://support.nepton.com/hc/articles/6887099778333>))
### Rakenteelliset muutokset
**Vanha** | **Uusi** | **Lisätiedot**  
---|---|---
[code] 
    <tyo:ParametersForTerminalLogin>  
      ...  
    </tyo:ParametersForTerminalLogin>
[/code]  
| 
[code] 
    <tyo:ParametersForTerminalLoginV2>  
      ...  
    </tyo:ParametersForTerminalLoginV2>
[/code]
| Kutsun juurielementin nimi muuttunut
[code] 
    <tyo:ReturnValueForTerminalLogin>  
      ...  
    </tyo:ReturnValueForTerminalLogin>
[/code]  
| 
[code] 
    <tyo:ReturnValueForTerminalLoginV2>  
      ...  
    </tyo:ReturnValueForTerminalLoginV2>
[/code]
| Vastauksen juurielementin nimi muuttunut
[code] 
    <OngoingActivity>  
      <BeginDateTime>2020-01-01 12:00:00</BeginDateTime>  
      <EndDateTime>2020-01-01 14:00:00</EndDateTime>  
      <ModifiedDateTime>2020-01-01 16:00:00</ModifiedDateTime>  
    </OngoingActivity>  
    
[/code]  
| 
[code] 
    <OngoingActivity>  
      <BeginDateTime>2020-01-01T12:00:00</BeginDateTime>  
      <EndDateTime>2020-01-01T14:00:00</EndDateTime>  
      <ModifiedDateTime>2020-01-01T16:00:00</ModifiedDateTime>  
    </OngoingActivity>      
[/code]
| Vastauksessa tapahtuman aikaleima-elementit ovat nyt datetime tyyppisiä, mikä vaikuttaa hieman päiväyksen muotoiluun (BeginDateTime, EndDateTime, ModifiedDateTime)  
### Poistuneet elementit
Aiemmassa versiossa vastaus sisälsi seuraavat elementit kahdesti, ensin OngoingActivity-elementin alla ja sitten myös ActivityDetails-elementin alla:
  * PlannedWorkCalculationUnit
  * PlannedWorkColor
  * PlannedWorkUseForWorkDayLengthCalculations
  * PlannedWorkCanBeCancelledUntil
  * PlannedWorkWorkTimeLimitOffsetStartInMins
  * PlannedWorkWorkTimeLimitOffsetEndInMins
  * PlannedWorkActivityGroupPublicInfo


Nämä löytyvät jatkossa ainoastaan ActivityDetails-elementin alta.
Seuraava elementti oli merkitty vanhentuneeksi jo aiemmassa versiossa ja on nyt poistettu vastauksesta:
  * RelatedActivityId


### Uudet ominaisuudet ja elementit
  * Rajapintavastaus sisältää henkilönumeron tapahtuman henkilölle (UserPersonnelNumber-elementti)
  * Rajapintavastaus sisältää henkilönumeron tapahtuman hyväksyjälle (ApproverPersonnelNumber-elementti)
  * Rajapintavastaus sisältää tapahtuman ulkoiset tunnisteet (ExternalIdentifiers-elementti)


## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForTerminalLoginV2 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
### Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForTerminalLoginV2>  
          <CallerAuthentication>  
            <CustomerId>1234</CustomerId>  
            <Username>PäätelaiteKäyttäjä</Username>  
            <Password>KuvitteellinenSalasana123</Password>  
            <RFID>2893789127981239</RFID> <!-- Päätelaitteella luettu RFID-koodi -->          
          </CallerAuthentication>  
        </tyo:ParametersForTerminalLoginV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
| ReturnValueForTerminalLoginV2 | XML element | 1 | Juuri, SOAP body:n alla  
1 | ResponseCode | integer | 1 | Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 0..1 | Koodin kuvaus  
1 | UserId | integer | 0..1 | Autentikoituneen henkilön Nepton-tunniste  
1 | CustomerId | integer | 0..1 | Työajan asiakkuuden Nepton-tunniste  
1 | Username | string | 0..1 | Autentikoituneen henkilön käyttäjätunnus  
1 | FirstName | string | 0..1 | Autentikoituneen henkilön etunimi  
1 | LastName | string | 0..1 | Autentikoituneen henkilön sukunimi  
1 | Locale | string | 0..1 | Autentikoituneen henkilön kieli. Tällä hetkellä mahdolliset arvot ovat: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
1 | AvailableProjects | XML element | 0..1 |  Projektit, joita henkilö voi kirjata tapahtumille. Huom! Vaikka projektin aktiivisuustila sekä alkamis- ja päättymispäivä palautetaan, vain ne projektit, jotka ovat aktiivisia menevällä päivällä, palautetaan.  
2 | Project | XML element | 0..n | Yhden projektin tiedot.  
3 | Id | integer | 0..1 | Projektin yksilöllinen Nepton-tunniste.  
3 | Name | string | 1 | Projektin nimi  
3 | Deleted | boolean | 0..1 | Onko projekti poistettu (`true`) vai ei (`false`)  
3 | Active | boolean | 0..1 | Onko projekti aktiivinen (`true`) vai ei (`false`)  
3 | Code | string | 0..1 | Projektin koodi  
3 | TypeInternalName | string | 0..1 | Projektin sisäinen nimi  
3 | Description | string | 0..1 | Projektin kuvaus  
3 | StartDate | date | 0..1 | Projektin alkamispäivä, muotona `VVVV-KK-PP`. Arvo voi myös olla `nil`, esimerkiksi: 
[code]
    <StartDate xsi:nil="true" />
[/code]  
3 | EndDate | date | 0..1 | Projektin päättymispäivä, muotona `VVVV-KK-PP`. Arvo voi myös olla `nil`, esimerkiksi: 
[code]
    <EndDate xsi:nil="true" />
[/code]  
3 | ParentProjectId | integer | 0..1 | Projektin yläprojektin Nepton-tunniste. Arvo voi myös olla `nil`, esimerkiksi: 
[code]
    <ParentProjectId xsi:nil="true" />
[/code]  
3 | ParentProjectCode | string | 0..1 | Projektin yläprojektin koodi. Arvo voi myös olla `nil`, esimerkiksi: 
[code]
    <ParentProjectCode xsi:nil="true" />
[/code]  
3 | Left | integer | 0..1 | Tietoa ei käytetä  
3 | Right | integer | 0..1 | Tietoa ei käytetä  
3 | ChildProjects | XML element | 0..1 | Projektin alaprojektit. Tietoa ei käytetä  
1 | ProjectsToContinue | XML element | 0..1 | Jatkettavat projektit  
2 | ProjectToContinue | XML element | 0..n |   
3 | Id | integer | 0..1 | Projektin yksilöllinen tunniste Neptonissa  
3 | Duration | integer | 0..1 | Projektin kesto minuutteina. Tietoa ei käytetä.  
3 | Name | string | 0..1 | Projektin nimi  
3 | Code | string | 0..1 | Projektin koodi  
1 | OnGoingActivity | XML element | 0..1 | Avoimena olevan tapahtuman tiedot  
2 | Id | integer | 0..1 | Tapahtuman yksilöllinen tunniste Neptonissa  
2 | UserId | integer | 0..1 | Henkilön yksilöllinen tunniste Neptonissa. Kuuluu henkilölle, jolla tapahtuma on.  
2 | UserFirstName | string | 0..1 | Henkilön etunimi. Kuuluu henkilölle, jolla tapahtuma on.  
2 | UserLastName | string | 0..1 | Henkilön sukunimi. Kuuluu henkilölle, jolla tapahtuma on.  
2 | UserUsername | string | 0..1 | Henkilön käyttäjätunnus. Kuuluu henkilölle, jolla tapahtuma on.  
2 | UserPersonnelNumber | string | 0..1 | Henkilön henkilönumero. Kuuluu henkilölle, jolla tapahtuma on.  
2 | UserSocialSecurityNumber | string | 0..1 | Henkilön henkilötunnus. Kuuluu henkilölle, jolla tapahtuma on.  
2 | ActivityTypeId | integer | 0..1 | Tapahtumatyypin yksilöllinen tunniste Neptonissa.  
2 | ActivityTypeName | string | 0..1 | Tapahtumatyypin nimi.  
2 | ActivityTypeCategoryId | string | 0..1 | Tapahtumatyypin kategorian yksilöllinen tunniste Neptonissa.  
2 | ActivityTypeCategoryName | string | 0..1 | Tapahtumatyypin kategorian nimi.  
2 | ApproverUserId | integer | 0..1 | Tapahtuman hyväksyneen henkilön yksilöllinen tunniste Neptonissa.  
2 | ApproverFirstName | string | 0..1 | Tapahtuman hyväksyneen henkilön etunimi.  
2 | ApproverLastName | string | 0..1 | Tapahtuman hyväksyneen henkilön sukunimi.  
2 | ApproverPersonnelNumber | string | 0..1 | Tapahtuman hyväksyneen henkilön henkilönumero.  
2 | BeginDateTime | dateTime | 0..1 | Tapahtuman alkupäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
2 | EndDateTime | dateTime | 0..1 | Tapahtuman päättymispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
2 | ModifiedDateTime | dateTime | 0..1 | Aika milloin tapahtumaa on viimeksi muutettu. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
2 | ModifiedByUserId | integer | 0..1 | Tapahtumaa viimeksi muuttaneen henkilön tunniste Neptonissa.  
2 | ModifiedFromIp | string | 0..1 | IP-osoite mistä tapahtumaa on viimeksi muutettu.  
2 | Comment | string | 0..1 | Tapahtumalle kirjatut huomiot.  
2 | IsClockedEvent | boolean | 0..1 | Onko tapahtuma kellotettu (`true`) vai ei (`false`).  
2 | IsCreatedWithPinCode | boolean | 0..1 | Onko tapahtuma kellotettu PIN-koodilla (`true`) vai ei (`false`).  
2 | OvertimeBasePartTargetedTo | string | 0..1 | Ylityön perusosan kohdenne tapahtumalla.  
2 | OvertimeIncrementPartTargetedTo | string | 0..1 | Ylityön korotusosan kohdenne tapahtumalla.  
2 | RelatedProjects | XML element | 0..1 | Tapahtumalle kirjatut projektit.  
3 | ActivityToProjectRelation | XML element | 0..n |   
4 | Id | integer | 0..1 | Projektin yksilöllinen tunniste Neptonissa  
4 | Duration | integer | 0..1 | Projektin kesto minuutteina  
4 | Name | string | 0..1 | Projektin nimi  
4 | Code | string | 0..1 | Projektin koodi  
2 | WorkIncrements | XML element | 0..1 | Tapahtumalle kirjatut työlisät.  
3 | WorkIncrement | XML element | 0..n |   
4 | Index | integer | 1 | Työlisän indeksi  
4 | Value | decimal | 1 | Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
2 | ActivityDetails | XML element | 0..1 | Tapahtuman lisätiedot  
3 | AbsenceDetails | XML element | 0..1 | Poissaolotapahtuman lisätiedot  
4 | CompensationTypeId | integer | 0..1 | Poissaolon korvaustyypin tunniste. Mahdolliset arvot: 
  * `1` \- palkallinen
  * `2` \- palkaton
  * `3` \- vähennetty palkka

  
4 | CompensationTypeName | string | 0..1 | Poissaolon korvaustyypin nimi  
4 | EarnsVacationDays | boolean | 0..1 | Ansaitaanko poissaolosta vuosilomapäiviä (`true`) vai ei (`false`)  
4 | AbsenceTypeId | integer | 0..1 | Poissaolotyypin tunniste. Poissaolotyypit näkee Työajasta, Työyhteisön asetuksista: Työtunnis > Poissaolotyypit  
4 | AbsenceTypeName | string | 0..1 | Poissaolotyypin nimi  
3 | PlannedWorkDetails | XML element | 0..1 | Suunnitellun työvuoron lisätiedot  
4 | PlannedWorkCalculationUnit | string | 0..1 | Työvuoron toimipisteen laskentayksikkö. Lue toimipisteen lisäyksestä ja laskentayksiköstä [täällä](<https://support.nepton.com/hc/fi/articles/360002575538>).  
4 | PlannedWorkColor | string | 0..1 | Työvuoron toimipisteen suunnittelutason tunnusväri. Tunnusvärin voi asettaa Vuorosuunnittelussa: Toimipisteet > Valitse suunnittelutaso > Suunnittelutason asetukset > Suunnittelutason väri  
4 | PlannedWorkUseForWorkDayLengthCalculations | boolean | 0..1 | Tuleeko työpäivän pituus työvuorosta (`true`) vai ei (`false`)  
4 | PlannedWorkCanBeCancelledUntil | string | 0..1 | Päivämäärä ja aika, mihin asti varattu vuorotarve on mahdollista perua. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
4 | PlannedWorkWorkTimeLimitOffsetStartInMins | integer | 0..1 |  Työvuorosta tulevan sallityn työn aloitusajan aikasiirtymä minuutteina. Arvo lisätään tapahtuman alkuaikaan, jota käytetään sallitun työn aloitusajan asettamiseen. Nolla-arvo asettaa sallitun työn aloitusajan tapahtuman aloitusajaksi.  
4 | PlannedWorkWorkTimeLimitOffsetEndInMins | integer | 0..1 |  Työvuorosta tulevan sallityn työn lopetusajan aikasiirtymä minuutteina. Arvo lisätään tapahtuman loppuaikaan, jota käytetään sallitun työn lopetusajan asettamiseen. Nolla-arvo asettaa sallitun työn lopetusajan tapahtuman lopetusajaksi.  
4 | AssumedLunchInMinutes | integer | 0..1 | Työvuorosta tulevan oletetun ruokatauon pituus minuutteina  
4 | PlannedWorkActivityGroupPublicInfo | string | 0..1 | Työvuoron ryhmän tietoihin annettu julkinen tieto  
3 | SickLeaveDetails | XML element | 0..1 | Sairausloman lisätiedot  
4 | CompensationTypeId | integer | 0..1 | Sairausloman korvaustyypin tunniste. Mahdolliset arvot: 
  * `1` \- palkallinen
  * `2` \- palkaton
  * `3` \- vähennetty palkka

  
4 | CompensationTypeName | string | 0..1 | Sairausloman korvaustyypin nimi  
4 | EarnsVacationDays | boolean | 0..1 | Ansaitaanko poissaolosta vuosilomapäiviä (`true`) vai ei (`false`)  
4 | SickLeaveTypeId | integer | 0..1 | Sairausloman tyypin tunniste. Mahdolliset arvot: 
  * `1` \- sairas
  * `2` \- lapsi sairas
  * `3` \- työtapaturma
  * `4` \- työmatkatapaturma
  * `5` \- vapaa-ajan tapaturma

  
4 | SickLeaveTypeName | string | 0..1 | Sairausloman tyypin nimi  
4 | MedicalCertificateGiven | boolean | 0..1 | Onko lääkärintodistus luovutettu (`true`) vai ei (`false`)  
4 | SupervisorsPermission | boolean | 0..1 | Onko sairauslomalle esimiehen hyväksyntä lääkärintodistuksen sijaan (`true`) vai ei (`false`)  
4 | ReasonCode | string | 0..1 | Sairausloman syykoodi  
2 | ExternalIdentifiers | XML element | 0..1 | Tapahtuman ulkoiset tunnisteet  
3 | ExternalIdentifier | XML element | 1..n | Tapahtuman ulkoinen tunniste  
4 | Identifier | string | 1 | Ulkoinen tunniste  
4 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Tällä hetkellä ainoa tuettu tyyppi on `External`  
2 | IsDeleted | boolean | 0..1 | Onko tapahtuma poistettu (`true`) vai ei (`false`)  
1 | ProjectMandatory | boolean | 0..1 | Onko projektin antaminen tapahtumille pakollista (`true`) vai ei (`false`)  
1 | WorkIncrementsForUser | XML element | 0..1 | Tapahtumille kirjattavissa olevat työlisät  
2 | WorkIncrement | XML element | 0..n |   
3 | Index | integer | 0..1 | Työlisän indeksi. Tietoa tarvitaan työlisien kirjaukseen, sillä työlisät kirjataa indeksin mukaan.  
3 | Name | string | 0..1 | Työlisän nimi  
3 | UsedUnit | XML element | 0..1 | Työlisän yksikkö. Palauttaa jonkun seuraavista arvoista: 
  * `minutes` \- Työlisän arvo annetaan minuutteina
  * `decimal` \- Työlisän arvo annetaan desimaalilukuna
  * `units` \- Työlisän arvo annetaan kokonaislukuna

  
1 | DiningIncrements | XML element | 0..1 | Viimeisimmän ruokailutapahtuman työlisät. Lue lisää ruokalapäätteistä ja niillä käytettävistä työlisistä täällä  
2 | ActivityId | integer | 1 | Ruokailutapahtuman Nepton-tunniste  
2 | WorkIncrement | XML element | 0..n |   
3 | Index | integer | 1 | Työlisän indeksi.  
3 | Value | decimal | 1 | Työlisän arvo  
1 | DefaultOvertimeBasePartTargetedTo | string | 0..1 | Ylityön perusosan oletuskohdenne  
1 | DefaultOvertimeIncrementPartTargetedTo | string | 0..1 | Ylityön korotusosan oletuskohdenne  
1 | ActivityTypes | XML element | 0..1 | Lista tapahtumista, joita henkilö voi päätelaitteen kautta kirjata  
2 | ActivityType | XML element | 0..n |   
3 | Id | integer | 1 | Tapahtumatyypin Nepton-tunniste  
3 | InternalName | string | 1 | Tapahtumatyypin sisäinen tunniste Neptonissa  
3 | TranslatedName | XML element | 0..n | Tapahtumatyypin käännetty nimi  
4 | Locale | string | 1 | Kieli. Tällä hetkellä mahdolliset arvot ovat: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
4 | Name | string | 1 | Tapahtumatyypin nimi  
3 | Code | string | 0..1 | Tapahtumatyypin koodi  
3 | Visible | boolean | 0..1 | Onko tapahtumatyyppi näkyvissä vai ei. Tietoa ei käytetä.  
3 | CanAssignWorkIncrements | boolean | 0..1 | Voiko tapahtumatyypille kirjata työlisiä (`true`) vai ei (`false`)  
3 | CanHaveRelatedProjects | boolean | 0..1 | Voiko tapahtumatyypille kirjata projekteja (`true`) vai ei (`false`)  
3 | CategoryInternalName | string | 1 | Tapahtumatyypin kategorian sisäinen tunniste Neptonissa  
3 | TranslatedCategoryName | XML element | 0..n | Tapahtumatyypin kategorian käännetty nimi  
4 | Locale | string | 1 | Kieli. Tällä hetkellä mahdolliset arvot ovat: 
  * fi_FI
  * en_US
  * sv_SE
  * da_DK
  * pl_PL
  * et_EE

  
4 | Name | string | 1 | Tapahtumatyypin kategorian nimi  
3 | BeginDateTimeInput | string | 0..1 | Tapahtumatyypille aloitettavan tapahtuman aloitusajan syöttö. Mahdollisia arvoja ovat: 
  * `disabled` \- Ei sallittu
  * `optional` \- Sallittu
  * `mandatory` \- Aloitusaika on pakko antaa

  
3 | EndDateTimeInput | string | 0..1 | Päätettävän tapahtuman aloitusajan syöttö. Mahdollisia arvoja ovat: 
  * `disabled` \- Ei sallittu
  * `optional` \- Sallittu
  * `mandatory` \- Päättymisaika on pakko antaa

  
1 | AccrualList | XML element | 0..1 | Lista kertymistä ja niiden arvoista  
2 | Accrual | XML element | 0..n |   
3 | InternalName | string | 1 | Kertymän tunnisteena käytettävä nimi  
3 | Name | string | 1 | Kertymän selkokielinen nimi  
3 | Amount | string | 1 | Kertymän arvo tunteina ja minuutteina, esimerkiksi `-02:43`  
3 | ChangeAmount | string | 0..1 | Paljonko kertymän arvo on muuttunut nykyisenä päivänä. Arvo tunteina ja minuutteina, esimerkiksi `+00:30`  
1 | CurrentDateTimeUTC | dateTime | 1 | Tämän hetkinen kellonaika UTC-aikavyöhykkeellä. Muotona on `VVVV-KK-PPTHH:MM:SS`, esimerkiksi `2021-02-18T12:30:00`.  
### Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForTerminalLoginV2>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <UserId>123456</UserId>  
          <CustomerId>1234</CustomerId>  
          <Username>matti.meikäläinen</Username>  
          <FirstName>Matti</FirstName>  
          <LastName>Meikäläinen</LastName>  
          <Locale>fi_FI</Locale>  
          <AvailableProjects>  
            <Project>  
              <Id>9001</Id>  
              <Name>Asiakaspalvelu</Name>  
              <Deleted>false</Deleted>  
              <Active>true</Active>  
              <Code>ASPA01</Code>  
              <TypeInternalName>project_work</TypeInternalName>  
              <Description>Asiakaspalvelutyö</Description>  
              <StartDate xsi:nil="true" />  
              <EndDate xsi:nil="true" />  
              <ParentProjectId xsi:nil="true" />  
              <ParentProjectCode xsi:nil="true" />  
            </Project>  
          </AvailableProjects>  
          <ProjectsToContinue>  
            <ProjectToContinue>  
              <Id>9001</Id>  
              <Name>Asiakaspalvelu</Name>  
              <Code>ASPA01</Code>  
            </ProjectToContinue>  
          </ProjectsToContinue>  
          <OnGoingActivity>  
            <Id>12345678</Id>  
            <UserId>123456</UserId>  
            <UserFirstName>Maija</UserFirstName>  
            <UserLastName>Meikäläinen</UserLastName>  
            <UserUsername>maija.meikäläinen</UserUsername>  
            <UserPersonnelNumber>1111</UserPersonnelNumber>  
            <ActivityTypeId>1</ActivityTypeId>  
            <ActivityTypeName>Työ</ActivityTypeName>  
            <ActivityTypeCategoryId>1</ActivityTypeCategoryId>  
            <ActivityTypeCategoryName>Työ</ActivityTypeCategoryName>  
            <BeginDateTime>2021-01-19T09:12:23</BeginDateTime>  
            <ModifiedDateTime>2021-01-19T09:12:23</ModifiedDateTime>  
            <ModifiedByUserId>123456</ModifiedByUserId>  
            <ModifiedFromIp>127.0.0.1</ModifiedFromIp>  
            <IsClockedEvent>true</IsClockedEvent>  
            <IsCreatedWithPinCode>false</IsCreatedWithPinCode>  
            <OvertimeBasePartTargetedTo>balance</OvertimeBasePartTargetedTo>  
            <OvertimeIncrementPartTargetedTo>uncompensated</OvertimeIncrementPartTargetedTo>  
            <RelatedProjects>  
              <ActivityToProjectRelation>  
                <Id>9001</Id>  
                <Duration>333</Duration>  
                <Name>Asiakaspalvelu</Name>  
                <Code>ASPA01</Code>  
              </ActivityToProjectRelation>  
            </RelatedProjects>  
            <IsDeleted>false</IsDeleted>  
          </OnGoingActivity>  
          <ProjectMandatory>true</ProjectMandatory>  
          <DefaultOvertimeBasePartTargetedTo>balance</DefaultOvertimeBasePartTargetedTo>  
          <DefaultOvertimeIncrementPartTargetedTo>uncompensated</DefaultOvertimeIncrementPartTargetedTo>  
          <ActivityTypes>  
            <ActivityType>  
              <Id>1</Id>  
              <InternalName>Work</InternalName>  
              <TranslatedName>  
                <Locale>fi_FI</Locale>  
                <Name>Työ</Name>  
              </TranslatedName>  
              <TranslatedName>  
                <Locale>en_US</Locale>  
                <Name>Work</Name>  
              </TranslatedName>  
              <CanAssignWorkIncrements>true</CanAssignWorkIncrements>  
              <CanHaveRelatedProjects>true</CanHaveRelatedProjects>  
              <CategoryInternalName>work</CategoryInternalName>  
              <TranslatedCategoryName>  
                <Locale>fi_FI</Locale>  
                <Name>Työ</Name>  
              </TranslatedCategoryName>  
              <TranslatedCategoryName>  
                <Locale>en_US</Locale>  
                <Name>Work</Name>  
              </TranslatedCategoryName>  
              <BeginDateTimeInput>disabled</BeginDateTimeInput>  
              <EndDateTimeInput>disabled</EndDateTimeInput>  
            </ActivityType>  
          </ActivityTypes>  
          <AccrualList>  
            <Accrual>  
              <InternalName>balance</InternalName>  
              <Name>Saldo</Name>  
              <Amount>13:05</Amount>  
            </Accrual>  
          </AccrualList>  
          <CurrentDateTimeUTC>2021-01-20T14:45:11</CurrentDateTimeUTC>  
        </ns1:ReturnValueForTerminalLoginV2>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
