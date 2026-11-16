---
id: 360005401578
title: Henkilöiden tuonti - Kieku "Työaikasäännöt"
url: https://support.nepton.com/hc/fi/articles/360005401578-Henkil%C3%B6iden-tuonti-Kieku-Ty%C3%B6aikas%C3%A4%C3%A4nn%C3%B6t
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
updated_at: '2026-06-26T06:36:51Z'
edited_at: '2026-06-26T06:36:51Z'
---

# Henkilöiden tuonti - Kieku "Työaikasäännöt"

Tämä tuontitapa on suunniteltu erityisesti Kieku-lähdejärjestelmälle ja "Työaikasäännöille". Se laajentaa yleisiä tuontisääntöjä erityisellä liiketoimintalogiikalla ja tietojen tunnisteilla. Katso myös [Kieku "Uudet tilit"](<https://support.nepton.com/hc/fi/articles/360005399958>) -tuontitapa varmistaaksesi, että valitset tarkoituksiisi oikean vaihtoehdon.  
Tämä tuontitapa on ensisijaisesti tarkoitettu XML-tiedostomuodolle, eikä siinä siksi ole määritelty sarakkeiden järjestystä. Tämä tekee solmunimistä pakollisia (tai sarakeotsikoista, jos käytetään muuta tiedostotyyppiä kuin XML).
# Kentät
Alla on luettelo tämän tuontitavan erityisistä tunnisteista ja kenttien käyttäytymisestä. Henkilön lisätietokenttiä voidaan tuoda käyttämällä [yleistä](<https://support.nepton.com/hc/fi/articles/360003762577>) tuontitapaa.
Tunniste | Tuontisarakkeen indeksi | Neptonin kenttään kohdistettu | Kuvaus  
---|---|---|---  
HenkiloNro | Ei sovellu | Henkilönumero |   
EtuNimi | Ei sovellu | Etunimi(t) |   
SukuNimi | Ei sovellu | Sukunimi |   
SahkopostiosoiteTeksti | Ei sovellu | Sähköposti |   
LahiOsoite | Ei sovellu | Katuosoite |   
PostiNro | Ei sovellu | Postinumero |   
PaikkakuntaKoodi | Ei sovellu | Kaupunki |   
PalvelussuhdeAlkuPvm | Ei sovellu | Sopimuksen alkamispäivä | Vain työntekijän työsopimuksen keston pidentämiseen  
PalvelussuhdeLoppuPvm | Ei sovellu | Sopimuksen päättymispäivä | Vain työntekijän työsopimuksen keston pidentämiseen  
TehtavaKuvausTeksti | Ei sovellu | Titteli |   
Organisaatiotaso1Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso2Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso3Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso4Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso5Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso6Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso7Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso8Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso9Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
Organisaatiotaso10Koodi | Ei sovellu | Käyttäjäryhmä | Kts. liiketoimintalogiikka  
# Liiketoimintalogiikka
  * **Ohita tiedot, joilla ei ole '**_**TyoAikaSuunnitelmaSaantoKoodi**_**'-solmua**   
Jokaisella tuotavalla henkilöllä on oltava XML-solmu nimeltä TyoAikaSuunnitelmaSaantoKoodi, jonka **kirjainkoolla on merkitystä** ja jonka arvo on 02 tai 03A. Muussa tapauksessa kyseisen henkilön tiedot ohitetaan.
  * **Käyttäjätunnus = henkilönumero**   
Käyttäjätunnus luodaan yleensä etu- ja sukunimien perusteella, mutta tässä kartoituksessa kopioidaan työntekijän numero.
  * **Henkilöryhmä OrganisaatiotasoKoodista**   
Henkilöryhmää päivitetään vain työsopimuksista tulevan tiedon perusteella, jotka kattavat nykyisen päivämäärän (eli alkamispäivä on <= nykyinen päivämäärä ja päättymispäivä > nykyinen päivämäärä)
    * Vain tällä hetkellä voimassa olevaan työ-sopimukseen liittyvät tiedot vaikuttavat henkilöryhmään
    * Vaikka OrganisaatiotasoKoodi -arvoja tuodaan jopa 10, uuden henkilöryhmän määrityksessä käytetään vain korkeimman kentän arvoa (missä Organisaatiotaso1Koodi on alin)
  * **Laajenna työsopimuksen kestoa**  

    * Jos henkilöllä on olemassa työsopimuksen alkamispäivä, tuotava alkamispäivä voi nollata olemassa olevan arvon tai muuttaa alkamispäivää aikaisemmaksi, mutta alkamispäivää ei voi muuttaa myöhemmäksi.
    * Jos henkilöllä on olemassa työsopimuksen päättymispäivä, tuotava päättymispäivä voi nollata olemassa olevan arvon tai muuttaa päättymispäivää myöhemmäksi, mutta päättymispäivää ei voi muuttaa aikaisemmaksi.
    * Nämä rajoitukset varmistavat, että henkilöitä, joilla on useita sopimuksia, voidaan tarkastella ja hallita oikein palvelussa
    * Esimerkkejä:
      *         1. Ei olemassa olevia työsopimuksen päiviä  
tuodut arvot  
PalvelussuhdeAlkuPvm: 20210501  
PalvelussuhdeLoppuPvm: 20220831  
tulos: 01.05.2021 - 31.08.2022 (uudet päivät voidaan lisätä, kun olemassa ei ole päiviä)
        2. Olemassa olevat työsopimuksen päivät 01.05.2021 - 31.08.2022  
tuodut arvot  
PalvelussuhdeAlkuPvm: 20210101  
PalvelussuhdeLoppuPvm: 20211231  
Tulos: 01.01.2021 - 31.08.2022 (alkamispäivää voi muuttaa aikaisemmaksi, mutta päättymispäivää ei)
        3. Olemassa olevat työsopimuksen päivät 01.01.2021 - 31.08.2022  
tuodut arvot  
PalvelussuhdeAlkuPvm: 20220101  
PalvelussuhdeLoppuPvm: 20221231  
Tulos: 01.01.2021 - 31.12.2022 (päättymispäivää voi jatkaa myöhemmäksi, mutta alkamispäivää ei)
        4. Olemassa olevat työsopimuksen päivät 01.01.2021 - 31.12.2022  
tuodut arvot  
PalvelussuhdeAlkuPvm:  
PalvelussuhdeLoppuPvm:  
Tulos: ei työsopimuksen alkamispäivää tai päättymispäivää (työsopimuksen alkamispäivä ja päättymispäivä voidaan aina tyhjentää)
  * **Sähköpostiosoite pieniksi kirjaimiksi**   
Kaikki sähköpostiosoitteet muunnetaan pieniksi kirjaimiksi
  * **Sähköposti ohitetaan, jos virheellinen**  
Sähköpostit, jotka eivät läpäise Neptonin sähköpostivarmennusta, jätetään pois tuonnista
