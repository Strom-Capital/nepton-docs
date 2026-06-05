---
id: 6881855535773
title: RunIntegrationRuleset
url: https://support.nepton.com/hc/en-gb/articles/6881855535773-RunIntegrationRuleset
locale: en-gb
category: Support
category_id: 360000446658
section: Example APIs and method descriptions
section_id: 4410135708433
section_path:
- Integration
- API
- Example APIs and method descriptions
labels: []
promoted: false
updated_at: '2026-06-01T14:44:17Z'
edited_at: '2022-09-28T12:03:06Z'
---

# RunIntegrationRuleset

This article has not been translated yet.
Tästä metodista on uudempi versio. Mikäli käytät jo tätä metodia, niin suosittelemme, että tarkastelet seuraavan version ohjeesta, mitä muutoksia vaaditaan uuden version käyttöönottamiseksi. Seuraavan version ohjeen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360014449458>)
## Rajapinnan yleiskuvaus
Nepton tarjoaa SOAP-verkkopalvelun sääntöjoukon ajamiselle. Ajamista varten tarvitsee määrittää sääntöjoukko. Voit lukea lisää sääntöjoukoista [täällä](<https://support.nepton.com/hc/fi/articles/360002492278>) ja sääntöjoukon poiminnan ohje löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>). 
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin. 
## Rajoitukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa
  * Aineiston voi pyytää maksimissaan kahden vuoden aikajaksolle
  * Aineiston muodostamisessa voi kestää kymmeniä minuutteja riippuen pyydetyn aineiston koosta. Asiakassovelluksen aikakatkaisulle kannattaa antaa korkea arvo. Aineiston muodostusajan voi tarkistaa muodostamalla aineiston käyttöliittymän kautta. Lisää siitä [täällä](<https://support.nepton.com/hc/fi/articles/360002492898>).


## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForRunIntegrationRuleset | XML-elementti | 1 |   
1 | CallerAuthentication | XML-elementti | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | IntegrationRulesetName | merkkijono | 1 | Sääntöjoukon nimi  
1 | FilterPeriodBeginDate | päivämäärä | 1 | Haettavan ajanjakson alkupäivä. Muoto `VVVV-KK-PP`  
1 | FilterPeriodEndDate | päivämäärä | 1 | Haettavan ajanjakson loppupäivä. Muoto `VVVV-KK-PP`  
### Kyselyn esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForRunIntegrationRuleset>  
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->  
          <IntegrationRulesetName>?</IntegrationRulesetName>  
          <FilterPeriodBeginDate>?</FilterPeriodBeginDate>  
          <FilterPeriodEndDate>?</FilterPeriodEndDate>  
          <ReturnFormat>formatDefinedInRulesetSettings</ReturnFormat>  
        </tyo:ParametersForRunIntegrationRuleset>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForRunIntegrationRuleset | XML-elementti | 1 |   
1 | ResponseCode | kokonaisluku | 1 | Lähetettyjen tietojen käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | merkkijono | 1 | Koodin kuvaus  
1 | Output | merkkijono | 0..1 |  Pyydetyn aineiston sisältö. Sisältö on siinä tiedostomuodossa, joka sääntöjoukolle on asetuksissa määritetty Jos aineisto ei ole tekstiä, se on base64 koodattuna. Tämä tapauksissa jolloin:
  * Aineisto on jaettu useaan tiedostoon. Sisältönä on base64 koodattu ZIP-tiedosto. Aineiston jakamisesta useaan tiedostoon voi lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/360006255458>).
  * Aineiston tiedostomuoto ei ole tekstiä. Tämä esimerkiksi Swgi-muodossa, jolloin sisältönä on base64 koodattu XLSX-tiedosto.

  
### Vastauksen esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForRunIntegrationRuleset>  
          <ResponseCode>1000</ResponseCode>  
          <ResponseString>All clear. No errors.</ResponseString>  
          <Output>909;Käyttäjä Admin;2016-05-12;2016-05-12;8.00;100;;Year leave;;;;;;;;;&#13;  
    909;Käyttäjä Admin;2016-05-10;2016-05-10;7.15;990;;Training;;;;;;;;;&#13;  
    909;Käyttäjä Admin;2016-05-11;2016-05-11;9.15;999;;Work;;;;;;;;;</Output>  
        </tyo:ReturnValueForRunIntegrationRuleset>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
