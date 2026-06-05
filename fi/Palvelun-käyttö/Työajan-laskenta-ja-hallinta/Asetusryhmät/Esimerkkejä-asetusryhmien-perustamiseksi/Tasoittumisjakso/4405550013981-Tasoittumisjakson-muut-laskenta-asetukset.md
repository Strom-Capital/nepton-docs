---
id: 4405550013981
title: Tasoittumisjakson muut laskenta-asetukset
url: https://support.nepton.com/hc/fi/articles/4405550013981-Tasoittumisjakson-muut-laskenta-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tasoittumisjakso
section_id: 4410638658833
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
- Tasoittumisjakso
labels:
- jaksolisätyö
promoted: false
updated_at: '2025-10-16T10:00:01Z'
edited_at: '2025-10-16T10:00:00Z'
---

# Tasoittumisjakson muut laskenta-asetukset

## Tasoittumisjakson laskennan asetukset  
Tasoittumisjaksolla on muita asetuksia, joilla voidaan ohjata erilaisten kertymien ja tapahtumatyyppien toimintaa tasoittumisjakson laskennassa sekä huomioida eri TES:ien eroavaisuuksia. Asetukset ja niiden toiminta on kuvattu alla.
### Käytä TES-asetuksia tapahtumatyyppien laskentaan jaksolle
Jos tämä asetus on päällä, tasoittumisjakson laskenta hyödyntää TES-asetuksia "[Tapahtumatyypit, jotka lasketaan työviikkoon](<https://support.nepton.com/hc/fi/articles/25639644303645>)" ja "[Poissaolotyypit, jotka lasketaan työviikkoon](<https://support.nepton.com/hc/fi/articles/28576011538077>)" sen määrittämiseen mitkä tapahtumatyypit lasketaan tasoittumisjakson työksi. Tämä mahdollistaa esimerkiksi sen että palkattomat poissaolot voidaan määrittää laskettavaksi 
"Poissaolotyypit, jotka lasketaan työviikkoon"-asetuksella voidaan määrittää että jotain poissaolotyyppiä ei lasketa tasoittumisjakson työksi, esimerkiksi jos on asetettu että palkaton poissaolo lasketaan, voidaan vielä erikseen määrittää että esimerkiksi Ammattiyhdistystoiminta-tyypin poissaoloa ei lasketa määrittämällä sille asetukseksi "Ei".
### Lisätyö lasketaan tasoittumisjakson työtunneiksi
Tämä asettaa sen, lasketaanko normaalista päivä- tai viikkoylityön laskennasta syntyvä lisätyö tasoittumisjakson työtunneiksi.
Esimerkiksi tasoittumisjakso on viikon mittainen ja oletettu työmäärä on 40 tuntia ja henkilö tekee 40 tuntia säännöllistä työtä ja 2,5 tuntia päiväkohtaista lisätyötä (ei tasoittumisjakson lisätyötä). Jos asetus on päällä, tasoittumisjaksolla tehdyt tunnit ovat 42,5h, muutoin tasoittumisjaksolla tehdyt tunnit ovat 40h. Asetus koskee vain palkkana maksettavaa lisätyötä.
### Käsittele juhlapyhät työpäivinä ylityön enimmäismäärän laskennassa
Lasketaanko tasoittumisjaksolla arkipäivänä (ma-pe) oleva, työviikkoa lyhentävä juhlapyhä työpäiväksi.
Esimerkin tasoittumisjakso on viikon mittainen, helatorstai on juhlapyhä ja "Rajat jakson työpäivinä" -asetus, kuten alla. Ylityötä on viikolla (tiistai 24.5.2022) kertynyt 2,5 tuntia.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/6533885294109)
![mceclip6.png](https://support.nepton.com/hc/article_attachments/6534341145885)
Jos asetuksen arvo on "Ei" tai "Ei asetettu", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **neljälle** työpäivälle 50% ylityönä, ja jakson muu ylityö on 100% ylityötä, jota voi olla työpäivää kohden tässä tapauksessa loputon määrä.
![mceclip7.png](https://support.nepton.com/hc/article_attachments/6534381945245)
Jos asetuksen arvo on "Kyllä", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **viidelle** työpäivälle 50% ylityönä.  
![mceclip8.png](https://support.nepton.com/hc/article_attachments/6534370301213)
### Käsittele poissaolopäivät työpäivinä ylityön enimmäismäärän laskennassa
Lasketaanko tasoittumisjaksolla oleva (ma-pe) sijoittuva poissaolo työpäiväksi.
Esimerkin tasoittumisjakso on viikon mittainen. Ma-to työpäiviä, pe poissaolopäivä (sairausloma) ja "Rajat jakson työpäivinä" -asetus, kuten alla. Ylityötä on viikolla (tiistai 7.6.2022) kertynyt 2,5 tuntia.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/6533885294109)
![mceclip5.png](https://support.nepton.com/hc/article_attachments/6534256647837)
Jos asetuksen arvo on "Ei" tai "Ei asetettu", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **neljälle** työpäivälle 50% ylityönä, ja jakson muu ylityö on 100% ylityötä, jota voi olla työpäivää kohden tässä tapauksessa loputon määrä.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/6533986226589)
Jos asetuksen arvo on "Kyllä", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **viidelle** työpäivälle 50% ylityönä.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/6534083233181)
### Käsittele vuosilomapäivät työpäivinä ylityön enimmäismäärän laskennassa
Lasketaanko tasoittumisjaksolla oleva (ma-pe) sijoittuva vuosiloma työpäiväksi.
Esimerkin tasoittumisjakso on viikon mittainen. Ma-to työpäiviä, pe vuosilomapäivä ja "Rajat jakson työpäivinä" -asetus, kuten alla. Ylityötä on viikolla (tiistai 7.6.2022) kertynyt 2,5 tuntia.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/6533885294109)
![mceclip0.png](https://support.nepton.com/hc/article_attachments/6533881998749)  
  
Jos asetuksen arvo on "Ei" tai "Ei asetettu", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **neljälle** työpäivälle 50% ylityönä, ja jakson muu ylityö on 100% ylityötä, jota voi olla työpäivää kohden tässä tapauksessa loputon määrä.  
  
![mceclip3.png](https://support.nepton.com/hc/article_attachments/6533986226589)
Jos asetuksen arvo on "Kyllä", jaetaan 2,5 tunnin ylityöstä 30 minuuttia **viidelle** työpäivälle 50% ylityönä.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/6534083233181)
### Käytä työpäivän keskipituutta tasoittumisjakson työpäiville, jotka ovat työsuhteen ulkopuolella
Lisätäänkö tasoittumisjakson tunteihin "Työpäivän keskipituus" -asetuksen mukainen määrä tunteja jokaista tasoittumisjaksolla maanantain ja perjantain välille sijoittuvaa päivää kohden, mikäli päivä ei sisälly työsuhteeseen.
Esimerkiksi tasoittumisjakso on viikon mittainen, ma-pe ovat työpäiviä, mutta työsuhde alkaa vasta tiistaina, ja "Työpäivän keskipituus" -asetus on 8 tuntia. Jos asetus on päällä, tasoittumisjakson (ti-pe aikana) toteutuneisiin työtunteihin lisätään laskennallinen 8 tuntia. Tunnit lisätään myös päiviltä, jotka ovat työsuhteen ulkopuolella ja joilla on tunteja lainattu kertymästä.
### Estä tapahtumia lisäämästä tasoittumisjaksolle ylityötä
Lasketaanko tapahtumatyypeille kirjattu aika tasoittumisjakson työtunneiksi vai ei.
Esimerkiksi tasoittumisjakso on viikon mittainen ja oletettu työmäärä on 40 tuntia ja henkilö tekee 40 tuntia säännöllistä työtä ja 8 tuntia matka-aikaa. Jos matka-aika on asetettu estämään ylityön lisääminen tasoittumisjaksolle, tasoittumisjaksolla tehdyt tunnit ovat 40h, muutoin tasoittumisjaksolla tehdyt tunnit ovat 48h.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4405534622493)
### Poissaolot, joiden laskennassa käytetään keston sijaan työpäivän keskipituutta
Lasketaanko tapahtumatyypeille kirjattu aika tasoittumisjakson työtunneiksi vai käytetäänkö kirjatun ajan sijaan "Työpäivän keskipituus" -asetuksen arvoa kullekin päivälle, jolla näitä tapahtumatyyppejä on merkitty.
Esimerkiksi tasoittumisjakson työpäivän keskipituus on 8 tuntia ja sairauslomat on asetettu käyttämään työpäivän keskipituutta. Henkilöllä on 9 tunnin työvuoro:
  * jos hän on sen kokonaisuudessaan sairauslomalla, päivän tunnit tasoittumisjakson laskennassa ovat 8h
  * jos hän tekee vuorosta 4 tuntia töitä, ja sen jälkeen lähtee sairauslomalle, päivän tunnit tasoittumisjakson laskennassa ovat 8h (työpäivän keskipituuden mukaan)
  * jos hän tekee vuorosta 8,5 tuntia töitä, ja sen jälkeen lähtee sairauslomalle, päivän tunnit tasoittumisjakson laskennassa ovat 8,5h (tehdyn työajan mukaan, kun aika ylittää työpäivän keskipituuden).


