---
id: 360003504177
title: IFS työajan vienti
url: https://support.nepton.com/hc/fi/articles/360003504177-IFS-ty%C3%B6ajan-vienti
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
updated_at: '2025-08-28T11:53:35Z'
edited_at: '2025-08-28T11:53:35Z'
---

# IFS työajan vienti

Nepton voidaan määrittää lähettämään työtunteja, projekti-/työtilauksia sekä palkkatietoja IFS-järjestelmään. Tiedot lähetetään tapahtumia tallennettaessa tai tehdessä muita toimenpiteitä kalenterinäkymässä (katso tarkemmat tiedot alhaalta kohdasta 'Viennin käynnistys'). Tapahtumia ei tallenneta, ellei työaikojen tallennus IFS:ään onnistu. Kaikki IFS:stä tulevat virheet näytetään käyttäjälle.
Jos [oletetut tapahtumat](<https://support.nepton.com/hc/fi/articles/360002558717>) ovat käytössä, lähetetään oletettujen tapahtumien tiedot IFS:ään sillä hetkellä, kun ne hyväksytään.
Lähetetyt tiedot määritetään sääntöjoukolla. Tietojen lähettämiseen vaaditaan IFS:n SOAP-verkkopalvelu (tai välijärjestelmä, kuten BizTalk). Tämän verkkopalvelun WSDL-skeema kuvataan alla.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden IFS-tunnukset voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360004710798)
HUOM! Jos henkilön IFS-tunnusta ei ole asetettu, käytetään henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymää varten tulee luoda liittymän sääntöjoukko. Sääntöjoukon poiminnan ohje löytyy artikkelista [sääntöjoukon poimintasääntöjen muodostaminen](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
**3\. Tietojen lähettäminen**
Seuraavat tiedot tulee asettaa työyhteisön tai asetusryhmän asetuksissa. Asetukset löytyvät poimintasäännön asetuksista kohdasta Viennin asetukset.
  * Viennin tiedostomuoto - Valitse tähän "IFS Salary data"
  * Viennin web service -osoite - Kirjoita tähän web service -rajapinnan osoite, mihin tiedot lähetetään


Lisäksi asetettavissa on API-avain, jota käytetään tunnistautumiseen. Tieto lähetetään kutsun HTTP-otsikoissa (HTTP headers). Käytetty otsikko on `TOKEN`.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4419570583185)
## Rajoitukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa
  * Jos rajapinta palauttaa vastauksena epäonnistumisen, tapahtuman tallentaminen estetään


## Viennin käynnistys
Vientiä ei ole aikataulutettu, vaan se käynnistyy reaaliajassa aina, kun käyttäjä tekee muutoksia tapahtumiin tai tiettyihin asetuksiin. Muutosten laskenta simuloidaan, jotta voidaan tarkistaa muutosten yhteensopivuus IFS:n kanssa. Alla lista tilanteista, milloin vienti tapahtuu:
  * Aina, kun tapahtuma tallennetaan mistä tahansa lähteestä, poikkeuksena tapahtumien hyväksyminen
  * Kun työpäivän pituus muutetaan kalenterissa.
  * Kun työviikon pituus muutetaan kalenterissa.
  * Kun sallitut tai oletetut työajat muutetaan kalenterissa.


