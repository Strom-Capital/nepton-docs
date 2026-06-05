---
id: 360008827678
title: Titania noutaa tapahtumia
url: https://support.nepton.com/hc/fi/articles/360008827678-Titania-noutaa-tapahtumia
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2026-03-04T13:14:53Z'
edited_at: '2026-03-04T13:14:53Z'
---

# Titania noutaa tapahtumia

Titania työvuorosuunnittelu on kehitetty työvuorojen systemaattiseen suunnitteluun ja seurantaan. Neptoniin merkityt tapahtumat voidaan määritellä siirrettäväksi Titaniaan. Siirrossa käytetään SOAP web services -rajapintaa, jonka tarkempi kuvaus on nähtävissä [täältä.](<https://support.nepton.com/hc/fi/articles/360004861558>)
Jos Nepton-ympäristössä on asetettu IP-rajoituksia Työsuhde > Hallinta > Turvallisuus > Salli kutsut Nepton API web service rajapintaan vain alla listatuissa IP-osoitteissa -asetuksessa, tällöin tulee olla tietoja hakevalle IP-osoitteelle annettu pääsy.
## Tapahtumien vientimuoto
Titania käsittelee työtapahtumia erilailla kuin Nepton. Neptonissa tapahtumat ovat tietyllä tapahtumatyypillä ja niillä on alku- ja loppuaika. Titaniassa tapahtumat ovat joko aloitus- tai lopetustapahtumia yhdellä ajalla.
Nepton tekee tätä varten muunnoksia. Esimerkiksi seuraavat Neptoniin kirjatut tapahtumat:
  * 08:00 - 13:00 Työ
  * 13:00 - 14:00 Koulutus
  * 14:00 - 16:00 Työ


Muutetaan seuraavaan muotoon, jonka Titania ymmärtää:
  * 08:00 Aloitus (ei syykoodia)
  * 13:00 Lopetus (koulutus)
  * 14:00 Aloitus (ei syykoodia)
  * 16:00 Lopetus (ei syykoodia)


## Määrittäminen
### Henkilöiden tunnusten määrittäminen
Titania käyttää henkilön tunnisteena joko henkilönumeroa tai henkilötunnusta, sekä joissain tapauksissa molempia.
Henkilön henkilönumero voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot -näkymässä, Tunnisteet -osiossa.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/13489634047133)
Henkilöiden henkilötunnukset voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot -näkymässä.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/13489634053533)
### Tapahtumatyyppien koodien ja käyttäytymisen määrittäminen
Nämä voidaan määritellä Titanian asetuksista: Työaika -> Hallinta -> Työyhteisön asetukset -> Liittymät -> Titania.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360008594917)
Kaikille tapahtumatyypeille voi määrittää seuraavat tiedot:
  * **Tapahtumatyypin syykoodi** \- Titania käyttää tätä tunnistamaan, mistä tapahtumasta on kyse
  * **Käsittele tapahtumatyyppi** \- Onko tapahtumatyypillä kirjattu tapahtuman alku joko sisään (aloitus) vai ulos (lopetus) leimaus. Asetuksen alla kerrotaan, mikä on tapahtumatyypin oletuskäsittelytapa, jos asetusta ei ole asetettu.
  * **Käsittele tapahtumatyyppi ylityönä** \- Onko tapahtuma ylityötä vai ei. Ylitöiden kirjauksesta enemmän alla olevissa esimerkeissä. Tämä asetus on asetettavissa vain työtä vastaaville tapahtumille, sitä ei esimerkiksi voi asettaa poissaoloille.


