---
id: 4410630282257
title: Tasoittumisjakson ylityölaskennan määrittely
url: https://support.nepton.com/hc/fi/articles/4410630282257-Tasoittumisjakson-ylity%C3%B6laskennan-m%C3%A4%C3%A4rittely
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
updated_at: '2025-11-24T08:54:38Z'
edited_at: '2025-11-24T08:54:38Z'
---

# Tasoittumisjakson ylityölaskennan määrittely

Tasoittumisjakson ylityörajat määritellään kuvaamalla, kuinka jaksolla oleva yksittäinen työpäivä vaikuttaa ylityörajojen muodostumiseen. Päiväkohtainen vaikutus kuvataan alla olevan kappaleen mukaisesti "Ylitöiden ansaintarajat päiväkohtaisena".
Mikäli työehtosopimuksessa kuvattuun jakson ylityörajoihin ei voida päätyä laskemalla jakson päiväkohtaista vaikutusta, niin määrittelyt tehdään kuten on kuvattu kappaleessa "Ylitöiden ansaintarajat jaksokohtaisena". 
Tasoittumisjakson ylitöiden laskenta-asetukset löytyvät asetusryhmän asetuksista kohdasta **Työtunnit > Kertymät > Laskennan asetukset: Tasoittumisjaksotunnit > Tasoittumisjakson rajat.**
## Ylitöiden ansaintarajat päiväkohtaisena
Tasoittumisjakson päiville asetetaan työpäivän keskipituus jakson enimmäistyöajan laskemiseksi. Jakson enimmäistyöajaksi muodostuu jakson arkipäivien lukumäärä kerrottuna asetetulla työpäivän keskipituudella. Jos työpäivän keskipituus on määritelty jakson asetuksiin, lasketaan työpäiviksi päivät maanantaista perjantaihin. Jos työpäivän keskipituus tulee vuorosta, lasketaan työpäiviksi päivät, joilla on suunniteltu vuoro.
Ylityötä korvataan siltä ajalta, jolloin toteutunut työaika ylittää jakson enimmäistyöajan. Jakson ylityötä korvataan lisätyönä asetettuun lisätyörajaan saakka. Tämän jälkeen muodostuu 50% ylityötä asetettuun 50% ylityörajaan saakka, jonka jälkeen muodostuu 100% ylityötä asetettuun 100% ylityörajaan saakka.
Jaksolle muodostuva lisä- ja ylityön enimmäismäärä lasketaan kertomalla jakson arkipäivien määrä asetetulla lisä- tai ylityön arvolla. Asetuksen arvoksi asetetaan se määrä, kuinka paljon yksi arkipäivä vaikuttaa jakson ylityörajaan. Näiden asetusten arvot asetetaan siten, että työehtosopimuksessa esitetty jaksoylityön laskenta toteutuu oikeilla jakson ylityörajoilla.
Tasoittumisjakson päivien ylityökorvausten määrät asetetaan muodossa TT:MM. Esimerkiksi 12 minuuttia muodossa 00:12 ja 5 tuntia muodossa 05:00.
Alla esimerkki asetuksista, jolla erään työehtosopimuksen jakson ylityölaskenta määritetään. Työehtosopimuksessa tasoittumisjakson laskenta on kuvattu näin:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21079162614941)
Tämän työehtosopimuksen mukainen **12 viikon tasoittumisjakson ylityölaskennan** tulkinta tehdään seuraavalla tavalla:
  * Työpäivän keskipituus saadaan jakamalla 12 viikon enimmäistyöaika 450 tuntia 12 viikolla ja viidellä päivällä, josta saadaan arvoksi 7:30
  * Lisätyön maksimimäärä asetetaan nollaksi, sillä tämä työehtosopimus ei korvaa tasoittumisjakson enimmäismäärän ylittävää työtä lisätyönä.
  * 50% ylityön maksimimäärä asetetaan sen mukaisesti, kuinka paljon työehtosopimuksessa korvataan 50% ylityötä. Yllä olevassa esimerkissä kaikki jakson enimmäistyöajan ylittävät työ korvataan 50% ylityönä. Tällöin päiväkohtaiseksi arvoksi asetetaan niin suuri arvo, että kaikki jakson enimmäismäärän ylittävät työ korvataan 50% korotuksella. Tällöin arvoksi asetetaan 10:00 tuntia. Tämä johtaisi laskennallisesti tässä esimerkissä 600 tunnin 50% ylityörajaan jaksolla (60 arkipäivää * 10:00 tuntia) 
  * 100% ylityön maksimimäärä asetetaan nollaksi, sillä esimerkin työehtosopimus ei korvaa jakson ylittävää työaikaa 100% ylityönä. Mikäli työehtosopimus korvaisi 100% ylityötä, niin 50% raja olisi työehtosopimuksen osoittama, jolloin 100% korvausta muodostuisi 50% ylityön jälkeen.


