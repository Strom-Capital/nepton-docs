---
id: 36513332931869
title: RunIntegrationRulesetV3
url: https://support.nepton.com/hc/fi/articles/36513332931869-RunIntegrationRulesetV3
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
updated_at: '2026-06-01T14:54:30Z'
edited_at: '2026-06-01T14:14:41Z'
---

# RunIntegrationRulesetV3

## Rajapinnan yleiskuvaus  
Nepton tarjoaa SOAP-verkkopalvelun sääntöjoukon ajamiselle. Ajamista varten tarvitsee määrittää sääntöjoukko. Voit lukea lisää sääntöjoukoista [täällä](<https://support.nepton.com/hc/fi/articles/360002492278>) ja sääntöjoukon poiminnan ohje löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin. 
## Muutokset aiempaan versioon nähden([RunIntegrationRulesetV2](<https://support.nepton.com/hc/fi/articles/360014449458>))
### Rakenteelliset muutokset
**Vanha** | **Uusi** | **Lisätiedot**  
---|---|---
[code] 
    <tyo:ParametersForRunIntegrationRulesetV2>
      ...
    </tyo:ParametersForRunIntegrationRulesetV2>
[/code]  
| 
[code]
    <tyo:ParametersForRunIntegrationRulesetV3>
    ...
    </tyo:ParametersForRunIntegrationRulesetV3>
[/code]
| Juurielementin nimi kutsussa muuttunut
[code] 
    <tyo:ReturnValueForRunIntegrationRuleset>
      ...
    </tyo:ReturnValueForRunIntegrationRuleset
[/code]  
| 
[code]
    <tyo:ReturnValueForRunIntegrationRulesetV3>
    ...
    </tyo:ReturnValueForRunIntegrationRulesetV3>
[/code]
| Juurielementin nimi vastauksessa muuttunut  
### Uudet ominaisuudet ja elementit
  * Mahdollista suodattaa henkilöitä henkilöiden ulkoisilla tunnisteilla
    * Lisätty PersonExternalIdentifier-elementti kutsuun
    * PersonExternalIdentifier sisältää Identifier- ja FieldName-kentät


## Rajoitukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa
  * Aineiston voi pyytää maksimissaan kahden vuoden aikajaksolle
  * Aineiston muodostamisessa voi kestää kymmeniä minuutteja riippuen pyydetyn aineiston koosta. Asiakassovelluksen aikakatkaisulle kannattaa antaa korkea arvo. Aineiston muodostusajan voi tarkistaa muodostamalla aineiston käyttöliittymän kautta. Lisää siitä [täällä](<https://support.nepton.com/hc/fi/articles/360002492898>).


## Lähetettävät tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForRunIntegrationRulesetV3 | XML-elementti | 1 |   
1 | CallerAuthentication | XML-elementti | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | IntegrationRulesetName | merkkijono | 1 | Sääntöjoukon nimi  
1 | FilterPeriodBeginDate | päivämäärä | 1 | Haettavan ajanjakson alkupäivä. Muoto `VVVV-KK-PP`  
1 | FilterPeriodEndDate | päivämäärä | 1 | Haettavan ajanjakson loppupäivä. Muoto `VVVV-KK-PP`  
1 | FilterByUsers | XML-elementti | 0..1 |  Henkilöt, joille sääntöjoukko ajetaan. Jos henkilörajausta ei anneta, sääntöjoukko ajetaan kaikille työympäristön henkilöille. Eri henkilötunnisteita voi käyttää yhdessä kyselyssä, esimerkiksi jos osalla henkilöistä tiedetään vain henkilönumero ja osalla vain henkilötunniste.  
2 | UserId | kokonaisluku | 0..n | Henkilön palvelun sisäinen tunniste  
2 | Username | merkkijono | 0..n | Henkilön käyttäjätunnus  
2 | PersonnelNumber | merkkijono | 0..n | Henkilön henkilönumero  
2 | PersonExternalIdentifier | XML-elementti | 0..n | Henkilöiden ulkoiset tunnisteet  
3 | Identifier | merkkijono | 1 | Henkilön ulkoisen tunnisteen arvo  
3 | FieldName | merkkijono | 1 | Henkilön ulkoisen tunnisteen kenttänimi  
2 | SocialSecurityNumber | merkkijono | 0..n | Henkilön henkilötunnus  
1 | ReturnFormat | merkkijono | 0..1 |  Tiedostomuoto, jos ei annettu tai arvona on `formatDefinedInRulesetSettings`, käytetään sääntöjoukon asetusta "Viennin tiedostomuoto". [Katso tuetut tiedostomuodot tästä](<https://support.nepton.com/hc/fi/articles/15468480461085>)  
### Kyselyn esimerkki
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForRunIntegrationRulesetV3>
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <IntegrationRulesetName>?</IntegrationRulesetName>
          <FilterPeriodBeginDate>?</FilterPeriodBeginDate>
          <FilterPeriodEndDate>?</FilterPeriodEndDate>
          <FilterByUsers> <!-- Kaikki 4 henkilöä palautetaan, 2 vastaavuutta käyttäjätunnuksille ja 2 vastaavuutta henkilönumeroille -->
            <Username>Matti Meikäläinen</Username>
            <Username>Maija Mehiläinen</Username>
            <PersonnelNumber>9001</PersonnelNumber>
            <PersonnelNumber>9002</PersonnelNumber>
            <PersonExternalIdentifier>
              <Identifier>EMP-12345</Identifier>
              <FieldName>ExternalIdentifier1</FieldName>
            </PersonExternalIdentifier>
            <PersonExternalIdentifier>
              <Identifier>EMP-67890</Identifier>
              <FieldName>ExternalIdentifier1</FieldName>
            </PersonExternalIdentifier>
          </FilterByUsers>
          <ReturnFormat>formatDefinedInRulesetSettings</ReturnFormat>
        </tyo:ParametersForRunIntegrationRulesetV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Vastaus
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForRunIntegrationRulesetV3 | XML-elementti | 1 |   
1 | ResponseCode | kokonaisluku | 1 | Lähetettyjen tietojen käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | ResponseString | merkkijono | 1 | Koodin kuvaus  
1 | Output | merkkijono | 0..1 |  Pyydetyn aineiston sisältö. Jos aineisto ei ole tekstiä, se on base64 koodattuna. Tämä tapauksissa jolloin:
  * Aineisto on jaettu useaan tiedostoon. Sisältönä on base64 koodattu ZIP-tiedosto. Aineiston jakamisesta useaan tiedostoon voi lukea lisää [täältä](<https://support.nepton.com/hc/fi/articles/360006255458>).
  * Aineiston tiedostomuoto ei ole tekstiä. Tämä esimerkiksi Swgi-muodossa, jolloin sisältönä on base64 koodattu XLSX-tiedosto.

  
### Vastauksen esimerkki
[code]
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ReturnValueForRunIntegrationRulesetV3>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <Output>909;Käyttäjä Admin;2016-05-12;2016-05-12;8.00;100;;Year leave;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-10;2016-05-10;7.15;990;;Training;;;;;;;;;&#13;
    909;Käyttäjä Admin;2016-05-11;2016-05-11;9.15;999;;Work;;;;;;;;;</Output>
        </tyo:ReturnValueForRunIntegrationRulesetV3>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
