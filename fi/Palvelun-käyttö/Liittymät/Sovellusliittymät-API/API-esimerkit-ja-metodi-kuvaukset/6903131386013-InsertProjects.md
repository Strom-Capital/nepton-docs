---
id: 6903131386013
title: InsertProjects
url: https://support.nepton.com/hc/fi/articles/6903131386013-InsertProjects
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
edited_at: '2022-11-14T10:53:52Z'
---

# InsertProjects

## Rajapinnan yleiskuvaus  
Verkkopalvelua käytetään siihen, että kutsussa annettu lista projekteista lisätään Neptoniin.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla[ täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
0 | ParametersForInsertProjects | XML element |  | Juurielementti SOAP bodyn alla  
1 | CallerAuthentication | XML element |  | tunnistautumistiedot (katso [Tunnistautuminen](<https://support.nepton.com/hc/fi/articles/360019983978>))  
1 | ProjectList | XML element |  | Lisättävät projektit  
2 | Id | int | 0..1 | EI käytetä tässä käyttötapauksessa  
2 | Name | string | 1 | Projektin nimi  
2 | Code | string |  | Projektin koodi  
2 | Deleted | boolean |  | Onko projekti poistettu (true/false)  
2 | Active | boolean |  | Onko projekti aktiivinen (true/false)  
2 | TypeInternalName | string |  |  Sisäinen merkkijonotunnus (ei sen asiakaskohtainen nimi tai kielikäännös) Oletusarvoinen järjestelmän projektien sisäinen merkkijonotunnus on _project_work_  
2 | Description | string |  | Projektin kuvaus  
2 | StartDate | date |  | Projektin alkamispäivä  
2 | EndDate | date |  | Projektin päättymispäivä  
2 | ParentProjectId | int |  | Jos ollaan lisäämässä aliprojektia niin tämä määrittää ylätason projektin nepton tunnisteen perusteella.  
2 | ParentProjectCode | string |  | Voidaan käyttää ParentProjectID-elementin sijaan jos halutaan viitata ylätason projektiin sen koodin perusteella  
2 | Left | int |  | Ei käytetä tässä käyttötapauksessa.  
2 | Right | int |  | Ei käytetä tässä käyttötapauksessa  
## Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForInsertProjects>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan mutta ei näytetä tässä esimerkissä -->  
          <ProjectList>  
            <Project>  
              <Name>laskutettava työ asiakas 1</Name>  
              <Deleted>false</Deleted>  
              <Code>L/001</Code>  
              <TypeInternalName>lta1</TypeInternalName>  
              <Description>Asiakas 1:n laskutettavien tuntien kohdistaminen</Description>  
              <StartDate>2020-01-01</StartDate>  
              <EndDate>2024-01-01</EndDate>  
            </Project>  
          </ProjectList>  
        </tyo:ParametersForInsertProjects>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
0 | ReturnValueForInsertProjects | XML element | 1 | Juurielementti SOAP bodyn alla  
1 | ResponseCode | integer | 1 |   
1 | ResponseString | string | 1 | Tekstimuotoinen kuvaus pyynnön onnistumisesta tai epäonnistumisesta  
1 | ProjectInsertResultList | XML element | 1 |   
2 | ProjectInsertResult | XML element | 0..n | Yksittäisen projektin lisäyksen tulos  
3 | ResponseCode | int |  | Koodi, joka kuvaa tämän projektin lisäämisen tilaa. Katso [vastauskoodit](<https://support.nepton.com/hc/fi/articles/360019841477>)  
3 | ResponseString | string |  | Tekstimuotoinen kuvaus projektin lisäämisen tilasta  
3 | ProjectId | int |  | Lisätyn projektin yksilöllinen Nepton tunniste  
### Vastauksen esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForInsertProjects>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors</ResponseString>  
          <ProjectInsertResultList>  
            <ProjectInsertResult>  
              <ResponseCode>1000</ResponseCode>  
              <ResponseString>All clear no errors</ResponseString>  
              <ProjectId>1</ProjectId>  
            </ProjectInsertResult>  
          </ProjectInsertResultList>  
        </tyo:ReturnValueForInsertProjects>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