![mceclip1.png](https://support.nepton.com/hc/article_attachments/4405534630045)
### Kertymään tehty tunti tunnista -ylityö lasketaan tasoittumisjaksoon
Näillä asetuksilla voidaan ohjata lasketaanko tunti tunnista - korvattava aika tasoittumisjakson työaikaan vai ei. Laskentaa voidaan ohjata se mukaan mihin kertymään tehty työ on kohdistettu.
Jos esimerkiksi pankkiin kohdistettu tunti tunnista korvattava työ halutaan laskea tasoittumisjakson työtunneiksi, se onnistuisi seuraavilla asetuksilla.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4405558260509)
### Työpäivän keskipituus
Mikä on laskennallinen työpäivän pituus ma-pe päivinä (Tasoittumisjakson laskennassa oletetut työpäivät ovat ma-pe). Jos tasoittumisjakson aikana tehdyt työtunnit jaetaan työpäivien kesken ja päiväkohtainen määrä ylittää työpäivän keskipituuden, muodostuu lisä- ja ylityötunteja.
Esimerkiksi tasoittumisjakso on viikon mittainen ja asetus on 8h, tällöin tasoittumisjakson työtunnit olisivat 40h (5 x 8h) ennen lisä- ja ylityötuntien muodostumista.
### Työpäivän pituus tulee työvuoroista
Lasketaanko tasoittumisjakson maksimityömäärä sillä olevien työvuorojen perusteella.
Esimerkiksi tasoittumisjakso on viikon mittainen ja jokaisella (ma-su) päivällä on 8h työvuoro. Jos asetus on päällä, tasoittumisjakson maksimityömäärä olisi 56h (7 x 8h)
### Rajat jakson työpäivinä
#### Työpäivän pituuden ylityksestä korvataan maksimissaan - Lisätyönä
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4405558279581)
Maksimilisätyön määrä per tasoittumisjakson työpäivä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 12 minuuttia asetetaan 00:12 ja 1 tunti 30 minuuttia asetetaan 01:30.
Esimerkiksi jos tasoittumisjakso on viikon mittainen ja asetus on 00:12, tällöin tasoittumisjakson maksimilisätyön määrä on 1h (5 työpäivää).
#### Työpäivän pituuden ylityksestä korvataan maksimissaan - 50% ylityönä
50% ylityön maksimimäärä per tasoittumisjakson työpäivä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 24 minuuttia asetetaan 00:24 ja 1 tunti 30 minuuttia asetetaan 01:30.
Esimerkiksi jos tasoittumisjakso on viikon mittainen ja asetus on 00:24, tällöin tasoittumisjakson 50% ylityön maksimimäärä on 2h (5 työpäivää).
#### Työpäivän pituuden ylityksestä korvataan maksimissaan - 100% ylityönä
100% ylityön maksimimäärä per tasoittumisjakson työpäivä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 5 tuntia asetetaan 05:00 ja 1 tunti 30 minuuttia asetetaan 01:30.
Esimerkiksi jos tasoittumisjakso on viikon mittainen ja asetus on 05:00, tällöin tasoittumisjakson 100% ylityön maksimimäärä on 25h (5 työpäivää).
### Tasoittumisjakson korvaus
#### Lisätyötä ansaitaan kokonaistuntien jälkeen
![mceclip4.png](https://support.nepton.com/hc/article_attachments/4405534647709)
Mikä on tasoittumisjakson enimmäistuntimäärä, jonka jälkeen ansaitaan lisätyötä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 10 tuntia 30 minuuttia asetetaan 10:30 ja 120 tuntia asetetaan 120:00.
#### 50% ylityötä ansaitaan kokonaistuntien jälkeen
Kuinka monen jaksotyötunnin jälkeen ansaitaan 50% ylityötä. Huomaa, että ennen tätä rajaa ansaitaan lisätyötä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 10 tuntia 30 minuuttia asetetaan 10:30 ja 126 tuntia asetetaan 126:00.
Esimerkiksi jos tasoittumisjakson enimmäistuntimäärä on 120h ja tämä asetus on 126h, koko tasoittumisjakson ajalta voi ansaita maksimissaan 6h lisätyötä ja 6 lisätyötunnin jälkeen ansaitaan 50% ylityötä.
#### 100% ylityötä ansaitaan kokonaistuntien jälkeen
Kuinka monen jaksotyötunnin jälkeen ansaitaan 100% ylityötä. Huomaa, että ennen tätä rajaa ansaitaan 50% ylityötä. Määrä asetetaan muodossa TT:MM eli esimerkiksi 10 tuntia 30 minuuttia asetetaan 10:30 ja 150 tuntia asetetaan 150:00.
Esimerkiksi jos tasoittumisjakson maksimityötunnit ovat 120h, maksimilisätyön määrä on 6h ja tämä asetus on 150h, koko tasoittumisjakson ajalta voi ansaita maksimissaan 24h 50% ylityötä, jonka jälkeen ansaitaan 100% ylityötä.
#### Tunteja ei korvata kokonaistuntien jälkeen
Kuinka monen jaksotyötunnin jälkeen tunteja ei enää korvata. Määrä asetetaan muodossa TT:MM eli esimerkiksi 10 tuntia 30 minuuttia asetetaan 10:30 ja 500 tuntia asetetaan 500:00.
Esimerkiksi jos tasoittumisjakson maksimityötunnit ovat 120h, maksimilisätyön määrä on 6h, 50% ylityön maksimimäärä on 24h ja tämä asetus on 500h, koko tasoittumisjakson ajalta voi ansaita maksimissaan 350h 100% ylityötä, jonka jälkeen ylityötunteja ei korvata.
Tämä asetuksen tuntimäärä useimmiten asetetaan niin korkeaksi, että raja ei tule vastaan.
### Lyhennykset tasoittumisjaksojen rajoihin juhlapyhinä
Työviikkoa lyhentävät juhlapyhät on mahdollista asettaa lyhentämään tasoittumisjakson:
  * Säännöllisen työajan maksimimäärään
  * Lisätyön maksimimäärään
  * 50% ylityön maksimimäärään


Esimerkit asetuksien käyttäytymisestä löydät artikkelista "[Työviikkoa lyhentävien juhlapyhien lyhennykset tasoittumisjaksolla](<https://support.nepton.com/hc/fi/articles/4410641911825>)"
