---
id: 26673567254173
title: Tapahtumien ja tulkitun työajan tiedot raportoinnissa
url: https://support.nepton.com/hc/fi/articles/26673567254173-Tapahtumien-ja-tulkitun-ty%C3%B6ajan-tiedot-raportoinnissa
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
updated_at: '2025-09-01T08:58:06Z'
edited_at: '2025-08-20T04:43:13Z'
---

# Tapahtumien ja tulkitun työajan tiedot raportoinnissa

Tämä artikkeli liittyy Raportit-palveluun. Tarkat tietojen poimintoihin käytettävät tietokantakentät löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
##  Perusperiaatteet
Työaikatiedoista voidaan poimia
  * Merkityt tapahtumat sellaisenaan
  * Merkityt tapahtumat mukaan lukien 
    * Aiemmat versiot
    * Poistetut tapahtumat
    * Asetetulla aikavälillä muokatut tapahtumat
  * Tulkittu työaikatieto


Tulkitusta työaikatiedosta ja merkityistä tapahtumista voidaan poimia mm. seuraavat tiedot
  * Erilaiset palkkalajit (esim. säännöllinen työaika, tunti tunnista korvattava aika, ylityöt (lisätyö, ylityö, TES-ylityö, tasoittumisjakson ylityöt), työkorotukset, työlisät, aloitus- ja lopetustyö ja niihin liittyvät ylityöt)
  * Mikä on tapahtumalle valittu ylityön kohdenne
  * Kertymien juoksevat/kumulatiiviset arvot, sekä kertymän muutos edellisestä päivästä
  * Kertymistä automaattisesti leikatut tunnit
  * Ruokatauko (kertoo, miten ruokatauko on laskennallisesti sijoitettu päivään)
  * Varallaolo (toteutunut määrä; muut merkityt päällekkäisyydet vähentää tätä aikaa)
  * Työaikarajoilla rajatut työajat (esim sallituilla työajoilla)
  * Kertymärajoilla leikatut tunnit (myös vakioraportilla ’Saldon hallinnolliset muutokset’)
  * Tapahtuman hyväksyneen henkilön tiedot
  * Hyväksymättömät tapahtumat


Tiedot voidaan ryhmitellä raportille laajasti eri tavoilla, yleisimpiä tapoja esimerkiksi
  * Tapahtumatyypin mukaan
  * Merkityn tapahtuman mukaan (esim. pitkäaikainen poissaolo)
  * Haetun ajanjakson mukaan
  * Korvaustyypin mukaan
  * Palkkalajin mukaan
  * Sen mukaan, millä päivällä työ on tehty 
    * Esimerkkejä: 
      * Voidaan määritellä vuorokauden yli jatkuva työ näkymään edellisellä päivällä (SalaryRenderingDate)
      * Voidaan määritellä ryhmittely haetun ajanjakson sisällä: esimerkiksi haetaan 6 kuukauden jakso, mutta tulokset näytetään kuukausittain yhteenlaskettuna


##  Mitä voidaan poimia
  * Määrä (tapahtuman kesto) 
    * Oletuksena arvo sekunneissa kaikissa muissa kuin kokonaisluvuissa
    * Voi olla muodossa kokonaisluku, desimaalikulu, sekunteja, tunteja, päiviä tai valuutta
  * Alkupäivä ja -aika, milloin 
    * Tulkittu työaika on ansaittu
    * Tulkittuun työaikaan liittyvä tapahtuma on merkitty
  * Loppupäivä ja -aika, milloin 
    * Tulkittu työaika on ansaittu
    * Tulkittuun työaikaan liittyvä tapahtuma on merkitty
  * Tapahtuman luomis- ja muokkausaika
  * Tapahtuman yksilöllinen tunniste 
    * Käytetään ryhmittelyyn (esim. vuosilomapalkka)
  * Tapahtuman kommentti (maks 2000 merkkiä)
  * Päivä, johon maksu/vuoro kuuluu
  * Tapahtumalle kirjattu aika 
    * Kirjauksen kellonajat
    * Ei muodosteta juhlapyhistä tai kertymien muutos- ja asetustapahtumista
  * Maksupäivä (Nepton Palkat)
  * Tapahtumatyypin koodi
  * Työkorotuksen järjestysnumero Neptonin asetuksissa
  * Työkorotuksen palkkakoodi
  * Työkorotuksen korvauksen kertymäkohdenne (palkkaan, saldoon, tai muuhun kertymään) 
    * Voidaan eritellä ylityön perusosa ja korotusosa
  * Työkorotuksen korotusprosentti ja minuuttia-/tunti-korotus
  * Tapahtuman ylityöprosentti, josta työkorotus on muodostunut
  * Työlisän nimi
  * Työlisän järjestysnumero (Neptonin asetuksissa)
  * Työlisän palkkalajinumero (Neptonin asetuksissa)
  * Työlisän päivämääräkenttä
  * Työlisän kommentti
  * Työlisän tyyppi (normaali, korjaus, ruokalapäätetyölisä, jne)
  * Työlisän korotusprosentti (kun kohdennettu kertymään) 
    * Esim jos halutaan seurata paljon on maksettu saldoja ulos henkilölle
  * Palkan perusosan kohdistus (esim saldoon)
  * Tulkittu työaika perustuen ylityön perusosan kohdistukseen (BasePartTarget), esim. palkkaan, saldoon, kun ei korvata.
  * Tulkittu työaika perustuen ylityön korotusosan kohdistukseen (OvertimeTarget), esim. palkkaan, saldoon, kun ei korvata.
  * Onko tapahtuma hyväksytty vai ei
  * Onko tapahtuma pyyntö-tyyppinen tapahtuma
  * Tapahtuman hyväksyjä (sisäinen tunniste, etu- ja sukunimi ja/tai henkilönumero) 
    * Tasoittumisjakson ja viikkolepoajan korvauksissa käytetään jakson viimeisen viikon viimeistä hyväksyjää
  * Sen kirjauspäätteen ID, jolla tapahtuma on aloitettu. 
    * Mikäli tapahtuma aloitetaan kirjauspäätteellä, mutta lopetetaan jotain muuta tapaa käyttäen, esimerkiksi mobiililaitteella, niin tapahtuman terminalID häviää lopetuskirjauksen yhteydessä. 


##  Mitä ei voida poimia
  * Projektituntien hyväksyjä
  * Tapahtumien liitteet
  * Vuosilomakertymän määrää
