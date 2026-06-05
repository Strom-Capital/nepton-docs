---
id: 6913825701277
title: GetAccrualValuesForUser
url: https://support.nepton.com/hc/fi/articles/6913825701277-GetAccrualValuesForUser
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
edited_at: '2025-01-10T08:21:15Z'
---

# GetAccrualValuesForUser

## Rajapinnan yleiskuvaus
Palvelulla haetaan henkilön kertymien arvot tietyltä päivämäärältä. Palautettavat kertymät ovat sellaisia, jotka on määritetty laskettavaksi henkilölle.
Osa kertymistä on käytössä oletuksena jokaisella asiakkaalla. Näitä ovat "saldo", "jousto" ja "pankki". Asiakkaat voivat myös määrittää omia kustomoitua kertymiä. Näiden kertymien nimet nähdään kyselyn tuloksista, jos ne ovat käytössä. Kaikki kertymät palautetaan kutsulla. Kertymän arvon lisäksi menetelmä palauttaa myös kyseisen päivän kertymän muutoksen.
Verkkopalvelun WSDL-skeema on julkisesti saatavilla [täällä](<https://time.nepton.com/WebService.php?WSDL>). Rajapinnat ovat yleisellä tasolla kuvattuna [täällä](<https://support.nepton.com/hc/fi/articles/360004861558>).
Kuvauksessa oleva sarake esiintymiskerrat määrittää sen onko jokin tieto pakollinen kutsussa vai ei. Esiintymiskerrat 0, tarkoittaa että kyseistä tietoa ei tarvitse siirtää kutsussa. Esiintymiskerrat 1 tarkoittaa, että tiedon tulee esiintyä kutsussa yhden kerran. Esiintymiskerrat 0..n tarkoittaa, että kyseinen tieto voi esiintyä kutsussa minkä tahansa määrän. Esiintymiskerrat 1..n tarkoittaa että kyseinen tieto tulee olla aineistossa ainakin kerran, mutta voi olla useamminkin.
## Lähetettävät tiedot
**Taso** | **Kentän nimi** | **Muoto** | **Esiintymiskerrat** | **Selite**  
---|---|---|---|---  
0 | ParametersForGetAccrualValues | XML element | 1 | Juurielementti SOAP bodyn alla  
1 | CallerAuthentication | XML element | 1 | Autentikointitiedot. katso [Tunnistautuminen](<https://support.nepton.com/hc/fi/articles/360019983978>)  
1 | UserPersonnelNumber | string | 1 | Henkilönumero käyttäjälle, jonka kertymiä ollaan hakemassa  
1 | SalaryDate | date | 0..1 | päivämäärä, jolloin kertymien arvot palautetaan, muoto VVVV-KK-PP esim. "2016-12-31". Huomautus: palauttaa kertymien arvot kaikkien kyseiseen päivään kuuluvien työvuorojen lopuksi.  
### Pyynnön esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ParametersForGetAccrualValuesForUser>  
          <CallerAuthentication /> <!-- Autentikointi vaaditaan mutta ei näytetä tässä esimerkissä -->  
          <UserPersonnelNumber>2345</UserPersonnelNumber>  
          <SalaryDate>2020-01-01</SalaryDate>  
        </tyo:ParametersForGetAccrualValuesForUser>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
## Vastaus
**Taso** | **Kentän nimi** | **Muoto** | **Esiintymiskerrat** | **Selite**  
---|---|---|---|---  
0 | ReturnValueForGetAccrualValues | XML element | 1 | Juurielementti SOAP bodyn alla  
1 | ResponseCode | int | 1 | Koodi joka kuvaa pyynnön onnistumista tai virhettä  
1 | ResponseString | string | 1 | Merkkijonomuotoinen kuvaus pyynnön onnistumisesta tai virheestä  
1 | AccrualList | XML element | 1 | Lista kertymistä  
2 | Accrual | XML element | 0..n | Kertymä  
3 | InternalName | string | 1 | kertymän sisäisen merkkijonon ID tunnus  
3 | Name | string | 1 | kertymän asiakkaalle määritelty/käytössä olevan kielen mukainen nimi  
3 | Amount | string | 1 | Kertymän määrä  
3 | ChangeAmount | string | 0..1 | kertymän muutoksen määrä edellisen päivän arvosta (ei palauteta, jos muutosta ei ole)  
### Vastauksen esimerkki
[code] 
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tyo="http://tyoaika.tyoteho.fi">  
      <soapenv:Header/>  
      <soapenv:Body>  
        <tyo:ReturnValueForGetAccrualValuesForUser>  
          <ResponseCode>?</ResponseCode>  
          <ResponseString>?</ResponseString>  
          <AccrualList>  
            <Accrual>  
              <InternalName>bank</InternalName>  
              <Name>pankki</Name>  
              <Amount>18</Amount>  
              <ChangeAmount>10</ChangeAmount>  
            </Accrual>  
          </AccrualList>  
        </tyo:ReturnValueForGetAccrualValuesForUser>  
      </soapenv:Body>  
    </soapenv:Envelope>
[/code]
