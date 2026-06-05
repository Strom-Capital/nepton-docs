---
id: 6885147716893
title: SetVisibleProjectsForUser
url: https://support.nepton.com/hc/fi/articles/6885147716893-SetVisibleProjectsForUser
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
edited_at: '2022-09-30T06:09:11Z'
---

# SetVisibleProjectsForUser

Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme, että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360005968797>)
## Rajapinnan yleiskuvaus
Rajapinnalla asetetaan ne projektit, jotka liitetään näkyvän henkilölle tapahtuman kirjauksen projektivalinnoissa.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
0 | ParametersForSetVisibleProjectsForUser | XML element | 1 | Juuri,  
SOAP body:n alla  
1 | CallerAuthentication | XML element | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | SetVisibleProjectsForUserList | XML element | 1 |   
2 | SetVisibleProjectForUser | XML element | 1..n | Yhden projektin näkyvyyden asetus yhdelle henkilölle.  
3 | ProjectId | unsignedIntt | 0..1 | Neptonin antama yksilöllinen projektin tunniste  
3 | ProjectCode | string | 0..1 | Projektin koodi  
3 | UserId | unsignedInt | 0..1 | Neptonin antama yksilöllinen henkilön tunniste  
3 | Username | string | 0..1 | Henkilön käyttäjätunnus  
3 | PersonnelNumber | string | 0..1 | Henkilön henkilönumero  
3 | ProjectVisible | boolean | 1 | Voiko henkilö nähdä projektin (`true`) vai ei (`false`)  
### Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
        <soapenv:Body>  
          <tyo:ParametersForSetVisibleProjectsForUser>  
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <SetVisibleProjectsForUserList>  
            <SetVisibleProjectForUser>  
              <PersonnelNumber>9001</PersonnelNumber>  
              <ProjectVisible>true</ProjectVisible>  
            </SetVisibleProjectForUser>  
          </SetVisibleProjectsForUserList>  
        </tyo:ParametersForSetVisibleProjectsForUser>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForSetVisibleProjectsForUser | XML element | 1 |   
1 | ResponseCode | integer | 1 | Lähetettyjen tietojen käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | string | 1 | Koodin kuvaus  
1 | SetVisibleProjectsForUserResultList | XML element | 1 |   
2 | SetVisibleProjectsForUserResult | XML element | 0..n | Tulos yhden projektin näkyvyyden asetukselle  
3 | ResponseCode | integer | 1 | Tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
3 | ResponseString | string | 1 | Tuloksen koodin kuvaus  
3 | ProjectId | unsignedInt | 0..1 | Neptonin antama projektin yksilöllinen tunniste. Arvona voi myös olla `null`, esimerkiksi: 
[code]
    <ProjectId xsi:nil="true" />
[/code]
Virhetilanteissa arvoa ei palauteta jos sitä ei ole annettu kyselyssä.  
3 | ProjectCode | string | 0..1 | Projektin koodi. Arvona voi myös olla `null`, esimerkiksi: 
[code]
    <ProjectCode xsi:nil="true" />
[/code]
Virhetilanteissa arvoa ei palauteta jos sitä ei ole annettu kyselyssä.  
3 | UserId | unsignedInt | 0..1 | Neptonin antama henkilön yksilöllinen tunniste. Arvona voi myös olla `null`, esimerkiksi: 
[code]
    <UserId xsi:nil="true" />
[/code]
Virhetilanteissa arvoa ei palauteta jos sitä ei ole annettu kyselyssä.  
3 | Username | string | 0..1 | Henkilön käyttäjätunnus. Arvona voi myös olla `null`, esimerkiksi: 
[code]
    <Username xsi:nil="true" />
[/code]
Virhetilanteissa arvoa ei palauteta jos sitä ei ole annettu kyselyssä.  
3 | PersonnelNumber | string | 0..1 | Henkilön henkilönumero. Arvona voi myös olla `null`, esimerkiksi: 
[code]
    <PersonnelNumber xsi:nil="true" />
[/code]
Arvoa ei palauteta jos sitä ei ole annettu kyselyssä.  
### Vastauksen esimerkki
[code] 
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi">  
      <SOAP-ENV:Body>  
        <ns1:ReturnValueForSetVisibleProjectsForUser>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <SetVisibleProjectsForUserResultList>  
            <SetVisibleProjectsForUserResult>  
              <ResponseCode>1000</ResponseCode>  
              <ResponseString>All clear. No errors.</ResponseString>  
              <ProjectId>76254</ProjectId>  
              <ProjectCode>1000/9001</ProjectCode>  
              <UserId>1234</UserId>  
              <Username>matti.meikäläinen</Username>  
              <PersonnelNumber>9001</PersonnelNumber>  
            </SetVisibleProjectsForUserResult>  
          </SetVisibleProjectsForUserResultList>  
        </ns1:ReturnValueForSetVisibleProjectsForUser>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
