---
id: 360010514358
title: Kertymän minimi- ja maksimimäärän asettaminen
url: https://support.nepton.com/hc/fi/articles/360010514358-Kertym%C3%A4n-minimi-ja-maksimim%C3%A4%C3%A4r%C3%A4n-asettaminen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Kertymät
section_id: 360000705197
section_path:
- Työajan laskenta ja hallinta
- Kertymät
labels:
- maksimisaldo
- saldoleikkuri
promoted: false
updated_at: '2026-02-12T11:12:24Z'
edited_at: '2026-02-12T11:01:06Z'
---

# Kertymän minimi- ja maksimimäärän asettaminen

Tässä ohjeessa on kerrottu, miten voit määritellä saldolle ja muille kertymille minimi- ja maksimirajat ja miten nämä rajat käyttäytyvät.
Huomaathan, että jos asetat kertymälle minimi- tai maksimirajan asetuksella "rajaa ei voi ylittää", et näe todellista kertymää kalenterinäkymässä, kun minimi- tai maksimiraja on saavutettu. Rajan ylittävät tunnit on kuitenkin mahdollista ohjata suoraan esimerkiksi palkkaan tai toiseen kertymään.
## Kertymän minimi- ja maksimirajan asettaminen
Tässä artikkelissa käytetään esimerkkinä saldoa, mutta samat asetukset löytyvät muidenkin kertymien alta. Saldon rajat voi asettaa joko työyhteisötasolle tai asetusryhmäkohtaisesti. Kyseinen määritys löytyy valikosta **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Kertymät ja ylityötunnit > Saldo > Rajoitukset ja säädöt. **Maksimiraja asetetaan asetuksella**Saldo saa nousta arvoon päivän alussa/lopussa** ja minimiarvo asetuksella**Saldo saa tippua arvoon päivän alussa/lopussa.**
![](https://support.nepton.com/hc/article_attachments/25462926451613)
Poikkeuksellisen saldon maksimi- ja minimimäärän voi asettaa myös henkilötason asetuksissa **Työaika > Henkilöt > Henkilön asetukset > Kertymät ja ylityötunnit - Saldo - Saldo saa nousta arvoon päivän lopussa/Saldo saa tippua arvoon päivän lopussa.** Tämä voi olla perusteltua tilanteessa, jossa saldon maksimi- ja minimimäärien nosto tai lasku on määräaikaista ja koskee vain yhtä tai muutamia yksittäisiä henkilöitä. Jos saldon ansainnan rajat määritetään henkilötason asetuksiin, on suositeltavaa dokumentoida muutos, jotta tieto henkilölle tehdystä muutoksesta on organisaatiossa tiedossa esimerkiksi pääkäyttäjähenkilöstön vaihtuessa. 
Huomioithan, että asetukset on aina hyvä tehdä [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
## Negatiivisen ja positiivisen rajan käyttäytyminen
Saldorajan käyttäytymisen asetuksella voidaan määrittää, mitä tapahtuu tilanteessa, kun asetettu minimi- tai maksimiarvo saavutetaan. 
![](https://support.nepton.com/hc/article_attachments/25462926455837)
### Negatiivisen saldorajan ylittävän osuuden käsittely
Negatiivisen saldorajan käyttäytyminen on oletuksena "Raja voidaan ylittää, pelkkä varoitus". Tämä tarkoittaa sitä, että kun raja saavutetaan, näytetään käyttäjän kalenterissa [poikkeuksellinen kirjaus](<https://support.nepton.com/hc/fi/articles/360002560618>), eli keltainen varoituskolmio. Tunnit voivat kuitenkin mennä yli asetetun rajan arvon. 
Voidaan myös määrittää, että rajaa ei voida ollenkaan ylittää määrittämällä asetukseen "Rajaa ei voi ylittää". Tällöin laskenta pysähtyy, kun asetettu minimiarvo on saavutettu, eikä kertymän arvo voi olla rajaa alempi. Tällöin todellista kertymän arvoa ei näe kalenterinäkymästä, vaan rajatut arvot nähdään saldon hallinnolliset muutokset-raportilta.
Mikäli määritykseksi on valittu "Rajaa ei voi ylittää" ja raja tulee vastaan, ei kalenteriin muodostu enää säännöllistä työaikaa jota lainataan kertymästä, sillä kertymästä ei voi enää lainata mitään.
#### Negatiivisen saldorajan ylittävän osuuden siirto palkkaan tai toiseen kertymään
Voidaan myös määrittää, että negatiivisen saldorajan ylitys vähennetään palkasta tai jostain toisesta kertymästä. Tämä tehdään asetuksella "Negatiivisen saldorajan käyttäytyminen" valinnalla: "Siirrä rajatut: kertymään X". Jos valinnaksi valitaan palkka, ilmaantuu usersalarydata-tauluun arvon ylityspäivälle Compensationtype = 'UnpaidOverMinAccrualLimit', joka voidaan lisätä palkkasiirron poimintasääntöön. Tällöin palkkaan siirtyy rajan ylittänyt negatiivinen arvo, eli miinusarvo vähentämään palkkaa.
#### Esimerkki 1. Negatiivinen saldoraja täyttyy kesken työpäivän
Esimerkiksi, on valittu, että saldokertymän rajan ylittävät tunnit siirretään pankkikertymään ja negatiiviseksi saldorajaksi on määritetty 40 tuntia. Esimerkkikuvan henkilön saldo saavuttaa negatiivisen saldorajan keskiviikkona 21.1., kun -40 tuntia tulee täyteen saldokertymästä lainatessa päivän säännöllistä työaikaa. Saldosta voidaan lainata 5,5h, jonka jälkeen sen raja on saavutettu ja työpäivän loppuvelvoite, eli 2 tuntia miinustetaan pankkikertymästä. 
![](https://support.nepton.com/hc/article_attachments/33598314714525)
Jos rajan ylittävä määrä vähennetään toisesta kertymästä, ilmaantuu kalenteriin varoituskolmio, joka kertoo mihin kertymään rajatut tunnit on siirretty. 
![](https://support.nepton.com/hc/article_attachments/33598331255453)
Negatiivisen saldon rajaan voidaan myös määrittää, miten se käyttäytyy, kun tulevaisuuteen leimataan kertymävapaita. Vaihtoehdot ovat samat kuin yllä, eli joko raja voidaan ylittää varoituksella, tai rajaa ei voida ylittää ollenkaan.
### Positiivisen saldorajan ylittävän osuuden käsittely
Positiivisen saldorajan käyttäytyminen on oletuksena "Raja voidaan ylittää, pelkkä varoitus". Tämä tarkoittaa sitä, että kun raja saavutetaan, näytetään käyttäjän kalenterissa [poikkeuksellinen kirjaus](<https://support.nepton.com/hc/fi/articles/360002560618>), eli keltainen varoituskolmio. Tunnit voivat kuitenkin mennä yli asetetun rajan arvon. 
Voidaan myös määrittää, että rajaa ei voida ollenkaan ylittää määrittämällä asetukseen "Rajaa ei voi ylittää". Tällöin laskenta pysähtyy, kun asetettu minimiarvo on saavutettu, eikä kertymän arvo voi olla rajaa suurempi. Tällöin todellista kertymän arvoa ei näe kalenterinäkymästä, vaan rajatut arvot nähdään saldon hallinnolliset muutokset-raportilta.
#### Positiivisen rajan ylittävän osuuden ohjaus palkkaan tai toiseen kertymään
Asetuksella "Positiivisen saldorajan käyttäytyminen" voidaan ohjata rajan ylittävät tunnit joko palkkaan tai johonkin muuhun kertymään. 
![](https://support.nepton.com/hc/article_attachments/25462926458141)
#### Esimerkki 1. Tapahtuma on ohjattu ylityönä saldoon, mutta saldon maksimiraja tulee täyteen
Saldon maksimirajan ylittävä määrä maksetaan ylityönä palkkaan. Esimerkkikuvassa on esitetty tilanne, jossa saldon maksimiraja on 40h ja positiivisen saldorajan käyttäytyminen on "Siirrä ylimääräiset: Palkkaan". 
![](https://support.nepton.com/hc/article_attachments/25462918436765)
Tiistaina 18.2. Saldon arvo on 38h, ja työntekijä tekee 11h30min mittaisen työpäivän. Tästä 7h30min on säännöllistä työaikaa. Koska työn ohjaus on ylityönä saldoon, siirtyy säännöllisen työajan ylittävä aika automaattisesti saldoon siihen asti, kunnes saldon maksimiraja tulee täyteen. Tämän jälkeen loput päivän ylitöistä siirtyy palkkaan. Ylityöerottelu näyttää kalenterissa, mihin kaikkialle ylityötä on ohjattu:
![](https://support.nepton.com/hc/article_attachments/25462918437917)
Klikkaamalla nuolia erottelu saadaan vielä tarkemmaksi, jolloin nähdään tarkat määrät kuhunkin kertymään/palkkaan ohjattua ylityötä prosentteineen. Tässä esimerkissä saldoon on siirtynyt ensimmäiset 30min lisätyötä, jonka jälkeen 1h päivä50%, eli saldoon on siirtynyt yhteensä 2h. Tässä kohtaa saldon maksimiraja on tullut täyteen, ja loput ylitöistä, eli 1h päivä 50% ja 1h30min päivä 100% maksetaan palkassa. Oletuksena kalenteriin ilmestyy myös poikkeuksellisen kirjauksen keltainen varoituskolmio huomioimaan, että raja on ylitetty.
#### Esimerkki 2. Kertymän enimmäismäärän rajoittaminen tiettynä päivänä ja ylityksen maksaminen palkassa
Rajat voidaan määrittää myös määrätyille päiville (esim. jonkun sovitun lomajakson lopussa), jolloin siinä tapauksessa, että muuntamispäivänä ei ehkä ole ylitöitä, aika voidaan viedä integraation sääntöjoukkojen avulla korvaustyyppinä "PayOverAccrualLimit" (UserSalaryDatasta). Tämä sisältää kertymästä automaattisesti leikatut tunnit. Jotta kyseinen korvaustyyppi nousee usersalarydataan, tulee asetuksessa "positiivisen saldorajan käyttäytyminen" olla arvona "siirrä ylimääräiset: palkkaan".
![](https://support.nepton.com/hc/article_attachments/25462918440349)
![](https://support.nepton.com/hc/article_attachments/25462926462621)
Yllä olevassa esimerkissä 10h pankista siirretään maksuun, kun sen maksimääräksi on asetettu 00:00 31.12.2024:
![](https://support.nepton.com/hc/article_attachments/25462918443549)