Oletuksena kaikki tapahtumatyypit viedään, vaikka niille ei olisi määritetty syykoodia. Jos halutaan, että tiettyä tapahtumatyyppiä ei viedä, sen syykoodiksi määritetään 0.
### Viennin asetukset
**Vientitiedoston nimi** -kenttää ei ole tarve määritellä koska kyseessä on SOAP-kutsu Neptoniin.
## Tapahtumatyyppien määritys- ja käyttöesimerkkejä
### Koulutus
Titaniassa koulutus on leimausten kannalta poissaoloa perustehtävän mukaisesta työstä. Koulutukseen mentäessä kesken työpäivän leimataan aina lopetus (koulutus).
Neptonissa koulutus saadaan määritettyä seuraavalla tavalla:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/360008675078)
### Ylityömääräys
Titaniassa ylityömääräys on joko aamulla tai illalla tehtyä ylityötä, sekä voi olla myös molempia. Jos henkilö tekee aamulla ylityötä, Titaniassa päivä aloitetaan "_aloitus (ylityö)"_ leimauksella. Erillistä leimausta ei tehdä, kun ylityö päättyy ja normaali työ alkaa. Sama toimintaperiaate on myös illalla. Erillistä ylityön aloitusta ei leimata, vaan työt päättyvät "_lopetus (ylityö)"_ leimaukseen.
Neptonissa tämä saadaan aikaseksi perustamalla oma "Ylityö" tapahtumatyyppi ja antamalla sille seuraavat asetukset:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360008675058)
Aamun ylityö kirjattaisiin Neptoniin seuraavasti:
  * 06:30 - 08:00 Ylityö
  * 08:00 - 16:00 Työ


Jolloin titaniaan siirtyvät seuraavat leimaukset:
  * 06:30 Aloitus (YT)
  * 16:00 Lopetus (ei syykoodia)


Illan / iltapäivän ylityö kirjattaisiin Neptoniin seuraavasti:
  * 08:00 - 16:00 Työ
  * 16:00 - 18:00 Ylityö


Jolloin titaniaan siirtyvät seuraavat leimaukset:
  * 08:00 Aloitus (ei syykoodia)
  * 18:00 Lopetus (YT)


### Käyttöesimerkkejä
Käyttötapaus | Tapahtumat Neptonissa | Titaniaan siirrettävät leimaukset  
---|---|---  
Normaali työvuoro, koulutus keskellä päivää | 
  * 08:00 - 13:00 Työ
  * 13:00 - 14:00 Koulutus
  * 14:00 - 16:00 Työ

|  Huom! Koulutuksen syykodiksi asetettuna `KO`
  * 08:00 Aloitus
  * 13:00 Lopetus (KO)
  * 14:00 Aloitus
  * 16:00 Lopetus

  
Oma asia vuoron lopussa | 
  * 08:00 - 16:00 Työ
  * 14:00 - 16:00 Oma asia

|  Huom! Oma asian syykoodiksi asetettuna `OA`
  * 08:00 Aloitus
  * 14:00 Lopetus (OA)

  
Oma asia vuoron alussa | 
  * 08:00 - 10:00 Oma asia
  * 10:00 - 16:00 Työ

|  Huom! Oma asian syykoodiksi asetettuna `OA`
  * 10:00 Aloitus (OA)
  * 16:00 Lopetus

  
Oma asia vuoron alussa ja lopussa | 
  * 08:00 - 10:00 Oma asia
  * 10:00 - 14:00 Työ
  * 14:00 - 16:00 Oma asia

|  Huom! Oma asian syykoodiksi asetettuna `OA`
  * 10:00 Aloitus (OA)
  * 14:00 Lopetus (OA)

  
Koko päivän kestävä oma asia | 
  * 08:00 - 16:00 Oma asia

|  Huom! Oma asian syykoodiksi asetettuna `OA`
  * 08:00 Lopetus (OA)

  
Ylityö vuoron lopussa | 
  * 08:00 - 16:00 Työ
  * 16:00 - 18:00 Ylityö

|  Huom! Ylityön syykoodiksi asetettuna `YT`
  * 08:00 Aloitus
  * 18:00 Lopetus (YT)

  
Ylityö vuoron alussa | 
  * 06:00 - 08:00 Ylityö
  * 08:00 - 16:00 Työ

|  Huom! Ylityön syykoodiksi asetettuna `YT`
  * 06:00 Aloitus (YT)
  * 16:00 Lopetus

  
Ylityö vuoron alussa ja lopussa | 
  * 06:00 - 08:00 Ylityö
  * 08:00 - 16:00 Työ
  * 16:00 - 18:00 Ylityö

|  Huom! Ylityön syykoodiksi asetettuna `YT`
  * 06:00 Aloitus (YT)
  * 18:00 Lopetus (YT)

  
