---
id: 360005073918
title: Kertymien asetukset
url: https://support.nepton.com/hc/fi/articles/360005073918-Kertymien-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Kertymät
section_id: 360000705197
section_path:
- Työajan laskenta ja hallinta
- Kertymät
labels:
- Työaikapankki
- Pankki
- Saldo
- Liukumasaldo
- työajanlyhennys
- työajanlyhennysvapaa
- pekkanen
- pekkaset
- jousto
- saldokertymä
- saldotilanne
- työlyhennysvapaa
- ylityö
- täytä työviikon tunnit
- pankkisaldo
- joustosaldo
- ylityöpankki
- pankkitunnit
- ylityöohje
promoted: false
updated_at: '2026-03-27T10:02:42Z'
edited_at: '2026-03-27T10:02:42Z'
---

# Kertymien asetukset

Kertymien asetukset määritellään joko työyhteisö- tai asetusryhmätasolla kohdassa **Työaika > Hallinta > Työyhteisön / Asetusryhmän asetukset > Työtunnit > Kertymät > Laskennan asetukset**: Klikkaa kertymää, jonka asetuksia haluat muokata. Palvelun vakiokertymillä on ne asetukset, jotka niille on määrätty (työajan lyhennysvapaa ja tasoittumisjaksotunnit kertyy ansaintataulukon mukaan, muille tätä taulukkoa ei ole), uusille kustomoiduille kertymille aukeaa kaikki mahdolliset asetukset, eli ne on mahdollista määrittää juuri sellaisiksi kun halutaan.
## Kertymien asetukset
Perusasetuksina jokaisella kertymälllä on:
![](https://support.nepton.com/hc/article_attachments/34932970549277)
**Nimi** Kertymän määritelty nimi ja sen mahdolliset kielivaihtoehdot.
**Näkyvissä viikkotaulussa** asetus määrittää, näytetäänkö kertymä ja sen arvo jokaisen käyttäjän kalenteri- ja taulukkonäkymässä. Kertymä näytetään omalla rivillään päivän alimmaisena. Arvo näytetään vihreällä jos se on positiivinen, ja punaisella, jos se on negatiivinen.
**Laske kertymän ennuste tulevaisuudessa** asetus märittää, ennustaako järjestelmä kertymän arvon tulevaisuuteen. Oletusarvo "Kyllä" jos ei asetettu. Koskee tulevaisuuteen tehtyjä suoraan kertymään vaikuttavia tapahtumia ,eli esimerkiksi kertymävapaata tai työvelvoitteen ylittävää työtä joka on ohjattu kertymään. Pelkkä työpäivän vajaaksi jäänyt velvoite ei näytä miinustunteja tulevaisuuteen.
**Koodi** Kertymälle annettu koodi, jota hyödynnetään integraatioissa identifioimaan kertymä.
Vanhoissa kustomoiduissa kertymissä oli myös tietokenttä "Kertymän yksikkö", mutta se on korvattu nyt ansainta-asetuksien osiolla.
### Lainaussäännöt
Osion asetuksilla voidaan määrittää, missä tilanteessa kertymästä lainataan automaattisesti vajaata työvelvoitetta.
![](https://support.nepton.com/hc/article_attachments/27862392391453)
**Kertymä lainaa automaattisesti kertymän saldosta** asetus määrittää, lainataanko aikaa kertymästä silloin, kun päivän työvelvoite ei ole täyttynyt.
**Älä lainaa saldosta, jos työvelvoite on käsinasetettu** asetus määrittää, lainataanko aikaa kertymästä tilanteessa, jossa päivän työvelvoite on asetettu manuaalisesti. Työvelvoite voidaan asettaa manuaalisesti kalenterinäkymässä muuttamalla päivän "Työpäivän pituus" - arvoa.
**Täytä työviikon tunnit saldosta työviikon viimeisenä päivänä** asetus määrittää, lainataanko aikaa kertymästä viikon päätteeksi tilanteessa, jossa viikon työvelvoite ei ole täyttynyt.
### Ansainnan säännöt
Osion asetuksilla määritetään, missä tilanteissa ja millä ehdoilla kertymään ansaitaan arvoa.
![](https://support.nepton.com/hc/article_attachments/27939113673629)
**Vuoden alkamispäivä** -kohdassa voidaan määrittää ansaintatulukon nollaus jollekin muulle päivälle kuin kuun alkuun tai nollaus jollekin muulle kuulle kuin tammikuuhuun. Oletuksena kertymän vuoden alkamispäivä on vuoden ensimmäinen päivä. Huom: Asetusta määrittäessä vuotena näkyy teknisistä syistä 2000. Tästä ei tarvitse välittää, riittää, että päivä ja kuukausi on määritelty oikein.
**Ansaintataulukko nollautuu joka** -kohta voidaan määritellä olemaan joko vuosi tai kuukausi. Jos ansaintakautena on vuosi, työajan lyhennysvapaan ansaita tapahtuu ansaitataulukon mukaisesti kalenterivuoden aikana. Jos ansaitakautena on kuukausi, ansainta tapahtuu joka kalenterikuukauden ajalta ansaintataulukon mukaisesti. Jos asetuksen arvoa ei ole asetettu, ansaintakautena käytetään vuotta.
**Ansaintaperuste** voidaan määritellä joko tunteina, päivinä tai kuukausina, oletus on tunteina.
Jos ansaintaperuste on kuukausina, vuosiloma-ajan laskennan työpäivien määrää tai työtuntien määrää käytetään katsomaan, ansaitaanko työkuukaudelta kertymää. Lue lisää vuosiloman ansainnan käyttöönotosta [täällä](<https://support.nepton.com/hc/fi/articles/360002560698>).
Jos ansaintaperuste on tunteina, ansaintakynnys voidaan asettaa minuuttien tarkkuudella.
Huom! Ansaintaperusteena ei voi käyttää kuukausina, jos ansaintakautena on kuukausi. Jos näin on asetettu, kertymää ei ansaita lainkaan.
**Ansaitaan** -kohtaan valitaan ansaitaanko vapaat tunteina vai päivinä.
**Laskentatapa osa-aikaisilla työntekijöillä** -kohdassa voidaan määrittää ansainnan tulevan henkilölle määritetyn työaikaprosentin mukaan. Jos työntekijät esimerkiksi ansaitsisivat 17 työpäivän jälkeen 8 tuntia kertymävapaata, 50% työaikaprosentilla työntekijä ansaitsisi 17 työpäivän jälkeen 4 tuntia kertymävapaata.
**Ohita ansaintaprosentti** -kohdassa voidaan määrittää ansainnan tulevan jonkin tietyn prosentin mukaan, esimerkiksi jos ansaintaprosentin tarvitsee olla eri kuin työntekijän työaikaprosentti.
**Ansaitse jos työsuhteen kesto ylittää** -kohdassa voidaan määritellä työsuhteen vähimmäiskesto kertymän ansaitsemiselle. Tämä on käytössä vain, jos Työsuhde-osiossa on määritelty työsuhteen alkamispäivä.
**Ansaitaan työsuhteen alusta** -kohdassa voidaan määrittää, että kertymää ansaitaan työsuhteen alusta lähtien. Jos arvona on "Ei" tai arvoa ei ole asetettu, kertymän ansainta alkaa vasta sen jälkeen, kun työsuhde on kestänyt kohdassa **Ansaitse jos työsuhteen kesto ylittää** määritettyjen kuukausien verran.
**Ansaitaan vain säännölliseltä työajalta** -kohdassa voidaan määrittää, että kertymää ansaitaan vain säännölliseltä työajalta, eli siten että ylityötä ei oteta huomioon.
**Ansaitse kertymästä lainatusta ajasta** -kohdassa voidaan määrittää, ansaitaanko kertymää ajasta joka on lainattu kertymästä, kuten esimerkiksi aika joka on lainattu saldosta.
**Ansaintataulukko** Jos kertymään ansaitaan kertymävapaata kun tietty määrä töitä on tehty, täytetään ansaintataulukkoon vaaditut työtunnit ja niistä ansaittavat vapaat. Taulukko voidaan täyttää joko työtunteina tai työpäivinä.
![](https://support.nepton.com/hc/article_attachments/27939137591965)
### Käyttämisen säännöt
Osion asetuksilla voidaan määrittää, missä tilanteissa kertymästä vähennetään arvoa ja minkä verran.
![](https://support.nepton.com/hc/article_attachments/27862396205597)
**Päivät, jotka lasketaan vapaaksi/lomaksi** asetus määrittää, mitkä viikonpäivät kuluttavat kertymän arvoa, kun kirjataan kertymävapaata. Myös alla olevat määritykset voivat vaikuttaa siihen, miten kertymää korvataan tai käytetään. Oletus on maanantaista sunnuntaihin.
**Vain päivät, joilla on työvelvoite, lasketaan vapaaksi/lomaksi** asetus määrittää, pitääkö päivällä olla työpäivän pituus/työvelvoite, jotta se lasketaan korvattavaksi vapaaksi/lomaksi.
**Vapaa/loma jätetään huomiotta päivinä, joilla on työtä** jos asetettu "Kyllä", mikä tahansa tehty työtapahtuma päivän aikana estää kertymävapaan käyttämisen tai sen vähenemisen kertymän saldosta kyseisenä päivänä. Oletuksena "Ei".
**Vapaa/loma jätetään huomiotta juhlapyhinä** \- Jos asetettu "Kyllä", juhlapyhänä kirjattu kertymävapaa ei vähene saldosta. Oletuksena "Ei".
**Vapaa/loma maksetaan, kuten** asetus määrittää, millä tavalla työntekijälle korvataan kertymän vapaa. Käytännössä tämä vaikuttaa siihen, miten kertymä näytetään kalenterissa ja viedään järjestelmästä eri palkkajärjestelmiin. Esimerkiksi "Säännöllinen työaika" näytetään kalenterissa ja viennissä ('BasicTime') normaalina palkkana, kun taas "Vuosiloma" ei näy kalenterissa eikä viedä Vuosilomana ('YearLeave') ulkoisiin järjestelmiin. Kertymävapaat jotka maksetaan kuten vuosiloma eivät tällä hetkellä näy vuosilomaraporteissa, koska vuosiloman kerryttämisessä ja käytössä tulee käyttää järjestelmän nykyistä olemassaolevaa vuosiloman laskentaa.
**Korvaus vapaa/lomapäivänä ja Kertymästä vähennettävä määrä vapaa/lomapäivänä** asetukset määrittävät, kuinka paljon työntekijälle korvataan ja kuinka paljon kertymästä vähennetään vapaa/lomapäivänä. Molemmissa määrityksissä on samat alla olevat vaihtoehdot. Määritykset on eriytetty, koska joskus voi olla tarkoituksenmukaista korvata henkilölle eri määrä kuin mitä kertymäsaldosta vähennetään, esimerkiksi korvaus maksetaan tunneissa, mutta saldo mitataan päivinä. Jos kertymä lasketaan päivissä, 1 päivä on 24 tuntia, puoli päivää on 12 tuntia jne.
  *     * **Käytetty velvoitteen määrä** \- Korvaus korvataan henkilölle työpäivän pituuden/työvelvoitteen mukaisesti. Esimerkiksi jos työpäivänä on käytetty tunnin vapaa kertymästä, maksetaan yhden tunnin edestä. Jos työpäivän pituus on 7,5 tuntia ja kertymävapaata merkitään 10 tuntia, maksetaan 7,5 tunnin edestä. Vapaapäivänä kertymävapaata ei makseta, riippumatta muista asetuksista.
    * **Prosenttiosuus (0-1) velvoitteesta** \- Mahdollista asettaa vain kertymästä vähennettävälle määrälle. Määrä joka kertymästä vähennetään perustuu prosenttiosuuteen työvelvoitteesta, joka voidaan määrittää arvoksi välillä 0-1. Toistaiseksi vähennys tukee vain arvoja 0, 0.5 ja 1, eli tässä järjestyksessä tarkoittavat prosenttiosuutena 0%, 50% ja 100%. Prosenttiosuuden vähentäminen on hyödyllistä esimerkiksi silloin kun kertymää halutaan merkitä kokonaisina tai puolikkaina päivinä. Jos kertymävapaa on yli 60% työpäivän pituudesta, käytetään kertymästä koko päivä.
    * **Kiinteä määrä / päivä** \- Kiinteä määrä joka työntekijälle korvataan ja/tai vähennetään työntekijän kertymän saldosta sekä päivinä että on työvelvoitetta että päivinä joilla ei ole työvelvoitetta (katso lisää alta)
    * **Työpäivän pituus** \- Korvaa ja/tai vähentää kertymän saldosta työntekijälle heidän kyseisen työpäivän pituuden mukaan.
    * **Viidesosa työviikon pituudesta** \- Korvaa ja/tai vähentää kertymän saldosta työntekijälle viidesosan heidän viikon työvelvoitteestaan. Tätä voidaan käyttää esimerkiksi kun vähennetään päiviä jolloin työtekijän ei odoteta tekevän töitä mutta jotka ovat kuitenkin määritetty päiviksi joiden pitäisi korvata kertymävapaata.
    * **Työpäivän enimmäispituus** \- Korvaa ja/tai vähentää kertymän saldosta työntekijälle heidän työpäivän enimmäispituuden mukaan.
      * **Määrä päivinä, joilla on työpäivän pituus/Määrä päivinä, joilla ei ole työpäivän pituutta** \- Jos "Kiinteä määrä / päivä" on käytössä, nämä tulee asettaa, jotta voidaan määrittää kuinka paljon korvataan/vähennetään päivinä jolloin työntekijällä on työpäivä ja vapaapäivä.


### Rajoitukset ja säädöt
Osiossa voidaan määrittää kertymälle maksimi- ja minimirajoja sekä määrittää mitä niiden saavuttaessa tapahtuu.
![](https://support.nepton.com/hc/article_attachments/27862396213149)
**Saldo saa tippua/nousta arvoon päivän alussa/lopussa** asetuksella määritellään, mikä on minimi/maksimi arvo, johon kertymän arvo voi pudota/nousta päivän alussa ja lopussa.
**Negatiivisen/Positiivisen saldorajan käyttäytyminen** määrittää, mitä tapahtuu tilanteessa, jossa asetettu minimi/maksimiarvo on saavutettu.
Kertymien minimi- ja maksimirajojen asetukset on kuvattu tarkemmin [tässä ohjeessa](<https://support.nepton.com/hc/fi/articles/360010514358>).
**Saldon enimmäiskertymä vuorokaudessa** asetuksella voidaan määrittää, kuinka paljon kertymää voi kerryttää maksimissaan yhden vuorokauden aikana.
## Esimerkki - Saldon yleisimmät määritykset
Tärkeimmät määritykset saldokertymään ovat saldon enimmäiskertymä vuorokaudessa sekä vähimmäis- ja enimmäismäärät. Vähimmäismäärää ei pääsääntöisesti kannata määrittää, koska silloin ei nähdä helposti, jos miinussaldo alkaa kertyä suuremmaksi kuin määritetty arvo. 
![](https://support.nepton.com/hc/article_attachments/27939208880413)
Asetuksella **Täytä työviikon tunnit saldosta työviikon viimeisenä päivänä** voidaan määrittää mahdolliset saldovähennykset tehtäväksi vasta työviikon viimeisenä päivänä. Mikäli tämän asetuksen ollessa käytössä halutaan välttää saldon väheneminen tiettyjä tapahtumatyyppejä käytettäessä, voidaan se määritellä kohdassa **Työtunnit > TES > Tapahtumatyypit, jotka lasketaan työviikkoon**. 
  * **Kyllä** : tapahtumatyyppi vaikuttaa viikoittaisen ylityön muodostumiseen, eikä tunteja täytetä saldosta työviikon viimeisenä päivänä.
  * **Ei** : tapahtumatyyppi ei vaikuta viikoittaisen ylityön muodostumiseen ja tunnit täytetään saldosta työviikon viimeisenä päivänä.
  * **Kyllä, mutta ei ylityön muodostumiseen** : tapahtumatyyppi ei vaikuta viikoittaisen ylityön muodostumiseen, mutta tunteja ei täytetä saldosta työviikon viimeisenä päivänä.


![mceclip0.png](https://support.nepton.com/hc/article_attachments/6989695773213)
## Esimerkki - Lomarahavapaan käyttö lauantaisin
Jos lomarahavapaan halutaan kuluttavan vuosiloman tyyliin vapaita maanantaista lauantaihin ja lauantaille kirjatut lomarahavapaapäivät halutaan nostaa palkka-aineistolle muiden lomarahavapaiden mukana, on tähän palvelussa neljä eri vaihtoehtoa.
**Vaihtoehto 1** \- Lauantai ei nouse palkka-aineistolle, jos päivän työvelvoite (eli työpäivän pituus) on 0h. [Työpäivän pituus ](<https://support.nepton.com/hc/fi/articles/360002558417>)-asetukseen voidaan asettaa poikkeus lauantaille sekä [työviikon pituus](<https://support.nepton.com/hc/fi/articles/360002558537>) -asetukseen poikkeus koko työviikolle, että jos päivälle on kirjattu tapahtumaa 'Lomarahavapaa'', työpäivän pituus ja työviikon pituus määrittyvät automaattisesti arvoon X. Tällöin kalenteriin muodostuu lomarahavapaapäiviltä säännöllistä työaikaa sekä viikolla tehty työn määrä kasvaa. Lomarahavapaa muodostaa palkka-aineistolle tulkittua työaikaa, mutta ilman työviikon pituuden kasvattamista näin ei tapahdu, jos työviikon pituus on aiemmin viikolla tehty jo täyteen. Tästä syystä poikkeus tarvitaan sekä lauantain työpäivän pituudelle että koko työviikolle.
**Vaihtoehto 2** \- Asetetaan lomarahavapaa-kertymän asetuksiin **Korvaus vapaa/lomapäivinä** -kohtiin **Määrä päivinä, joilla on työpäivän pituus** ja **Määrä päivinä, joilla ei ole työpäivän pituutta** jokin kiinteä tuntimäärä**.** Asetuksella määritetään, kuinka paljon työntekijälle korvataan vapaa/lomapäivänä ja paljonko korvaus on päivinä, joille on määritetty työpäivän pituus ja paljonko päivinä, joilla ei ole työpäivän pituutta. 
![](https://support.nepton.com/hc/article_attachments/20192177644957)
**Vaihtoehto 3** \- Muodostetaan lomarahavapaiden poimintasääntö merkityn työajan (MarkedTime) mukaan. Poimintasääntö löytyy [täältä,](<https://support.nepton.com/hc/fi/articles/360008045337>) kohdasta ''Poimitaan lomarahavapaa myös lauantailta, jolla ei työvelvoitetta''. Poiminnassa on otettu huomioon, että sunnuntai ei nouse aineistolle, vaikka sunnuntaillekin olisi kirjattu lomarahavapaata. 
**Vaihtoehto 4** \- Jos halutaan, että lomarahavapaa käyttäytyy kuin vuosiloma, tällöin neljäs vaihtoehto on luoda palveluun uusi, kustomoitu lomarahavapaa-tapahtumatyyppi, joka käyttäytyy kuin vuosiloma ja tätä tapahtumatyyppiä vastaava kertymä. Katso alta ohje uuden kertymän luomisesta. Ohje uuden tapahtumatyypin luomiseen puolestaan löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002519157-Tapahtumatyyppien-lis%C3%A4%C3%A4minen-k%C3%A4ytt%C3%B6%C3%B6notto-ja-muokkaaminen>).
