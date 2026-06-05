---
id: 6899092915101
title: GetActivityTypes
url: https://support.nepton.com/hc/fi/articles/6899092915101-GetActivityTypes
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
edited_at: '2022-10-13T12:24:21Z'
---

# GetActivityTypes

## Rajapinnan yleiskuvaus
Verkkopalvelua käytetään tapahtumatyyppien noutamiseen neptonista.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Lähetettävät tiedot
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ParametersForGetActivityTypes | XML element | 1 | Juurielementti SOAP bodyn alla  
1 | CallerAuthentication | XML element |  | Tunnistautumistiedot (katso [Tunnistautuminen](<https://support.nepton.com/hc/articles/360019983978#CallerAuthentication>))  
1 | FilterByIds | XML element | 0..1 |  Suodatus tapahtumatyyppien nepton tunnisteiden perusteeella  
2 | Id | integer | 0..n | Yksittäinen tapahtumatyypin Nepton tunniste  
1 | FilterByInternalNames |  | 0..1 | Suodatus tapahtumatyyppien sisäisten nimien perusteella  
2 | InternalName | string | 0..n | Tapahtymatyypin sisäinen nimi  
### Kutsun esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForGetActivityTypes>  
          <CallerAuthentication / > <!-- Autentikoituminen vaaditaan mutta jätetty pois tästä esimerkistä. -->  
          <FilterByIds>  
            <Id>1</Id>  
          </FilterByIds>  
          <FilterByInternalNames>  
            <InternalName>work</InternalName>  
          </FilterByInternalNames>  
        </tyo:ParametersForGetActivityTypes>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
TASO | KENTÄN NIMI | MUOTO | ESIINTYMISKERRAT | SELITE  
---|---|---|---|---  
0 | ReturnValueForGetActivityTypes | XML element | 1 | Juurielementti SOAP bodyn alla  
1 | ResponseCode | integer | 1 | Numeerinen arvo, joka kuvaa pyynnön onnistumista tai epäonnistumista, katso [Vastauskoodit](<https://support.nepton.com/hc/articles/360019841477#ResponseCodes>)  
1 | ResponseString | string | 1 | Tekstikuvaus vastauksen onnistumisesta tai epäonnistumisen syystä  
1 | ActivityTypeList | XML element | 1 | Lista tapahtumatyypeistä  
2 | ActivityType | XML element | 0..n | Yksittäinen tapahtumatyyppi  
3 | Id | integer | 1 | Tapahtumatyypin Nepton tunniste  
3 | InternalName | string | 1 | tapahtumatyypin sisäinen nimi  
3 | TranslatedName | XML element | 0..n | Kielikohtaiset nimet tapahtumatyypille. Elementtien lukumäärä on sama kuin Neptonissa tuettujen kielten lukumäärä. Katso tuetut kielet ja niiden koodit [tästä](<https://support.nepton.com/hc/fi/articles/6904407712413>)  
4 | Locale | string | 1 | Käännetyssä nimessä käytetyn kielen koodi  
4 | Name | string | 1 | Tapahtumatyypin käännetty nimi  
3 | Code | string | 0..1 | Tapahtumatyypin koodi  
3 | Visible | boolean | 0..1 | true, jos tapahtumatyyppi näkyy Neptonissa, false, jos ei  
3 | CanAssignWorkIncrements | boolean | 0..1 |  Voiko tapahtumatyypille liittää korotuksia (true/false)  
3 | CanHaveRelatedProjects | boolean | 0..1 |  Voiko tapahtumatyypille liittää projekteja (true/false)  
3 | CategoryInternalName | string | 0..1 |  Tapahtumatyypin kategorian sisäinen nimi  
3 | TranslatedCategoryName | XML element | 0..n | Kielikohtaiset nimet tapahtumatyypin kategorioille. Elementtien lukumäärä on sama kuin Neptonissa tuettujen kielien lukumäärä. katso tuetut kielet ja niiden koodit tästä --todo--  
4 | Locale | string |  1 |  Nimessä käytetyn kielen koodi  
4 | Name | string |  1 |  Tapahtumatyypin kategorian nimi käännettynä   
3  | BeginDateTimeInput | string | 0..1 |  Aloitusajan asettamisen määritys. Mahdolliset arvot: | mandatory | pakollinen  
  
---|---  
optional | valinnainen  
  
disabled | poistettu käytöstä  
  
3 | EndDateTimeInput | string | 0..1 | Lopetusajan asettamisen määritys. Samat vaihtoehdot kuin BeginDateTimeInput elementillä  
### Vastauksen esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForGetActivityTypes>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors</ResponseString>  
          <ActivityTypeList>  
            <ActivityType>  
              <Id>1</Id>  
              <InternalName>work</InternalName>  
              <TranslatedName>  
                <Locale>fi_FI</Locale>  
                <Name>työ</Name>  
              </TranslatedName>  
              <TranslatedName>  
                <Locale>en_US</Locale>  
                <Name>work</Name>  
              </TranslatedName>  
              <Code>456/w</Code>  
              <Visible>true</Visible>  
              <CanAssignWorkIncrements>true</CanAssignWorkIncrements>  
              <CanHaveRelatedProjects>true</CanHaveRelatedProjects>  
              <CategoryInternalName>test</CategoryInternalName>  
              <TranslatedCategoryName>  
                <Locale>fi_FI</Locale>  
                <Name>testausta</Name>  
              </TranslatedCategoryName>  
              <TranslatedCategoryName>  
                <Locale>en_US</Locale>  
                <Name>testing</Name>  
              </TranslatedCategoryName>  
              <BeginDateTimeInput>mandatory</BeginDateTimeInput>  
              <EndDateTimeInput>optional</EndDateTimeInput>  
            </ActivityType>  
          </ActivityTypeList>  
        </tyo:ReturnValueForGetActivityTypes>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