**Yön yli kestävät työvuorot**
Käyttötapaus | Tapahtumat Neptonissa | Titaniaan siirrettävät leimaukset  
---|---|---  
Normaali työvuoro | 
  * Pv1 22:00 - Pv2 06:00 Työ

| 
  * Pv1 22:00 Aloitus
  * Pv1 24:00 Lopetus
  * Pv2 00:00 Aloitus
  * Pv2 06:00 Lopetus

  
Yön yli kestävä sairausloma vuoron lopussa | 
  * Pv1 22:00 - 23:30 Työ
  * Pv1 23:30 - Pv2 06:00 Sairausloma

|  Huom! Sairausloman syykoodiksi asetettuna `SA`
  * Pv1 22:00 Aloitus
  * Pv1 23:30 Lopetus (SA)

  
Yön yli kestävä sairausloma (lapsi sairas) vuoron alussa | 
  * Pv1 22:00 - Pv2 01:00 Lapsi sairas
  * Pv2 01:00 - 06:00 Työ

|  Huom! Sairausloman (lapsi sairas) syykoodiksi asetettuna `LS`
  * Pv2 01:00 Aloitus (LS)
  * Pv2 06:00 Lopetus

  
Yön yli kestävä ylityö vuoron lopussa | 
  * Pv1 14:00 - 22:00 Työ
  * Pv1 22:00 - Pv2 01:15 Ylityö

|  Huom! Ylityön syykoodiksi asetettuna `YT`
  * Pv1 14:00 Aloitus
  * Pv1 24:00 Lopetus (YT)
  * Pv2 00:00 Aloitus (YT)
  * Pv2 01:15 Lopetus (YT)

  
## Kyselyn tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ParametersForGetTitaniaWorkingTimeEvents | XML elementti | 1 |   
1 | CallerAuthentication | XML elementti | 1 | Lisää tietoa autentikoitumisesta [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).  
1 | organisation | XML elementti | 0..1 | Organisaation tiedot. Ei käytössä.  
2 | code | merkkijono | 1 | Organisaation koodi  
2 | name | merkkijono | 0..1 | Organisaation nimi  
1 | period | XML elementti | 1 | Aikaväli, miltä tapahtumat haetaan.  
2 | beginDate | päivämäärä | 1 | Aikavälin alkupäivä, muodossa `YYYYMMDD`  
2 | endDate | päivämäärä | 1 | Aikavälin loppupäivä, muodossa `YYYYMMDD`  
1 | schedulingUnit | XML elementti | 1..n | Aikataulutusyksikkö, käytössä Titaniassa, ei vaikutusta Neptoniin  
2 | code | merkkijono | 1 | Aikataulutusyksikön koodi, käytössä Titaniassa, ei vaikutusta Neptoniin  
2 | name | merkkijono | 0..1 | Aikataulutusyksikön nimi, käytössä Titaniassa, ei vaikutusta Neptoniin  
2 | person | XML elementti | 0..n | Aikataulutusyksikön henkilö, jolle tapahtumia haetaan.  
3 | SSN | merkkijono | 1 | Henkilön henkilötunnus. Voi olla tyhjä jos henkilöä haetaan henkilönumeron perusteella.  
3 | employeeId | merkkijono | 0..1 | Henkilön henkilönumero.  
3 | name | merkkijono | 0..1 | Henkilön nimi, ei käytössä.  
### Kyselyn esimerkki
[code]
    <?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">
      <soapenv:Header/>
      <soapenv:Body>
        <tyo:ParametersForGetTitaniaWorkingTimeEvents>
          <CallerAuthentication /> <!-- Autentikoituminen vaaditaan, mutta on jätetty tässä esimerkissä pois -->
          <period>
            <beginDate>20200501</beginDate>
            <endDate>20200531</endDate>
          </period>
          <schedulingUnit>
            <code>E1100</code>
            <name>Suunnittelupiste A</name>
            <person>
              <SSN/>
              <employeeId>9001</employeeId>
              <name>Yli Yhdeksän Tuhatta</name>
            </person>
            <person>
              <SSN>999999-9999</SSN>
            </person>
          </schedulingUnit>
        </tyo:ParametersForGetTitaniaWorkingTimeEvents>
      </soapenv:Body>
    </soapenv:Envelope>
