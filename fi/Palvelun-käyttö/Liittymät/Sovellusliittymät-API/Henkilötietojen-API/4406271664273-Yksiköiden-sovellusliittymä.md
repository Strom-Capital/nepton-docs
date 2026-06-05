---
id: 4406271664273
title: Yksiköiden sovellusliittymä
url: https://support.nepton.com/hc/fi/articles/4406271664273-Yksik%C3%B6iden-sovellusliittym%C3%A4
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
- yksikkö
- API
promoted: false
updated_at: '2021-11-23T13:43:31Z'
edited_at: '2021-11-23T13:43:31Z'
---

# Yksiköiden sovellusliittymä

Tässä artikkelissa kuvataan HR API -menetelmiä yksiköiden käsittelyyn.  
## GetUnits
Tämä toiminto palauttaa tiedot työyhteisön yksiköistä.
Pyynnön kentät:
UserName |  Kutsuvan henkilön käyttäjätunnus  
---|---  
UserPassword |  Kutsuvan henkilön salasana  
DeploymentID |  Asiakkaan yksilöllinen työyhteisön ID (Neptonin toimittama)  
WebServicePassword |  Yksilöllinen salasana asiakkaan työyhteisöön (Neptonin toimittama)  
IncludeDeletedUnits |  Mahdolliset arvot ovat True tai False. **True** : Jos arvo on "True", palautetaan kaikki yksiköt, myös poistetut. **False** : Jos arvo on 'False', palautetaan vain poistamattomat yksiköt.  
Vastauskentät:
ErrorMessage | Jos verkkopalvelu ei saa yksikkötietoja, tämä kenttä sisältää syyn, miksi se ei onnistu.  
---|---  
ReturnUnit > Id | Yksikön id  
ReturnUnit > Code | Yksikön yksilöllinen tunniste  
ReturnUnit > Name | Yksikön nimi  
ReturnUnit > IsDeleted |  Mahdolliset arvot ovat True tai False. **True** : yksikkö ei ole aktiivinen ja se poistetaan **False** : yksikkö on aktiivinen  
ReturnUnit > ModifiedDateTime | Päivämäärä ja aika, jolloin yksikköä on viimeksi muutettu
