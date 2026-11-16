---
id: 17842757043613
title: Käyttöoikeusryhmät
url: https://support.nepton.com/hc/fi/articles/17842757043613-K%C3%A4ytt%C3%B6oikeusryhm%C3%A4t
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Oikeudet
section_id: 360000705217
section_path:
- Oikeudet
labels: []
promoted: false
updated_at: '2026-10-13T08:09:14Z'
edited_at: '2026-10-13T08:08:26Z'
---

# Käyttöoikeusryhmät

Tässä artikkelissa kerrotaan käyttöoikeusryhmien käyttöönotosta ja hyödyntämisestä organisaatiossa. Käyttöoikeusryhmät mahdollistavat tarkkaan määritellyn oikeuksien hallinnan Neptonissa. Käyttöoikeusryhmässä voidaan määritellä mihin tietoihin käyttäjällä on katseluoikeudet ja mihin tietoihin muokkausoikeudet. Käyttöoikeusryhmiä käytetään uuden konseptin, pääsy henkilöryhmiin, kanssa. Tämä mahdollistaa käyttäjille erilaisten oikeuksien antamisen eri henkilöryhmiin. Käyttäjän ei tarvitse olla henkilöryhmän jäsen, vaan hänelle annetaan pääsy valittuihin henkilöryhmiin.
Käyttöoikeusryhmät soveltuvat erityisesti isojen yritysten tarpeisiin ja mahdollistavat tarkan pääsynhallinnan organisaatiorakenteen ja roolien mukaisesti. Käyttöoikeusryhmiä luodessasi voit ottaa tietosuojan huomioon erityisellä tavalla, koska voit antaa käyttäjille pääsyn ainoastaan niihin tietoihin ja niihin ryhmiin, joita he roolissaan tarvitsevat.
## Käyttöönotto
Tässä lyhyt ohje käyttöoikeusryhmien käyttöönottoon:
  1. **Henkilöryhmien luominen** : Mikäli organisaatioon ei ole vielä luotu henkilöryhmiä, luodaan sopivat henkilöryhmät, jotka edustavat organisaatiorakennetta, tiimejä tai rooleja. Tämä tehdään osiossa _Työaika > Hallinta > Henkilöryhmät._
  2. **Käyttöoikeusryhmän luominen** : Luodaan käyttöoikeusryhmä, johon määritellään halutut oikeudet, kuten tiettyjen tietojen katseluoikeudet ja tiettyjen tietojen muokkausoikeudet. Tämän pääsevät tekemään "Ylläpitäjä", "Henkilöstöhallinto" ja "Palkkahallinto"-rooleissa olevat osiossa _Työsuhde > Oikeudet > Käyttöoikeusryhmät._
  3. **Asetetaan oikeudet henkilön tiedoissa** : Valitaan henkilö, jolle halutaan antaa oikeuksia. Henkilön tiedoissa kohdassa _Pääsy henkilöryhmiin_ valitaan käyttöoikeusryhmä, joka määrittelee mitä oikeuksia henkilöllä on. Tämän lisäksi valitaan henkilöryhmä, joka määrittelee, mihin ryhmään henkilöllä on kyseiset oikeudet. Pääsy henkilöryhmiin kenttää pääsevät muokkaamaan "Ylläpitäjä", "Henkilöstöhallinto" ja "Palkkahallinto"-rooleissa olevat.


Mikäli henkilölle on asetettu useita oikeuksia eri henkilöryhmiin siten, että ne ovat päällekäisiä (henkilöllä on useampi kuin yksi suhde henkilöryhmään, suoraan tai periytymisen kautta), käyttöoikeudet yhdistyvät.
## Esimerkkejä käyttötapauksista
**Vastaanottovirkailija**
  * Luodaan käyttöoikeusryhmä nimeltä "Vastaanottovirkailija", jolla on oikeudet nähdä ihmisten nimet ja puhelinnumerot sekä muokata RFID-tunnisteita.
  * Vastaanottovirkailijana toimivalle henkilölle annetaan "Vastaanottovirkailijan" oikeudet suhteessa henkilöryhmään, joka edustaa fyysistä sijaintia esim. Espoon toimipistettä. Espoon toimipiste -henkilöryhmällä voi olla useita alaryhmiä.
  * Vastaanottovirkailijalla on nyt pääsy etsiä ja tarkastella kaikkia Espoossa työskenteleviä henkilöitä, nähdä heidän nimensä ja puhelinnumeronsa sekä muokata/lisätä RFID-tunnisteita vastaanoton tiskillä, joita tarvitaan rakennukseen pääsyyn.


**Maan raportoija**
  * Luodaan käyttöoikeusryhmä nimeltä "Raportoija", jolla on oikeudet ainoastaan tarkastella ja raportoida ei-sensitiivisiä työaikatietoja, kuten tapahtumien tunteja, projekteja ja perustietoja poissaoloista.
  * Maan raportoinnista vastaavalle henkilölle annetaan "Raportoijan" oikeudet yhdistettynä maatason henkilöryhmään, joka mahdollistaa kyseisen maan kaikkien työaikatietojen raportoinnin.


## Työajan oikeudet
Tällä hetkellä tuetut työajan oikeudet, jotka voidaan antaa käyttöoikeusryhmällä (merkattu x:llä).
| **Tarkastelu** | **Muokkaus** | **Hyväksyntä**  
---|---|---|---  
Työajan tapahtumat | x | x* | x  
Sairausloman sairaustodistus | x | x | -  
Sairausloman palkallisuus | x | x | -  
Sairausloman syykoodi | - | x | -  
Työajan tapahtumian liitteet | x | x | -  
Henkilöiden asetukset ja projektit työajassa** | - | x | -  
*Oikeus muokata tapahtumia antaa myös oikeuden määrittää poissaolon palkallisuus (palkallinen, vähennetty palkka, palkaton) sekä muokata työpäivän ja työviikon pituutta ja oletettuja sekä sallittuja työaikoja.
** Muokkausoikeus henkilöiden asetuksiin ja projekteihin työajassa sisältää myös lukitusoikeiden.
## Henkilötietokenttien oikeudet
Kaikkiin henkilötietokenttiin voidaan antaa oikeudet käyttöoikeusryhmällä.
## Vuorosuunnittelun oikeudet
Vuorosuunnittelun oikeuksilla määritellään, voiko käyttäjä tarkastella vuoropohjalle liitettyjä toimipisteitä vai myös lisätä ja muokata niitä. 
Tarkasteluoikeudella käyttäjä näkee, mille toimipisteille vuoropohja on lisätty. Muokkausoikeus antaa laajemmat valtuudet: sen avulla käyttäjä voi lisätä uusia toimipisteitä ja muokata olemassa olevia suoraan vuoropohjalla sekä valita toimipisteen jo vuoropohjaa luotaessa.
