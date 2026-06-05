---
id: 13106403486109
title: EnsureProjectsExistV3
url: https://support.nepton.com/hc/fi/articles/13106403486109-EnsureProjectsExistV3
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
edited_at: '2026-06-01T11:41:57Z'
---

# EnsureProjectsExistV3

Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/36507754396573>).
## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään siihen, että kutsussa annettu lista projekteista päivitetään Neptoniin. Mikäli projekti on olemassa niin sen tietoja päivitetään. Mikäli projektia ei ole olemassa niin se luodaan. Päivitettävä projekti tunnistetaan joko Projektin Nepton tunnisteella (Id), ExistingIdentifier-elementissä määritetyllä tunnisteella tai projektin koodilla (Code). Projektin projektipäälliköitä voidaan muokata välittämällä projektin ProjectManagers - elementissä ProjectManager - elementtejä. ProjectManager - elementissä annetaan projektipäällikön tunnistetieto, joka voi olla joko henkilönumero (PersonnelNumber), käyttäjätunnus (Username) tai Neptonin sisäinen käyttäjätunniste (UserId). Projektipäälliköiden päivitys voidaan tehdä joko niin että kutsussa välitetyt projektipäälliköt lisätään aiempien Neptonissa projektissa olevien projektipäälliköiden lisäksi (oletus) tai lisäys tyhjentää aiemmat Neptonissa projektissa olevat projektipäälliköt joita ei ole välitetty kutsussa asettamalla ProjectManagers - elementissä tieto RemoveOthers jonka arvo on `true`.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon nähden ([EnsureProjectsExistV2](<https://support.nepton.com/hc/fi/articles/360005783318>))
### Rakenteelliset muutokset
**Vanha** | **Uusi** | **Lisätiedot**  
---|---|---
[code] 
    <tyo:ParametersForEnsureProjectsExistV2>
      ...
    </tyo:ParametersForEnsureProjectsExistV2>
[/code]  
| 
[code]
    <tyo:ParametersForEnsureProjectsExistV3>
      ...
    </tyo:ParametersForEnsureProjectsExistV3>
[/code]
|  Kutsussa juurielementin nimi vaihtunut
[code] 
    <tyo:ReturnValueForEnsureProjectsExistV2>
      ...
    </tyo:ReturnValueForEnsureProjectsExistV2>
[/code]  
| 
[code]
    <tyo:ReturnValueForEnsureProjectsExistV3>
    ...
    </tyo:ReturnValueForEnsureProjectsExistV3>
[/code]
|  Vastauksessa juurielementin nimi muuttunut  
### Uudet ominaisuudet ja elementit
  * Projektille voidaan lisätä projektipäälliköitä välittämällä nämä tämän projektin Project - elementin alla olevassa ProjectManagers - elementissä
    * ProjectManagers - elementti lisätty kutsuun
  * ProjectManagers - elementille voidaan määrittää RemoveOthers - elementti, jolla voidaan määrittää poistetaanko projektilta aiemmat projektipäälliköt joita ei ole lisätty kutsussa. Tämä tapahtuu määrittämällä RemoveOthers - elementin arvoksi `true`.
    * ProjectManagers - elementin alle lisätty RemoveOthers - elementti
  * ProjectManagers - elementille voidaan määrittää ProjectManager - elementtejä, joissa määritetään lisättävät projektipäälliköt
    * ProjectManager - elementti lisätty kutsuun
      * ProjectManager - elementin alle lisätty UserId-, UserName- ja PersonnelNumber - elementit.
  * ProjectManagers - elementti lisätty vastaukseen ja palautetaan silloin jos projektipäälliköitä on päivitetty, eli jos kutsu sisältää ProjectManagers - elementin.


### Poistuneet ominaisuudet ja elementit
  * Käytöstä kokonaan poistuneet Left ja Right -elementit poistettu lähetettävästä pyynnöstä


