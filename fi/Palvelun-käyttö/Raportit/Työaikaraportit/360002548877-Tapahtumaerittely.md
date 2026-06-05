---
id: 360002548877
title: Tapahtumaerittely
url: https://support.nepton.com/hc/fi/articles/360002548877-Tapahtumaerittely
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työaikaraportit
section_id: 360005870318
section_path:
- Raportit
- Työaikaraportit
labels:
- NEPTONNEEDSREVIEW
- työaikaleimaustieto
- tapahtumatyyppiraportti
promoted: false
updated_at: '2026-03-23T12:59:39Z'
edited_at: '2026-03-23T12:59:39Z'
---

# Tapahtumaerittely

Tapahtumaerittelyllä voidaan raportoida tallennettuja sekä poistettuja tapahtumia. Raportin sisältöä on mahdollista rajata hakusanalla.
Tapahtuerittely löytyy palvelun työaika-puolelta valikossa**Työaika > Työtunnit > Raportit.**
Huomaathan, että tapahtumaerittely raportoi merkittyä työaikaa, ei tulkittua työaikaa. Oletetut tapahtumat näkyvät raportilla vain, jos ne on hyväksytty.
## Raportin valinnat
Raporttia ottaessa syötetään aikaväli, valinta halutaanko raportille myös poistetut tapahtumat sekä mahdollinen hakusana.
### Hakusanat
Hakusana etsii annettua merkkijonoa seuraavista tiedoista:
  * Tapahtuman tyypin nimi
  * Tapahtuman huomautus
  * Tapahtuman alkuaika (voidaan etsiä päivämäärällä muodossa pp-kk-vvvv, esim. 02-09-2021 tai kellonajalla muodossa hh:mm, esim. 08:00)
  * Tapahtumaan liitetyn projektin nimi
  * Tapahtumaan liitetyn projektin koodi
  * Tapahtumaan liitetyn projektin kuvaus


Hakusanaan voidaan antaa välilyönnillä monta eri sanaa, jolloin kaikkien hakusanojen tulee esiintyä hakutuloksessa. Hakutuloksesta voidaan poistaa avainsanalla laittamalla hakusanan eteen miinusmerkki. Haettavana merkkijonona voisi olla esimerkiksi 'matka-aika -toimisto', jolloin raportille haetaan ne tapahtumat, joissa esiintyy sana 'matka-aika', mutta ei esiinny sanaa 'toimisto'. Jos halutaan käyttää kahta eri hakusanaa, esim. tapahtumaa, voit tällöin kirjoittaa ne muotoon esim. Etätyö + Koulutus. Tämä etsii tuloksena päivät, joilla on joko Etätyötä, Etätyötä + Koulutusta ja vain Koulutusta.
![](https://support.nepton.com/hc/article_attachments/27307663615773)
Esimerkiksi hakemalla hakusanalla "matka-aika" sisältäen poistetut tapahtumat saadaan seuraava raportti:  
![](https://support.nepton.com/hc/article_attachments/27307663616413)
Tuloksissa on mukana sekä Työ-tapahtuma, jonka kommentissa ilmenee sana "Matka-aika", että erilaisia matka-aikatapahtumia, joista yksi on poistettu.
## Raportin tiedot
Raportin tiedot esitetään näytöllä. Tulokset voidaan myös viedä Exceliin tai tulostaa. Raportin tietoja voidaan suodattaa Excelissä sarakkeiden mukaan, jolloin voidaan tarkastella kirjattuja tietoja yksityiskohtaisella tasolla.
Raportin sarakkeet ovat;  
Henkilönumero - Henkilön henkilönumero (jos asetettu)  
Työntekijä - Henkilön nimi  
Henkilöryhmä - Henkilön henkilöryhmä (jos asetettu)  
Raportin lisätieto - Henkilön tietoihin tallennettu Raporteilla näkyvä lisätieto -kentän sisältö (jos asetettu)  
Tapahtumatyyppi - Käytetty tapahtumatyyppi  
Kirjauspäivä - Päivä, jolle tapahtuma on kirjattu  
Aloitusaika - Tapahtuman aloitusaika  
Lopetusaika - Tapahtuman lopetusaika  
Kesto - Tapahtuman kesto  
Projektit - Tapahtumaan liitetyt projektit  
Tapahtuman luoja - kuka on kirjannut tapahtuman  
Luotu - Koska tapahtuma on alunperin luotu  
Muokattu - Koska tapahtumaa on viimeksi muokattu  
Tapahtuman hyväksynyt - Kuka on hyväksynyt tapahtuman  
Tapahtuman huomautus - Tapahtuman huomautus -kentän teksti  
100% - onko tapahtuma manuaalisesti asetettua 100% ylityötä  
Kirjauspääte - Kirjauspäätteen ID, jos tapahtuma luotu kirjauspäätteellä
  
![](https://support.nepton.com/hc/article_attachments/27307661143325)
## Poistettujen tapahtumien raportointi
Mikäli raporttia otettaessa on valittuna valinta "Näytä myös poistetut tapahtumat", tulee raportille Poistettu-sarake, jossa näytetään tieto Kyllä/Ei. Poistetut tapahtumat näytetään raportilla harmaalla fontilla.
![](https://support.nepton.com/hc/article_attachments/27307781737117)
Poistetuista tapahtumista näytetään seuraavat tiedot:
  * Henkilönumero
  * Käyttäjän nimi (kenen kalenteriin tapahtuma lisättiin alunperin)
  * Henkilöryhmä
  * Raportin lisätieto
  * Käytetty tapahtumatyyppi
  * Kirjauspäivä (mille päivälle tapahtuma on kirjattu)
  * Tapahtuman aloitusaika, lopetusaika ja kesto
  * Tapahtuman projektit
  * Tapahtuman alkuperäinen luoja
  * Tapahtuman alkuperäinen luomisaika
  * Tapahtuman viimeisin muokkauspäivä (poistetussa tapahtumassa poistoaika)
  * Tapahtuman hyväksyjä (jos tapahtuma oli hyväksytty)
  * Tapahtuman huomautus (Lisätty kommentti)
  * 100% (oliko tapahtuma 100% ylityötä)
  * Poistettu-tieto (kyllä/ei)
  * Työaikapääte (Näyttää päätteen, jolla työtapahtuma on aloitettu, jos tapahtuma päätetään toisella päätteellä, se ei näy raportissa)


Tapahtuman poistaneen henkilön käyttäjätunnusta/nimeä ei tallenneta tai näytetä raportilla.
Tapahtuma voidaan avata uuteen ikkunaan "tapahtumatyyppi" sarakkeen tietoa klikkaamalla. Tästä ikkunasta poistettu tapahtuma voidaan myös palauttaa aktiiviseksi.
