---
id: 5529131389341
title: CGI Prima vuosiloma
url: https://support.nepton.com/hc/fi/articles/5529131389341-CGI-Prima-vuosiloma
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2022-08-25T10:12:53Z'
---

# CGI Prima vuosiloma

# Tiedostomuoto
Siirtotiedostona käytetään .dat-päätteistä tekstimuotoista tiedostoa. Jokainen merkintä on erotettu omalle rivilleen. Kentillä ei ole erotinta vaan ne tulkitaan suoraan niiden sijainnin ja pituuden mukaan. kaikki numeroarvot täytetään etunollilla tarvittavaan pituuteen ja kaikki merkkijonot saavat eteensä välimerkkejä mikäli sisältö on lyhyempi kuin kentän pituus.
Rivinvaihto merkki on CR+LF ja merkistökoodaus on ISO-8859-1.
Desimaalikentät tiedostossa käyttävät pistettä (.) desimaalierottimena ja sisältävät kaksi desimaalia. Päivämäärät ovat muodossa vvvvkkpp
# Rajaukset
Jokaiselle tiedostoon tulevalle riville/merkinnälle asetetaan yksilöllinen tunniste (Vuosiloman tunniste -kenttä), joka muodostetaan tapahtuman pohjalta. Tähän tiedostoon tulevat tiedot tulisi tämän takia poimintasäännössä ottaa tapahtuma-taulusta (UserEventData).
Poistettuja tapahtumia (tapahtumalaji 'P') voidaan myös siirtää. Poistetut tapahtumat löytyvät historia-taulusta, mutta tällöin pitää säännössä rajata ettei poimita myös historian kaikkia muutosrivejä.
# Aineiston tietueet
Sarake | Kuvaus | Sääntöjoukon kentän nimi | Muoto | Lisätiedot  
---|---|---|---|---  
A | Henkilötunnus | OverrideUserIntegrationId | merkkijono | Suomalainen henkilötunnus. Oletuksena poimitaan käyttäjän tiedoista. Ylikirjoitettavissa.  
B | Lomavuosi |  | number | Poimitaan loman päiväyksen perusteella  
C | Tapahtumalaji |  | merkkijono | Arvona joko 'L'(lisäys) tai 'P' (poisto).   
D | Loman alkupäivä |  | date | Vuosilomatapahtuman alkupäivä  
E | Loman päättymispäivä |  | date | Vuosilomatapahtuman loppupäivä  
F | Lomajakson tyyppi | VacationType | Merkkijono |  Mahdolliset arvot: 'L'(vloma), 'S'(svapaa), 'V'(vaihtovapaa), 'O' (osa-aik-vloma). Oletuksena arvo 'L'. Ylikirjoitettavissa  
G | Vuosiloman tunniste |  | aikaleima | Vuosiloman tunniste. Henkilötunnisteen kanssa yksilöi tämä merkinnän/rivin primassa. Muodostetaan Neptonin tapahtuman luontiajasta  
H | Maksutapa | PaymentType | Merkkijono | Maksutapa. Oletuksena tyhjä. 1=maksetaan etukäteen. Ylikirjoitettavissa  
I | Kesto |  | merkkijono | Siirretään aina tyhjänä  
J | Päättäjän tunnus | DecisionMakerId | merkkijono | maksimipituus 8-merkkiä. Oletuksena tyhjä. Voidaan ylikirjoittaa  
K | Päätöksen numero | DecisionNumber | merkkijono | Maksimipituus 10-merkkiä. Oletuksena tyhjä. Voidaan ylikirjoittaa  
L | Päätöksen päivämäärä | DecisionDate | date | Oletuksena tyhjä. Voidaan ylikirjoittaa  
M | Prosentti | Percentage | desimaali | Oletuksena tyhjä arvo. Osa-aikaisen lomatyypin prosentti. Pakollinen osa-aik. vlomalla
