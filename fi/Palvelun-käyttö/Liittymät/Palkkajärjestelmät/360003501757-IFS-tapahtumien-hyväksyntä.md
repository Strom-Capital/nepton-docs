---
id: 360003501757
title: IFS tapahtumien hyväksyntä
url: https://support.nepton.com/hc/fi/articles/360003501757-IFS-tapahtumien-hyv%C3%A4ksynt%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2024-05-08T11:29:03Z'
---

# IFS tapahtumien hyväksyntä

Nepton voidaan määrittää lähettämään tapahtumien hyväksynnät IFS-järjestelmään. Tiedot lähetetään, kun henkilöiden tapahtumia hyväksytään tai niiden hyväksyntää poistetaan. Hyväksyntää tai hyväksynnän poistoa ei tehdä, jos IFS ei palauta vastauksena, että hyväksynnän muutos onnistui.
Tietojen lähettämiseen vaaditaan IFS:n SOAP-verkkopalvelu (tai välijärjestelmä, kuten BizTalk). Tämän verkkopalvelun WSDL-skeema kuvataan alla.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden IFS-tunnukset voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/11562495151005)
HUOM.! Jos henkilön IFS-tunnusta ei ole asetettu, käytetään henkilönumeroa.
**2\. Tietojen lähettäminen**
Web servicen päätepisteen (minne hyväksynnät ja niiden poistot lähetetään) ja yrityksen tunnuksen / nimen määritys tapahtuu työyhteisön asetuksista, Työaika > Hallinta > Työyhteisön asetukset > Liittymät > IFS Tapahtumien hyväksyntä. Jos liittymässä käytetään API avaimella tunnistamista, se asetetaan myös samassa paikassa.
![](https://support.nepton.com/hc/article_attachments/11562367400861)
Web servicen päätepisteen ja API avaimen voi myös asettaa asetusryhmäkohtaisesti Työaika > Hallinta > Asetusryhmät > Asetusryhmä-valikko: Haluttu asetusryhmä > Toiminto-valikko: Asetusryhmän asetukset > Liittymät > IFS Tapahtumien hyväksyntä
## Rajoitukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa
  * Jos henkilön hyväksyntää tai sen poistoa ei saatu käsiteltyä vastaanottavassa päässä, sitä ei tehdä
  * Yksittäisten tapahtumien hyväksyntää ei tueta, koska sen sijaan lähetetään hyväksyttyjä / hyväksymättömiä päiviä. Voit poistaa yksittäisten tapahtumien hyväksynnän / hyväksynnän poiston käytöstä ottamalla "Hyväksy tapahtumat päivältä" -kohdan päälle työkaudella > Ylläpito > Työyhteisön asetukset > Työajat > Tapahtumien lukitseminen ja hyväksyminen.


## Viennin käynnistys
Vientiä ei ole aikataulutettu, mutta se käynnistetään reaaliajassa aina, kun käyttäjä hyväksyy tai hylkää tapahtumia. Vientiä ei käynnistetä yksittäisiä tapahtumia hyväksyttäessä.
## Lähetettävät tiedot
Taso | Kentän nimi | Sääntöjoukon kentän nimi | Formaatti | Esiintymiskerrat | Selite  
---|---|---|---|---|---  
Root,  
under SOAP body | AUTHORIZE_REPORT |  | XML element | 1 |   
1 | COMPANY |  | string (20) | 0..1 | Yrityksen tunnus / nimi. Annetaan IFS Tapahtumien hyväksynnän asetuksissa  
1 | EMP_ID | _Lisätään automaattisesti, ei korvattavissa_ | string (11) | 0..1 | Henkilön IFS-tunnus / henkilönumero  
1 | AUTHORIZE_TRANSACTIONS |  | XML element | 1 |   
2 | AUTHORIZE_TRANSACTION |  | XML element | 0..n |   
3 | START_DATE | StartDateTime | date | 1 | Hyväksynnän aikavälin alkupäivä, formaatti `YYYY-MM-DD`  
3 | END_DATE | EndDateTime | date | 0..1 | Hyväksynnän aikavälin loppupäivä, formaatti `YYYY-MM-DD`  
3 | STATE | If SalaryCode equals 'Approve' 1 is returned, otherwise 0 | string (1) | 1 | Hyväksynnän tila: 
  * 1 - hyväksytty
  * 0 - ei hyväksytty

  
3 | AUTH_ID | _Lisätään automaattisesti, ei korvattavissa_ | string (20) | 1 | Hyväksynnän tekijän IFS-tunnus / henkilönumero  
Kyselyn esimerkki:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wo="WO.fi.TyoTeho.Schemas.AuthorizationFromTyoTeho">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <wo:AUTHORIZE_REPORT>  
          <wo:COMPANY>CompanyID</wo:COMPANY>  
          <wo:EMP_ID>1230</wo:EMP_ID>  
          <wo:AUTHORIZE_TRANSACTIONS>  
            <wo:AUTHORIZE_TRANSACTION>  
              <wo:START_DATE>2019-06-01</wo:START_DATE>  
              <wo:END_DATE>2019-06-30</wo:END_DATE>  
              <wo:STATE>1</wo:STATE>  
              <wo:AUTH_ID>1240</wo:AUTH_ID>  
            </wo:AUTHORIZE_TRANSACTION>  
            <wo:AUTHORIZE_TRANSACTION>  
              <wo:START_DATE>2019-06-01</wo:START_DATE>  
              <wo:END_DATE>2019-06-30</wo:END_DATE>  
              <wo:STATE>1</wo:STATE>  
              <wo:AUTH_ID>1250</wo:AUTH_ID>  
            </wo:AUTHORIZE_TRANSACTION>  
          </wo:AUTHORIZE_TRANSACTIONS>  
        </wo:AUTHORIZE_REPORT>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Odotettu vastaus
Liittymä odottaa suoraa vastausta paluusanomana. Paluusanoman muoto on seuraava:
Taso | Kentän nimi | Formaatti | Esiintymiskerrat | Selite  
---|---|---|---|---  
Root,  
under SOAP body | Response | XML element | 1 |   
1 | Success | boolean | 1 | Saatiinko lähetetyt hyväksynnät tai hyväksynnän poistot käsiteltyä onnistuneesti vai ei  
1 | Message | string | 0..1 | Valinnainen viesti, käytetään virheviestin esittämiseen kun hyväksynnät / hyväksynnän poistoja ei saatu käsiteltyä.  
  
Jos hyväksynnät tai niiden poistoja saatiin käsiteltyä, viestissä odotetaan olevan niiden henkilöiden IFS-tunnukset / henkilönumerot, joiden hyväksyntä tai sen poisto onnistui. Henkilönumerot erotetaan toisistaan pilkulla.  
Sanoman esimerkki:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://WO.fi.TyoTeho.Schemas.TimeReportResponse">  
      <SOAP-ENV:Body>  
        <ns1:Response>  
          <Success>true</Success>  
          <Message>1011,2011,3011</Message>  
        </ns1:Response>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
