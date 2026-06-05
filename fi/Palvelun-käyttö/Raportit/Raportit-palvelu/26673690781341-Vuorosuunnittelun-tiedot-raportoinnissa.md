---
id: 26673690781341
title: Vuorosuunnittelun tiedot raportoinnissa
url: https://support.nepton.com/hc/fi/articles/26673690781341-Vuorosuunnittelun-tiedot-raportoinnissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Raportit-palvelu
section_id: 25746849648925
section_path:
- Raportit
- Raportit-palvelu
labels: []
promoted: false
updated_at: '2025-09-29T08:53:43Z'
edited_at: '2025-09-29T08:53:43Z'
---

# Vuorosuunnittelun tiedot raportoinnissa

Tämä artikkeli liittyy Raportit-palveluun. Tarkat tietojen poimintoihin käytettävät tietokantakentät löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
##  Perusperiaatteet
Vuorosuunnitteluun tallennetusta tiedosta voidaan poimia:
  * Suunnitellut ja julkaistut vuorot riippumatta toteutustavasta
  * Vuorojen yhdistelmät, esimerkiksi: 
    * Kuinka paljon suunniteltu työtä pe-la, la-su ja su-ma yhdistelmille
    * Arkipyhille suunnitellut työt
  * Lepoaikojen seurantaan liittyvät, esimerkiksi: 
    * Erilaiset vuorotyypit, vain jos käytössä vuorokalenteri 
      * Esim kuinka monesti tehty iltavuoro -> aamuvuoro -yhdistelmiä
      * Perinteisellä tavalla (ei vuorokalentereilla) ei vuorotyyppejä eli ei voi saada tätä tietoa
  * Huomioitava, että poiminnoissa ei oteta huomioon vuorosuunnittelun kautta oletettua ruokataukoa. Esim: Suunniteltu 8h vuoro, josta automaattinen 30 min ruokatauko -> Saadaan siirtymään 8h vuoro. Ei siirry 7:30.


##  Mitä voidaan poimia
  * Asetettu vuosityöajan tavoite (minuutteina)
  * Henkilön vuorokalenterin koodi ja nimi
  * Henkilön lomakalenterin koodi ja nimi
  * Vuorosuunnittelun kautta ja vuorokalentereilla suunnitellut ja julkaistut vuorot (alku- ja loppuaika: päivä ja kellonajat)
  * Suunnitellun ja julkaistun vuoron 
    * suunniteltu tapahtumatyyppi (koodi)
    * lyhenne (vuorokalenterista)
    * vuorotyypin lisätieto
    * vuoron julkinen tieto (vuororyhmän julkista tietoa ei voida poimia raportille) 
      * Julkisesta tiedosta voidaan hakea myös haluttu merkki tai merkkijono (esim tietty sana).


##  Ei voida poimia
  * Vuorokalentereiden sisältöjä (skeemoja)
  * Lomakalentereiden sisältöjä (skeemoja)
  * Vuorotarpeita
  * Tehtäviä
  * Osaamisia
  * Vuororyhmän suunnittelutieto
  * Vuororyhmän julkinen tieto
  * Vuoron suunnittelutieto
