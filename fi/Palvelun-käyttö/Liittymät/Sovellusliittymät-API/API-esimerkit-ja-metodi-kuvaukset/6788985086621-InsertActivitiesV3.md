---
id: 6788985086621
title: InsertActivitiesV3
url: https://support.nepton.com/hc/fi/articles/6788985086621-InsertActivitiesV3
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
edited_at: '2026-06-01T09:22:38Z'
---

# InsertActivitiesV3

Huom! Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version löydät [täältä](<https://support.nepton.com/hc/fi/articles/27550371952925>)
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatietojen lisäämiseen Neptonissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat on kuvattu yleisellä tasolla [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää, onko tieto kutsussa pakollinen vai ei. Esiintymiskerrat 0 tarkoittaa, että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa, että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([InsertActivitiesV2](<https://support.nepton.com/hc/fi/articles/6788513921565>))
### Rakenteelliset muutokset
vanha | Uusi | Lisätiedot  
---|---|---
[code] 
    <tyo:ParametersForInsertActivitiesV2>
      ...
    </tyo:ParametersForInsertActivitiesV2>
[/code]  
| 
[code]
    <tyo:ParametersForInsertActivitiesV3>
      ...
    </tyo:ParametersForInsertActivitiesV3>
[/code]
| Pyynnön juurielementin nimi muuttunut
[code] 
    <tyo:ParametersForInsertActivitiesV2>
      ...
    </tyo:ParametersForInsertActivitiesV2>
[/code]  
| 
[code]
    <tyo:ParametersForInsertActivitiesV3>
      ...
    </tyo:ParametersForInsertActivitiesV3>
[/code]
| Vastauksen juurielementin nimi vaihtunut  
### Uudet ominaisuudet ja elementit
  * Tapahtumatyyppi voidaan valita koodin perusteella
    * ActivityTypeCode-elementti lisätty pyyntöön
  * Sairaslomien ja poissaolojen tarkemmat tiedot mahdollista määrittää
    * Lisätty ActivityDetails-elementti pyyntöön


## Käyttäjäviittaukset
Tapahtuman luonnissa on pakollinen tieto henkilöstä sekä ei-pakollinen tieto tapahtuman hyväksyneestä henkilöstä. Kumpaankin henkilötietoon voi viitata käyttäen tunnisteena jotain seuraavista: Neptonin yksilöllinen käyttäjä-ID, käyttäjänimi, käyttäjän henkilötunnus tai käyttäjän henkilönumero. Jos tapahtuman hyväksyjä määritetään, niin tapahtuma merkitään samalla hyväksytyksi. Katso lähetettävät tiedot -taulukosta tarkemmat tiedot elementeistä, joissa tiedot tulisi ilmoittaa.
## Lähetettävät tiedot
**TASO** | **KENTÄN NIMI** | **MUOTO** | **ESIINTYMISKERRAT** | **SELITE**  
---|---|---|---|---  
0 | ParametersForInsertActivitiesV3 | XML element | 1 | SOAP body:n alla oleva juurielementti  
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 | ActivityList | XML element | 1 | Lista lisättävistä tapahtumista  
2 | Activity | XML element | 1..n | Lisättävä tapahtuma  
3 | UserId | integer | 0..1 | Henkilön Nepton-tunniste, jolle tapahtuma lisätään  
3 | UserUsername | string | 0..1 | Henkilön käyttäjätunnus, jolle tapahtuma lisätään.  
3 | UserSocialSecurityNumber | string | 0..1 | Henkilö, jolle tapahtuma lisätään. Viittaus henkilötunnuksen perusteella  
3 | UserPersonnelNumber | string | 0..1 | Henkilö, jolle tapahtuma lisätään. Viittaus henkilönumeron perusteella  
3 | ActivityTypeId | integer | 0..1 |  **Huom!** Käytä ActivityTypeCode-kenttää, ActivityTypeId-kenttää käyttävät vanhemmat toteutukset. Käytettävä tapahtumatyyppi. Viittaus tapahtumatyypin Nepton tunnisteella. Mikäli ActivityTypeId- tai ActivityTypeCode-tietoa ei anneta kutsussa, tapahtuma luodaan Työ-tapahtumana.  
3 | ActivityTypeCode | string | 0..1 |  Käytettävä tapahtumatyyppi. Viittaus tapahtumatyypin koodin perusteella. Jos useampi tapahtumatyyppi käyttää samaa koodia, kutsussa käytetään ensimmäistä löytynyttä tapahtumatyyppiä. Mikäli ActivityTypeId- tai ActivityTypeCode-tietoa ei anneta kutsussa, tapahtuma luodaan Työ-tapahtumana.  
3 | BeginDateTime | dateTime | 1..1 |  Tapahtuman alkamispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS` , esimerkiksi `2021-02-18T12:30:00` . Pakollinen  
3 | EndDateTime | dateTime | 0..1 |  Tapahtuman päättymispäivä ja -aika. Muotona on `VVVV-KK-PPTHH:MM:SS` , esimerkiksi `2021-02-18T12:30:00` . Jos tietoa ei anneta tai se on tyhjä, tapahtuma luodaan ilman päättymisaikaa.  
3 | ApproverUserId | integer | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus käyttäjän yksilöllisen tunnisteen perusteella (löytyy käyttäjän profiilin URL:sta).  
![](https://support.nepton.com/hc/article_attachments/22428530899997)  
3 | ApproverUsername | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus käyttäjänimen perusteella  
3 | ApproverUserSocialSecurityNumber | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus käyttäjän henkilötunnuksen perusteella.  
3 | ApproverUserPersonnelNumber | string | 0..1 | Tapahtuman hyväksynyt henkilö. Viittaus käyttäjän henkilönumeron perusteella  
3 | Comment | string | 0..1 | Tapahtumalle kirjattavat huomiot.  
3 | IsClockedEvent | boolean | 0..1 | Onko lisättävä tapahtuma kellotettu ( `true` ) vai ei ( `false` ).  
3 | IsCreatedWithPinCode | boolean | 0..1 | Onko lisättävä tapahtuma kellotettu PIN-koodilla ( `true` ) vai ei ( `false` ).  
3 | OvertimeBasePartTargetedTo | string | 0..1 | Ylityön perusosan kohdenne lisättävällä tapahtumalla.  
3 | OvertimeIncrementPartTargetedTo | string | 0..1 | Ylityön korotusosan kohdenne lisättävällä tapahtumalla.  
3 | RelatedProjects | XML element | 0..1 | Tapahtumalle kirjattavat projektit. Tämän elementin sisään laitetaan ActivityToProjectRelation - elementtejä jokaista tapahtuman projektilinkitystä kohden (ks. lisää seuraavasta kohdasta).  
4 | ActivityToProjectRelation | XML element | 0..n | Tapahtumaan lisättävän projektimerkinnän tiedot. Katso lisätietoja ja esimerkki [tästä.](<https://support.nepton.com/hc/fi/articles/360019840217-Tapahtumien-API#ActivityToProjectRelation>)  
5 | Id | integer | 0..1 | Projektin yksilöllinen tunniste Neptonissa. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
5 | Duration | integer | 0..1 | Projektin kesto minuutteina  
5 | Name | string | 0..1 | Projektin nimi. Tietoa ei käytetä.  
5 | Code | string | 0..1 | Projektin koodi. Projektin yksilöllinen tunniste tai projektin koodi täytyy antaa.  
3 | WorkIncrements | XML element | 0..1 | Tapahtumalle kirjattavat työlisät.  
4 | WorkIncrement | XML element | 0..n |   
5 | Index | integer | 1 | Työlisän indeksi  
5 | Value | decimal | 1 | Työlisän arvo minuutteina, yksikköinä tai desimaalina.  
3 | ExternalIdentifiers | XML element | 0..1 | Tapahtumalle asetettavat ulkoiset tunnisteet  
4 | ExternalIdentifier | XML element | 1..n | Tapahtumalle asetettava ulkoinen tunniste  
5 | Identifier | string | 1 | Ulkoinen tunniste  
5 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on `External` .  
3 | ActivityDetails | XML element | 0..1 | Tietue joka sisältää tapahtumatyyppikohtaiset lisätiedot kuten esimerkiksi sairausloman tai poissaolon lisätiedot jotka on kuvattuna alla.  
4 | AbsenceDetails | XML element | 0..1 |  Jos tapahtumatyyppi on poissaolo-tyyppinen, poissaolon tarkemman tiedot voidaan välittää AbsenceDetails-tietueen alitietueina. AbsenceDetails välitetään ActivityDetails-tietueen alitietueena. Jos AbsenceDetails - kenttiä ei ole määritetty, käytetään poissaolotyypin ja tapahtumatyypin oletusarvoja. Jos pyyntö sisältää vain poissaolotyypin, korvaus ja lomapäivien kerryttäminen määritetään automaattisesti samalla tavalla kuin tapahtuman muokkaussivulla palvelun käyttöliittymässä. Käyttöoikeudet toimivat samalla tavalla kuten käyttöliittymän "Lisää/Muokkaa tapahtumaa" - sivun käyttöoikeudet.  
5 | AbsenceTypeId | Int | 0..1 | Käytettävän poissaolotyypin ID. Käyttöliittymästä nämä näkee kohdasta: Asetukset > Työtunnit > Poissaolotyypit  
5 | AbsenceTypeName | String | 0..1 | Vaihtoehtoinen tapa osoittaa käytettävä poissaolotyyppi nimen/käännöksen mukaan, esim. "Ammattiyhdistystoiminta". On suositeltavaa käyttää ensisijaisesti AbsenceTypeId -kenttää, jos mahdollista  
5 | CompensationTypeId | Int | 0..1 | Poissaolon korvauksen tunniste  
1 = palkallinen,  
2 = palkaton,  
3 = vähennetty palkka  
5 | CompensationTypeName | string | 0..1 | Vaihtoehtoinen tapa määrittää korvauksen tunniste, esim. "palkallinen", "paid", "palkaton", "unpaid", "vähennetty palkka", "reduced salary"  
5 | EarnsVacationDays | bool | 0..1 | Kerryttääkö poissaolo lomapäiviä (true/false)  
4 | SickLeaveDetails | XML element | 0..1 |  Jos tapahtumatyyppi on sairausloma, niin lisätiedot voidaan välittää SickLeaveDetails - tietueen alitietueina. SickLeaveDetails välitetään ActivityDetails-tietueen alitietueena. Jos sairauslomatyypin tietoja ei välitetä pyynnössä, käytetään "Sairas" -sairauslomatyyppiä oletuksena. Jos korvaustietoa tai lomapäivien kerryttämistä ei ole määritetty, korvaus ja lomapäivien kerryttäminen määritetään automaattisesti samalla tavalla kuin tapahtuman muokkaussivulla palvelun käyttöliittymässä. Käyttöoikeudet toimivat samalla tavalla kuten käyttöliittymän "Lisää/Muokkaa tapahtumaa" - sivun käyttöoikeudet.  
5 | SickLeaveTypeId | Int | 0..1 | Sairausloman tyypin tunniste:  
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
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV3>
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>201</ActivityTypeCode>
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
        </tyo:ParametersForInsertActivitiesV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
### Kyselyn esimerkki poissaolo/sairasloma
Poissaolon AbsenceDetails - tietue ja sairasloman SickLeaveDetails - tietue välitetään ActivityDetails - tietueen alitietueina alla olevien esimerkkien mukaisesti.
#### Poissaolo
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV3>
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>4</ActivityTypeCode>
              <BeginDateTime>2024-01-19T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-19T16:00:00</EndDateTime>
              <ApproverUserPersonnelNumber>9999</ApproverUserPersonnelNumber>
              <ActivityDetails>
                <AbsenceDetails>
                  <AbsenceTypeId>8</AbsenceTypeId>
                  <CompensationTypeId>1</CompensationTypeId>
                  <EarnsVacationDays>true</EarnsVacationDays>
                </AbsenceDetails>
              </ActivityDetails>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
#### Sairasloma
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForInsertActivitiesV3>
          <CallerAuthentication /><!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <ActivityList>
            <Activity>
              <UserPersonnelNumber>9001</UserPersonnelNumber>
              <ActivityTypeCode>2</ActivityTypeCode>
              <BeginDateTime>2024-01-22T08:00:00</BeginDateTime>
              <EndDateTime>2024-01-22T16:00:00</EndDateTime>
              <ApproverUserPersonnelNumber>9999</ApproverUserPersonnelNumber>
              <ActivityDetails>
                <SickLeaveDetails>
                  <SickLeaveTypeId>3</SickLeaveTypeId>
                  <MedicalCertificateGiven>true</MedicalCertificateGiven>
                  <SupervisorsPermission>true</SupervisorsPermission>
                  <ReasonCode>12345</ReasonCode>
                  <CompensationTypeId>1</CompensationTypeId>
                  <EarnsVacationDays>true</EarnsVacationDays>
                </SickLeaveDetails>
              </ActivityDetails>
            </Activity>
          </ActivityList>
        </tyo:ParametersForInsertActivitiesV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
### Vastaus
**TASO** | **KENTÄN NIMI** | **MUOTO** | **ESIINTYMISKERRAT** | **SELITE**  
---|---|---|---|---  
0 | ReturnValueForInsertActivitiesV3 | XML element | 1 | SOAP body:n alla oleva juurielementti  
1 | ResponseCode | integer | 1 | Käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 1 | Koodin kuvaus  
1 | ActivityList | XML element | 1 |   
1 | ActivityList | XML element | 0..1 | Lisätyt tapahtumat  
2 | Activity | XML element | 0..n | Lisätty tapahtuma  
3 | Id | integer | 0..1 | Lisätyn tapahtuman yksilöllinen Nepton-tunniste.  
3 | ExternalIdentifiers | XML element | 0..1 | Lisätyn tapahtuman ulkoiset tunnisteet. Virhetilanteissa ensisijaisesti palautetaan kutsussa ollut `ExternalIdentifiers` ja toisisjaisesti kutsussa ollut `ExistingExternalIdentifier` .  
4 | ExternalIdentifier | XML element | 1..n |   
5 | Identifier | string | 1 | Ulkoinen tunniste  
5 | IdentifierType | string | 1 | Ulkoisen tunnisteen tyyppi. Ainoa tuettu tyyppi tällä hetkellä on `External` .  
3 | Success | boolean | 1 | Onnistuiko tapahtuman lisäys ( `true` ) vai ei ( `false` ).  
3 | ErrorCode | integer | 0..1 | Jos tapahtuman lisäys ei onnistunut, syyn virhekoodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
3 | ErrorMessage | string | 0..1 | Jos tapahtuman lisäys ei onnistunut, syyn selite.  
### Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForInsertActivitiesV3>
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
        </tyo:ReturnValueForInsertActivitiesV3>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
