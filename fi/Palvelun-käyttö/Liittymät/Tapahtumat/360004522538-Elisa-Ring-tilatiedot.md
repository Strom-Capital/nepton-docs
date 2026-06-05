---
id: 360004522538
title: Elisa Ring tilatiedot
url: https://support.nepton.com/hc/fi/articles/360004522538-Elisa-Ring-tilatiedot
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
updated_at: '2024-08-23T09:33:03Z'
edited_at: '2023-09-11T12:07:24Z'
---

# Elisa Ring tilatiedot

Palvelusta voidaan lähettää henkilöiden tilatiedot Elisan kulunvalvontapalveluun. Tilatietoja käytetään hyväksi Elisa Ring -puhelinjärjestelmässä, esimerkiksi ohjaamalla saapuvat puhelut paikalla oleville henkilölle. Liittymä ja sen käyttöönotto on vakioitu.
## Kuvaus liittymän toiminnasta
Kun liittymä on määritelty käyttöön, Nepton lähettää tilatiedot koko henkilöstöstä Elisa Ringiin. Liittymä siirtää tietoa kerran minuutissa ja mikäli henkilöllä on alkanut tai päättynyt tapahtuma Neptonissa, niin henkilön uusi tila siirretään Elisa Ringiin. Esimerkiksi jos henkilö on työssä ja on kirjannut koulutuksen alkamaan 11:00 niin tällä ajankohdalla Elisa Ringiin siirretään tieto siitä että henkilön tila on koulutuksessa.
Liittymä siirtää jokaiselle henkilölle tilatiedon siten, että henkilön tilaa kuvaa koodi. Koodit määritellään Neptonin käyttöliittymässä ja siirretään sellaisenaan Elisa Ringiin. Eri tapahtumatyypit voivat jakaa saman koodin. Esimerkiksi sairauslomat voidaan siirtää poissaolo-koodilla, jotta ei välitetä sellaista henkilöön liittyvää tietoa, jota Elisa Ringissä ei hyödynnetä.
## Elisa Ring liittymän käyttöönotto
Liittymän käyttöönotto tehdään seuraavalla tavalla.
### 1\. Määrittele henkilöiden tunnisteet
Henkilöiden Elisa Ring -tunnisteet määritetään muokkaamalla henkilötietoja **Työsuhde** \- **Henkilön tiedot** \- **Tunnisteet**. Mikäli Elisa Ring tunnusta ei määritetä käytetään siirrossa henkilön henkilönumeroa. Tunnisteet voidaan päivittää myös massana palveluun käyttäen [henkilöiden tuonnin](<https://support.nepton.com/hc/fi/articles/360003762577>) toiminnallisuuksia.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/21078310177437)
### 2\. Määrittele tapahtumatyyppien koodit
Tapahtumatyyppien koodit määritetään työyhteisön asetuksista, **Työaika** \- **Hallinta** \- **Työyhteisön asetukset** \- **Liittymät** \- **Elisa Ring (eIP Kulva)**
![mceclip7.png](https://support.nepton.com/hc/article_attachments/21078310185501)
Määritettävät koodit ovat ne, mitä Elisa Ring -järjestelmään siirretään ja niiden tulee vastata Elisa Ringin liittymään määritettyjä koodeja. Usealle tapahtumatyypille on mahdollista asettaa sama koodi.
Koodi määritetään myös sille, kun henkilöllä ei ole meneillään olevaa tapahtumaa. Tämä koodi lähetetään liittymällä silloin kun henkilöllä ei ole meneillään olevaa tapahtumaa.
![mceclip6.png](https://support.nepton.com/hc/article_attachments/21078310180893)
### 3\. Määrittele liittymän asetukset 
Liittymän siirto aktivoituu, kun Neptoniin määritellään alla olevat asetukset. Nämä määritellään työyhteisön asetuksista, **Työaika** -**Hallinta** -**Työyhteisön asetukset** -**Liittymät** -**Elisa Ring (eIP Kulva)** \- **Kokoonpano**
![mceclip2.png](https://support.nepton.com/hc/article_attachments/21078297927965)
  * Elisan integraatiopalvelut toimittaa seuraavat tiedot, jotka tulee asettaa Neptoniin: 
    * Web servicen päätepiste
    * Web servicen käyttäjätunnus
    * Web servicen salasana
    * asiakastunniste
  * Laitetunniste on informatiivinen tieto, joka esitetään Elisa Ringissä. Tällä tiedolla vaihteenhoitaja tietää mistä palvelusta tilatieto on siirretty. Tähän määritetään arvo 'NEPTON'
  * Lähetettävien tilapäivityksien maksimimäärään ei tehdä muutoksia. Asetus on käyttöliittymässä sellaisia tilanteita varten, että teknisistä syistä liittymän siirtonopeutta tulee rajata. Esimerkiksi vanhemmat puhelinvaihteen tietoliikennelaitteet voivat aiheuttaa rajoitteita.


## 
## Liittymän tekninen toiminta
## Rajaukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa


## Autentikaatio
Lähetettävä sanoma autentikoidaan NTLM protokollalla. Web service käyttäjätunnus ja salasana lähetetään kutsun headerissa arvolla 10005. PHP konekielisenä muuttujana (PHP) tähän viitataan CULROPT_USERPWD nimellä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360020687218)
## Lähtösanoma
Muuttuneet tilatiedot lähetetään minuutin välein. Lähetettävät tiedot ovat kuvattu alla. Liittymä on vakioitu eikä tietosisältöön ole tarvetta tehdä muutoksia.
Taso | Kentän nimi | Formaatti | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | Stamps | XML element | 1 |   
1 | entries | XML element | 0..1 |   
2 | Entry | XML element | 0..n | Yhden henkilön uusi tilatieto  
3 | Identity | XML element | 1 |   
4 | ClientId | string | 1 | Tietojen lähetysasetuksissa määritetty asiakastunniste  
4 | DeviceId | string | 1 | Tietojen lähetysasetuksissa määritetty laitetunniste  
3 | CardId | string | 1 | Henkilön Elisa Ring -tunnus / henkilönumero  
3 | ReasonCode | string | 1 | Elisa Ring asetuksissa määritetty tapahtumatyypin koodi  
3 | OccurredTime | datetime | 1 | Aika milloin henkilön tilatieto on muuttunut. Formaatti: `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
3 | EndTime | datetime | 0..1 | Jos on etukäteen tiedossa, mihin asti tietty tila on voimassa (esimerkiksi paikalla, eli töissä), päättymisaika lähetetään. Formaatti: `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
Kyselyn esimerkki:
[code] 
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
      <s:Body>  
        <Stamps xmlns="http://www.elisa.fi/kulva">  
          <entries xmlns:a="http://schemas.datacontract.org/2004/07/KulvaWCF" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">  
            <a:Entry>  
              <a:Identity>  
                <a:ClientId>F9E2348B-C20E-4A0E-B2D5-725DC34B9230</a:ClientId>  
                <a:DeviceId>NEPTON</a:DeviceId>  
              </a:Identity>  
              <a:CardId>2222</a:CardId>  
              <a:ReasonCode>1</a:ReasonCode>  
              <a:OccurredTime>2015-04-15T18:11:26+03:00</a:OccurredTime>  
              <a:EndTime i:nil="true"/>  
            </a:Entry>  
            <a:Entry>  
              <a:Identity>  
                <a:ClientId>F9E2348B-C20E-4A0E-B2D5-725DC34B9230</a:ClientId>  
                <a:DeviceId>NEPTON</a:DeviceId>  
              </a:Identity>  
              <a:CardId>1111</a:CardId>  
              <a:ReasonCode>5</a:ReasonCode>  
              <a:OccurredTime>2015-04-15T18:11:26+03:00</a:OccurredTime>  
              <a:EndTime>2015-04-15T20:11:26+03:00</a:EndTime>  
            </a:Entry>  
          </entries>  
        </Stamps>  
      </s:Body>  
    </s:Envelope
[/code]
## Paluusanoma
Liittymä odottaa suoraa vastausta paluusanomana. Paluusanoman muoto on seuraava:
Taso | Kentän nimi | Formaatti | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | StampsResponse | XML element | 1 |   
1 | StampsResult | XML element | 0..1 |   
2 | GenericResult | XML element | 0..n | Yhden henkilön tilatiedon päivityksen tulos  
3 | DeviceId | string | 1 | Lähetetty laitetunniste  
3 | CardId | string | 1 | Lähetetty henkilön Elisa Ring -tunnus / henkilönumero  
3 | Code | integer | 1 | Paluukoodi 
  * 0 = OK
  * 1 = ClientId puuttuu
  * 2 = DeviceId puuttuu
  * 3 = CardId puuttuu
  * 4 = ReasonCode puuttuu
  * 10 = Tallennus epäonnistui

  
3 | Message | string | 1 | Tarkempi selitys tapahtumalle  
Sanoman esimerkki:
[code] 
    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">  
      <s:Body>  
        <StampsResponse xmlns="http://www.elisa.fi/kulva">  
          <StampsResult xmlns:a="http://schemas.datacontract.org/2004/07/KulvaWCF" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">  
            <a:GenericResult>  
              <a:DeviceId>NEPTON</a:DeviceId>  
              <a:CardId>2222</a:CardId>  
              <a:Code>0</a:Code>  
              <a:Message>OK</a:Message>  
            </a:GenericResult>  
            <a:GenericResult>  
              <a:DeviceId>NEPTON</a:DeviceId>  
              <a:CardId>1111</a:CardId>  
              <a:Code>0</a:Code>  
              <a:Message>OK</a:Message>  
            </a:GenericResult>  
          </StampsResult>  
        </StampsResponse>  
      </s:Body>  
    </s:Envelope>
[/code]