## Lähetettävät tiedot
Palkkatiedot lähetetään käyttäjäkohtaisesti vähintään viikon ajalta. Koko viikko lähetetään, sillä alkuviikon muutokset voivat vaikuttaa viikon päättyessä ansaittuun palkkaan. Tietyissä tilanteissa kuluvalle päivälle tehty muutos voi vaikuttaa aiemman päivän laskentoihin. Tällöin myös aiempi päivä lähetetään. Useimmiten tämä liittyy tilanteeseen, jossa yön ylittävän työvuoron / oletetun työajan alle osuvat merkinnät lasketaan vuoron alkamispäivän mukaan.
Käyttäjän palkkatapahtuman tiedot (WSDL-kuvauksesta löytyy lisää tietoa):
Taso | Kentän nimi | Sääntöjoukon kentän nimi | Formaatti | Esiintymiskerrat | Selite  
---|---|---|---|---|---  
Juuri,  
SOAP body:n alla | SALARY_EXPORTS |  | XML element | 1 |   
1 | EXPORT_START_DATE |  | datetime | 1 | Vietävän ajanjakso alkupäivä ja aika. Formaatti `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
1 | EXPORT_END_DATE |  | datetime | 1 | Vietävän ajanjakson loppupäivä ja aika. Formaatti `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
1 | EMP_ID | _Lisätään automaattisesti, ei korvattavissa_ | string (100) | 1 | Henkilön IFS-tunnus / henkilönumero  
1 | SALARY_EXPORT |  | XML element | 0..n |   
2 | SALARY_DATE | SalaryRenderingDate | datetime | 1 | Päivä, mille palkkatieto kuuluu. Jos palkkatieto kuulu esimerkiksi maanantaille, maanantain päivämäärää ja aikaa käytetään. Formaatti `YYYY-MM-DD'T'HH:MM:SS[Z|(+|-)hh:mm]`  
2 | COMPANY_ID |  | string (20) | 0..1 | Juurihenkilöryhmän koodi, minkä alaryhmän jäsenenä henkilö on.  
2 | AMOUNT | Amount | decimal | 1 | Määrä, esimerkiksi yksikkömäärä tai tunnit desimaalilukuna  
2 | PROJECT_CODE | ProjectCode1 | string (200) | 0..1 |  Jos projektille on asetettu ulkoinen tunniste (`ProjectExternalIdentifier1`) ja projektin koodina (`ProjectCode1`) ei ole "DEFAULT", käytetään ulkoista tunnistetta. Muussa tapauksessa käytetään projektin koodia (`ProjectCode1`)  
2 | PROJECT_TYPE |  | string (10) | 0..1 |  Jos projektille on asetettu ulkoinen tunniste (`ProjectExternalIdentifier1`) ja projektin koodina (`ProjectCode1`) ei ole "DEFAULT", arvona siirretään "Project_sequence" Jos projektille on asetettu ulkoinen tunniste, mutta halutaan käyttää muuta tyyppiä kuin "Project_sequence", projektin tyyppi voidaan yliajaa sääntöjoukon säännössä asettamalla tyypin arvo kentälle IntegrationProjectType, esim. `SELECT *, CASE WHEN ProjectType1 != 'project_work' AND ProjectExternalIdentifier1 NOT NULL THEN ProjectType1 ELSE null END AS IntegrationProjectType FROM UserSalaryData` Muussa tapauksessa käytetään kirjatun projektin projektityypin sisäistä nimeä, esimerkiksi "project_work"  
2 | SALARY_CODE | SalaryCode | string (100) | 0..1 | Palkkatiedon palkkalajikoodi  
2 | COMMENT | Comment | string (2000) | 0..1 | Tapahtuman kuvaus  
2 | CRAFTREPORT_CODE | UserCostGroup | string (100) | 0..1 | Henkilön oletuskalleusluokka  
2 | ADDINFO |  | string (2000) | 0..1 | Voidaan lisätä liittymään tarvittaessa. Kenttä viedään ainoastaan, jos sitä käytetään poimintasäännössä, esimerkiksi 'SELECT ExternalIdentifier AS AddInfo'  
Kyselyn esimerkki:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wo="http://WO.fi.TyoTeho.Schemas.Salary_Export">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <wo:SALARY_EXPORTS>  
          <EXPORT_START_DATE>2019-06-01T00:00:00+03:00</EXPORT_START_DATE>  
          <EXPORT_END_DATE>2019-06-03T00:00:00+03:00</EXPORT_END_DATE>  
          <EMP_ID>1240</EMP_ID>  
          <SALARY_EXPORT>  
            <SALARY_DATE>2019-06-01T00:00:00+03:00</SALARY_DATE>  
            <COMPANY_ID>CompanyID</COMPANY_ID>  
            <AMOUNT>7.50</AMOUNT>  
            <PROJECT_CODE>PRJ01</PROJECT_CODE>  
            <PROJECT_TYPE>project_work</PROJECT_TYPE>  
            <SALARY_CODE>100</SALARY_CODE>  
            <COMMENT>Saturday work</COMMENT>  
            <CRAFTREPORT_CODE>GRP01</CRAFTREPORT_CODE>  
          </SALARY_EXPORT>  
          <SALARY_EXPORT>  
            <SALARY_DATE>2019-06-02T00:00:00+03:00</SALARY_DATE>  
            <COMPANY_ID>CompanyID</COMPANY_ID>  
            <AMOUNT>7.50</AMOUNT>  
            <PROJECT_CODE>PRJ02</PROJECT_CODE>  
            <PROJECT_TYPE>project_work</PROJECT_TYPE>  
            <SALARY_CODE>100</SALARY_CODE>  
            <COMMENT>Sunday work</COMMENT>  
            <CRAFTREPORT_CODE>GRP01</CRAFTREPORT_CODE>  
          </SALARY_EXPORT>  
        </wo:SALARY_EXPORTS>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Odotettu vastaus
Liittymä odottaa vastausta paluusanomana. Paluusanoman muoto on seuraava:
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri,  
SOAP body:n alla | Response | XML element | 1 |   
1 | Success | boolean | 1 | Saatiinko lähetetyt palkkatiedot käsiteltyä onnistuneesti vai ei  
1 | Message | string | 0..1 | Valinnainen viesti. Käytetään pääosin virheviestin näyttämiseen, kun palkkatietoja ei saatu käsiteltyä  
Sanoman esimerkki:
[code] 
    <?xml version="1.0" encoding="UTF-8"?>  
    <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://WO.fi.TyoTeho.Schemas.TimeReportResponse">  
      <SOAP-ENV:Body>  
        <ns1:Response>  
          <Success>true</Success>  
          <Message>MESSAGE</Message>  
        </ns1:Response>  
      </SOAP-ENV:Body>  
    </SOAP-ENV:Envelope>
[/code]
