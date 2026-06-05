---
id: 360019841477
title: Työajan API:n vastauskoodit
url: https://support.nepton.com/hc/fi/articles/360019841477-Ty%C3%B6ajan-API-n-vastauskoodit
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
- API
- vastauskoodit
- response code
promoted: false
updated_at: '2025-09-08T07:42:25Z'
edited_at: '2025-09-08T07:42:25Z'
---

# Työajan API:n vastauskoodit

Tässä artikkelissa kuvataan [Työajan API](<https://support.nepton.com/hc/articles/360004861558>) -menetelmien vastauskoodit ja käsittelyvirhevastaukset.
## Vastauskoodit (Response codes)
Vastauskoodit, jotka voidaan palauttaa ResponseCode-kenttään. Katso lisätietoja Virhevastausten käsittelystä.
  * 1000: Ei virheitä.
  * 1001: Todennus epäonnistui. Tarkista, että annetut CallerAuthentication-tunnistetiedot ovat oikein ja että työyhteisön Customer ID on olemassa.
  * 1002: Tapahtumaa ei löytynyt annetulla tunnisteella.
  * 1003: Henkilöä ei löytynyt annetulla tunnisteella.
  * 1004: Projektia ei löytynyt annetulla tunnisteella.
  * 1005: Pyynnössä ei annettu kaikkia tarvittavia asetuksia.
  * 1006: Asetus ei ollut kelvollinen puuttuvan tunnisteen vuoksi.
  * 1007: Asetus on virheellinen.
  * 1008: Nykyisen asetuksen käsittely epäonnistui.
  * 1009: Projekti on virheellinen.
  * 1010: Virhe tietokantayhteyden aikana.
  * 1011: Poistotoiminto epäonnistui tietokannassa.
  * 1012: Parametrit olivat virheellisiä.
  * 1013: Kohdepäivämääriä ei löytynyt.
  * 1014: Asetusta ei tunnistettu tai sitä ei tueta.
  * 1015: Ei oikeuksia hakea tai muokata pyydettyä objektia.
  * 1016: Tarjottua parametria ei tueta.
  * 1017: Nepton-palvelu ei tue pyydettyä toimintoa.
  * 1018: Liian monta epäonnistunutta kirjautumisyritystä henkilön tunnuksella tai IP-osoitteesta. Kirjautuminen on väliaikaisesti lukittu.
  * 1019: Yhden tai useamman luettelon kohteen käsittely epäonnistui – katso Virhevastausten käsittely.
  * 1020: Kirjautuminen epäonnistui, koska henkilön tili on poistettu käytöstä
  * 999: Odottamaton virhe. Viestin ResponseString -kentässä saattaa olla lisätietoja. Tarkista, että kaikki annetut parametrit ovat oikein. Tämä voi johtua myös Neptonin sisäisestä virheestä. Sinun on ehkä ilmoitettava tästä virheestä Neptonille.


## Virhevastausten käsittely
Kun päivität tietoja Neptoniin, on tärkeää tarkistaa, että ResponseCode on 1000. Jos ResponseCode on muu kuin 1000, jotain ei ole päivitetty oikein. Katso koodien selitykset yllä. ResponseString -kenttä voi sisältää yleistä tietoa virheestä, mutta saadaksesi tarkempaa tietoa siitä, missä ongelma tarkalleen esiintyy, sinun on tarkistettava vastauksen tiedot.
Esimerkiksi InsertActivities-pyyntö palauttaa luettelon tapahtumista Activity-elementteinä, jotka vastaavat pyynnön toimintoelementtejä Success-kentässä. Arvo on true (tosi) kullekin onnistuneesti lisätylle kentälle ja false (epätosi) tapahtumille, joissa on ongelmia. ErrorMessage-elementti puolestaan sisältää tiedot yksittäisestä kyseiseen kenttään liittyvästä ongelmasta.
Kutsuvan ohjelmiston vastuulla on näyttää tai tallentaa lokiin yksittäisiin viesteihin liittyvät asianmukaiset virheilmoitukset, koska virheilmoituksia ei mahdollisesti löydy Neptonista myöhemmin.
