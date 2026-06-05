---
id: 360002425517
title: RFID-tunnisteen lisääminen henkilölle
url: https://support.nepton.com/hc/fi/articles/360002425517-RFID-tunnisteen-lis%C3%A4%C3%A4minen-henkil%C3%B6lle
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Henkilötietojen käsittely
section_id: 360004485937
section_path:
- Henkilöstö
- Henkilötietojen käsittely
labels:
- rfid
- rdif
- kortinlukija
- leimaustunniste
- lätkä
promoted: false
updated_at: '2024-11-18T09:43:51Z'
edited_at: '2024-11-07T13:33:44Z'
---

# RFID-tunnisteen lisääminen henkilölle

Jos yhteisössä on käytössä RFID-tunnisteet ja niitä käytetään työajan kirjaamiseen työaikapäätteellä, tulee RFID-tunniste asettaa jokaisen työntekijän tietoihin.
## RFID-tunnisteen lisääminen manuaalisesti
RFID-tunnisteen voi asettaa työntekijälle **Työsuhde** -osiossa **Henkilöt** -välilehdellä kohdassa **Henkilön tiedot - > Tunnisteet **  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360006278118)  
Tunnisteita voi olla yksi tai useampi. Mikäli halutaan lisätä useampi tunniste, erotellaan ne piippumerkillä (|). Kun olet lisännyt tunnisteen tiedot, tallenna muutokset vasemman alareunan sinisestä **Tallenna** -linkistä. Huomioithan, että kenttä toimii [voimassaolotoiminnolla](<https://support.nepton.com/hc/fi/articles/360004856937>).
Sama RFID-tunniste ei voi olla useamman henkilön tiedoissa, joten työntekijän työsuhteen päättyessä pitää RFID-tunniste poistaa ennen henkilön [tunnuksen poistoa.](<https://support.nepton.com/hc/fi/articles/360002424617>)
Osassa RFID-tunnisteita tunnisteen päällä lukeva koodi ei ole varsinainen tunnisteen koodi. Oikean numeron saat tarkastettua näyttämällä RFID-tunnistetta kirjauspäätteellä. Mikäli tunniste ei ole kenellekään käyttäjälle asetettuna, ilmoittaa kirjauspääte, ettei tunnistetta löydy, sekä antaa näyttöön tunnisteen koodin. Tallenna tämä koodi henkilön henkilötietoihin.
## RFID-tunnisteen lisääminen lukijalla
RFID-tunnisteen voi lisätä työntekijän tietoihin myös liittämällä RFID-lukija tietokoneen USB-porttiin ja näyttämällä henkilön tunnistetta lukijalle, jolloin se lukee oikean tunnistesarjan suoraan henkilön tietoihin.
  1. Kytke lukija (kuva alla) tietokoneeseen kiinni (USB-porttiin).


![mceclip0.png](https://support.nepton.com/hc/article_attachments/21082155871517)
  2. Kirjaudu Neptoniin.
  3. Avaa henkilön tiedot.
  4. Klikkaa hiirellä RFID-tunniste-kenttää.


![mceclip2.png](https://support.nepton.com/hc/article_attachments/21082145359517)
  5. Näytä tunnistetta (kuva alla) lukijalle.


![keyfob.jpg](https://support.nepton.com/hc/article_attachments/21082155872541)
  6. Kenttään ilmaantuu numerosarja.


![mceclip4.png](https://support.nepton.com/hc/article_attachments/21082145361565)
  7. Tallenna tiedot sivun alalaidan Tallenna-napista.


Tunnisteen tiedot on nyt tallennettu henkilön tietoihin.
## RFID-tunnisteiden lisääminen ja poistaminen massana 
#### RFID-tunnisteiden lisääminen massana
RFID-tunnisteet voidaan tuoda palveluun myös massana sisäänluettavaa exceliä hyödyntäen. Tukipalvelumme artikkeli [Henkilöiden manuaalinen tuonti ](<https://support.nepton.com/hc/fi/articles/360018767498-Henkil%C3%B6iden-manuaalinen-tuonti>)opastaa, kuinka massatuonti onnistuu.
#### RFID-tunnisteiden poistaminen massana
RFID-tunnisteita voidaan poistaa massana henkilötietojen tuontia hyödyntäen. Valitse Työsuhde-osiosta koko henkilöstö (tai rajaa sitä haluamallasi tavalla) ja lataa henkilöstön tiedot sisäänluettavaan exceliin:
![](https://support.nepton.com/hc/article_attachments/22690535104157)
Käsittele tiedosto Excelissä niin, että halutuilta henkilöiltä on poistettu RFID-tunnisteriviltä RFID-tunnisteen tiedot kokonaan. Tallenna tekemiesi muutosten jälkeen tiedosto itsellesi talteen. Tuo muokkaamasi aineisto takaisin Neptoniin henkilötuonnin kautta (Työsuhde > Henkilöt > Tuo henkilöitä)
![A screenshot of a computer

Description automatically generated](https://support.nepton.com/hc/article_attachments/22690557702429)**Henkilötuonnin tyyppi** määrittelee, miten tiedoston sisältö tulkitaan Neptonissa. Yleisesti Nepton suosittelee käyttämään tuontityyppinä valintaa **O****letus.**
Manuaalisessa henkilötuonnissa tyhjät kentät tuontitiedostossa eivät oletuksena muuta olemassa olevien kenttien arvoja. RFID-tunnisteiden poistossa on valittava "Olemassaolevat kenttien arvot poistetaan (tarkka)", jolloin tietojen poisto pakotetaan. Tämän kanssa on oltava varovainen, sillä toiminto ylikirjoittaa kaikki tuonnissa tuotavat kentät.
#### Massana poistetun RFID-tunnisteen uudelleenkäyttäminen toisella henkilöllä
Kun tyhjä RFID-kenttä tuodaan henkilötuonnin yhteydessä, jää RFID-tunnisteen historiatieto palveluun. Tämä tarkoittaa sitä, että mikäli henkilöiden tiedoista poistetuja RFID-tunnisteita halutaan käyttää uudelleen toisella henkilöllä. on ne lisättävä uusille henkilöille voimassaolotoimintoa käyttäen. RFID-tunnisteen voi lisätä voimassaolotoimintoa käyttämällä reittiä Työsuhde > valitse haluttu henkilö, jolle RFID-tunniste halutaan lisätä > Tunnisteet: RFID-tunniste. Voimassaolotoiminto (kalenterikuvakkeen näköinen painike) tulee näkyviin tekstikenttää (kenttä, johon arvo syötetään) painamalla. 
![](https://support.nepton.com/hc/article_attachments/22690557703325)
