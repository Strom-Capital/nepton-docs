---
id: 360005539397
title: Toimipisteiden hallinta
url: https://support.nepton.com/hc/fi/articles/360005539397-Toimipisteiden-hallinta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vuorosuunnittelun määrittely
section_id: 360003275658
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Vuorosuunnittelun määrittely
labels: []
promoted: false
updated_at: '2025-07-31T04:23:57Z'
edited_at: '2025-07-31T04:23:57Z'
---

# Toimipisteiden hallinta

Kaikki palvelussa suunniteltavat vuorot suunnitellaan toimipisteille. Toimipisteitä voidaan hallita 'Toimipisteet' - otsikon alta.
Toimipisteet perustetaan niille palveluun perustetuille [yksiköille](<https://support.nepton.com/hc/fi/articles/360002590317>), joille suunnittelua tehdään. Toimipisteet luodaan ja hallitaan jokaisella yksiköllä erikseen. Henkilöitä voidaan [liittää](<https://support.nepton.com/hc/fi/articles/360015675918>) omien yksiköidensä toimipisteisiin, jolloin heille voidaan suunnitella vuoroja näille toimipisteille. Suunnittelijoilla on näkyvyys oman yksikkönsä suunnitteluun.
Jos Työajan projektiseuranta on käytössä, varmista että [yksiköillä](<https://support.nepton.com/hc/fi/articles/360002590317>) ei ole käytössä koodia joka on käytössä [projektilla](<https://support.nepton.com/hc/fi/articles/360002561017>).
Toimipistettä muodostaessa pakollisena tietona on toimipisteen nimi sekä laskentayksiköt. Laskentayksiköt on toimipisteen tunniste ja se syötetään merkkijonona.
Toimipisteet ovat hierarkkinen rakenne. Toimipisteelle voi valinnaisena antaa kategorian, jolloin perustettava toimipiste muodostuu kategoriana annetun toimipisteen alle.
Voimassa alkaen ja voimassa päättyen -kentät estävät vuorojen suunnittelun toimipisteelle näiden päivämäärien ulkopuolella. Suunnittelua ei voi tehdä toimipisteelle niille päivämäärille, jotka ovat ennen voimassa alkaen - päivämäärää tai voimassa asti - päivämäärän jälkeen. Mikäli kenttä on tyhjä, rajausta ei tehdä.
![Screenshot 2025-07-10 132053.png](https://support.nepton.com/hc/article_attachments/28750785561757)
## Projektien muodostuminen
Palvelu luo automaattisesti toimipisteitä vastaavat [projektit](<https://support.nepton.com/hc/fi/articles/360002561017>). Toimipisteisiin tehtävät muutokset päivittyvät automaattisesti projekteihin. Toimipisteen voimassaolon päättäminen päättää projektin. Toimipisteen poisto poistaa projektin. Toimipisteisiin liittyvien projektien muutokset pitää tehdä toimipisteisiin, sillä niitä vastaavien toimipisteiden tiedot syrjäyttävät suoraan projekteihin tehdyt muutokset. Tämäntyyppisten projektien muokkaus onkin estetty Työaika-osion Projektit-valikon kautta.
Projektin koodiksi muodostetaan laskentayksikön koodi, joka liittää projektin toimipisteeseen. Projektin nimeksi muodostuu toimipisteen nimi. Projektit liitetään yläprojektiin, joka muodostuu sen yksikön tiedoista, joille toimipisteitä luodaan. Yläprojektiksi muodostuu projekti, jonka nimenä on yksikön nimi ja projektin koodina yksikön koodi.
Toimipisteen kautta luotu projekti voi olla henkilön oletusprojekti, samoin kuin projekti-osion kautta luodut projektit. Mikäli toimipisteen kautta luodulle projektille halutaan määrittää projektipäällikkö, voi tämän tehdä Työaika > Hallinta > Henkilöt > Henkilön hallinnoimat projektit -määrityksistä.
Toimipisteiden ja yksiköiden näyttäminen työaikapäätteellä määritetään [Työajan projektien hallinnassa](<https://support.nepton.com/hc/fi/articles/360002561017>). Oletuksena toimipisteet ja yksiköt luodaan niin että ne näkyvät työaikapäätteellä. Vain työaikapäätteellä näyttämistä voi muokata toimipisteille ja yksiköille Työajan projektien hallinnassa.
## Toimipisteen laskentayksikön ehdottaminen
Sivun alalaidassa on esitetty seuraava vapaa - toiminto. Tämä toiminto ehdottaa automaattisesti seuraavaa käyttämätöntä laskentayksikön koodia. Tällöin toimipisteen muokkaaja tai lisääjä ei epähuomioissa käytä samoja laskentayksiköitä kuin on käytetty muissa yksiköissä. Seuraava vapaa koodi tunnistetaan siten, että palvelu etsii kaikista yksiköistä suurimman käytetyn laskentayksikön ja lisää tähän lukuun yhden. Niitä laskentayksiköitä, joita ei voi tulkita numeroksi, ei huomioida numeron muodostumisessa.
Vapaana laskentayksikkönä esitetään viisi laskentayksikön tasoa. Laskentayksiköt voidaan perustaa merkkijonona siten, että ne on jaoteltu kenoviivalla. Tätä tapaa on mahdollista käyttää siten, että kenoviivalla eritellyt laskentayksikön osat kuvaavat liiketoiminnan eri tunnisteita. Esimerkiksi laskentayksikkö 50/200 voisi kuvata liiketoimintayksikön '50' toimipistettä '200'. Perustettu toimipiste muodostaa työaikaan projektin, jossa projektin koodiksi asetetaan laskentayksikkö. Niiden projektien tapahtumat, jotka ovat eritelty erotinmerkillä, kuten kenoviivalla, voidaan aineistosiirrossa kohdistaa kaikkiin annettuihin laskentayksikön tasoihin. Esimerkiksi palkkaviennissä työn kohdistus ja palkkakulu voisi tässä tapauksessa kohdistua sekä tiettyyn asiakkaaseen, että toimipisteeseen.
## Toimipisteen voimassa alkaen ja voimassa asti -päivämäärien päivittäminen
Kun toimipisteen voimassa alkaen ja voimassa asti -päivämääriä muutetaan, on tärkeää varmistaa, että kaikilla alatoimipisteillä on voimassa asti -päivämäärät asetettu ennen päätason toimipisteen päivittämistä. Vastaavasti kun toimipisteen voimassa alkaen -päivämäärä asetetaan, kaikilla alatoimipisteillä tulee olla sama voimassa alkaen -päivämäärä.
![Screenshot 2025-07-10 133931.png](https://support.nepton.com/hc/article_attachments/28750785567261)
## Toimipisteen poistaminen
Toimipistettä ei voida poistaa, vaan se voidaan ainoastaan merkitä päättyneeksi.
## Toimipisteiden suodattaminen
Päättyneiden toimipisteiden näkyvyyttä voidaan hallita "Näytä päätetyt toimipisteet" -valintaruudulla. Kun päätetyt toimipisteet on valittu näkymään, näkyvät ne kursiivilla toimipistepuussa.
![Screenshot 2025-07-10 134406.png](https://support.nepton.com/hc/article_attachments/28750801644061)
