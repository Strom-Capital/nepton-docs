---
id: 13129687045789
title: Työsuhteen päivämäärien muokkaus henkilötuonnissa
url: https://support.nepton.com/hc/fi/articles/13129687045789-Ty%C3%B6suhteen-p%C3%A4iv%C3%A4m%C3%A4%C3%A4rien-muokkaus-henkil%C3%B6tuonnissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels: []
promoted: false
updated_at: '2024-02-06T11:13:45Z'
edited_at: '2024-02-06T11:13:43Z'
---

# Työsuhteen päivämäärien muokkaus henkilötuonnissa

Tämä artikkeli kuvaa sen miten henkilöiden työsuhteiden alku- ja päättymispäiviä voidaan muokata henkilötuonnissa. Arikkelissa kuvataan myös se miten mahdolliset virheet työsuhteiden alku- ja päättymispäivissä korjataan tuonnilla.
Huomaa, että työsuhteen päivämäärien muokkaus toimii samalla logiikalla kaikissa henkilötuonnin tyypeissä paitsi Oletus-vaihtoehdossa.
## Miten päivämäärien muokkaus toimii?
  * Jos henkilölle on asetettu työsuhteen alkupäivä, tuotu päivämäärä voi tyhjentää olemassa olevan arvon tai aikaistaa sitä mutta työsuhteen alkupäivää ei voida muuttaa myöhemmäksi päivämääräksi
  * Jos henkilölle on asetettu työsuhteen päättymispäivä, tuotu päivämäärä voi tyhjentää olemassa olevan arvon tai muuttaa arvon myöhemmäksi mutta työsuhteen päättymispäivää ei voida muuttaa aiemmaksi päivämääräksi
  * Näiden rajoitusten on tarkoitus varmistaa, että henkilöitä, joilla on useita työsuhteen päivämääriä, voidaan tarkastella ja hallinnoida palvelussa oikein
  * Tuki usealle työsuhteelle per henkilö lisätään palveluun myöhemmin  
  
Esimerkkejä:


  1. Alkutilanne: Henkilöllä ei ole olemassa olevia työsuhteen alku- tai päättymispäivämääriä  
Tuodaan arvot  
Työsuhteen alkupäivämäärä: 01.05.2021  
Työsuhteen päättymispäivämäärä: 31.08.2022  
Tilanne tuonnin jälkeen: Henkilön työsuhteen päivämäärät ovat 01.05.2021-31.08.2022, eli uusia päivämääriä voidaan lisätä kun olemasa olevia päivämääriä ei ole  
  

  2. Alkutilanne: Henkilön työsuhteen päivämäärät ovat 01.05.2021-31.08.2022  
Tuodaan arvot:  
Työsuhteen alkupäivämäärä: 01.01.2021  
Työsuhteen päättymispäivämäärä: 31.12.2021  
Tilanne tuonnin jälkeen: Henkilön työsuhteen päivämäärät ovat 01.01.2021-31.08.2022, eli alkupäivämäärää voidaan aikaistaa mutta loppumispäivämäärä ei  
  

  3. Alkutilanne: Henkilön työsuhteen päivämäärät ovat 01.01.2021-31.08.2022  
Tuodaan arvot:  
Työsuhteen alkupäivämäärä: 01.01.2022  
Työsuhteen päättymispäivämäärä: 31.12.2022  
Tilanne tuonnin jälkeen: Henkilön työsuhteen päivämäärät ovat 01.01.2021-31.12.2022, eli loppumispäivämäärä voidaan siirtää eteenpäin mutta alkupäivämäärää ei  
  

  4. Alkutilanne: Henkilön työsuhteen päivämäärät ovat 01.01.2021-31.12.2022  
Tuodaan arvot:  
Työsuhteen alkupäivämäärä: "" (eli tyhjä kenttä)  
Työsuhteen päättymispäivämäärä: ""  
Tilanne tuonnin jälkeen: Henkilöllä ei ole työsuhteen päivämääriä määriteltynä, eli työsuhteen päivämäärät voidaan aina tyhjentää


## Miten korjataan työsuhteen päivämäärien tuonnissa tapahtuneet virheet?
  * Haluamme tuoda henkilölle työsuhteen päivämäärät "01.01.2021 - 31.12.2023"  

    * Tuomme erehdyksessä seuraavat päivämäärät  
Työsuhteen alkupäivämäärä: 01.01.2022  
Työsuhteen päättymispäivämäärä: 31.12.2022  
Tilanne tuonnin jälkeen: 01.01.2021 - 31.12.2023
  * Voimme korjata virheen seuraavilla toimenpiteillä  

    1. Tuodaan ensin arvot  
Työsuhteen alkupäivämäärä: ""  
Työsuhteen päättymispäivämäärä: 31.12.2022  
Tilanne tuonnin jälkeen: "" - 31.12.2023
    2. Tuodaan seuraavaksi seuraavat arvot  
Työsuhteen alkupäivämäärä: 01.01.2021  
Työsuhteen päättymispäivämäärä: 31.12.2022  
Tilanne tuonnin jälkeen: 01.01.2021 - 31.12.2023
