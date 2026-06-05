---
id: 25397332335773
title: Parhaat käytännöt sääntöjoukkojen muokkaamiseen
url: https://support.nepton.com/hc/fi/articles/25397332335773-Parhaat-k%C3%A4yt%C3%A4nn%C3%B6t-s%C3%A4%C3%A4nt%C3%B6joukkojen-muokkaamiseen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels:
- liittymät
- työajan liittymät
- poimintasäännöt
- sääntöjoukot
- rulesets
promoted: false
updated_at: '2025-03-27T13:22:18Z'
edited_at: '2025-03-27T13:21:25Z'
---

# Parhaat käytännöt sääntöjoukkojen muokkaamiseen

Tässä artikkelissa kuvataan, kuinka hallita sääntöjoukkoja oikeaoppisesti. Artikkelissa kerrotaan vinkit, jotka helpottavat muutoshallintaa ja aiemman sääntöjoukon nopeaa käyttöönottoa, mikäli uutta sääntöjoukkoa ei syystä tai toisesta halutakaan ottaa vielä sellaisenaan käyttöön. Tämä artikkeli käsittelee vain Neptonista poimittavien tietojen (esimerkiksi palkka-aineisto, poissaolot, lomat, PowerBI) sääntöjoukkoja.
Sääntöjoukot rakennetaan Neptonissa yleisesti ottaen mahdollisimman ylös asetusryhmärakenteessa: joko Työyhteisötasolle tai ylimpiin asetusryhmiin. Pääset käsiksi sääntöjoukkoihin reittiä **Työaika > Hallinta > Työyhteisön asetukset > Liittymät: Poimintasäännöt** tai **Työaika > Hallinta > Asetusryhmät: valitse haluttu asetusryhmä ja sen asetukset > Liittymät: Poimintasäännöt**.
## Poimintasäännön muuttaminen niin, että vanha sääntö jää talteen historiatietona
Poimintasääntöä muutettaessa on tärkeää huomioida, että vanha sääntö, joka on todettu jo toimivaksi, jätetään "talteen" historiaan.
  1. Valitse haluamasi sääntö edellä mainittua polkua pitkin ja kopioi vanha sääntö kokonaisuudessaan talteen CTRL C -näppäinyhdistelmällä.
  2. Siirry säännön voimassaolotoiminto-kenttään Poimintasääntö-laatikon oikealla puolella olevasta kalenterikuvakkeen näköisestä painikkeesta  
  
![](https://support.nepton.com/hc/article_attachments/25402811561757)  
  

  3. Voimassaolotoimintopainikkeesta aukeaa uusi näkymä, jossa näkyy tällä hetkellä voimassaoleva sääntö. Aseta vanhalle säännölle Voimassa saakka -päivämäärä (tämä on hyvä olla joko kuun vaihteessa tai palkanmaksukauden vaihteessa, jotta poimintasääntö ei muutu kesken palkanmaksukauden). On tärkeää, että vanhan säännön voimassaolo päättyy ennen kuin uusi sääntö alkaa. Jos voimassaolot ovat päällekkäin, **noudattaa Nepton vanhan säännön voimassaoloaikaa.**
  4. Paina "Lisää" -painikkeesta lisätäksesi uutta sääntöä varten oman rivinsä.
  5. Liitä kohdassa 1. kopioimasi vanha sääntö avautuvaan näkymään (esimerkiksi CTRL V -näppäinyhdistelmällä). Tee tässä yhteydessä myös haluamasi muutokset sääntöön, mikäli teet muutokset käyttöliittymässä. Mikäli käytät säännön muuttamiseen toista sovellusta, liitä muutettu, uusi sääntö tähän kenttään suoraan toisesta sovelluksesta.
  6. Aseta uudelle säännölle voimaantulopäivämäärä. Tämän päivämäärän on oltava seuraava päivä vanhan säännön päättymispäivästä katsottuna, mikäli tarkoituksena on, että vanhan ja uuden säännön väliin ei tule katkoa.   
  
![](https://support.nepton.com/hc/article_attachments/26177444403229)  
  

  7. Lisää uuden säännön yläreunaan kommentti, joka sisältää tarkan kuvauksen siitä, **mitä** muutoksia on tehty, **milloin** , **kenen** pyynnöstä ja **kuka** on tehnyt muutoksen. Kommentin voi lisätä sääntöön käyttämällä rivin alkuun kahta viivaa (--), tämä estää kommentin vaikutuksen itse poimintasäännön toimintaan. Katso alta esimerkki kommentin lisäämisestä.   
  
![](https://support.nepton.com/hc/article_attachments/26176865975197)  
  

  8. Kun olet tyytyväinen tekemiisi muutoksiin, paina lopuksi voimassaolotoiminto-ikkunassa Tallenna-painiketta saattaaksesi tehdyt muutokset voimaan.
  9. Tehtyjen muutosten jälkeen on ensisijaisen tärkeää myös testata, että halutut muutokset toimivat oikein. Uutta sääntöä voi testata kokonaisuudessaan ajamalla liittymän esikatselu-tilassa valittujen testi- tai esimerkkihenkilöiden osalta. Ohje työajan liittymien ajamiseen löytyy tukipalvelustamme [täältä](<https://support.nepton.com/hc/fi/articles/360002492898-Ty%C3%B6ajan-liittym%C3%A4t>).
