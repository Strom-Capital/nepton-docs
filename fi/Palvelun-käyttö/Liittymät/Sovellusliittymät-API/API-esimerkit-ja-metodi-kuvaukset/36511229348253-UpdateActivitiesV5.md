---
id: 36511229348253
title: UpdateActivitiesV5
url: https://support.nepton.com/hc/fi/articles/36511229348253-UpdateActivitiesV5
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
edited_at: '2026-06-01T13:30:21Z'
---

# UpdateActivitiesV5

## Rajapinnan yleiskuvaus  
Verkkopalvelua käytetään tapahtumatietojen päivittämiseen Neptonissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Huom! Jos jotain tapahtuman tietoa ei ole kutsussa, tietoa ei nollata. Tieto jätetään päivittämättä.
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([UpdateActivitiesV3](<https://support.nepton.com/hc/articles/6865760767645>))
### Uudet ominaisuudet ja kentät
  * Tapahtuman omistajan tunnistaminen on mahdollista tehdä ulkoisella tunnisteella
    * UserPersonExternalIdentifier-elementti lisätty kyselyyn
  * Tapahtuman hyväksyjän tunnistaminen on mahdollista tehdä ulkoisella tunnisteella
    * ApproverUserPersonExternalIdentifier-elementti lisätty kyselyyn
  * UserPersonExternalIdentifier ja ApproverUserPersonExternalIdentifier sisältävät Identifier- ja FieldName-kentät


## Käyttäjäviittaukset
Tapahtuman henkilö ja tapahtuman hyväksynyt henkilö voidaan asettaa kutsussa. Henkilöön voi viitata jollain seuraavista tunnisteista: Käyttäjän yksilöllinen Nepton ID, käyttäjänimi, käyttäjän henkilötunnus, tai käyttäjän henkilönumero. Kaikki näihin liittyvät kentät voi jättää pois mikäli näihin ei ole tarkoitus tehdä muutoksia. Jos halutaan poistaa tapahtuman hyväksyntä ja hyväksynyt henkilö niin tunnistekenttää täytyy antaa tyhjä arvo (nil). Katso lähetettävät tiedot -taulukosta tarkemmat tiedot elementeissä, joissa tiedot tulisi antaa.
## Lähetettävät tiedot
**TASO** | **KENTÄN NIMI** | **MUOTO** | **ESIINTYMISKERRAT** | **SELITE**  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForUpdateActivitiesV5 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 | ActivityList | XML element | 1 | Lista päivitettävistä tapahtumista  
2 | Activity | XML element | 1..n | Päivitettävä tapahtuma  
3 | ActivityId | integer | 0..1 | Päivitettävä tapahtuma. Viittaus yksilöllisen Nepton tunnisteen perusteella. Joko tämä tai ulkoinen tunniste on pakko ilmoittaa  
3 | ExistingExternalIdentifier | XML element | 0..1 | Päivitettävän tapahtuma. Viittaus ulkoisen tunnisteen perusteella. Joko tämä tai Nepton tunniste on ilmoitettava  
4 | Identifier | string | 1 | Ulkoinen tunniste  
4 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Tällä hetkellä ainoa tuettu tyyppi on `External`  
3 | UserId | integer | 0..1 | Tapahtuman henkilö. Viittaus Nepton tunnisteen perusteella.  
3 | UserUsername | string | 0..1 | Tapahtuman henkilö. Viittaus käyttäjänimen perusteella.  
3 | UserSocialSecurityNumber | string | 0..1 | Tapahtuman henkilö. Viittaus henkilötunnuksen perusteella.  
3 | UserPersonnelNumber | string | 0..1 | Tapahtuman henkilö. Viittaus henkilönumeron perusteella.  
3 | UserPersonExternalIdentifier | XML element | 0..1 | Henkilö, jolle tapahtuma lisätään. Viittaus ulkoisen tunnisteen perusteella  
3 | Identifier | string | 1 | Henkilön ulkoisen tunnisteen arvo  
3 | FieldName | string | 1 |  Henkilön ulkoisen tunnisteen kenttänimi. Tuetut arvot:
[code] 
    ExternalIdentifier1
[/code]  
3 | ActivityTypeId | integer | 0..1 | Tapahtumatyyppi yksilöllisen Nepton tunnisteen perusteella. Voidaan jättää pois, jos ei haluta muuttaa tapahtumatyyppiä. Järjestelmän tapahtumatyypit mahdollista hakea API:n kautta. Lue lisää [täältä](<https://support.nepton.com/hc/fi/articles/6899092915101>)  
3 | ActivityTypeCode | string | 0..1 | Käytettävä tapahtumatyypi tapahtumatyypin koodin perusteella. Jos useampi tapahtumatyyppi käyttää samaa koodia, käytetään ensimmäistä löytynyttä tapahtumatyyppiä.  
3 | BeginDateTime | dateTime | 0..1 | Tapahtuman alkamispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS` , esimerkiksi `2021-02-18T12:30:00` .  
3 | EndDateTime | dateTime | 0..1 |  Tapahtuman päättymispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS` , esimerkiksi `2021-02-18T12:30:00` . Jos tietoa ei anneta kutsussa, tapahtuman päättymisaikaa ei päivitetä. Tyhjän ( `nil` ) arvon antaminen poistaa tapahtuman päättymisajan.  
3 | ApproverUserId | integer | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus Nepton tunnisteen perusteella  
3 | ApproverUsername | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus käyttäjänimen perusteella  
3 | ApproverUserSocialSecurityNumber | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus henkilötunnuksen perusteella  
3 | ApproverUserPersonnelNumber | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus henkilötunnuksen perusteella  
3 | ApproverUserPersonExternalIdentifier | XML element | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus ulkoisen tunnisteen perusteella  
3 | Identifier | string | 1 | Tapahtuman hyväksyneen henkilön ulkoisen tunnisteen arvo  
3 | FieldName | string | 1 |  Tapahtuman hyväksyneen henkilön ulkoisen tunnisteen kenttänimi. Tuetut arvot:
[code] 
    ExternalIdentifier1
[/code]  
3 | Comment | string | 0..1 | Tapahtumalle kirjattavat huomiot.  
3 | IsClockedEvent | boolean | 0..1 | Onko päivitettävä tapahtuma kellotettu ( `true` ) vai ei ( `false` ).  
3 | IsCreatedWithPinCode | boolean | 0..1 | Onko päivitettävä tapahtuma kellotettu PIN-koodilla ( `true` ) vai ei ( `false` ).  
3 | OvertimeBasePartTargetedTo | string | 0..1 | Ylityön perusosan kohdenne päivitettävällä tapahtumalla.  
3 | OvertimeIncrementPartTargetedTo | string | 0..1 | Ylityön korotusosan kohdenne päivitettävällä tapahtumalla.  
3 | ResetValue | decimal | 0..1 | Kertymän päivitetty arvo minuutteina tai päivinä riippuen kertymän tyypistä.  
3 | ChangeValue | decimal | 0..1 | Kertymän muutoksen arvo minuutteina tai päivinä riippuen kertymän tyypistä.  
3 | RelatedProjects | XML element | 0..1 | Tapahtumalle kirjattavat projektit. Tämän elementin sisään laitetaan ActivityToProjectRelation - elementtejä jokaista tapahtuman projektilinkitystä kohden (kts. lisää seuraavasta kohdasta).  
4 | ActivityToProjectRelation | XML element | 0..n | Tapahtumaan lisättävän projektimerkinnän tiedot. Katso lisätietoja ja esimerkki [tästä.](<https://support.nepton.com/hc/fi/articles/360019840217-Tapahtumien-API#ActivityToProjectRelation>)  
5 | Id | integer | 0..1 | Projektin yksilöllinen tunniste Neptonissa. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
5 | Duration | integer | 0..1 | Projektin kesto minuutteina  
5 | Name | string | 0..1 | Projektin nimi. Tietoa ei käytetä.  
5 | Code | string | 0..1 | Projektin koodi. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
3 | WorkIncrements | XML element | 0..1 | Tapahtumalle kirjattavat työlisät.  
4 | WorkIncrement | XML element | 0..n |   
5 | Index | integer | 1 | Työlisän indeksi  
5 | Value | decimal | 1 | Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
3 | SetDeleted | boolean | 0..1 | Merkitäänkö tapahtuma poistetuksi  
3 | ExternalIdentifiers | XML element | 0..1 | Tapahtumalle asetettavat ulkoiset tunnisteet  
4 | ExternalIdentifier | XML element | 1..n | Tapahtumalle asetettava ulkoinen tunniste  
5 | Identifier | string | 1 | Ulkoinen tunniste  
5 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on `External` .  
3 | ActivityDetails | XML element | 0..1 | Tietue joka sisältää tapahtumatyyppikohtaiset lisätiedot kuten esimerkiksi sairausloman tai poissaolon lisätiedot, jotka on kuvattuna alla.  
4 | AbsenceDetails | XML element | 0..1 |  Jos tapahtumatyyppi on poissaolo-tyyppinen, poissaolon tarkemman tiedot voidaan välittää AbsenceDetails-tietueen alitietueina Jos AbsenceDetails - kenttiä ei ole määritetty, käytetään poissaolotyypin ja tapahtumatyypin oletusarvoja. Jos pyyntö sisältää vain poissaolotyypin, korvaus ja lomapäivien kerryttäminen määritetään automaattisesti samalla tavalla kuin tapahtuman muokkaussivulla palvelun käyttöliittymässä. Käyttöoikeudet toimivat samalla tavalla kuten käyttöliittymän "Lisää/Muokkaa tapahtumaa" - sivun käyttöoikeudet.  
5 | AbsenceTypeId | integer | 0..1 | Käytettävän poissaolotyypin ID. Käyttöliittymästä nämä näkee kohdasta: Asetukset > Työtunnit > Poissaolotyypit  
5 | AbsenceTypeName | string | 0..1 | Vaihtoehtoinen tapa osoittaa käytettävä poissaolotyyppi nimen/käännöksen mukaan, esim. "Ammattiyhdistystoiminta". On suositeltavaa käyttää ensisijaisesti AbsenceTypeId -kenttää, jos mahdollista  
5 | CompensationTypeId | integer | 0..1 | Poissaolon korvauksen tunniste  
1 = palkallinen,  
2 = palkaton,  
3 = vähennetty palkka  
5 | CompensationTypeName | string | 0..1 | Vaihtoehtoinen tapa määrittää korvauksen tunniste, esim. "palkallinen", "paid", "palkaton", "unpaid", "vähennetty palkka", "reduced salary"  
5 | EarnsVacationDays | boolean | 0..1 | Kerryttääkö poissaolo lomapäiviä (true/false)  
4 | SickLeaveDetails | XML element | 0..1 |  Jos tapahtumatyyppi on sairausloma, niin lisätiedot voidaan välittää SickLeaveDetails - tietueen alitietueina Jos sairauslomatyypin tietoja ei välitetä pyynnössä, käytetään "Sairas" -sairauslomatyyppiä oletuksena. Jos korvaustietoa tai lomapäivien kerryttämistä ei ole määritetty, korvaus ja lomapäivien kerryttäminen määritetään automaattisesti samalla tavalla kuin tapahtuman muokkaussivulla palvelun käyttöliittymässä. Käyttöoikeudet toimivat samalla tavalla kuten käyttöliittymän "Lisää/Muokkaa tapahtumaa" - sivun käyttöoikeudet.  
5 | SickLeaveTypeId | integer | 0..1 | Sairausloman tyypin tunniste:  
1=Sairas,  
2=Lapsi sairas,  
3=Työtapaturma, 4=Työmatkatapaturma,  
5=Vapaa-ajan tapaturma  
5 | SickLeaveTypeName | String | 0..1 | Vaihtoehtoinen tapa määrittää sairausloman tyyppi perustuen sairauslomatyypin nimeen tai käännökseen. On suositeltavaa käyttää ensisijaisesti SickLeaveTypeId - kenttää jos mahdollista.  
5 | MedicalCertificateGiven | bool | 0..1 | Onko Lääkärin todistus vastaanotettu? (true/false)  
5 | SupervisorsPermission | bool | 0..1 | Onko poissaololle esihenkilön hyväksyntä? (true/false)  
5 | ReasonCode | String | 0..1 | Syykoodi  
5 | CompensationTypeId | Int | 0..1 | Poissaolon korvauksen tunniste  
1 = palkallinen,  
2 = palkaton,  
3 = vähennetty palkka  
5 | CompensationTypeName | string | 0..1 | Vaihtoehtoinen tapa määrittää korvauksen tunniste, esim. "palkallinen", "paid", "palkaton", "unpaid", "vähennetty palkka", "reduced salary"  
5 | EarnsVacationDays | Bool | 0..1 | Kerryttääkö sairausvapaa lomapäiviä? (true/false)  
4 | PlannedWorkDetails | XML element | 0 | Ei käytössä. Parempi tuki erilaisten tapahtumatyyppien suunnitteluun ja ryhmittelyyn mahdollistetaan tulevissa versioissa.  
### Kyselyn esimerkki
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForUpdateActivitiesV5>
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
        </tyo:ParametersForUpdateActivitiesV5>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Vastaus
**TASO** | **KENTÄN NIMI** | **MUOTO** | **ESIINTYMISKERRAT** | **SELITE**  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForUpdateActivitiesV5 | XML element | 1 |   
1 | ResponseCode | integer | 1 | Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 1 | Koodin kuvaus  
1 | ActivityList | XML element | 1 |   
1 | ActivityList | XML element | 0..1 | Lisätyt / päivitetyt tapahtumat  
2 | Activity | XML element | 0..n | Lisätty / päivitetty tapahtuma  
3 | Id | integer | 0..1 | Lisätyn / päivitetyn tapahtuman yksilöllinen Nepton-tunniste.  
3 | ExternalIdentifiers | XML element | 0..1 | Lisätyn / päivitetyn tapahtuman ulkoiset tunnisteet. Virhetilanteissa ensisijaisesti palautetaan kutsussa ollut `ExternalIdentifiers` ja toisisjaisesti kutsussa ollut `ExistingExternalIdentifier` .  
4 | ExternalIdentifier | XML element | 1..n |   
5 | Identifier | string | 1 | Ulkoinen tunniste  
5 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on `External` .  
3 | Success | boolean | 1 | Onnistuiko tapahtuman lisäys ( `true` ) vai ei ( `false` ).  
3 | ErrorCode | integer | 0..1 | Jos tapahtuman päivitys ei onnistunut, syyn virhekoodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
3 | ErrorMessage | string | 0..1 | Jos tapahtuman päivitys ei onnistunut, syyn selite.  
### Vastauksen esimerkki
[code]
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForUpdateActivitiesV5>
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
        </tyo:ReturnValueForUpdateActivitiesV5>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
