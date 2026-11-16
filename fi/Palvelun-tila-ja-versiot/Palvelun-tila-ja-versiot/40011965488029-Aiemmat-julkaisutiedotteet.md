---
id: 40011965488029
title: Aiemmat julkaisutiedotteet
url: https://support.nepton.com/hc/fi/articles/40011965488029-Aiemmat-julkaisutiedotteet
locale: fi
category: Palvelun tila ja versiot
category_id: 22476701377821
section: Palvelun tila ja versiot
section_id: 360000934197
section_path:
- Palvelun tila ja versiot
labels: []
promoted: false
updated_at: '2026-10-19T11:42:18Z'
edited_at: '2026-10-19T11:28:31Z'
---

# Aiemmat julkaisutiedotteet

Tässä artikkelissa listataan aiemmat julkaisutiedotteet, jotta julkaisutiedotesivu ei kasvaisi liian pitkäksi. Uusimmat julkaisutiedotteet voit lukea [täältä](<https://support.nepton.com/hc/fi/articles/360006615478>). 20.9.2025 vanhemmat julkaisutiedotteet löytyy [täältä](<https://support.nepton.com/hc/fi/articles/4408626793105>).
##  **22.09.2026** julkaisu (2.17.62)
###  __ Parannus
  * #### Neptonin Microsoft-kirjautuminen tukee nyt Microsoftin v2-identiteettialustaan perustuvaa uutta tunnistautumisprosessi
Olemassa oleviin Microsoft-kirjautumisen määrityksiin ei tule muutoksia.
[ref ND-5141]


###  __ Korjaus
  * #### Projektiasetukset eivät näkyneet asetusryhmätasolla.
[ref ND-5062]


##  **08.09.2026** julkaisu (2.17.61)
###  __ Parannus
  * #### Kertymien ansainnan kynnysarvojen määrä on nostettu 80 rivistä 150 riviin
Tyhjät kynnysarvojen asetusrivit on piilotettu ja niitä voi lisätä "Lisää ansainnan kynnysarvo" -painikkeella.
[ref ND-2846]


###  __ Muutos
  * #### Popup-ohjeistuksia ei enää esitetä Neptonin mobiiliversion työpöytänäkymässä
[ref ND-4957]


###  __ Korjaus
  * #### Liittymät-osio ja sen asetukset saattoivat avautua hitaasti ympäristöissä, joissa oli runsaasti liittymätoteutuksia
[ref ND-4375]


##  **25.08.2026** julkaisu (2.17.60)
###  __ Korjaukset
  * #### Raportointijakson päivämäärien muuttujat eivät olleet käytettävissä mukautettavilla raporteilla.
[ref ND-4865]
  * #### Sairauspoissaolot henkilöryhmittäin -raportti kaatui, mikäli valittuna oli tyhjä henkilöryhmä.
[ref ND-4948]
  * #### Korjattu ongelma, joka saattoi aiheuttaa Microsoft-kirjautumisten epäonnistumisen osalla käyttäjistä tietyillä tunnistautumiskäytäntöjen asetuksilla.
[ref ND-4952]


##  **23.08.2026** julkaisu (2.17.59)
###  __ Parannus
  * #### Sisäiset parannukset
[ref ND-4952]


##  **22.08.2026** julkaisu (2.17.58)
###  __ Korjaus
  * #### Microsoft-kirjautumisen korjaus.
Parannettu yhteensopivuutta Microsoft Entra ID:n Conditional Access -tunnistautumiskäytäntöjen kanssa vaikutuksen piirissä olevien käyttäjien kirjautumisongelmien ehkäisemiseksi.
[ref 4952]


##  **18.08.2026** julkaisu (2.17.57)
###  __ Parannukset
  * #### Suunnittelijat voivat määrittää sallitut työajat vuorojen, vuoropohjien ja vuorokalenterien kautta.
    * Vuorosuunnittelijat voivat nyt määrittää sallitut työajat suoraan vuorosuunnittelun työkaluilla yksittäisille vuoroille, vuoropohjien vuoroille ja vuorokalentereiden vuoroille.
    * Sallitut työajat voidaan määrittää kahdella tavalla:
      * Tarkat kellonajat (esim. 07:00 - 18:00).
      * Aloitus- ja lopetusajan poikkeamat vuoron ajoista (esim. 30 minuuttia ennen vuoron alkua, 15 minuuttia vuoron päättymisen jälkeen).
    * Vuorosuunnittelussa määritetyt sallitut työajat vuoroille ohittavat Työajassa määritetyt sallitun työajan asetukset.
      * Jos sallittuja työaikoja ei ole määritelty vuorosuunnittelussa, käytetään Työajan asetuksissa määritettyjä sallittuja työaikoja.
[ref ND-2806]
  * #### Yksittäisen viikkolepokorvauksen kohdentaminen kertymään.
    * Uusi tapahtumatyyppi "Viikkolepokorvauksen siirto" mahdollistaa yksittäisen viikkolepokorvauksen kohdentamisen tiettyyn kohteeseen asetusten oletuskohteen sijaan.
    * Uusi Työajan asetus "Työtunnit > Viikkolepo > Viikkolepokorvaus > voidaan siirtää kertymään" määrittää ne kertymät, joihin viikkolepokorvaus voidaan siirtää.
[Ohje](<https://support.nepton.com/hc/fi/articles/360007389978>)  
[ref ND-4314]
  * #### Päällekkäisten työkorotusten ansaintajärjestys.
    * Uusi työkorotusten asetus "Päällekkäisten työkorotusten ansaintajärjestys" määrittää, mikä työkorotuksista ansaitaan, kun niiden ansaintakaudet menevät päällekkäin. Ensisijainen työkorotus ansaitaan täysin, ja alemman prioriteetin työkorotuksesta/työkorotuksista vähennetään työkorotusten ansaintakausien päällekkäinen osuus. Muut osat maksetaan normaalisti.
    * Jos asetusta ei ole määritetty, työkorotukset ansaitaan aiempaan tapaan.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002560978>)  
[ref ND-4341]


###  __ Korjaukset
  * #### Mukautettujen raporttien avaaminen Excelissä kaatui joissain tilanteissa.
[ref ND-3886]
  * #### Joitain liittymäasetuksia näytettiin virheellisesti käyttäjä- ja asetusryhmätasoilla, vaikka ne olivat käytettävissä vain työyhteisötasolla.
[ref ND-4360]
  * #### Microsoft Login -kirjautumisen ongelma.
Sisäänkirjautuminen epäonnistui evästeiden poistumisen vuoksi, mikä johti palautumiseen takaisin Neptonin kirjautumissivulle.
[ref ND-4681]


##  **11.08.2026** julkaisu (2.17.56)
###  __ Korjaukset
  * #### SD Worx (Erot) -liittymä ei jakanut tiedostoja asetuksen "Jaa tiedostoihin arvoilla" mukaisesti silloin, kun liittymä muodosti erotusrivejä.
[ref ND-2849]
  * #### ZIP-tiedostojen lähettäminen sähköpostitse ei ollut mahdollista liittymien historianäkymässä.
[ref ND-3520]
  * #### Henkilöt, joiden Rooli on "Henkilöstöhallinto" eivät nähneet henkilöiden vuoroja suunnittelunäkymässä.
[ref ND-3568]
  * #### Hyväksy tunteja -näkymän avaaminen saattoi joissain tapauksissa päätyä virheeseen. 
[ref ND-4867]


##  **04.08.2026** julkaisu (2.17.55)
###  __ Korjaus
  * #### Joillain asiakkaillamme Microsoft Login-kirjautuminen palautui takaisin Neptonin kirjautumissivulle.
[ref ND-4861]


##  **28.07.2026** julkaisu (2.17.54)
###  __ Parannus
  * #### Projektityyppien hallinta -näkymässä näytetään projektityypin luonti- ja muokkausajat. Nykyisille projektityypeille näitä arvoja ei näytetä.
[ref ND-4834]


###  __ Korjaukset
  * #### Kalenteri- ja taulukkonäkymissä kertymän laskentaa ei näytetty tapahtumaa lisättäessä, mikäli tapahtumaa lisättiin kuluvalle päivälle.
[ref ND-3677]
  * #### Jotkin liittymän sääntöjoukon säännöistä saatettiin jättää osittain suorittamatta asetusryhmätasolla, mikäli henkilö oli asetusryhmän jäsen vain osan aikaa käsitellystä ajanjaksosta.
[ref ND-4298]
  * #### Hyväksy tunteja -näkymä saattoi päätyä virheeseen, mikäli valittuna oli suuri määrä käyttäjiä.
[ref ND-4376]
  * #### Kertymän käytön laskenta ei huomioinut viikonloppuja, kun kertymävapaita lisättiin Työajan kalenteri- tai taulukkonäkymässä.
[ref ND-4827]


##  **21.07.2026** julkaisu (2.17.53)
###  __ Korjaukset
  * #### Pieni korjaus Työsuhde-osion henkilöiden vienti Exceliin-toiminnallisuuteen.
[ref 16588]
  * #### Henkilölistan suodatin toimii nyt suunnittelunäkymässä oikein.
[ref 16661]
  * #### Vuorolista päiväsarakkeilla -raportti saattoi kaatua tietyissä tapauksissa, mikäli ajanjakso sisälsi lukittuja päiviä ja sairauspoissaoloja.
[ref 17388]


##  **14.07.2026** julkaisu (2.17.52)
###  __ Parannus
  * #### Suorituskykyparannuksia RFID-tunnisteella ja PIN-koodilla kirjautumiseen.
[ref 17037]


###  __ Korjaukset
  * #### Suunnittelunäkymässä tehtävien poisto massatyökalulla johti joissain tapauksissa virheilmoitukseen.
[ref 16680]
  * #### Työnkorotuksia ei ansaittu, kun vuoropoikkeama oli suunniteltu massatoiminnoilla.
[ref 16800]
  * #### Suunnittelunäkymässä julkaisuvaihtoehto puuttuu, kun tehtäviä lisätään tai poistetaan massatoiminnoilla vuorokalenterin vuoroon.
[ref 17505]
  * #### Kertymä saattoi tietyissä tilanteissa lainata yli viikkovelvoitteen, kun viikko sisälsi tapahtumia, jotka laskettiin osaksi viikkovelvoitetta, mutta ei osaksi viikkoylityön rajaa.
[ref 17416]


##  **30.06.2026** julkaisu (2.17.51)
###  __ Korjaukset
  * #### Projektien kestoa ei tallennettu oikein "HH:MM" -muodossa kalenterinäkymän massatoiminnolla.
[ref 17459]
  * #### Varallaoloajasta voidaan vähentää lounas Työajan asetuksissa.
    * Asetus koskee sekä merkittyjä että oletettuja lounaita.
[ref 17440]


##  **16.06.2026** julkaisu (2.17.50)
###  __ Parannukset
  * #### Suunnittelunäkymän Näkymän valinnat-osion Henkilöt-valikko päivittyy valitun toimipisteen tai vuorokalenterien perusteella.
[ref 16624]
  * #### Viikkolepo liukuvalla ansaintajaksolla.
    * Ansaintajakso voi alkaa viimeisimmän työvuoron päättymisestä ennen vähiten työtä sisältävää päivää.
    * Mahdollistaa “liukuvan” ansaintajakson (ei aina klo 00:00 alusta).
[ref 17248]


###  __ Korjaukset
  * #### Tapahtumille kohdennettujen projektien korvaaminen kalenterinäkymän massatoiminnolla ei toiminut oikein.
[ref 16397]
  * #### Työvuorot näyttivät virheellisesti varoituksen osaamispuutteesta vaikka henkilöllä oli vaadittu osaaminen.
[ref 16583]
  * #### Valmiita ilmoituksia käytettäessä varoitettiin virheellisesti hyväksymättömistä tapahtumista hyväksytyillä päiviltä, joilla oli suunniteltu vuoro.
[ref 17441]
  * #### Päiväkohtaisen poikkeusasetuksen asettaminen oli mahdollista ilman työajan roolin oikeutta avata lukittuja päiviä.
[ref 16593]
  * #### Parannuksia viikkolevon laskennan asetusten otsikoihin.
[ref 16596]
  * #### Tunnit näytettiin desimaaliarvoina kertymiin liittyvissä valmiissa ilmoituksissa.
    * Uusi muoto on HH:MM.
[ref 17395]
  * #### InsertActivities-rajapinta saattoi virheellisesti varoittaa puutteellisista oikeuksista asettaa työlisiä.
[ref 17429]
  * #### Työaikaprosentti jätetään nyt huomiotta silloin, kun työvuorot asettavat työviikon pituuden.
[ref 16964]
  * #### Viennin tiedostomuodot SD Worx (Ero) ja SD Worx (Työ) tukevat poimintasäännön arvoja 'OverrideStartDateTime' ja 'OverrideEndDateTime'.
[ref 14440]
  * #### Henkilön lisääminen toimipisteelle saattoi joskus valita väärän henkilön tilanteissa, joissa usealla henkilöllä oli sama sukunimi.
[ref 17353]
  * #### Lomakalenterista poistettu vuoro jäi virheellisesti näkyviin suunnittelu- ja työaikanäkymiin.
[ref 17359]
  * #### Työajan kalenteri näytti aiheettoman virheilmoituksen henkilöille, joiden työsuhde ei ollut aktiivinen.
[ref 17312]
  * #### Tietyissä tilanteissa Nepton Flexim -päätteillä oli mahdollista valita yläprojekteja tapahtumien kohdenteiksi.
[ref 17348]


##  **02.06.2026** julkaisu (2.17.49)
###  __ Korjaukset
  * #### Jotkin päivämääräkentät eivät avanneet kalenteria päivämäärän valitsemiseksi.
[ref 17284]
  * #### Vuosityöajan jaksotavoitteen asetuksen nimi näytetään oikein kaikilla kielillä.
[ref 17236]
  * #### Vuorokalenterin poikkeukselle asetettu tehtävä ei näkynyt työajan kalenterissa.
[ref 16527]


##  **26.05.2026** julkaisu (2.17.48)
###  __ Uutta
  * #### Ulkoisista HR-järjestelmistä tuotujen henkilöiden tietoja voidaan jatkossa hallita myös henkilötietoihin lisätyn "Ulkoinen tunniste 1"-tietokentän avulla:
    * Tunniste voidaan asettaa niin manuaalisessa kuin liittymien kautta tehtävissä tuonneissa
    * Henkilötuonneissa voidaan nyt myös määrittää henkilön tunnistamiseen käytettävä tunniste
    * Työajan webserviceen lisätty mahdollisuus viitata käyttäjiin ulkoisen tunnisteen avulla
    * Henkilöiden ulkoista tunnistetta voidaan käyttää työajan sääntöjoukoissa
[Henkilöiden manuaalinen tuonti](<https://support.nepton.com/hc/fi/articles/360018767498>)  
[Henkilötietojen ajastettu tuonti](<https://support.nepton.com/hc/fi/articles/360002489317>)  
[Henkilötuonnin kentät](<https://support.nepton.com/hc/fi/articles/360015933397>)  
[Henkilötietojen sovellusliittymä](<https://support.nepton.com/hc/fi/articles/4406271660945>)  
[Henkilötietojen vienti Exceliin](<https://support.nepton.com/hc/fi/articles/360002430478>)  
[Vie henkilöt - JSON-tietomuoto](<https://support.nepton.com/hc/fi/articles/7982660700189>)  
[ref 17140]


###  __ Parannukset
  * #### SAML SSO kirjaston päivitys
Päivitys parantaa palveluun kirjautumisen tietoturvallisuutta.
[ref 17232]
  * #### Työsuhteen päättymispäivä -kentän varoitustekstin muutos
[ref 17346]


###  __ Korjaukset
  * #### Työajan tapahtumatuontien lokitiedot antavat yksityiskohtaisemman tiedon tuonnin tuloksista
[ref 16699]
  * #### Työajan tapahtumatuonti ei poistanut tapahtumaa, mikäli poistettavan tapahtuman alku- ja loppuaika oli tuotavan ajanjakson ensimmäisellä päivällä.
[ref 16699]
  * #### Vuoropohjaan lisätty kentät "Vuorotiedot" ja "Vuorotiedot suunnittelijalle"
[Ohje](<https://support.nepton.com/hc/fi/articles/28074659621917>)  
[ref 16585]
  * #### Työajan vuorolistanäkymissä henkilölistaus ei päivittynyt, kun ajanjaksoa muutettiin
[ref 17314]


##  **19.05.2026** julkaisu (2.17.47)
###  __ Uutta
  * #### Nepton tyytyväisyyskysely 2026 H1
Kysely esitetään johtajille ja esihenkilöille 25.5. ja työntekijöille 27.5. alkaen.
[Lisätietoa](<https://support.nepton.com/hc/fi/articles/16439727874717>)  
[ref 17333]


###  __ Korjaukset
  * #### Nepton Palkat (Salaxy) palkkalaskelmat ovat nyt ladattavissa suomeksi, ruotsiksi ja englanniksi käyttäjän valitseman kielen mukaisesti.
    * Muille kielille käytetään englantia. 
[ref 16147]
  * #### Suunnittelunäkymässä näkyvät ainoastaan henkilöt, jotka on liitetty valittuun vuorokalenteriin tai lisätty valitun toimipisteen resurssiksi.
[ref 17081]
  * #### SD Worx (erot) -liittymä kirjoitti vientipuskuriin myös silloin, kun maksuryhmän palkkakausi oli asettamatta.
[ref 17142]
  * #### Jo käytössä olevan koodin asettaminen vuorokalenteriryhmälle antaa selkeän varoituksen.
[ref 17238]


##  **07.05.2026** julkaisu (2.17.46)
###  __ Korjaus
  * #### Korjattu uloskirjautumisongelma, joka ilmeni, kun mobiilinäkymä oli asetettu oletusnäkymäksi ja käytössä oli Firefox-selain.
[ref 17278]


##  **05.05.2026** julkaisu (2.17.45)
###  __ Korjaukset
  * #### Henkilön vuororyhmään tehdyt muutokset eivät poista henkilölle luotuja vuoropoikkeuksia.
[ref 17281]
  * #### Korjattu virheellinen varoitus työsuhteen päättymisestä, vaikka päättymispäivä on tulevaisuudessa.
[ref 17285]


##  **29.04.2026** julkaisu (2.17.44)
###  __ Korjaus
  * #### Korjattu virhe, jossa henkilöiden tuonti epäonnistui, jos työsuhteen päättymispäivä oli asetettu tulevaisuuteen.
[ref 17283]


##  **28.04.2026** julkaisu (2.17.43)
###  __ Parannukset
  * #### Mahdollisuus luoda uusi sääntöjoukko ympäristössä jo olemassaolevan sääntöjoukon pohjalta.
[ref 17260]
  * #### Yleisiä suorituskykyparannuksia työajan laskentaan.
[ref 17261]
  * #### Henkilön tiedot- sivu:
    * Kun henkilön työsuhteelle lisätään päättymispäivämäärä, näytetään huomioteksti ja linkki ohjeeseen henkilön poiston yhteydessä tehtävistä toimenpiteistä.
    * Muutettu termi 'Poista' termiksi 'Poista käytöstä' henkilön poiston yhteydessä.
[ref 17229]


###  __ Korjaus
  * #### Nepton Palkat (Likeit-versio) ei näyttänyt palkkalaskelmanäkymää oikein Työajan kalenterissa, jos palkkalaskelmia ei ollut saatavilla.
[ref 16119]


##  **21.04.2026** julkaisu (2.17.42)
###  __ Parannukset
  * #### Nepton Palkat (Likeit-version) käyttäjät voivat nyt halutessaan piilottaa palkkalaskelmaluonnokset työntekijöiltä.
[ref 17234]
  * #### Yleisiä suorituskykyparannuksia työajan laskentaan.
Uudet poikkeusasetusten sääntökomennot poissaolotyypeille:
    * [WORK-DAY-HAS-ANY-OF-ABSENCE-TYPES|1|2|3|jne]
    * [WORK-DAY-HAS-ABSENCE-TYPES-OTHER-THAN|1|2|3|jne]
[ref 17235]
  * #### Varoitus näytetään, kun henkilön vuororyhmä tai asetusryhmä vaihdetaan, päätetään tai poistetaan.
[ref 15514]


###  __ Muutos
  * #### Nepton SSO Service Provider -varmenteen päivitys.
[ref 17240]


###  __ Korjaukset
  * #### Osa reaaliaikaisista liittymistä lähetti tietoja turhaan useaan kertaan, kun hyväksyttiin projektityötunteja
[ref 16504]
  * #### Suorituskykyparannuksia Hyväksy tapahtumapyyntöjä-näkymään.
[ref 17045]
  * #### Kun henkilön vuororyhmä päättyy tai poistetaan, kaikki tulevaisuuteen tehdyt poikkeamat ja niihin liittyvät työajan tulkinnat poistetaan automaattisesti.
[ref 15514]


##  **14.04.2026** julkaisu (2.17.41)
###  __ Korjaukset
  * #### Korjattu virhe Poikkeukselliset kirjaukset ‑raportin sähköposti‑ilmoitusten vastaanottajissa.
[ref 17222]
  * #### Joissakin tapauksissa Nepton Flexim -päätteet loivat päällekkäisiä tapahtumia.
[ref 17231]


##  **08.04.2026** julkaisu (2.17.40)
###  __ Korjaukset
  * #### Korjattu Rajaa Nepton API käyttäjiä -asetuksen asettelua.
[ref 16998]
  * #### Nepton Palkat-asiakkailla henkilöiden palkkalaskelmat avautuvat oikein.
[ref 16998]
  * #### Korjattu sairauspoissaolojen korvaustietojen näkyvyys työaika‑ ja projektiraporteilla.
[ref 17204, 17206]


##  **31.03.2026** julkaisu (2.17.39)
###  __ Parannukset
  * #### Netvisor‑liittymän autentikointitapa päivitetty vastaamaan uusimpia vaatimuksia.
[ref 16115]
  * #### Parannuksia sairauspoissaolojen ja poissaolojen näkyvyyteen projektiraporteissa
    * Uusi työajan roolien oikeus: "Voi raportoida sairauspoissaolojen ja poissaolojen tunnit hallinnoiduista projekteista".
    * Sairauspoissaolojen ja poissaolojen tuntien sisällyttäminen on valinnaista.
    * Sairauspoissaolo- ja poissaolotapahtumien huomautuksien sisällyttäminen on valinnaista "Projektityön yhteenveto henkilöittäin" raportilla.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002548957>)  
[ref 16306]


###  __ Korjaukset
  * #### Tapahtumien tuonti saattoi epäonnistua, mikäli tapahtuma sisälsi saman päivämäärän kuin sarake "Poissaolo tai sairauspoissaolo palkallinen päivämäärään saakka" tai "Poissaolo tai sairauspoissaolo palkallinen päivämäärän jälkeen"
[ref 17115]
  * #### Päiväperusteisen kertymän arvo saattoi muuttua hieman liikaa desimaalivirheen vuoksi.
    * Esimerkiksi arvo "1 päivä "saattoi joissain tilanteissa näkyä muodossa "1,01 päivä".
[ref 16832]


##  **28.03.2026** julkaisu (2.17.38)
###  __ Korjaus
  * #### Henkilötuonnin ajastettu tehtävä ei käynnistynyt joillain asiakkailla.
[ref 17170]


##  **28.03.2026** julkaisu (2.17.37)
###  __ Parannus
  * #### Uusia asetuksia sunnuntaiylityön laskentaan.
    * Sunnuntaiylityön ansainta voidaan määrittää alkamaan sunnuntaita/juhlapyhää edeltävänä päivänä tiettynä kellonaikana.
    * Sunnuntaiylityötä voidaan määrittää ansaittavaksi juhlapyhänä tehdystä työstä.
    * 50%/100% sunnuntaiylityön ansaintaraja voidaan nyt määrittää viikkotasolle.
[ref 15893]


###  __ Korjaus
  * #### Henkilötuonnin ajastettu tehtävä ei käynnistynyt joillain asiakkailla.
[ref 17170]
  * #### Henkilötuonnin ajaminen manuaalisesti ei käynnistynyt joillain asiakkailla.
[ref 17110]


##  **26.03.2026** julkaisu (2.17.36b)
###  __ Korjaus
  * #### Nepton Palkkojen maksuryhmien vienti ei toiminut oikein.
[ref 17143]


##  **24.03.2026** julkaisu (2.17.36)
###  __ Korjaukset
  * #### Työsuhteen Hallinta-osion asetusten nimien oikaisuja.
[ref 16838]
  * #### Poissaolo-tapahtuman aloittaminen saattoi aiheuttaa virheen Nepton Flexim -päätteellä, mikäli käynnissä oleva tapahtuma oli kohdennettu ylityöksi. 
[ref 16924]
  * #### Henkilöiden ajastettu vienti Nepton Palkkoihin toimii oikein.
[ref 17046]
  * #### Sairausloman palkallisuuden näkyvyyttä on rajattu "Vuorolista päiväsarakkeilla" ja "Vuorolista projekteittain" raporteilla.
[ref 17084]
  * #### "Vuorolista projekteittain" raportti ei näyttänyt tapahtumia kaikissa tapauksissa.
[ref 17084]
  * #### Liittymät olivat pysäytettyinä vanhan huoltoikkunan mukaisesti torstaina 13:00 - 13:30. Jatkossa liittymät ovat pysäytettyinä uuden huoltoikkunan aikataulun mukaisesti tiistaisin klo 19.15 - 19.45.
[ref 17101]
  * #### Oletustyöaikaryhmä henkilötuonnissa
Työsuhde > Hallinta löytyvää työajan oletusasetusryhmän asetusta voidaan hyödyntää ajastetuissa henkilötuonneissa, joissa asetusryhmätieto ohitetaan tuotavana henkilötietokenttänä tai sitä ei tuoda lainkaan.
[ref 16252]


##  **10.03.2026** julkaisu (2.17.34)
###  __ Korjaukset
  * #### Tapahtuman kohdentamisessa projekteille projektinhakutoiminto toimii oikein.
[ref 17064]
  * #### Mukautetun viennin tiedostot eivät enää sisällä ylimääräisiä otsikkorivejä, kun useita tapahtumia yhdistetään vientipuskurista yhteen vientitiedostoon.
[ref 17062]
  * #### Korjaus kumulatiivisten kertymäarvojen laskentaan arkipyhäviikoilla, kun työviikon laskentatapana on "Työviikkoa lyhentävien juhlapyhien työtunnit lasketaan työpäivien jälkeen".
[ref 16802]


##  **05.03.2026** julkaisu (2.17.33)
###  __ Korjaukset
  * #### Työajan roolin oikeudella "Voi muokata kaikkien ruokailutapahtumia" ei ollut mahdollista lisätä ruokailu-tapahtumia.
[ref 17025]
  * #### Kalenterinäkymän henkilöhaun kentän aktivoiminen vaati kaksi napsautusta Chrome- ja Edge-selaimissa.
[ref 16903]


##  **03.03.2026** julkaisu (2.17.32)
###  __ Korjaukset
  * #### Henkilö voidaan vaihtaa tai lisätä vuorolle massatoimintojen avulla vuorosuunnittelunäkymässä
[ref 17014]
  * #### Vuoron toimipiste voidaan vaihtaa massatoimintojen avulla vuorosuunnittelunäkymässä
[ref 17015]
  * #### "Anna henkilölle vuoroja" -työkalun avulla vuoroja voidaan jakaa henkilöille vuorosuunnittelunäkymässä
[ref 17013]
  * #### Vuorokalenterissa tehty vuoromuutos näkyy suunnittelunäkymässä oikealla värillä
[ref 17033]
  * #### Vuosiloma tasoittumisjaksolla saattoi muodostaa liikaa lisätyötä, mikäli päivällä oli suunniteltu vuoro
[ref 16966]


##  **26.02.2026** julkaisu (2.17.31)
###  __ Parannukset
  * #### Vuorokalenterin vuorotyypille voidaan lisätä oletetun ruokatauon vähennys.
[ref 16521]
  * #### Henkilölle asetetun työaikaprosentin huomiointi lisätyön laskennassa, kun arkipyhä lyhentää työviikkoa.
    * Uusi asetus löytyy Työajan asetuksista Työtunnit > TES > Lisätyön korotusprosentti määrittämällä "Käytä työaikaprosenttia, kun arkipyhä lyhentää työviikkoa".
    * Oletuksena nykyinen toiminnallisuus säilyy ennallaan ja työaikaprosentti otetaan huomioon.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002559438>)  
[ref 16910]


###  __ Korjaukset
  * #### Parannuksia virheviesteihin sekä käytettävyyteen sallittujen ja oletetettujen työaikojen päiväkohtaisessa asetusnäkymässä.
[ref 16626]
  * #### Asetusten "Suurin sallittu määrä lisätyötä päivässä" ja "Suurin sallittu määrä lisätyötä viikossa" määrityksen periytyminen voidaan estää ala-asetusryhmissä.
[ref 16934]
  * #### Salasanan palautussähköpostit sisältävät nyt klikattavan palautuslinkin pelkän tekstimuotoisen URL-osoitteen sijaan.
[ref 16974]


##  **21.02.2026** julkaisu (2.17.30)
###  __ Parannukset
  * #### Yleisiä suorituskykyparannuksia.
    * Olemme vähentäneet teknistä velkaa ja optimoineet keskeisiä toiminnallisuuksia, mikä parantaa suorituskykyä ja tarjoaa asiakkaille sujuvamman ja entistä luotettavamman käyttökokemuksen.
[ref 15355]
  * #### Suorituskykyparannuksia työajanlaskentaan.
[ref 16231]
  * #### Kun kertymän saldo ylittää negatiivisen rajan, voidaan rajan ylittävä aika siirtää vähennettäväksi palkasta.
Rajan ylittävä aika voidaan hakea sääntöjoukon poimintasäännöllä UserSalaryData - taulusta ehdolla Compensationtype = 'UnpaidOverMinAccrualLimit'.
[Ohje](<https://support.nepton.com/hc/fi/articles/360010514358>)  
[ref 16933]


##  **19.02.2026** julkaisu (2.17.29)
###  __ Korjaukset
  * #### Kirjautumissivu skaalatautuu oikein kaikilla laitteilla.
[ref 16636]
  * #### Korjattu virhetilanne henkilötietojen siirrossa Neptonista Priimaan.
[ref 16983]


##  **12.02.2026** julkaisu (2.17.28)
###  __ Parannukset
  * #### Uusia työajan roolin oikeuksia, joiden avulla kaikkien henkilöiden sairauspoissaolon korvaus- ja lääkärintodistuskenttiä voidaan tarkastella ja muokata ilman, että tarvitsee myöntää "Kaikki ylemmän tason ja ylempää tasoa alemmat oikeudet".
[Ohje](<https://support.nepton.com/hc/fi/articles/360002554338>)  
[Ohje](<https://support.nepton.com/hc/fi/articles/17842757043613>)  
[ref 16662]
  * #### Uusi työajan roolin oikeus, joka mahdollistaa työvuorojen tuonnin API:n kautta ilman, että tarvitsee myöntää "Kaikki ylemmän tason ja ylempää tasoa alemmat oikeudet".
[Ohje](<https://support.nepton.com/hc/fi/articles/360002554338>)  
[ref 16662]
  * #### Sairauspoissaoloon viitataan yhdenmukaisilla termeillä.
[ref 16479]


###  __ Korjaukset
  * #### Työsuhteen ulkopuolinen juhlapyhä saattoi virheellisesti nostaa tasoittumisjakson enimmäistyöaikaa.
[ref 16892]
  * #### Varallaolo laskettiin väärin päivinä, joilla oli sovitun lisä- / ylityön tavoin käyttäytyviä tapahtumia.
[ref 16715]
  * #### Korjattu satunnaisia Nepton Touch -kirjauspäätteiden jäätymisiä.
[ref 16160]
  * #### Parannettu Nepton Touch -kirjauspäätteen RFID-lukijan suorituskykyä.
[ref 16160]


##  **05.02.2026** julkaisu (2.17.27)
###  __ Uutta
  * #### Uusi valmis ilmoitus, jolla voidaan ilmoittaa asetetun saldorajan ylittymisestä.
[ref 15379]


###  __ Parannukset
  * #### Salli työvuorojen siirtäminen henkilöltä toiselle API:n ja ajastetun tapahtumien tuonnin kautta.
Muita tapahtumatyyppejä ei voi siirtää. Jos tätä yritetään, näytetään virheilmoitus.
[ref 16862]
  * #### Datamäärältään isot raportit avautuvat selaimen sijaan excelissä.
[ref 16890]


###  __ Korjaukset
  * #### Parannuksia tietoturvaan.
[ref 16862]
  * #### Korjauksia työajan valikkojen näkyvyyteen
    * Vuorolista projekteittain oli saatavilla vaikka projektit-ominaisuus ei ollut käytössä
    * Työtunnit ei ollut saatavilla kaikissa tapauksissa missä sen piti
[ref 16492]
  * #### Vuorosuunnittelun toiminnon 'Jaa vuorot henkilöille automaattisesti" käyttö näytti aiheettoman virheilmoituksen.
[ref 16893]
  * #### Korjattu valmiiden ilmoitusten henkilöryhmävalintaan ja lähettämiseen liittyviä ongelmia.
[ref 16734]
  * #### Vuosiloman laskenta tasoittumisjaksolla korjattu.
    * Vuosiloma käyttää työpäivän keskipituutta vain, jos se on listattu asetuksessa “Poissaolot, joiden laskennassa käytetään keston sijaan työpäivän keskipituutta”.
    * Muussa tapauksessa vuosiloma vaikuttaa tasoittumisjaksoon koko kestollaan.
    * Jos halutaan säilyttää aiempi (keskipituuteen perustuva) laskentatapa, vuosiloma tulee lisätä asetukseen.
[ref 16920]


##  **29.01.2026** julkaisu (2.17.26)
###  __ Parannukset
  * #### Kun kertymän saldo laskee negatiivisen rajan alle, voidaan alijäämä siirtää vähennettäväksi toisesta kertymästä.
[Ohje](<https://support.nepton.com/hc/articles/360010514358>)  
[ref 15747]
  * #### Vuosilomien raporttien suorituskykyä parannettu.
[ref 16791]


###  __ Korjaukset
  * #### Korjauksia kertymiin, joiden ansainta perustuu ansaintataulukkoon:
    * Poistettu ylimääräinen kertymän 'Yksikkö'-asetus
    * Korjattu kertymän ansaintataulukon asetusten periytymisen näkyvyyttä ja asetusten periytymisen estoa
[ref 16609, 16537]
  * #### Tapahtumatyyppien näkyvyys voidaan asettaa 'Ei asetettu' asetusryhmätasoilla.
[ref 16400]


##  **22.01.2026** julkaisu (2.17.25)
###  __ Parannukset
  * #### Työehtosopimuksen mukainen työviikon pituus ja enimmäistyöaika viikossa voidaan määrittää perustumaan suunniteltujen vuorojen kestoon.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002558537>)  
[ref 16785]
  * #### Projektien tuonnin suorituskykyparannuksia.
[ref 13283]
  * #### Suorituskykyparannuksia työtuntien hyväksyntään.
[ref 16231]


###  __ Korjaus
  * #### Korjattu sijaintipohjaisista rajoituksista annettavia ilmoituksia Nepton Flexim-päätteissä (v5.6.0).
[ref 16826]


##  **15.01.2026** julkaisu (2.17.24)
###  __ Parannus
  * #### Suorituskykyparannuksia henkilötuonteihin
[ref 16719]


###  __ Korjaukset
  * #### Työajan roolin keskitason oikeuksissa määritys "Kaikki keskitason ja keskitasoa alemmat oikeudet" myöntää työajan roolille käyttöoikeudet kaikkiin keskitason oikeuksiin.
[ref 16490]
  * #### Reaaliaikaisissa vienneissä palvelulokiin muodostuu merkintä vain niistä tapahtumista, jotka siirretään liittymällä.
[ref 16434]
  * #### Joissain tilanteissa työajan lyhennysvapaita ansaittiin liian aikaisin.
[ref 16395]


##  **08.01.2026** julkaisu (2.17.23)
###  __ Uutta
  * #### Lisätty henkilön aktiivisen työsopimuksen alkamispäivämäärä ja päättymispäivämäärä UserData-tietokantatauluun.
[ref 16708]
  * #### Ilmoitus-toiminnossa uusi valmis ilmoitus työhön liittyvistä vuosipäivistä, esim. muistutus esimiehille työntekijän 10-vuotispäivästä.
[ref 16709]


###  __ Korjaukset
  * #### Ilmoitusten asetussivu ei toiminut joissain tilanteissa.
[ref 16710]
  * #### Pieniä korjauksia ja viimeistelyä henkilöryhmien hallintatoimintoihin.
[ref 16693]
  * #### Salasanan palautuslinkki toimii nyt kaikista sähköpostiohjelmista.
[ref 16728]
  * #### Henkilön oletusprojektin lisääminen ja muuttaminen toimii jälleen.
[ref 16711]


##  **18.12.2025** julkaisu (2.17.22)
###  __ Korjaus
  * #### Henkilötasolla "Salli tunti tunnista ylityön ansaita sairauspoissaolosta" -asetukseen määritelty "Kyllä" ei enää aktivoidu asetusryhmätasolle.
[ref 16452]


##  **16.12.2025** julkaisu (2.17.21)
###  __ Korjaus
  * #### Jatkokorjaus ongelmaan, jossa osa asiakkaista ei voinut käyttää Neptonin kirjautumislinkkiä kolmannen osapuolen käyttöliittymän kautta.
[ref 16706]


##  **15.12.2025** julkaisu (2.17.20)
###  __ Korjaus
  * #### Osa asiakkaista ei voinut käyttää Neptonin kirjautumislinkkiä kolmannen osapuolen käyttöliittymän kautta.
[ref 16706]


##  **12.12.2025** julkaisu (2.17.19)
###  __ Korjaukset
  * #### Vuorosuunnittelun asetus "Juhlapyhinä päivittäinen työvelvoite lisätään työtunteihin päivälle suunnitellun työn lisäksi" otetaan huomioon juhlapyhien laskennassa.
[ref 16509]
  * #### Vuorokalenterin vuorojen muokkauksessa ilmennyt ongelma on korjattu.
[ref 16695]


##  **11.12.2025** julkaisu (2.17.18)
###  __ Uutta
  * #### Valmiit ja muokattavat sähköposti-ilmoitukset.
    * Valmiit sähköposti-ilmoituksen pohjat, joilla ilmoitetaan esihenkilöille hyväksyntää tarvitsevista tapahtumista.
    * Sähköposti-ilmoitukset voidaan ajastaa.
    * Sääntöjoukkojen avulla ylläpitäjät voivat määrittää mukautettuja sääntöjä sähköposti-ilmoitusten lähettämiseen.
    * Ominaisuutta aiotaan laajentaa tulevaisuudessa.
[ref 15919, 15920, 16449, 16149, 15968]
  * #### Sallittujen IP-osoitteiden määritteleminen työajan kirjaamiseen.
    * Henkilöryhmittäin voidaan rajata työajan kirjaaminen määrättyihin IP-osoitteisiin tai päätteisiin.
    * Sallimattomasta lähteestä tehty kirjaus voidaan joko estää kokonaan tai se voidaan merkata poikkeukselliseksi kirjaukseksi.
    * Toiminto aktivoidaan ottamalla yhteyttä Neptonin asiakaspalveluun.
[ref 15407, 15966, 16039, 16541]
  * #### Mukautettu Työajan vienti voidaan määrittää suoritettavaksi reaaliajassa vientipuskuriin.
[ref 16194]


###  __ Parannukset
  * #### Työajan käyttöoikeuksia laajennettu uudella oikeudella, joka sallii vain omien avoimien työtapahtumien projektien muokkaukset.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002554338>)  
[ref 16038]
  * #### Unohtunut salasana -sivun ulkoasua on päivitetty.
[ref 16061]
  * #### Nepton Palkat ja Saarni EXP henkilötietojen vienti ei joissain tilanteissa toiminut oikein. Ajastetun tehtävän "Tietoja muokattaessa"-vientitavalle voidaan nyt määrittää päivittäinen ajankohta, jolloin yön aikana tapahtuneet muutokset synkronoidaan.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002489357>)  
[ref 15760]


###  __ Korjaukset
  * #### Tasoittumisjakson enimmäistyöaika laskettiin tietyissä tilanteissa väärin kun tasoittumisjaksolla oli työsuhteen ulkopuolisia päiviä
[ref 16258]
  * #### Huomautustapahtuman muokkaus päivittyy myös suunnittelunäkymään.
[ref 16433]
  * #### Joissain tilanteissa Esimies-roolissa olevat vuorosuunnittelua tekevät henkilöt eivät nähneet vuosityöajan arvoja suunnittelunäkymässä.
[ref 16489]
  * #### Sairauspoissaolot henkilöryhmittäin -raportti näyttää raportoidun tiedon oikein henkilöryhmärajauksia käytettäessä.
[ref 16393]
  * #### Suunnittelunäkymän tiedot skaalautuvat oikein.
[ref 16392]
  * #### Voimassaolotoiminto pysyy henkilön lisätietokentässä, kun lisätietokentän asetuksia muokataan.
[ref 16573]
  * #### Kaikkia oikeuksia jotka saadaan "Pääsy henkilöryhmiin" -toiminnon kautta sovelletaan nyt myös rooleihin, jotka ovat samalla tai ylemmällä tasolla kuin oikeudet saava henkilö
[ref 16498]


##  **04.12.2025** julkaisu (2.17.17)
###  __ Parannus
  * #### Matkalaskujen vuoden 2026 ulkomaan päivärahojen enimmäismäärät lisätty palveluun
[ref 14982]


###  __ Korjaukset
  * #### Vuororaporteissa saatettiin näyttää poissaolon tietoja henkilöille, joilla ei ollut oikeutta nähdä kyseisiä tietoja
[ref 16431]
  * #### Edellisen vuorokalenterijakson "Ohita juhlapyhät" -asetus säilyy vuorokalenterijakson luonnin yhteydessä
[ref 16551]


##  **27.11.2025** julkaisu (2.17.16)
###  __ Parannus
  * #### Palvelulokin viestit virheellisestä SFTP -palvelimen kirjautumistunnuksista ovat aiempaa hyödyllisemmät
[ref 15868]


###  __ Korjaukset
  * #### Lomakalenterin juhlapyhille voi taas lisätä vuorotyyppejä.
[ref 16505]
  * #### Näytä “Viikonloput” on nyt näkyvissä Suunnittelunäkymän valinnoissa.
[ref 16428]
  * #### Tapahtumatyyppiä voidaan muokata massatoimintojen avulla suunnittelunäkymässä, kun vuorokalenterit ovat käytössä.
[ref 16526]
  * #### Julkaistulle vuorotarpeelle annettu vuorotieto säilyy työvuorossa, kun työvuoro varataan
[ref 16249]


##  **24.11.2025** julkaisu (2.17.15)
###  __ Uutta
  * #### Uusi Nepton - Populus vuosilomaliittymä
[ref 16326]


##  **20.11.2025** julkaisu (2.17.14)
###  __ Uutta
  * #### Suunnittelunäkymän massatoimintoja voidaan nyt käyttää myös vuorokalenterin työvuorojen kanssa.
[ref 14499]


###  __ Parannukset
  * #### Työajan vuororaporteista voi jättää pois tapahtumat, jotka eivät ole työvuoroja.
[ref 16015]
  * #### Vuorokalentereihin on lisätty asetus, joka mahdollistaa arkipyhien ohittamisen vuorokierrossa.
[ref 16016]
  * #### Useita käyttevyysparannuksia vuorotarpeiden viestintätoimintoon, sisältäen:
    * Viestiketju voidaan merkitä käsitellyksi tai käsittelemättömäksi, ja odottavien viestien laskuri näyttää nyt käsittelemättömien viestiketjujen määrän erillisten viestien sijaan.
    * Vuorotarpeen varaajana näytetään aina henkilö. jolle työvuoro on osoitettu  
Muita pieniä parannuksia
[ref 16057]
  * #### Tasoittumisjakson asetuksia on parannettu:
    * Tyhjät ansaintakaudet on piilotettu.
    * "Lisää ansaintakausi" -painikkeella voidaan lisätä uusi ansaintakausi.
[ref 16224]
  * #### Vuorokalenterijaksolle tehdyt vuoropoikkeamat näytetään ryhmiteltyinä vuorosuunnittelunäkymässä.
[ref 16333]
  * #### Joissain tilanteissa Vuorosuunnittelun suunnittelunäkymä latautui ja aukesi hitaasti. Suunnittelunäkymän latausaikaa ja suorituskykyä on parannettu.
[ref 16206]
  * #### Vuosityöajan tavoitteen muodostuminen on raportoitavissa muokattavilla raporteilla.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002489257>)  
[ref 16159]
  * #### Uusia sääntöjoukon apufunktioita.
[Ohje](<https://support.nepton.com/hc/fi/articles/360009018778>)  
[ref 16159]
  * #### Kun henkilölle lisätään vuororyhmää, näytetään vuororyhmä sekä mihin vuorokalenteriin ryhmä kuuluu.
[ref 16447]


###  __ Korjaukset
  * #### Yksikön johtajat näkevät Henkilöt-näkymässä kaikki ne henkilöt, joiden tietojen tarkastelemiseen heillä on oikeus
[ref 16142]
  * #### Ratkaistu työsuhdetietoihin liittyvä käyttöoikeusongelma, joka koski pientä joukkoa esimiehiä ja yksikönjohtajia
Jos järjestelmätason asetuksissa Työsuhde > Hallinta > Yleiset oli asetettu roolikohtaisia oikeuksia, ja henkilöllä oli käyttöoikeuksia sekä roolin että käyttöoikeusryhmän kautta, sallittiin pääsy laajempiin henkilötietoihin kuin käyttöoikeusryhmän kenttäkohtaiset rajoitukset sallivat.
[ref 16261, 16257]
  * #### Joissain tilanteissa, työkorotuksen ansainta ei toiminut oikein, kun samalle päivälle kirjattiin Korjaus-tapahtuma.
[ref 16248]
  * #### Työvuorot ja vuorokierrossa ohitetut juhlapyhät ryhmitellään nyt oikein suunnittelunäkymän toimipisteosiossa.
[ref 16232]
  * #### Vuorokalenterin vapaapäiviä ei enää näytetä toimipisteosiossa juhlapyhien kohdalla.
[ref 16232]
  * #### Suunnittelunäkymän henkilöiden rajaus ei toiminut oikein kaikissa tapauksissa.
[ref 16275]
  * #### Vuosityöajan tavoite tai suunniteltu aika oli negatiivinen joissain tapauksissa
[ref 16334]
  * #### Vuosilomaa ei otettu huomioon käytettäessä tasoittumisjakson asetusta "Käytä TES-asetuksia tapahtumatyyppien laskentaan jaksolle".
[Ohje](<https://support.nepton.com/hc/fi/articles/4405550013981>)  
[ref 16224]


##  **13.11.2025** julkaisu (2.17.13)
###  __ Parannus
  * #### Henkilöiden tuonti varoittaa nyt asianmukaisesti, jos tiedoissa on virheellisiä voimassaolopäiviä
[ref 15931]


###  __ Korjaukset
  * #### Katkenneelle AKT kuorma-autoalan TES:n mukaiselle tasoittumisjaksolle saattoi joissain tapauksissa muodostua liikaa ylitöitä, mikäli viikonlopulla oli työpäiviä.
[ref 15754]
  * #### Poissaolot sisällytettiin aina ylityön enimmäismäärään AKT kuorma-autoalan TES:n mukaisella katkenneella tasoittumisjaksolla.
[ref 16381]


##  **06.11.2025** julkaisu (2.17.12)
###  __ Korjaukset
  * #### Tapahtumatyyppien pudotusvalikko oli tietyissä tilanteissa tyhjä vuorosuunnittelu- ja vuoropohjanäkymässä
[ref 16328]
  * #### Joissain tilanteissa Esimies-roolissa olevat vuorosuunnittelua toteuttavat käyttäjät eivät nähneet vuositavoitteiden tietoja suunnittelunäkymässä
[ref 16264]
  * #### Suunnittelunäkymä aukeaa kaikille normaalisti.
[ref 16345]
  * #### Poissaolot eivät katkaisseet tasoittumisjaksoa AKT kuorma-autoalan TES:n mukaisesti, mikäli yhtään poissaolotyyppiä ei ollut valittu asetuksessa "Poissaolot, jotka eivät katkaise tasoittumisjaksoa AKT kuorma-autoalan TES:n mukaisesti".
[ref 16372]


##  **30.10.2025** julkaisu (2.17.11)
###  __ Parannukset
  * #### Parannuksia vuosityöaikaan
    * Tietyt tapahtumatyypit voidaan asettaa lyhentämään vuosityöajan tavoitetta, joko keskimääräisen viikon pituuden mukaan tai päällekkäisien vuorojen mukaan
    * Tietyt tapahtumatyypit voidaan asettaa lyhentämään suunniteltua aikaa keskimääräisen viikon pituuden mukaan
[Ohje](<https://support.nepton.com/hc/articles/29569021494685>)  
[ref 15997]
  * #### Uudella asetuksella "Viikkotyöaikaan vaikuttava määrä vapaa/lomapäivänä" voidaan määrittää, paljonko vuosilomapäivä vaikuttaa viikkotyöaikaan.
[Ohje](<https://support.nepton.com/hc/articles/360002560698>)  
[ref 16246]


###  __ Korjaukset
  * #### SQL-pohjaiset poikkeusasetukset eivät toimineet joidenkin asetusten kohdalla
[ref 16236]
  * #### Työsopimuksen kenttien automaattinen täydennys työsuhteen tiedoista toimii oikein
[ref 16250]
  * #### Tapahtumien hyväksymisnäkymän ponnahdusikkuna peitti tulevat päivät
[ref 16339]


##  **23.10.2025** julkaisu (2.17.10)
###  __ Korjaukset
  * #### Tapahtumien tuonnissa ja Accountor Mepco HRM -poissaolotuonnissa aiheutui virhe joissain tilanteissa.
[ref 15794]
  * #### Työvuorot näyttivät virheellisesti varoituksen osaamispuutteesta vaikka henkilöllä oli vaadittu osaaminen.
[ref 16234]
  * #### Joissakin tapauksissa projektipäälliköt pystyivät raportoimaan projektitunteja projekteille, joita he eivät hallinneet.
    * Ongelma oli raporteissa projektitunnit henkilöittäin ja projektituntien ylityöt.
[ref 16263]


##  **17.10.2025** julkaisu (2.17.9)
###  __ Korjaus
  * #### Ratkaistu tietoturvaongelma, joka koski pientä joukkoa esimiehiä ja yksikön johtajia, joilla on pääsy henkilötietojen Excel-vientitoimintoon. Otamme tarvittaessa yhteyttä niihin asiakkaisiin, joita asia mahdollisesti koskee. Tällä hetkellä meillä ei ole viitteitä henkilötietojen vaarantumisesta, eikä asiakkailta vaadita toimenpiteitä.
[ref 16244]


##  **16.10.2025** julkaisu (2.17.8)
###  __ Parannukset
  * #### Työajan käyttöoikeuksia laajennettu uudella oikeudella, joka sallii vain omien avoimien työtapahtumien projektien muokkaukset.
[Ohje](<https://support.nepton.com/hc/fi/articles/360002554338>)  
[ref 16038]
  * #### Sallittujen ja oletettujen työaikojen päiväkohtaisen poikkeuksen näkymä on uudistettu.
[ref 15784]


###  __ Korjaukset
  * #### Suunnittelunäkymän ylävalikon Selite- ja Viestit-toiminnot näkyvät oikein.
[ref 16204]
  * #### Tasoittumisjaksokertymien vähennykset tehtiin työsopimuksen päättymisen jälkeen, vaikka ansaintakautta ei ollut määritetty.
[Tasoittumisjakson käyttöönotto](<https://support.nepton.com/hc/fi/articles/360002559537>)  
[Joustotyöajan perustaminen](<https://support.nepton.com/hc/fi/articles/360004339858>)  
[ref 16173]
  * #### Työpäivän keskipituutta ei kaikissa tapauksissa laskettu tasoittumisjaksolle oikein, mikäli henkilön työsuhde oli päättynyt.
[Tasoittumisjakson käyttöönotto](<https://support.nepton.com/hc/fi/articles/360002559537>)  
[Joustotyöajan perustaminen](<https://support.nepton.com/hc/fi/articles/360004339858>)  
[ref 16173]
  * #### Muutoksia työaikapäätteen uusimpaan versioon
    * Tapahtuman lisääminen tulevaisuuteen ei enää lopeta käynnissä olevaa tapahtumaa.
    * Lisätty mahdollisuus lopettaa käynnissä oleva tapahtuma, kun luodaan tapahtuma tulevaisuuteen.
    * Yhteenvedossa näytetään tapahtuman tiedot.
[ref 14987]
  * #### Työsuhteen Hallinta-osion Vuorosuunnittelu-asetukseen Juhlapyhän lyhennetty pituus voidaan tallentaa tyhjä arvo
[ref 15263]
  * #### Vuorokalenterin yövuoro ei vähentänyt lounasta oikein
[ref 16094]
  * #### Suunnittelunäkymässä oikean hiiren painalluksen Muokkaa-pikavalinta ei toiminut oikein
[ref 16230]


##  **13.10.2025** julkaisu (2.17.7)
###  __ Muutos
  * #### Tietokannan tietojen korjaus
[ref 16170]


##  **09.10.2025** julkaisu (2.17.6)
###  __ Parannus
  * #### Suunnittelunäkymään on lisätty varoitus vuoroihin, joissa henkilön taidot eivät vastaa vuoron vaatimuksia.
[ref 16118]


###  __ Korjaukset
  * #### Vuorokalenteri ei korostanut yleisiä pyhäpäiviä viikonloppuisin.
[ref 15139]
  * #### Vuorosuunnittelu > Näkymän asetukset > Henkilösuodatin listasi virheellisesti henkilöitä, joihin suunnittelijoilla ei ollut käyttöoikeutta.
[ref 14464]
  * #### Vuororyhmän koodin yksilöllisyys varmistetaan nyt oikein. Asiakkailta ei vaadita toimenpiteitä.
[ref 14073]


##  **07.10.2025** julkaisu (2.17.5)
###  __ Parannus
  * #### Parannettu suunnittelunäkymän visuaalisuutta ja käytettävyyttä.
[ref 15942]


###  __ Korjaukset
  * #### Korjattu virhe, joka johtui virheellisestä työajan poikkeusasetuksen säännöstä.
[ref 15423]
  * #### Vuorosuunnittelussa tasoittumisjaksojen tiedot eivät olleet aina näkyvissä.
[ref 16138]
  * #### Muut kuin Työ-tapahtumat eivät kerryttäneet tunteja suunnittelunäkymän resurssitaulukkoon.
[ref 16137]
  * #### Työajan tasoittumisjakson laskenta saattoi tietyissä tilanteissa aiheuttaa virheen Työajan kalenterissa.
[ref 16148]
  * #### Tapahtumatyypit, jotka oli poistettu käytöstä vuorosuunnittelussa, saattoivat aiheuttaa virhetilanteen vuoroa muokattaessa.
[ref 16158]


##  **02.10.2025** julkaisu (2.17.4)
###  __ Parannus
  * #### Työajan liittymien asetussivuja on parannettu
    * Tyhjät kentät on piilotettu sääntöjoukon, työlisien ja työkorotusten asetuksissa
    * "Lisää" -painikkeella on mahdollista lisätä listaan uusia asetuksia
[ref 15818]


###  __ Korjaukset
  * #### Suunnittelunäkymä saattoi näyttää vuorot väärässä kohdassa näkymää, jos niitä oli suuri määrä
[ref 16089]
  * #### Tasoittumisjakson enimmäistyöaikaa ei laskettu oikein joissain tapauksissa
[ref 15981]
  * #### Joissakin tapauksissa päivillä oli virheellisiä oletettuja tapahtumia.
[ref 15934]


##  **29.09.2025** julkaisu (2.17.3)
###  __ Korjaukset
  * #### Työajan kalenteriin lisätyt huomautus-tapahtumat eivät näkyneet vuorosuunnittelussa, vaikka näkyvyys oli määritetty työyhteisön asetuksissa.
[ref 16110]
  * #### Flexim-päätteet näyttivät väärän virheviestin, jos RFID-tagia ei tunnistettu.
[ref 16111]


##  **25.09.2025** julkaisu (2.17.2)
###  __ Korjaukset
  * #### Julkaistut vuorokalenterin vuorot eivät aina näkyneet oikein vuorosuunnittelussa tai työajan kalenterissa.
[ref 16087]
  * #### Ylläpitäjä ei voinut lisätä uutta vuoropohjaa
[ref 16076]


##  **25.09.2025** julkaisu (2.17.1)
###  __ Parannukset
  * #### Työajan liittymien asetukset on jaoteltu selkeämmin.
    * **Sääntöjoukko** määrittää liittymälle muodostettavan sisällön ja muodon. **Ajastus** määrittää, milloin liittymä suoritetaan. **Kohdepalvelin** määrittää minne tieto siirretään. 
[SFTP-tiedonsiirron määrittäminen](<https://support.nepton.com/hc/fi/articles/360003722778>)  
[Työajan vientiliittymien kohdepalvelimet](<https://support.nepton.com/hc/fi/articles/26861716054045>)  
[ref 15502]
  * #### Mepco ja Populus poissaolojen vienti -liittymiä on parannettu.
    * Liittymät käyttävät jatkossa kohdepalvelimen asetuksia.
    * Luotettavuutta on parannettu uudella puskurointiteknologialla.
[Mepco poissaolo- ja vuosilomatapahtumien vienti reaaliajassa](<https://support.nepton.com/hc/fi/articles/23700503323933>)  
[Populus poissaolotapahtumien vienti reaaliajassa](<https://support.nepton.com/hc/fi/articles/25674625747869>)  
[ref 15502]
  * #### Vientitiedosto voidaan jakaa osiin myös reaaliaikaisten liittymiä käytettäessä
[Ohje](<https://support.nepton.com/hc/fi/articles/360006255458>)  
[ref 15890]


###  __ Korjaukset
  * #### Työajassa eräiden tiedostotyyppien lataaminen johti virheeseen.
[ref 16069]
  * #### Suunnitellun vuoron tapahtumatyypin muuttaminen ei ollut mahdollista joissain tilanteissa.
[ref 16073]
  * #### Eräissä tapauksissa vuorokalenterien poikkeamia ei julkaistu oikein Työaikaan.
[ref 16075]
  * #### Ylläpitäjä ei voinut lisätä uutta vuoropohjaa.
[ref 16076]
  * #### Nepton Palkat Likeit-version palkkalaskelman lataaminen toimii oikein.
[ref 16074]
  * #### Suunnittelussa yövuoroihin tehdyt poikkeamat saattoivat johtaa väärin laskettuun tuntien yhteismäärään.
[ref 16065]
  * #### Vuorokalenterivuoroa muokattaessa näkymää ei enää vieritetä vuoron muutoksen jälkeen.
[ref 16086]


##  **20.09.2025** julkaisu (2.17 - Vuorosuunnittelu)
###  __ Uutta
  * #### Vuosityöajan seuranta vuorosuunnittelussa
    * Työajan asetuksiin on tuotu uusi Vuosityöaika-asetus, jolla voidaan määritellä vuosityöajan tavoite tunneissa.
    * Kun suunnitellaan vuoroja, nähdään suunniteltujen vuorojen tunnit sekä vuoden tavoitteen täyttyminen yhdellä silmäyksellä. 
[ref 14491] [Ohje](<https://support.nepton.com/hc/fi/articles/29569021494685-Vuosity%C3%B6ajan-k%C3%A4ytt%C3%B6%C3%B6notto>)
  * #### Uudistetut vuorosuunnittelun viestintätoiminnot
    * Suunnittelijat ja työntekijät voivat keskustella vuoroihin liittyvistä asioista suoraan Viestit-toiminnon kautta.
    * Vuorosuunnittelija näkee kaikki vuorojen varaukset ja vuoroihin liittyvät viestit uudessa Viestit-näkymässä, joka löytyy suunnittelunäkymän yläosasta.
    * Työntekijä voi lähettää viestin avaamalla vuoron Työaikanäkymässä ja kirjoittamalla viestin uuteen Viesti-kenttään.
[ref 15399, 15559] [Ohje](<https://support.nepton.com/hc/fi/articles/28409976774557-Vuorosuunnittelun-Viestit-toiminto>)
  * #### Uusi oikeus vuoropohjien lisäämiseksi toimipisteelle
    * Vuorosuunnittelijat voivat määrittää, missä toimipisteissä vuoropohjat ovat käytettävissä.
    * Oikeus annetaan käyttöoikeusryhmän kautta.
[ref 15741] [Ohje](<https://support.nepton.com/hc/fi/articles/28074659621917-Vuoropohjan-luominen-ja-hallinnointi>)
  * #### Uusi tietokantataulu PlanningYearTargetData vuosityöaikaan liittyvien tietojen poimimiseen
[Ohje](<https://support.nepton.com/hc/fi/articles/360002489257>)
  * #### Työaika-asetusten muutokset kirjataan nyt palvelulokiin, mukaan lukien valinnainen kirjallinen syy muutokselle
Ylläpitäjät voivat määrittää syyn kirjaamisen pakolliseksi.
[ref 15749] [Ohje](<https://support.nepton.com/hc/fi/articles/30424538977309>)


###  __ Parannukset
  * #### Parannuksia vuorosuunnittelun käytettävyyteen
    * Vuoropohjat voidaan nyt määrittää usealle päivälle, mukaan lukien tyhjät päivät. Lisäksi ne sisältävät kaikki vuoroihin liittyvät kentät.
    * Varausviesteille ja vuorotehtäville on lisätty omat kenttänsä.
    * Vuoroihin on lisätty uusi "Vuorotiedot suunnittelijalle" -kenttä, joka ei näy muille käyttäjille ja helpottaa yhteistyötä vuorosuunnittelijoiden välillä.
    * Vuorojen, vuorotarpeiden, vuorokalentereista tulevien vuorojen sekä poikkeamien toiminnallisuudet on yhdenmukaistettu.
    * Useiden suunnittelunäkymien käytettävyyttä on parannettu ja näkymän asetuksien määrittely on suoraviivaisempaa.
[ref 13632]
  * #### Suunnittelunäkymän suorituskykyä on parannettu
[ref 15889]
