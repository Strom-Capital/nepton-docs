---
id: 4406446686609
title: Henkilötietojen sovellusliittymien vastausviestit ja -koodit
url: https://support.nepton.com/hc/fi/articles/4406446686609-Henkil%C3%B6tietojen-sovellusliittymien-vastausviestit-ja-koodit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen API
section_id: 4406143245713
section_path:
- Liittymät
- Sovellusliittymät (API)
- Henkilötietojen API
labels:
- response code
- Vastauskoodi
promoted: false
updated_at: '2025-09-08T07:36:13Z'
edited_at: '2024-06-20T07:22:51Z'
---

# Henkilötietojen sovellusliittymien vastausviestit ja -koodit

Tässä artikkelissa kuvataan HR API:n vastauksia ja tietoa eri tuloskoodeista ja niiden merkityksestä.
Vastaukset tehdään XML SOAPilla. Alla on esimerkki vastauksesta ja solmujen yksityiskohtainen erittely. Huomaa, että FunctionResponse ja FunctionResult korvataan todellisilla funktioiden nimillä.
## Esimerkkivastaus XML
[code] 
    <soap:Envelope xmlns:soap="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>" xmlns:xsd="<http://www.w3.org/2001/XMLSchema>">  
      <soap:Body>  
         <FunctionResponse xmlns="<http://tempuri.org/>">  
            <FunctionResult>  
               <ResultCode>8</ResultCode>  
               <ResultMessage>Failure. Please see breakdown for more details.</ResultMessage>  
               <ResultBreakdown>  
                  <ArrayOfString>  
                     <string>ERROR: Tuontikenttää 'TEST_HEADER_001' ei tunnistettu</string>  
                     <string>ERROR: Tuontikenttää 'TEST_HEADER_002' ei tunnistettu</string>  
                  </ArrayOfString>  
               </ResultBreakdown>  
            </FunctionResult>  
         </FunctionResponse>  
      </soap:Body>  
    </soap:Envelope>
[/code]
## Vastauksen erittely
**Solmu** |  **Valinnainen  
** |  **Kuvaus**  
---|---|---  
ResultCode |  Ei |  Tämä koodi osoittaa tuontitoiminnon kokonaistuloksen. Kaikki muut koodit kuin 1000 tarkoittavat, että on havaittu ongelma. Katso alla olevasta Tuloskoodit -kohdasta lisätietoja tiettyjen koodien merkityksistä.  
ResultMessage |  Ei |  Tämä on selkokielinen viesti tuontitoiminnan kokonaistuloksesta, joka on ensisijaisesti tarkoitettu virheenkorjaukseen.  
ResultBreakdown |  Ei |  Säiliö havaittujen ongelmien tai varoitusten selvittämiseen.  
ArrayOfString |  Kyllä |  Eritelty lista havaituista ongelmista tai varoituksista. Jos ongelmia ei ole havaittu, tämä solmu ei välttämättä sisälly vastaukseen.  
string |  Kyllä |  Jokainen ArrayOfString-solmu voi sisältää kokoelman merkkijonosolmuja. Jokainen näistä osoittaa tuonti-indeksiin liittyvän virheen tai varoituksen.  
## Vastauskoodit (Result Codes)
Alla on tuloskoodit, jotka palautetaan ResultCode-kenttään. Vastauskoodi "1000" tarkoittaa täydellistä onnistumista. Mikä tahansa muu arvo (myös tyhjä) ilmaisee ongelman, joka tulee tutkia Neptonin palvelulokin ja pyynnön tekevän ohjelmiston lokien avulla. Virhekoodien 1 - 10 tapauksessa voidaan olettaa että kutsu epäonnistui, eikä haluttua toiminnetta suoritettu edes osittain (esim. yhtäkään henkilöä ei tuotu). 
**Vastaus- koodi** |  **Vastauksen tyyppi** |  **Kuvaus**  
---|---|---  
1000 |  Onnistunut |  Ei virheitä.  
998 |  Varoitus |  Tulos oli tyhjä. Useimmissa tapauksissa tätä voidaan pitää virheenä.  
999 |  Virhe |  Odottamaton tai tuntematon virhe. Tämä tarkoittaa yleensä käsittelemättömän poikkeuksen havaitsemista.  
1 |  Virhe |  Virheellinen salasana  
2 |  Virhe |  Virheellinen työyhteisön Id  
3 |  Virhe |  Pääsy estetty  
4 |  Virhe |  Virheelliset parametrit. Yksi tai useampi parametreista oli huonosti muotoiltu, virheellinen tai puuttui.  
5 |  Virhe |  Ei tueta. Yleinen, kohdetta ei tueta -vastaus. Tarkista lisätiedot erittelystä, jos saatavilla.  
6 |  Virhe |  Ei löydetty. Yleinen, kohdetta ei löydy -vastaus. Tarkista lisätiedot erittelystä, jos saatavilla.  
7 |  Virhe |  Työyhteisön asetuksia ei löydy. Tämä tarkoittaa yleensä huonosti määriteltyä työyhteisöä.  
8 |  Virhe |  Kokoelma sisältää virheitä. Kokoelmassa havaittiin yksi tai useampi virhe.  
9 |  Virhe |  Koodausvirhe.  
10 |  Virhe |  Ei tunnistettu. Yleinen, kohdetta ei tunnistettu -vastaus. Tarkista lisätiedot erittelystä, jos saatavilla.
