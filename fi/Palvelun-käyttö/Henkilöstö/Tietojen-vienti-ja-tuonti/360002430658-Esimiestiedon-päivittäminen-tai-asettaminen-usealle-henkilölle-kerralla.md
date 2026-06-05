---
id: 360002430658
title: Esimiestiedon päivittäminen tai asettaminen usealle henkilölle kerralla
url: https://support.nepton.com/hc/fi/articles/360002430658-Esimiestiedon-p%C3%A4ivitt%C3%A4minen-tai-asettaminen-usealle-henkil%C3%B6lle-kerralla
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tietojen vienti ja tuonti
section_id: 360004488578
section_path:
- Henkilöstö
- Tietojen vienti ja tuonti
labels:
- sisäänluku
promoted: false
updated_at: '2024-11-18T14:31:33Z'
edited_at: '2024-03-05T14:44:09Z'
---

# Esimiestiedon päivittäminen tai asettaminen usealle henkilölle kerralla

Tässä esimerkissä käytetään manuaalista henkilötuontia .csv-tiedostomuodossa UTF-8-koodauksella. Lisätietoja eri tuontivaihtoehdoista löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360003762577>).
## Esimiehen lisääminen jo määritettyjen esimiesten lisäksi
  1. Ota Työsuhde-osiossa **Henkilöt - > Henkilöt **ja **Vie sisäänluettavaan Exceliin -** painikkeesta.  
  

  2. Poista Excel-tiedostosta kaikki muut sarakkeet paitsi **Henkilönumero, Ensisijaiset esimiehet ja Toissijaiset esimiehet**. Myös sarakkeet **Etunimi** ja **Sukunimi** voidaan jättää, mikäli ne helpottavat tiedoston käsittelyä.  
  

  3. Mikäli henkilöllä on jo määritettyjä esimiehiä (esimiesten hlönumeroita), **älä** poista niitä aineistosta.  
  

  4. Lisää kullekin henkilölle tämän uuden esimiehen henkilönumero Toissijaiset esimiehet -sarakkeeseen. Mikäli henkilöllä on jo esimiehiä, erota uuden esimiehen henkilönumero jo olemassa olevista | - merkillä, ilman välilyöntiä.  
  
Em. vaiheiden jälkeen Excel-tiedoston tulisi näyttää seuraavalta:  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4417158733201)  
  

  5. Tämän jälkeen tallenna tiedosto **CSV UTF-8** -muodossa.  
  

  6. Tiedosto on nyt valmis ladattavaksi palvelun Työsuhde-osion Henkilöt-välilehdeltä löytyvän Tuo henkilöitä -työkalun avulla (ks. [Henkilöiden manuaalinen tuonti](<https://support.nepton.com/hc/fi/articles/360018767498>)).  
  

  7. Hae henkilöaineisto koneeltasi raahaamalla tiedosto viivoitetulle alueelle tai valitsemalla Valitse tiedosto -painikkeesta.  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21079102933405)
  8. Valitse tiedostomuoto UTF-8 ja henkilötuonnin tyyppi "Oletus". Paina lopuksi Tuo henkilöt -painiketta. Palvelu ilmoittaa onnistuneesta tai epäonnistuneesta tuonnista. Jos tuonti epäonnistuu, antaa palvelu tarkemmat tiedot aineistossa olevasta virheestä.


On suositeltavaa testata esimiestiedon tuontia ensin yhdellä henkilöllä, jotta voidaan varmistua tiedostomuodon oikeellisuudesta sekä halutusta lopputuloksesta. Varmista, että ainakin yksi esimies on määritetty ensisijaiseksi esimieheksi. Ilmoitukset arkaluonteisista toimista, kuten sairausloma-, saldo- ja vuosilomapyynnöistä, lähetetään ainoastaan ensisijaisille esimiehille.