[/code]
## Vastauksen tiedot
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | ReturnValueForGetTitaniaWorkingTimeEvents | XML elementti | 1 |   
1 | ResponseCode | numero | 1 |  Tietojen haun käsittelyn tuloksen koodi. Mahdolliset koodit löytyvät [täältä](<https://support.nepton.com/hc/fi/articles/360004861558>). Huomioithan sen, että koodia 1019 käytetään vain tapauksissa milloin yhtä tai useampaa kyselyssä ollutta henkilöä ei löytynyt.  
1 | ResponseString | merkkijono | 1 | Koodin kuvaus / viesti.  
1 | schedulingUnit | XML elementti | 1..n | Aikataulutusyksikkö. Vastauksessa listataan kyselyssä annetut aikatauluyksiköt.  
2 | code | merkkijono | 1 | Kyselyssä lähetetty aikataulutusyksikön koodi  
2 | name | merkkijono | 0..1 | Kyselyssä lähetetty aikataulutusyksikön nimi  
2 | person | XML elementti | 0..n | Aikataulutusyksikön henkilö, jonka tapahtumat listataan.  
3 | ResponseCode | numero | 1 | Koodina joko `1000` (kaikki kunnossa) tai `1003` (henkilöä ei löytynyt)  
3 | ResponseString | merkkijono | 1 | Koodin kuvaus.  
3 | SSN | merkkijono | 1 | Kyselyssä lähetetty henkilön henkilötunnus.  
3 | employeeId | merkkijono | 0..1 | Kyselyssä lähetetty henkilön henkilönumero.  
3 | name | merkkijono | 0..1 | Kyselyssä lähetetty henkilön nimi.  
3 | stampedWorkingTimeEvents | XML elementti | 1 | Henkilön työaikaleimaukset  
4 | event | XML elementti | 0..n | Työaikaleimaus  
5 | date | päivämäärä | 1 | Työaikaleimauksen päivämäärä, muodossa `YYYYMMDD`  
5 | beginTime | aika | 0..1 | Työaikaleimauksen alkuaika, käytetään vain sisään-leimauksille. Ajan muoto on `HHMM`. Työaikaleimauksella on vain joko alku tai loppuaika.  
5 | beginReasonCode | merkkijono | 0..1 | Aloitus-leimauksen syykoodi.  
5 | endTime | aika | 0..1 | Työaikaleimauksen loppuaika, käytetään vain ulos-leimauksille. Ajan muoto on `HHMM`. Työaikaleimauksella on vain joko alku tai loppuaika.  
5 | endReasonCode | merkkijono | 0..1 | Lopetus-leimauksen syykoodi.  
### Vastauksen esimerkki
[code]
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://tyoaika.tyoteho.fi">
      <SOAP-ENV:Body>
        <ns1:ReturnValueForGetTitaniaWorkingTimeEvents>
          <ResponseCode>1000</ResponseCode>
          <ResponseString>All clear. No errors.</ResponseString>
          <schedulingUnit>
            <code>E1100</code>
            <name>Suunnittelupiste A</name>
            <person>
              <ResponseCode>1000</ResponseCode>
              <ResponseString>All clear. No errors.</ResponseString>
              <SSN/>
              <employeeId>9001</employeeId>
              <name>Yli Yhdeksän Tuhatta</name>
              <stampedWorkingTimeEvents>
                <event>
                  <date>20200505</date>
                  <beginTime>0800</beginTime>
                </event>
                <event>
                  <date>20200505</date>
                  <endTime>2000</endTime>
                  <endReasonCode>YT</endReasonCode>
                </event>
              </stampedWorkingTimeEvents>
            </person>
            <person>
              <ResponseCode>1000</ResponseCode>
              <ResponseString>All clear. No errors.</ResponseString>
              <SSN>999999-9999</SSN>
              <stampedWorkingTimeEvents>
                <event>
                  <date>20200505</date>
                  <beginTime>0800</beginTime>
                </event>
                <event>
                  <date>20200505</date>
                  <endTime>1200</endTime>
                  <endReasonCode>KO</endReasonCode>
                </event>
              </stampedWorkingTimeEvents>
            </person>
          </schedulingUnit>
        </ns1:ReturnValueForGetTitaniaWorkingTimeEvents>
      </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>
[/code]
