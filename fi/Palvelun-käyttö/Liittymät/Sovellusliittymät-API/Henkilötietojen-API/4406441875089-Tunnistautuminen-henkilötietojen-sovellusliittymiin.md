---
id: 4406441875089
title: Tunnistautuminen henkilötietojen sovellusliittymiin
url: https://support.nepton.com/hc/fi/articles/4406441875089-Tunnistautuminen-henkil%C3%B6tietojen-sovellusliittymiin
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen API
section_id: 4406143245713
section_path:
- Liittymät
- Sovellusliittymät (API)
- Henkilötietojen API
labels: []
promoted: false
updated_at: '2025-09-08T07:31:11Z'
edited_at: '2025-03-21T10:01:47Z'
---

# Tunnistautuminen henkilötietojen sovellusliittymiin

[Henkilötietojen sovellusliittymien](<https://support.nepton.com/hc/articles/360004855857>) toimintoja ei ole vielä standardoitu ja sen vuoksi niissä on erityyppisiä tunnistautumisratkaisuja käytössä. Tulevaisuudessa kaikki toiminnot muutetaan käyttämään tunnistautumistietoja, jotka on sidottu Nepton-palvelussa olevaan henkilöön, ja sovellusliittymän käyttöoikeudet tulevat olemaan samat kuin kyseiselle henkilölle on asetettu Neptoniin.  
Suosittelemme perustamaan testausta ja automaattista käyttöä varten erillisen käyttäjän, jota ei käytetä muihin tarkoituksiin. Ks. [ohjeet henkilön lisäämiseksi](<https://support.nepton.com/hc/articles/360002427618>). Käyttäjällä täytyy olla ylläpitäjän oikeudet.
## Tunnistautuminen
Monia [henkilötietojen sovellusliittymien](<https://support.nepton.com/hc/articles/360004855857>) toiminnoista ei ole vielä standardoitu. Tarkista toiminnon kuvauksesta asiaan liittyvistä artikkeleista saadaksesi lisätietoja tunnistautumiseen ja palvelupyynnön suorittamiseen vaadittavista kentistä. Voit myös katsoa tiedot sovellusrajapintatoiminnon automaattisesti muodostetusta dokumentaatiosta: <https://go.nepton.com/API/SOAPWebService.asmx>
Standardoiduille toiminnoille tunnistautumisessa käytettävät kentät ovat:
  * **Username** \- Nepton-palveluun tallennetun henkilön käyttäjätunnus.
  * **UserPassword** \- Em. henkilön salasana. **HUOM. Salasana ei voi päättyä &-merkkiin, rikkoo XML-sanoman.**
  * **DeploymentId** \- Numeerinen tunnus, jolla työyhteisösi on tunnistettavissa. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.
  * **WebServicePassword** \- Salasana, joka liittyy työyhteisön tietoihin. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.


## Esimerkki
Tässä on esimerkki GetUnits-SOAP-viestistä käyttäen tunnistautumiskenttiä:
  * Metodi: POST
  * Yhteysosoite: https://go.nepton.com/API/SOAPWebService.asmx
  * Otsikot:  

    * Content-Type: text/xml; charset=utf-8
  * Sisältö:  

[code] <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
          <soap:Body>
            <GetUnits xmlns="http://tempuri.org/">
              <Request>
                <Username>Integration Account</Username>
                <UserPassword>e8bc7c00-17c8-4802-8962-c77e1071116c</UserPassword>
                <DeploymentId>285057</DeploymentId>
                <WebServicePassword>060b20fe-cd2a-4629-bdc5-7b896a1cebc6</WebServicePassword>
                <IncludeDeletedUnits>false</IncludeDeletedUnits>
              </Request>
            </GetUnits>
          </soap:Body>
        </soap:Envelope>
        
[/code]
