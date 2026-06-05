---
id: 5359083245341
title: CGI Prima, poissaolot
url: https://support.nepton.com/hc/fi/articles/5359083245341-CGI-Prima-poissaolot
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
edited_at: '2022-08-25T10:12:34Z'
---

# CGI Prima, poissaolot

# Tiedostomuoto  
Siirtotiedostona käytetään .dat-päätteistä tekstimuotoista tiedostoa. Jokainen merkintä on erotettu omalle rivilleen. Kentillä ei ole erotinta vaan ne tulkitaan suoraan niiden sijainnin ja pituuden mukaan. kaikki numeroarvot täytetään etunollilla tarvittavaan pituuteen ja kaikki merkkijonot saavat eteensä välimerkkejä mikäli sisältö on lyhyempi kuin kentän pituus.
Rivinvaihto merkki on CR+LF ja merkistökoodaus on ISO-8859-1.
Desimaalikentät tiedostossa käyttävät pistettä (.) desimaalierottimena ja sisältävät kaksi desimaalia. Päivämäärät ovat muodossa vvvvkkpp
# Rajaukset
Jokaiselle tiedostoon tulevalle riville/merkinnälle asetetaan yksilöllinen tunniste (poissaolon tunniste -kenttä), joka muodostetaan tapahtuman pohjalta. Tähän tiedostoon tulevat tiedot tulisi tämän takia poimintasäännössä ottaa tapahtuma-taulusta (UserEventData).
Poistettuja tapahtumia (tapahtumalaji 'P') voidaan myös siirtää. Poistetut tapahtumat löytyvät historia-taulusta, mutta tällöin pitää säännössä rajata, ettei poimita myös historian kaikkia muutosrivejä.
# Aineiston tietueet
Sarake | Kuvaus | Sääntöjoukon kentän nimi | Muoto | Lisätiedot  
---|---|---|---|---  
A | Henkilötunnus | OverrideUserIntegrationId | merkkijono | Oletuksena henkilötunnus käyttäjän tiedoista. Ylikirjoitettavissa  
B | Poissaolon koodi |  | merkkijono | Asetuksiin määritetty tieto. maksimipituus 3-kirjainta  
C | Tapahtumalaji |  | merkkijono | Arvona joko 'L'(lisäys) tai 'P' (poisto)   
D | Poissaolon alkupäivä |  | date | poissaolotapahtuman alkupäivä  
E | Poissaolon loppupäivä |  | date | poissaolotapahtuman loppupäivä  
F | Poissaolon tunniste |  | aikaleima(sekunnin sadasosan tarkkuudella) | Tunniste, joka henkilötunnuksen kanssa tunnistaa tämän merkinnän Primassa.  
G | Poissaolon tunnit | AbsenceHours | desimaali | Ilmoitettava, jos poissaolo on tuntiperusteinen. Oletuksena tyhjä. Ylikirjoitettavissa  
H | Poissaoloprosentti | Percentage | desimaali | Osa-aikaisen poissaolon poissaoloprosentti. Oletuksena tyhjää.  
I | Jatkoloma | IsContinuationLeave | bool | Onko jatkoa edelliseen lomaan? Oletuksena tyhjä. Voidaan ylikirjoittaa  
J | Päättäjän tunnus | DecisionMakerId | merkkijono | maksimipituus 8-merkkiä. Oletuksena tyhjä. Voidaan ylikirjoittaa  
K | Päätöksen numero | DecisionNumber | merkkijono | Maksimipituus 10-merkkiä. Oletuksena tyhjä. Voidaan ylikirjoittaa  
L | Päätöksen päivämäärä | DecisionDate | date | Oletuksena tyhjä. Voidaan ylikirjoittaa
