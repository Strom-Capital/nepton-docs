---
id: 36506225707677
title: ClearVisibleProjectsForUserV2
url: https://support.nepton.com/hc/fi/articles/36506225707677-ClearVisibleProjectsForUserV2
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
edited_at: '2026-06-01T10:52:14Z'
---

# ClearVisibleProjectsForUserV2

## Rajapinnan yleiskuvaus
Verkkopalvelun avulla voidaan poistaa määritetyltä henkilöltä kaikki käyttäjätason projektinäkyvyydet. Tämä ei vaikuta millään tavalla henkilöryhmän kautta määritettyihin projekteihin.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla[ täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Muutokset aiempaan versioon ([ClearVisibleProjectsForUser](<https://support.nepton.com/hc/fi/articles/6919474574237>))
V2-versio lisää seuraavan uuden kentän: 
Kenttä | Kuvaus  
---|---  
PersonExternalIdentifier | Mahdollistaa käyttäjän tunnistamisen ulkoisella tunnisteella  
## Käyttäjäviittaukset
Kohdekäyttäjä voidaan tunnistaa yksilöllisen Nepton tunnisteen, käyttäjän henkilönumeron, ulkoisen tunnisteen tai käyttäjätunnuksen perusteella. Jokin näistä on annettava. Palvelu palauttaa virheen mikäli yhtään käyttäjätunnistetta ei ole määritetty tai tunnistetta vastaavaa käyttäjää ei löytynyt.
## Lähetettävät tiedot
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ParametersForClearVisibleProjectsForUserV2 | XML element | 1 | Juurielementti,  
SOAP body:n alla  
1 | CallerAuthentication | XML element | 1 | Tunnistautumistiedot. Katso tarkemmat tiedot [täältä](<https://support.nepton.com/hc/fi/articles/360019983978>)  
1 | ClearVisibleProjectsForUserList | XML element | 1 |   
2 | ClearVisibleProjectForUser | XML element | 1..n |   
3 | UserId | integer | 0..1 | Kohdekäyttäjän Nepton tunniste.  
3 | PersonnelNumber | string | 0..1 | Kohdekäyttäjän henkilönumero.   
3 | PersonExternalIdentifier | XML Element | 0..1 | UUSI V2:ssa - Kohdekäyttäjän ulkoinen tunniste  
4 | Identifier | string | 1 | Ulkoisen tunnisteen arvo  
4 | FieldName | string | 1 |  Ulkoisen tunnisteen kenttänimi. Tuetut arvot:
[code] 
    ExternalIdentifier1
[/code]  
### Vastaus
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ReturnValueForClearVisibleProjectsForUserV2 | XML element | 1 | Juurielementti,  
SOAP body:n alla  
1 | Responsecode | integer | 1 | Yleinen vastauskoodi  
1 | ResponseString | string | 1 | Yleinen vastausviesti  
1 | ClearVisibleProjectsForUserResultList | XML element | 1..n | Lista käsitellyistä riveistä  
2 | ResponseCode | integer | 1 | Yksittäisen rivin vastauskoodi  
2 | ResponseString | string | 1 | Yksittäisen rivin vastausviesti  
2 | UserId | integer | 1 | Kohdekäyttäjän ID  
2 | Username | string | 1 | Kohdekäyttäjän käyttäjätunnus  
2 | PersonnelNumber | string | 1 | Kohdekäyttäjän henkilönumero.   
2 | PersonExternalIdentifier | XML element | 1 | UUSI V2:ssa - Kohdekäyttäjän ulkoinen tunniste  
3 | Identifier | string | 1 | Ulkoisen tunnisteen arvo  
3 | FieldName | string | 1 |  Ulkoisen tunnisteen kenttänimi. Tuetut arvot:
[code] 
    ExternalIdentifier1
[/code]  
### Esimerkkipyyntö
#### Esimerkki ulkoisella tunnisteella (V2 uusi ominaisuus)
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForClearVisibleProjectsForUserV2>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->  
          <ClearVisibleProjectsForUserList>  
            <ClearVisibleProjectForUser>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-12345<Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUser>  
            <ClearVisibleProjectForUser>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-67890<Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUser>  
          </ClearVisibleProjectsForUserList>  
        </tyo:ParametersForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
#### Esimerkki henkilönumerolla
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForClearVisibleProjectsForUserV2>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan, mutta on jätetty pois tästä esimerkistä -->  
          <ClearVisibleProjectsForUserList>  
            <ClearVisibleProjectForUser>  
              <PersonnelNumber>12345</PersonnelNumber>  
            </ClearVisibleProjectForUser>  
          </ClearVisibleProjectsForUserList>  
        </tyo:ParametersForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
### Esimerkkivastaus
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForClearVisibleProjectsForUserV2>  
          <ResponseCode>0</ResponseCode>  
          <ResponseString>No errors</ResponseString>  
          <ClearVisibleProjectsForUserResultList>  
            <ClearVisibleProjectForUserResult>  
              <ResponseCode>0</ResponseCode>  
              <ResponseString>No errors</ResponseString>  
              <UserId>1234</UserId>  
              <Username>matti.meikalainen</Username>  
              <PersonExternalIdentifier>  
                <Identifier>EXP-12345</Identifier>  
                <FieldName>ExternalIdentifier1</FieldName>  
              </PersonExternalIdentifier>  
            </ClearVisibleProjectForUserResult>  
          </ClearVisibleProjectsForUserResultList>  
        </tyo:ReturnValueForClearVisibleProjectsForUserV2>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
