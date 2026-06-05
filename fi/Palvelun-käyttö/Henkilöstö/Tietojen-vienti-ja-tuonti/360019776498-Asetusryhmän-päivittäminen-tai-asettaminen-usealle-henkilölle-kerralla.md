---
id: 360019776498
title: Asetusryhmän päivittäminen tai asettaminen usealle henkilölle kerralla
url: https://support.nepton.com/hc/fi/articles/360019776498-Asetusryhm%C3%A4n-p%C3%A4ivitt%C3%A4minen-tai-asettaminen-usealle-henkil%C3%B6lle-kerralla
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
- massamuutos
promoted: false
updated_at: '2024-11-18T14:31:33Z'
edited_at: '2024-08-23T10:58:31Z'
---

# Asetusryhmän päivittäminen tai asettaminen usealle henkilölle kerralla

Jos halutaan siirtää henkilöitä massana toiseen asetusryhmään, on tähän useita eri toteutusvaihtoehtoja. Tässä artikkelissa kuvataan kaikki vaihtoehdot ja niihin liittyvät yksityiskohdat.
Katso myös yksittäisen henkilön asetusryhmän päivittämisen tai asettamisen ohje [tästä artikkelista.](<https://support.nepton.com/hc/fi/articles/360002557357>)
## Henkilöiden siirtäminen asetusryhmään siitä hetkestä, kun muutos tehdään - Työaika-osio
\- Valitse**Työaika - > Hallinta -> Asetusryhmät -> Asetusryhmä: Valitse asetusryhmä, johon haluat siirtää henkilöt -> Toiminto: Asetusryhmän jäsenet.**
\- Tämän jälkeen valitse henkilön nimen edessä oleva valintakenttä kaikkien niiden henkilöiden kohdalta, jotka haluat siirtää tähän ryhmään.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080521254173)
\- Valitse sivun alareunasta **Tallenna**.  
  
Tällä toteutustavalla henkilöt siirretään ko. asetusryhmään alkaen siitä päivästä, jolloin tallennus tehdään.
## Henkilöiden siirtäminen asetusryhmään siitä hetkestä, kun muutos tehdään - Työsuhde-osion massa-ajo
\- Valitse **Työsuhde - > Henkilöt -> Henkilöt.**
\- Valitse **Vie sisäänluettavaan Exceliin**. Avaa Excel, joka latautuu. Excelissä näet sarakkeen 'Työajan asetusryhmä'.
\- Jätä listalle vain ne henkilöt, joiden asetusryhmän haluat muuttaa (poista tiedostolta kokonaan kaikki muut henkilöt).
\- Jätä listalle vain sarakkeet 'Henkilönumero', 'Etunimi', 'Sukunimi' ja 'Työajan asetusryhmä'.
\- Täydennä tiedostoon 'Työajan asetusryhmä' -sarakkeeseen sen asetusryhmän koodi, johon haluat siirtää henkilöt.
\- Tallenna tiedosto (nimellä ei merkitystä).
Esimerkkikuva tiedoston sisällöstä:
![mceclip1.png](https://support.nepton.com/hc/article_attachments/21080521256093)
\- Valitse **Työsuhde - > Henkilöt -> Tuo henkilöitä**. Lataa tallentamasi tiedosto.  
  
Tällä toteutustavalla henkilöt siirretään ko. asetusryhmään alkaen siitä päivästä, jolloin tallennus (tiedoston ajo) tehdään. Tällä toteutustavalla voidaan muokata myös muita henkilöiden tietoja massana samalla, jos halutaan. Tällöin jätetään tiedostoon ne sarakkeet jotka halutaan päivittää. Päivitys on kaikkien sarakkeiden kohdalla voimassa siitä hetkestä, kun tiedosto ajetaan sisään.
## Henkilöiden siirtäminen asetusryhmään mistä päivästä tahansa eteenpäin - myös takautuvasti - Työaika-osio
Henkilöt voidaan siirtää asetusryhmään myös siten, että voidaan valita mistä päivästä eteenpäin muutos on voimassa. Tämä muutos voidaan tehdä massana tai yksitellen jokaiselle henkilölle [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
## Asetusryhmän muokkaaminen usealle henkilölle (voimassaolo alkaen menneisyydessä tai tulevaisuudessa)
Asetusryhmän muokkaaminen usealle henkilölle siten, että asetusryhmän voimassaolopäivä on menneisyydessä tai tulevaisuudessa tehdään samoin kuin kohta 2. (Henkilöiden siirtäminen asetusryhmään siitä hetkestä, kun muutos tehdään - Työsuhde-osion massa-ajo), mutta siirrettävään Excel-tiedostoon sisällytetään myös kenttä 'Voimassa alkaen'.
Esimerkkikuva tiedoston sisällöstä:
![mceclip2.png](https://support.nepton.com/hc/article_attachments/21080526335005)
## Asetusryhmän muokkaaminen yksitellen voimassaolotoiminnon kautta (voimassaolo alkaen menneisyydessä tai tulevaisuudessa)
\- Valitse**Työaika - > Hallinta -> Asetusryhmät -> Asetusryhmä: Mikä tahansa asetusryhmä -> Toiminto: Asetusryhmän jäsenet.**  
\- Valitse henkilö, jonka asetusryhmää haluat muuttaa.
\- Valitse henkilön nimen vierestä kalenterikuvakkeen kuva eli [voimassaolotoiminto](<https://support.nepton.com/hc/fi/articles/360002559358>).
\- Valitse **Lisää asetusarvo**. Merkitse tähän uusi asetusryhmä alasvetovalikosta.
\- Valitse vanhalle asetusryhmälle voimassaolopäivät ja uudelle (juuri lisäämällesi riville) voimassa alkaen -päivämäärä.
\- Valitse ponnahdusikkunasta **Tallenna**. Ponnahdusikkuna sulkeutuu ja muutos on voimassa niiden päivämäärien mukaisesti, jotka valitsit. Muutosta ei tarvitse tallentaa erikseen listauksen alareunasta.  
  
Jos muutos tehdään menneisyyteen, tulee henkilöiden kalenterit vielä päivittää, jotta muutos päivittyy voimaan. Ohjeet kalenterin uudelleenlasketukseen löytyy [täältä](<https://support.nepton.com/hc/fi/articles/4411220910865>).