## Lähetettävät tiedot
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForEnsureProjectsExistV3 | XML element | 1 |   
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>)  
1 | ProjectList | XML element | 1 | Listaus projekteja  
2 | Project | XML element | 1..n | Yhden projektin tiedot. Yleisten elementtien sisällön näkee [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
3 | ExistingProjectIdentifier | XML element | 0..1 | Tunniste, jolla haetaan olemassaolevaa projektia. Jos projekti löytyy, sen tiedot päivitetään, muutoin luodaan uusi projekti. Tässä elementissä annettua tunnistetta ei tallenneta projektin tietoihin.  
4 | Identifier | string | 1 | Projektin tunnisteen arvo.  
4 | IdentifierType | string | 1 |  Projektin tunnisteen tyyppi. Voi olla joko
  * `ProjectCode` \- projektin koodi
  * `ExternalIdentifier` \- projektin ulkoinen tunniste

Lue lisää projektin koodista ja ulkoisesta tunnisteesta [täällä](<https://support.nepton.com/hc/fi/articles/360006768998>).  
3 | Id | unsignedInt | 0..1 | Neptonin antama yksilöllinen projektin tunniste. Määritä vain, jos haluat järjestelmän tunnistavan olemassaolevan projektin tämän tiedon perusteella.  
3 | ExternalIdentifier | XML element | 0..n | Ulkoisen järjestelmän tunniste, joka tallennetaan projektille  
4 | Identifier | string | 1 | Projektin tunnisteen arvo. Projektin ulkoisen tunnisteen merkkiraja 64 merkkiä.  
4 | IdentifierType | string | 1 |  Projektin tunnisteen tyyppi. Tällä hetkellä ainoa tuettu arvo on
  * `ExternalIdentifier` \- projektin ulkoinen tunniste

Lue lisää ulkoisesta tunnisteesta [täällä](<https://support.nepton.com/hc/fi/articles/360006768998>).  
3 | Name | string | 1 | Projektin nimi. Merkkiraja 255 merkkiä.  
3 | Deleted | boolean | 0..1 | Onko projekti poistettu vai ei. Poistetut projektit säilyvät tietokannassa, mutta niiden palauttaminen ei ole mahdollista tämän rajapinnan kautta.  
3 | Active | boolean | 0..1 |  Jos kentän arvona on `true`, projektin päättymispäivä tyhjennetään. Jos kentän arvona on `false`, päättymispäiväksi asetetaan eilinen päivä. Jos `EndDate` kentällä on arvo, tämän kentän tiedot sivuutetaan.  
3 | Code | string | 0..1 | Projektin koodi. Jos ID tai ExistingIdentifier elementtejä ei ole kutsussa määritetty niin olemassaoleva projektia koitetaan löytää tämän perusteella. Merkkiraja 255 merkkiä.  
3 | TypeInternalName | string | 0..1 | Projektin tyypin sisäinen tunniste. Arvo täytyy antaa projektia luodessa. Jos erillisiä projektityyppejä ei ole asetettuna, arvona on `project_work`. Merkkiraja 190 merkkiä.  
3 | Description | string | 0..1 | Projektin kuvaus  
3 | StartDate | date | 0..1 |  Projektin alkamispäivä. Projektia ei voida asettaa tapahtumien kohdisteeksi tai projektin tunteja raportoida ennen tätä päivää. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <StartDate xsi:nil="true" />
[/code]  
3 | EndDate | date | 0..1 |  Projektin päättymispäivä. Projektia ei voida asettaa tapahtumien kohdisteeksi tai projektin tunteja raportoida tämän päivän jälkeen. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <EndDate xsi:nil="true" />
[/code]  
3 | ParentProjectId | unsignedInt | 0..1 |  Projektin yläprojektin Neptonin yksilöllinen tunniste. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <ParentProjectId xsi:nil="true" />
[/code]  
3 | ParentProjectCode | string | 0..1 |  Projektin yläprojektin projektikoodi. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <ParentProjectCode xsi:nil="true" />
[/code]  
3 | ParentProjectIdentifier | XML element | 0..1 |  Projektin yläprojektin tunniste. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <ParentProjectIdentifier xsi:nil="true" />
[/code]  
4 | Identifier | string | 1 | Yläprojektin tunniste  
4 | IdentifierType | string | 1 | Yläprojektin tunnisteen tyyppi. Voi olla joko `ProjectCode` tai `ExternalIdentifier`  
3 | ChildProjects | XML element | 0..n | Tietoa ei käytetä  
3 | ProjectManagers | XML element | 0..1 | Projektipäälliköt, jotka tallennetaan projektille  
4 | RemoveOthers | boolean | 0..1 | Jos annettu arvo "true", poistetaan projektista aiemmat projektin projektipäälliköt joita ei ole määritetty kutsussa projektipäälliköksi  
4 | ProjectManager | XML element | 0..n | Projektille lisättävän projektipäällikön tunnistetieto  
5 | UserId | unsignedInt | 0..1 | Neptonin antama yksilöllinen henkilön tunniste  
5 | Username | string | 0..1 | Henkilön käyttäjätunnus  
5 | PersonnelNumber | string | 0..1 | Henkilön henkilönumero  
### Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForEnsureProjectsExistV3>
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <ProjectList>
            <Project>
              <ExistingProjectIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ExistingProjectIdentifier>
              <ExternalIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ExternalIdentifier>
              <Name>Projekti X</Name>
              <Code>1000/9001</Code>
              <TypeInternalName>project_work</TypeInternalName>
              <Description>Lorem ipsum primis venenatis justo mollis fringilla lectus sociosqu nostra, vehicula nunc massa sodales habitasse duis</Description>
              <StartDate>2001-01-01</StartDate>
              <EndDate xsi:nil="true" />
              <ParentProjectIdentifier>
                <Identifier>45453ddd-f167-408b-9e75-6c419755caf8</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ParentProjectIdentifier>
              <ProjectManagers>
                <RemoveOthers>true</RemoveOthers>
                <ProjectManager>
                  <PersonnelNumber>27</PersonnelNumber>
                </ProjectManager>
                <ProjectManager>
                  <UserName>Example Username</PersonnelNumber>
                </ProjectManager>
              </ProjectManagers>
            </Project>
          </ProjectList>
        </tyo:ParametersForEnsureProjectsExistV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Vastaus
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForEnsureProjectsExistV3 | XML element | 1 |   
1 | ResponseCode | integer | 1 | Projektien käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 1 | Koodin kuvaus  
1 | EnsureProjectsExistResultList | XML element | 1 |   
2 | EnsureProjectsExistResult | XML element | 0..n | Yhden projektin käsittelyn tulos  
3 | ResponseCode | integer | 1 | Tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360019841477>).  
3 | ResponseString | integer | 1 | Tuloksen koodin kuvaus  
3 | ProjectId | unsignedInt | 1 |  Käsitellyn projektin Neptonin antama yksilöllinen tunniste. Arvona voi myös olla `null`, esimerkiksi:
[code] 
    <ProjectId xsi:nil="true" />
[/code]
Virhetilanteissa palautetaan `null` jos kyselyssä ei annettu Neptonin antamaa yksilöllistä tunnistetta.  
3 | ProjectIdentifier | XML element | 1 | Tunniste, joka lähetettiin kyselyssä `ExistingProjectIdentifier` kentässä.  
4 | Identifier | string | 1 | Projektin tunnisteen arvo  
4 | IdentifierType | string | 1 |  Projektin tunnisteen tyyppi. Voi olla joko
  * `ProjectCode` \- projektin koodi
  * `ExternalIdentifier` \- projektin ulkoinen tunniste

Lue lisää projektin koodista ja ulkoisesta tunnisteesta [täällä](<https://support.nepton.com/hc/fi/articles/360006768998>).  
3 | ProjectManagers | XML element | 0..1 | Projektin projektipäälliköt. Palautetaan vain jos pyynnössä on päivitetty projektipäälliköitä.  
4 | ProjectManager | XML element | 0..n | Projektin projektipäällikön tunnistetieto  
5 | UserId | unsignedInt | 0..1 | Neptonin antama yksilöllinen henkilön tunniste  
5 | Username | string | 0..1 | Henkilön käyttäjätunnus  
5 | PersonnelNumber | string | 0..1 | Henkilön henkilönumero  
### Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <tyo:ReturnValueForEnsureProjectsExistV3>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <EnsureProjectsExistResultList>
            <EnsureProjectsExistResult>
              <ResponseCode>1000</ResponseCode>
              <ResponseString>All clear. No errors.</ResponseString>
              <ProjectId>76254</ProjectId>
              <ProjectIdentifier>
                <Identifier>4a78611d-4a00-4c4a-a987-865664d732ce</Identifier>
                <IdentifierType>ExternalIdentifier</IdentifierType>
              </ProjectIdentifier>
              <ProjectManagers>
                <ProjectManager>
                  <UserId>09876543210</UserId>
                  <UserName>Test User</UserName>
                  <PersonnelNumber>27</PersonnelNumber>
                </ProjectManager>
                <ProjectManager>
                  <UserId>1234567890</UserId>
                  <UserName>Example Username</PersonnelNumber>
                  <PersonnelNumber>1274</PersonnelNumber>
                </ProjectManager>
              </ProjectManagers>
            </EnsureProjectsExistResult>
          </EnsureProjectsExistResultList>
        </tyo:ReturnValueForEnsureProjectsExistV3>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
