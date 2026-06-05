---
id: 360005399958
title: Henkilötuonti - Kieku "Uudet tilit"
url: https://support.nepton.com/hc/fi/articles/360005399958-Henkil%C3%B6tuonti-Kieku-Uudet-tilit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels:
- Person Import
promoted: false
updated_at: '2025-06-10T11:36:42Z'
edited_at: '2025-06-10T11:36:42Z'
---

# Henkilötuonti - Kieku "Uudet tilit"

Tämä tuontikartoitus on suunniteltu erityisesti Kieku-lähdejärjestelmää ja "uusia tilejä" varten. Se laajentaa yleisiä tuontisääntöjä erityisellä liiketoimintalogiikalla ja datatunnisteilla. Katso myös[ Kieku "Työaikasäännöt"](<https://support.nepton.com/hc/fi/articles/360005401578>) -kartoitus varmistaaksesi, että valitset oikean vaihtoehdon käyttötarkoituksiisi.
Tämä kartoitus on ensisijaisesti tarkoitettu XML-tiedostomuodolle, eikä siinä siksi ole määriteltyä sarakejärjestystä. Tämä tekee solmujen nimistä pakollisia (tai sarakeotsikoista, jos käytetään muita tiedostotyyppejä kuin XML).
## Kentät
Alla on luettelo tähän tuontitapaan liittyvien kenttien erityistunnisteista ja toiminnoista. Lisätietokenttiä voidaan tuoda [yleisten tuontiohjeiden](<https://support.nepton.com/hc/fi/articles/360003762577>) avulla.
Tunniste | Tuonnin sarake indeksi | Liitetty Neptonin kenttään | Kuvaus  
---|---|---|---  
HenkiloNro | N/A | Henkilönumero |   
EtuNimi | N/A | Etunimi |   
SukuNimi | N/A | Sukunimi |   
SahkopostiosoiteTeksti | N/A | Sähköpostiosoite |   
LahiOsoite | N/A | Katuosoite |   
PostiNro | N/A | Postinumero |   
PaikkakuntaKoodi | N/A | Postitoimipaikka |   
PalvelussuhdeAlkuPvm | N/A | Työsuhteen alkupäivä | Voi vain venyttää työsuhteen kestoa  
PalvelussuhdeLoppuPvm | N/A | Työsuhteen päättymispäivä | Voi vain venyttää työsuhteen kestoa  
TehtavaKuvausTeksti | N/A | Ammattinimike |   
Organisaatiotaso1Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso2Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso3Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso4Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso5Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso6Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso7Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso8Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso9Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
Organisaatiotaso10Koodi | N/A | Henkilöryhmä | Katso kohta "logiikka"  
## Logiikka
  * **Henkilönumerosta tulee automaattisesti käyttäjätunnus**  
Koska Kieku-järjestelmässä ei ole henkilön käyttäjätunnusta ja Neptonissa käyttäjätunnus on pakollinen, käytetään henkilönumeroa uusien tuotujen henkilöiden käyttäjätunnuksena. Jos tuotavat tiedot sisältävät käyttäjätunnuksen, sitä käytetään henkilönumeron sijaan.
  * **Vain voimassa olevien työsopimusten tiedot huomioidaan  
** Tämä liittymätapa sisältää tietoja vain aktiivisista työsopimuksista. 
    * Aktiiviset sopimukset määritetään tyosuhdetilakoodi-solmun perusteella, joka sijaitsee palvelusuhdetyyppi-solmun alla. Jos arvo on 3, sopimusta pidetään aktiivisena. Muussa tapauksessa se katsotaan passiiviseksi ja ohitetaan.
  * **Henkilöryhmä OrganisaatiotasoKoodi:sta**  

    * Henkilöryhmää päivitetään vain aktiivisista työsopimuksista tulevilla tiedoilla, jotka kattavat myös kuluvan päivämäärän (eli aloituspäivämäärä on <= kuluva päivämäärä ja päättymispäivämäärä > kuluva päivämäärä).
    * Eli vain aktiiviseen työsopimukseen liittyvät tiedot vaikuttavat henkilöryhmään.
    * Vaikka OrganisaatiotasoKoodiin tuodaan jopa 10 arvoa, vain korkeimman kentän arvoa käytetään uuden henkilöryhmän määrittämiseen (jossa Organisaatiotaso1Koodia pidetään pienimpänä).
  * **Venytä työsuhteen kestoa  
** Katso lisätiedot [täältä.](<https://support.nepton.com/hc/fi/articles/13129687045789>)
  * **Sähköpostiosoite pieniksi kirjaimiksi**  
Kaikki sähköpostiosoitteet muuttuvat pieniksi kirjaimiksi.
  * **Sähköposti ohitetaan jos se on viallinen**  
Sähköpostit, jotka eivät läpäise Neptonin sähköpostivahvistusta, ohitetaan eikä niitä tuoda.
