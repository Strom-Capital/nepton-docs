---
id: 360002559537
title: Tasoittumisjakson käyttöönotto
url: https://support.nepton.com/hc/fi/articles/360002559537-Tasoittumisjakson-k%C3%A4ytt%C3%B6%C3%B6notto
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
- tasoittumis
- jaksoylityö
- työajantasaamis
- tasoitusjakso
- tasoittuva
- periodityö
promoted: false
updated_at: '2025-11-19T13:27:59Z'
edited_at: '2025-11-19T13:27:59Z'
---

# Tasoittumisjakson käyttöönotto

Tässä ohjeessa kuvataan määritykset tasoittumisjakson työajan laskennan käyttöönottamiseksi. Tasoittumisjakson laskenta esittää kulloinkin raportoitavan ajanjakson tasoittumisjakson tulokset lisätyön ja ylityöprosenttien mukaan tulkittuna.
Tasoittumisjaksomääritysten kautta on mahdollista seurata myös vuosityöaikaa. Vuosityöajan seurannan kuvauksen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360016341617>).
## Käyttöönoton edellytykset
Tasoittumisjakson käyttöönotto vaatii oman asetusryhmänsä. Asetusryhmä on suositeltavaa lisätä omaksi pääryhmäkseen, ts. siten, että sillä ei ole pääaasetusryhmää. Näin estetään tarpeeton asetusten periytyminen tasoittumisjakson asetusryhmään.
Ohjeistus uuden asetusryhmän lisäämiseksi löytyy [täältä.](<https://support.nepton.com/hc/fi/articles/360002557537>)
**Tasoittumisjakson asetusryhmässä tulee ottaa huomioon seuraavat asiat:**
\- Työpäivän pituus määritetään työehtosopimuksessa määritelmän mukaisesti (esim. 40h / 5 päivää = 8h per päivä)   
\- Työviikon pituus jätetään määrittelemättä, koska tehtyä työtä seurataan jaksokohtaisesti. Varsinainen jaksolta muodostuva laskenta määritellään Tasoittumisjakso-asetuksissa, jotka käydään myöhemmin läpi tässä ohjeessa.   
\- Jos käytössänne on Vuorosuunnittelu, ja työpäivien pituudet muodostuvat suunnitelluista työvuoroista, työpäivien pituuksia ei ole tarpeen määrittää asetusryhmän asetuksissa 
Ohje työpäivän pituuksien määritykseen löytyy ohjeesta [täältä.](<https://support.nepton.com/hc/fi/articles/360002558417>)
## Tasoittumisjaksolaskennan käyttöönotto
Tasoittumisjakson laskennan käyttöönotto on kuvattu alla vaihe vaiheelta (1-10). Tässä ohjeessa kuvataan tasoittumisjaksolaskennan minimivaatimukset sen käyttöönotolle. Tasoittumisjakson työajan tulkintaa on käytettävissä monia täsmentäviä asetuksia, jotka on kuvattu ohjeessa [Tasoittumisjakson muut laskenta-asetukset.](<https://support.nepton.com/hc/fi/articles/4405550013981>)
1\. Määritä säännöllisen työajan ylittävän työn oletusohjaus **Työtunnit > Ylityö-asetuksissa** seuraavasti:  
![](https://support.nepton.com/hc/article_attachments/26147103735069)  
Ylityön perus- ja korotuosa korvataan käytännössä "Tunti tunnista - Tasoittumisjaksotuntikertymä"-ohjauksella, sillä tasoittumisjaksolaskenta Neptonissa toteutetaan omalla kertymällään. 
2\. Määritä Tasoittumisjaksotunnit-kertymä käyttöön asetuksissa kohdasta **Työtunnit > Kertymät > Tasoittumisjaksotunnit**  
**![](https://support.nepton.com/hc/article_attachments/26147153010461)**
3\. Siirry samaisissa**Kertymät-asetuksissa Laskennan asetukset-otsikon** alla löytyvien **Tasoittumisjaksotunnit-kertymän** asetuksiin
![](https://support.nepton.com/hc/article_attachments/26147103737117)
4\. Määritä asetukseen **Lainaussäännöt > Kertymä lainaa automaattisesti kertymän saldosta** "Kyllä"
![](https://support.nepton.com/hc/article_attachments/26147153011997)
5\. Määritä tasoittumisjaksotuntikertymän nollaus tulevien jaksojen alkupäivänä asetukseen **Saldo saa nousta arvoon päivän alussa**.   
![](https://support.nepton.com/hc/article_attachments/26147103746973)
Nollaus tulee määrittää voimassaolotoiminnon kautta käyttäen poikkeusasetusta [ACCRUAL-EARNING-PERIOD-START-DATE|levellingperiodhours].
![](https://support.nepton.com/hc/article_attachments/26147153014557)
Tasoittumisjaksotunti-kertymän nollaus tapahtuu tämän poikkeussäännön myötä aina tasoittumisjaksolle määritettyjen jaksojen alkupäivinä. Jaksojen määrittäminen käydään läpi tämän ohjeen vaiheessa 10.   
Voimassaolotoiminnon käytöstä on kerrottu tarkemmin ohjeessa [täällä](<https://support.nepton.com/hc/fi/articles/360002559358>) ja poikkeusasetuksista tarkemmin [täällä](<https://support.nepton.com/hc/fi/articles/360002560677>).
6\. Määritä asetukseen **Kertymään tehty tunti tunnista -ylityö lasketaan tasoittumisjakson työtunneiksi** "Kyllä"  
  
![](https://support.nepton.com/hc/article_attachments/26147153019805)
7\. Määritä asetukseen **Tasoittumisjakson rajat: Työpäivän keskipituus** arvo mikäli työpäivän pituus ei perustu suunniteltuun työvuoroon, muutoin jätä asetus tyhjäksi. Jos tähän on määritelty arvo, olettaa palvelu työpäiviksi arkipäivät eli maanantai - perjantai. 
Mikäli työpäivän pituus perustuu suunnitellun vuoron pituuteen, määritä asetukseen **Työpäivän pituus tulee vuorosta** "Kyllä". Tällöin työpäiväksi oletetaan päivä, jolla on työvuoro, oli se sitten mikä viikonpäivä tahansa.  
Työpäivän keskipituus muodostuu tasoittumisjakson enimmäispituudesta (tunteina) jaettuna jakson työpäivien lukumäärällä. Esimerkiksi 3 viikon/120h jaksolla on 15 työpäivää, jolloin työpäivän keskipituus on 120h / 15 = 8h.  
![](https://support.nepton.com/hc/article_attachments/26147153022365)
8\. Määritä tasoittumisjakson ylitöiden ansaintarajat
Tasoittumisjakson ylitöiden ansaintarajat voidaan määrittää asettamalla ylityörajat joko jakso- tai päiväkohtaisiksi. Katso tarkemmat ohjeet tasoittumisjakson ylitöiden määrittämiseen ohjeesta [Tasoittumisjakson ylityölaskennan määrittely](<https://support.nepton.com/hc/fi/articles/4410630282257>). Ohjeet on eriytetty tästä ohjeartikkelista niiden laajuuden vuoksi. 
Jaksokohtaiset ylityörajat 3 viikon jaksolla, 120 tunnin enimmäistyöajalla voivat olla esimerkiksi seuraavanlaiset:  
  
![](https://support.nepton.com/hc/article_attachments/26147103770781)
Tällaisilla ylityörajoilla tulkinta on:
  * jakson toteutunut työaika 120h - 126h muodostuu jakson lisätyötä
  * jakson toteutunut työaika 126h - 150h muodostuu jakson 50% ylityötä
  * jakson toteunut työaika 150h alkaen muodostuu jakson 100% ylityötä


9\. Määritä tarvittaessa asetukseen **Lyhennykset tasoittumisjaksojen rajoihin juhlapyhinä** arkipyhien lyhennyksen määrä jakson enimmäistyöaikaan. Alla olevan määrityksen mukaisesti jaksolla, jolla normaalitilanteessa enimmäistyöaika on 120h, enimmäistyöaika lyhenee 8 tunnilla 112 tuntiin. 
HUOM! Tasoittumisjakson yhteydessä asetusryhmään ei pääsääntöisesti määritetä työviikon pituutta. Näin ollen myöskään Neptonin Juhlapyhät-asetuksissa määritetty juhlapyhän käyttäytyminen ei ole voimassa tasoittumisjakson enimmäistyöajan vähennyksen osalta vaan lyhentävä määritys asetetaan tällä Tasoittumisjaksotunnit-kertymän asetuksissa olevalla asetuksella.   
  
![](https://support.nepton.com/hc/article_attachments/26147153032477)
10\. Määritä ensimmäisen jakson alkupäivä. Voit määrittää vain ensimmäisen jakson alkupäivän ja hyödyntää **Toistuvan jakson pituus viikkoina tai Toistuvan jakson pituus päivinä-asetusta** toistaaksesi jaksoa. Alla olevassa esimerkissä jakso alkaa 6.1.2025 ja päättyy 26.1.2025. Seuraava kolmen viikon jakso alkaa tästä seuraavana päivänä 27.1.2025.
![](https://support.nepton.com/hc/article_attachments/26147153033501)  
  
Mikäli jaksojen pituudet ovat epäsäännölliset eikä niitä ole mahdollista toistaa sellaisenaan, voidaan jaksojen alkupäivät laittaa yksitellen omille riveilleen tai mikäli jakso ei jakaudu tasan viikkotasolla, voidaan jakson pituus määrittää toistumaan myös päiväperusteisena.   
  
![](https://support.nepton.com/hc/article_attachments/26147153035421)
Huomioithan, että mikäli henkilön työsuhde loppuu kesken jakson, jatkuu tasoittumisjaksotunnit -kertymästä lainaaminen myös työsuhteen ulkopuolella. Työsuhteen päättyessä on tärkeää päättää henkilön asetusryhmän voimassaolo[ tämän tukipalvelumme ohjeen](<https://support.nepton.com/hc/fi/articles/360002575438>) mukaisesti.
## Tasoittumisjakson lisä- ja ylityön seuranta
Tasoittumisjaksolta muodostuva lisätyö, 50% ylityö ja 100% ylityö eritellään Tapahtumat kalenterissa-näkymässä tasoittumisjakson päättymispäivällä. Nämä palkkalajit on mahdollista siirtää myös palkka-aineistolla niitä varten perustetuilla SQL-poimintasäännöillä muiden palkkalajien ohella.
**Enimmäistyöajan ylitys - esimerkki**
Alla olevassa esimerkissä on nähtävillä kolmen viikon tasoittumisjakson 27.1.2025 - 16.2.2025 viimeinen viikko. Henkilö on työskennellyt muutoin säännöllisen työajan puitteissa (tasan 8h per päivä) mutta jakson viimeisellä viikolla perjantain 14.2. osalta säännöllinen työaika on ylittynyt kahdella tunnilla. Näin ollen jakson enimmäistyöaika 120 tuntia on ylittynyt samaisella kahdella tunnilla muodostaen jaksolla kaksi tuntia jakson lisätyötä.
Tasoittumisjakson lisä- ja ylityön määrä esitetään jakson päättymispäivällä 16.2.2024 riippumatta Tapahtumat kalenterissa-näkymässä valitusta ajanjaksosta.
![](https://support.nepton.com/hc/article_attachments/26147103793181)
Tasoittumisjaksotunnit-kertymä laskee päiväkohtaisesti poikkeamaa toteutuneen työajan ja määritetyn työpäivän pituuden välillä, sillä säännöllisen työajan ylittävän osuuden ohjaus on määritetty olemaan "Tunti tunnista - Tasoittumisjaksotunnit. Tasoittumisjakson aikana tasoittumisjaksotuntikertymään ansaittua työaikaa voidaan käyttää vapaana erillisenä tasoittumisjaksotuntivapaana. 
**Enimmäistyöajan alitus - esimerkki**
Jos tasoittumisjaksolla on tehty työtä vähemmän kuin enimmäistyömäärä, näytetään tämä kalenterissa punaisella. Alla olevassa esimerkissä 3 viikon tasoittumisjakson 27.1.2025 - 16.2.2025 enimmäistyöaika 120 tuntia on alittunut kahdella tunnilla. 
![](https://support.nepton.com/hc/article_attachments/26147153038493)
Huom! Ennen versiota 2.14.9 kertymästä lainattu aika laskettiin aina oletuksena työajaksi. Nyt tätä varten on lisätty asetus "Kertymästä automaattisesti lainattu aika lasketaan työaikaan" sijaintiin Työtunnit > Tasoittumisjakso. Oletuksena asetus on "Ei". Kun päivän työaika alittaa normaalin työajan, voidaan nyt valita miten kertymästä vähennetty aika käsitellään. Se voidaan voidaan laskea mukaan työaikaan, mikä vaikuttaa tasoittumisjakson työtunteihin tai voidaan valita ettei näin tehdä.
Tasoittumisjakson enimmäistyöaikaa ja toteutunutta työaikaa voi tarkastella myös Tapahtumat kalenterissa-yhteenvedossa sivun alaosassa.  
  
![](https://support.nepton.com/hc/article_attachments/26148396789277)
Yhteenvedossa näkyvästä i-painikkeesta avautuu tarkempaa tietoa tasoittumisjakson enimmäistyöajasta, toteutuneesta työajasta sekä mahdollisesta enimmäistyöajan ylittymisestä tai alittumisesta.   
  
![](https://support.nepton.com/hc/article_attachments/26148380625949)
## Tasoittumisjakson hyväksyntä
Tasoittumisjakso katsotaan hyväksytyksi kun kaikki sen tapahtumat on hyväksytty. Jos tasoittumisjakso on yli viikon pituinen, katsotaan ovatko jakson viimeisen viikon kaikki tapahtumat hyväksyttyjä. Tasoittumisjakson ylityöt tulkitaan hyväksytyksi silloin kun tasoittumisjakso on hyväksytty.