![blobid0.png](https://support.nepton.com/hc/article_attachments/21079175796893)
## Ylitöiden ansaintarajat jaksokohtaisena
Tasoittumisjaksolle asetetaan rajat, jonka jälkeen tasoittumisjaksolta muodostuu lisätyötä tai ylityötä. Tasoittumisjakson ylityökorvausten määrät asetetaan muodossa TT:MM. Esimerkiksi 120 tuntia muodossa 120:00. 
Alla esimerkki asetuksista, jossa**kolmen viikon tasoittumisjaksolla**
  * Työpäivän keskipituus saadaan jakamalla 3 viikon enimmäistyöaika 120 tuntia 3 viikolla ja viidellä työpäivällä, josta saadaan arvoksi 8:00 tuntia.
  * Lisätyötä ansaitaan tasoittumisjakson 126 tuntiin asti, jonka jälkeen ansaitaan 50% ylityötä.
  * 50% ylityötä ansaitaan tasoittumisjakson 150 tuntiin asti, jonka jälkeen ansaitaan 100% ylityötä
  * 500 tasoittumisjakson tunnin jälkeen tunteja ei korvata. Tämä määritys on tekninen, ja se asetetaan niin suureksi, että kaikki jakson ylittävä työaika korvataan vähintään 100% korvauksella.


![blobid1.png](https://support.nepton.com/hc/article_attachments/21079175800477)
Jos henkilö esimerkiksi työskentelee 158 tuntia tasoittumisjakson aikana, ylityöt lasketaan seuraavasti:
  * 6 tuntia lisätyötä
  * 24 tuntia 50% ylityötä
  * 8 tuntia 100% ylityötä


Huom! Mikäli tasoittumisjakson ylityörajat muuttuvat kesken tasoittumisjakson, käyttää palvelu päättymispäivänä voimassa olevia asetusarvoja.
## Tasoittumisjakson määrittäminen osa-aikaisille
Katso erillinen artikkeli "[Tasoittumisjakson määrittäminen osa-aikaisille](<https://support.nepton.com/hc/fi/articles/14849123960989>)".
## Tasoittumisjakson ylityökorvaukset palkkavientiin ryhmitettynä projekteittain
Tasoittumisjakson ylityökorvaukset voidaan sisällyttää palkkavientiin ryhmiteltynä projekteittain määrittämällä "Ryhmittele tasoittumisjakson korvaus projektikohtaisesti palkkaviennissä" Kyllä. Jos toiminnallisuus on käytössä, tasoittumisjakson ylityökorvaukset ryhmitellään siten, että ne vastaavat eri projekteihin kohdennettua työtä tasoittumisjakson aikana. Aiemmin tietyissä vanhoissa liittymäajoissa erittely on tehty ilman erillistä asetusta, mutta jatkossa asetus tulee asettaa erikseen tarvittaessa. Tämän toiminnallisuuden käyttöönotto hidastaa hieman laskennan suorituskykyä.
## AKT kuorma-autoalan TES:n mukainen katkennut tasoittumisjakso ja ylityötulkinta
Mikäli asetus **Käsittele katkennut tasoittumisjakso AKT kuorma-autoalan TES:n mukaisesti** on käytössä, tulkitaan tasoittumisjakso katkenneeksi seuraavissa tapauksissa:
  * Työsuhde on alkanut myöhemmin kuin tasoittumisjakso.
  * Työsuhde on loppunut aikaisemmin kuin tasoittumisjakso.
  * Tasoittumisjaksolla on mikä tahansa poissaolo (sairasloma, vuosiloma, poissaolo jne.)


Huomioitavaa katkenneeseen jaksoon liittyen:
  * Katkenneella jaksolla ylityöt lasketaan kaavalla _((tasoittumisjakson työtunnit) / työpäivää - työpäivän keskipituus) * työpäivät_. Työtunnit ovat tunteja päivillä, jotka eivät katkaise jaksoa ja työpäivät päiviä, joilla nämä tunnit ovat. Työpäivän keskipituus tulee tasoittumisjakson asetuksista. Mikäli työpäivän keskipituutta ei ole asetettu, käytetään oletusarvona 7,5 tuntia. 
  * Poissaolo ei katkaise jaksoa, mikäli samalla päivällä on työtapahtumia. Poissaolon tulee olla ainoa tapahtuma.
  * Asetuksella **Poissaolot, jotka eivät katkaise tasoittumisjaksoa AKT kuorma-autoalan TES:n mukaisesti** voidaan määrittää poissaolotyypit, jotka eivät katkaise tasoittumisjaksoa.
  * Mikäli päivällä on ei-katkaiseva ja katkeiseva poissaolo, tasoittumisjakso ei katkea.
  * Katkenneen jakson ylitöiden tulkinnassa yön yli kestävät työtapahtumat lasketaan kahtena työpäivänä. Esimerkiksi perjantaina klo 22:00 alkava ja lauantaina klo 06:00 loppuva työtapahtuma = 2 työpäivää.
  * Seuraavat Tasoittumisjakson ylityön laskennan asetukset käsitellään katkenneessa jaksossa kuten kuvattu ohjeessa [täällä](<https://support.nepton.com/hc/fi/articles/4405550013981-Tasoittumisjakson-muut-laskenta-asetukset#h_01HF90A3SVMZNFGBWQCE00TMCG>). 
    * Käsittele juhlapyhät työpäivinä ylityön enimmäismäärän laskennassa
    * Käsittele poissaolopäivät työpäivinä ylityön enimmäismäärän laskennassa
    * Käsittele vuosilomapäivät työpäivinä ylityön enimmäismäärän laskennassa
Nämä asetukset eivät kuitenkaan määritä poissaolopäiviä, vuosilomapäiviä tai juhlapyhiä työpäiviksi katkenneella jaksolla. 


![](https://support.nepton.com/hc/article_attachments/25672706621597)
![](https://support.nepton.com/hc/article_attachments/21079196190749)
Esimerkki 1: Luvaton poissaolo -tapahtuma ei katkaise tasoittumisjaksoa. Työpäivän keskipituus on 8 tuntia. Lisätyön määrä päivää kohden korkeintaan 0 tuntia, 50% ylityön määrä päivää kohden korkeintaan 1 tuntia 12 minuuttia. 100% ylityötä päivää kohden voi olla ns. loputtomasti, asetuksissa 99 tuntia. Kahden viikon jaksolla on työtunteja yhteensä 90. Koska jakso ei katkea, käytetään 80 tunnin rajaa jakson ylityötulkinnassa. 
![](https://support.nepton.com/hc/article_attachments/21079175817373)
![](https://support.nepton.com/hc/article_attachments/21079175803677)
Esimerkki 2: Muuten samat asetukset kuin yllä, mutta luvaton poissaolo -tapahtuma katkaisee jakson eli asetuksella **Poissaolot, jotka eivät katkaise tasoittumisjaksoa AKT kuorma-autoalan TES:n mukaisesti** ei ole määritetty poikkeuksia. Jakson ylityötulkinnan raja määrittyy nyt yllämainitun kaavan mukaisesti eli otetaan huomioon työpäivien määrä ja työpäivän keskipituus (9 * 8 = 72 tuntia). Yli menevä aika on ylityötä.
![](https://support.nepton.com/hc/article_attachments/21079196198301)
Tasoittumisjakson ylitöiden yhteenvedon i-ikonia painamalla voidaan tarkastella tasoittumisjakson enimmäistyöaikaa. Mikäli jakso on katkennut TES:n mukaisesti, on se mainittu näkymässä.
![](https://support.nepton.com/hc/article_attachments/21079196202269)
HUOM! Joissakin tapauksissa katkenneen tasoittumisjakson tulkinta antaa epäjohdonmukaisen lopputuloksen. Näin voi tapahtua esimerkiksi silloin, kun on työskennelty useana päivänä ja ylitetty jakson normaali enimmäistyöaika. Mikäli jakso tällöin katkeaa hyväksytyn syyn, kuten sairausloman takia, voi ylitöitä muodostua vähemmän kuin muodostuisi katkeamattomalla jaksolla. Mikäli jakso ei katkea luvattomasta poissaolosta, kuten yllä on määritelty, ansaitaan luvattomalla poissaololla enemmän ylitöitä kuin luvallisella. Katso esimerkit alla.
Esimerkki (katkennut tasoittumisjakso, sairausloma): Jakso katkeaa sairausloman takia. Töitä on 11 päivänä ja jokaisena päivänä 8 tuntia. Katkenneelle jaksolle ei muodostu ylitöitä, koska toteutuneiden työpäivien keskipituus on sama kuin työpäivän keskipituus jakson asetuksissa.
![](https://support.nepton.com/hc/article_attachments/21079196216349)
![](https://support.nepton.com/hc/article_attachments/21079196205725)
Esimerkki (katkeamaton tasoittumisjakso, luvaton poissaolo): Ylläolevan esimerkin sairausloma muutetaan luvattomaksi poissaoloksi. Se on määritelty poissaoloksi, joka ei katkaise jaksoa. Tällöin jaksolla sovelletaan normaalia jakson ylityötulkintaa ja 80 tunnin ylittävä aika tulkitaan ylityönä.
![](https://support.nepton.com/hc/article_attachments/21079196209181)
![](https://support.nepton.com/hc/article_attachments/21079175840157)
Mikäli näissä tapauksissa lisättäisiin vielä molemmille sunnuntaille 8 tunnin työpäivät, sairausloman takia katkenneelle jaksolle ei edelleenkään muodostuisi ylityötä. Luvattoman poissaolon jaksolle muodostuisi vastaavasti 16 tuntia lisää ylityötä.
