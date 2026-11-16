---
id: 360002489417
title: Yleiset periaatteet liittymien toteutukseen
url: https://support.nepton.com/hc/fi/articles/360002489417-Yleiset-periaatteet-liittymien-toteutukseen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels:
- NEPTONNEEDSREVIEW
- liittymäkuvaus
- ajastuspalvelut
- integraatio
- henkilötietoliittymä
- henkilöliittymä
promoted: false
updated_at: '2026-08-14T10:05:38Z'
edited_at: '2025-07-25T10:07:39Z'
---

# Yleiset periaatteet liittymien toteutukseen

Liittymällä viitataan tapaan siirtää tietoa joko Neptonista toiseen järjestelmään tai toisesta järjestelmästä Neptoniin. Liittymätapoja ovat
  * tiedostopohjainen [SFTP](<https://support.nepton.com/hc/fi/articles/360003762477>)-siirto  
tai
  * [API:n](<https://support.nepton.com/hc/fi/articles/360004861518>) hyödyntäminen


Tiedostopohjaisia SFTP-siirron periaatteena on, että lähdejärjestelmä muodostaa aineiston ajastetusti SFTP-palvelimelle. Kohdejärjestelmä noutaa ja käsittelee aineiston toisella ajastuksella. Tyypillisesti aineistoja siirretään yöaikaan ja muodostamisen ja noutamisen väliin jätetään riittävästi aikaa, jotta lähdejärjestelmä on varmasti muodostanut aineiston.
![](https://support.nepton.com/hc/article_attachments/14011900014877)
API-sovellusliittymä perustuu kutsuihin, jotka toteutetaan niin, että vastajärjestelmästä kutsutaan Nepton API:a halutun tiedon saamiseksi. Nämä Neptonin API-sovellusliittymässä käytettävissä olevat mahdollisuudet on kuvattu seuraavissa artikkeleissa:
[Työajan API](<https://support.nepton.com/hc/fi/articles/360004861558>)
[HR-API](<https://support.nepton.com/hc/fi/articles/360004855857>)
![](https://support.nepton.com/hc/article_attachments/13997381126173)
Tiedostopohjainen SFTP-siirto on luonteltaan ajastetumpi ja siinä usein siirretään suurempi määrä tietoa kerralla (esim. henkilötuonnissa uudet henkilöt ja henkilötietojen muutokset) kun taas API-sovellusliittymää hyödynnetään tilanteessa, jossa tiedon siirto tulee olla nopeampaa ja käytössä Neptonissa välittömästi (esim. projektitiedon tuonti tai vienti vastajärjestelmään tai vastajärjestelmästä).
Kun liittymiä toteutetaan, tulee huomioida seuraavia toimintaperiaatteita:
### Ongelmien havaitseminen ja ratkaisu
Mahdollisten [ongelmien havaitseminen ja ratkaisu](<https://support.nepton.com/hc/fi/articles/9056347382813>) pitää ottaa huomioon jo liittymän toteutusvaiheessa.
### Ajastus
SFTP-palvelimen kautta toimivat liittymät voidaan ajastaa Neptonissa. Lue lisää näistä:
  * [Henkilötietojen ajastettu tuonti](<https://support.nepton.com/hc/fi/articles/360002489317-Henkil%C3%B6tietojen-ajastettu-tuonti>)
  * [Henkilötietojen ajastettu vienti](<https://support.nepton.com/hc/fi/articles/360002489357-Henkil%C3%B6tietojen-ajastettu-vienti>)
  * [Työajan vienti/tuonti liittymien ajastus](<https://support.nepton.com/hc/fi/articles/10510800700573-Ty%C3%B6ajan-vienti-tuonti-liittymien-ajastus>)


Näiden lisäksi on muutama lähes reaaliaikainen liittymä, jotka ajetaan kerran minuutissa. Tällaisia ovat liittymät puhelinvaihde- ja läsnäolojärjestelmiin:
  * [Elisa Ring (eIPKulva)](<https://support.nepton.com/hc/fi/articles/360004522538-Elisa-Ring-tilatiedot>)
  * [Mitel Aastra ja Telia Merex](<https://support.nepton.com/hc/fi/articles/360013422917-Mitel-Aastra-ja-Telia-Merex-tilatiedot-Flexim>)


### Siirrettävän henkilön henkilönumero tai liittymätunniste
Henkilölle voidaan asettaa henkilönumero, jota käytetään kaikissa siirroissa. Mikäli käytössä on useampi tunnisteita, voidaan järjestelmäkohtainen tunniste asettaa henkilölle tämän tiedoissa Työsuhde-osiossa, jolloin tätä tunnistetta käytetään kyseisen järjestelmän siirroissa. Koodi '0' (nolla) on erikoiskoodi, jolla voidaan ohittaa kyseisen henkilön tiedon siirto. Tätä koodia tulee käyttää henkilön tunnisteena vain silloin kun kyseisen henkilön tietoja tai tapahtumia ei haluta siirtää.
### Siirron suorittava käyttäjä
Siirtoja varten luodaan oma käyttäjä Neptoniin, joka on vain tätä tarkoitusta varten. Käyttäjälle annetaan tarvittavat oikeudet siirtojen suorittamiseen. Henkilötietoja siirtäessä käyttäjällä pitää olla ylläpitäjän oikeudet. Työaikatietoja siirtäessä pitää olla lisäksi seuraavat työajan oikeudet (riippuen mitä tietoa siirretään):
Tiedon viemiseen:   
Voi nähdä kaikkien henkilöiden tapahtumat
Tapahtumien tuomiseen:  
Voi muokata ja hyväksyä kaikkien tapahtumia  
Voi lukita tapahtumapäiviä  
Voi poistaa tapahtumien lukituksen päiviltä  
Voi asettaa ja muokata saldon arvoa  
Voi muokata hyväksyttyjä tapahtumia  
Voi tarkastella tapahtumien ulkoista tunnistetta  
Voi muokata tapahtumien ulkoista tunnistetta
Projektitiedon siirtämiseen:  
Voi hallinnoida projekteja ja projektisuhteita  
Voi hallinnoida henkilöiden asetuksia ja projekteja
Jos henkilötietoihin pitää muuttaa henkilöryhmää, asetusryhmää, työajan roolia:  
Voi hallinnoida työajan henkilöryhmiä  
Voi hallinnoida asetusryhmiä  
Voi hallinnoida työajan rooleja
