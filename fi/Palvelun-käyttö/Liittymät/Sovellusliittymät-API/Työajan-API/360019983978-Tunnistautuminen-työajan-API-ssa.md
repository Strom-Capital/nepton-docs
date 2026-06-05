---
id: 360019983978
title: Tunnistautuminen työajan API:ssa
url: https://support.nepton.com/hc/fi/articles/360019983978-Tunnistautuminen-ty%C3%B6ajan-API-ssa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työajan API
section_id: 360005706218
section_path:
- Liittymät
- Sovellusliittymät (API)
- Työajan API
labels:
- Työajan API
promoted: false
updated_at: '2025-02-27T07:06:26Z'
edited_at: '2022-11-10T07:22:14Z'
---

# Tunnistautuminen työajan API:ssa

Kaikki Työajan API viestit vaativat tunnistautumisen Nepton-palvelussa olevan henkilön tunnuksilla ja sovellusliittymän käyttöoikeudet ovat samat kuin kyseiselle henkilölle on asetettu Neptoniin.
On suositeltavaa, että jokaiselle sovellusliittymää käyttävälle ratkaisulle perustetaan oma henkilö eli käyttäjätunnus. Näitä käyttäjätunnuksia ei käytetä mihinkään muuhun tarkoitukseen kuin API:n käyttöön. Ks. [ohje henkilön lisäämiseksi.](<https://support.nepton.com/hc/fi/articles/360002427618>)
Tunnistautumista varten kutsussa yhtenä SOAP elementtinä tulee olla CallerAuthentication-elementti.
## Tunnistautuminen
CallerAuthentication-elementissä on tunnistautumistiedot. Standardoiduille toiminnoille tunnistautumisessa käytettävät kentät ovat:
  * CustomerId - Työyhteisön Id-numero. Ota yhteyttä asiakaspalveluun saadaksesi oikean arvon.
  * Username - Nepton-palveluun tallennetun henkilön käyttäjätunnus.
  * Password - Em. henkilön salasana. **HUOM. Salasana ei voi päättyä &-merkkiin, rikkoo XML-sanoman.**


Muut tunnistautumiseen liittyvät kentät, jotka on listattu API kuvauksessa ovat ainoastaan sisäiseen käyttöön.
### Esimerkki
[code] 
    <CallerAuthentication>  
      <CustomerId>xxxxxxxxx</CustomerId>  
      <Username>xxxxxxxxx</Username>  
      <Password>xxxxxxxxx</Password>  
    </CallerAuthentication>
[/code]
