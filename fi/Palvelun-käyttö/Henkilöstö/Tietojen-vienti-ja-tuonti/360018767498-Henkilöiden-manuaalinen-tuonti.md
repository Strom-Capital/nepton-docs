---
id: 360018767498
title: Henkilöiden manuaalinen tuonti
url: https://support.nepton.com/hc/fi/articles/360018767498-Henkil%C3%B6iden-manuaalinen-tuonti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tietojen vienti ja tuonti
section_id: 360004488578
section_path:
- Henkilöstö
- Tietojen vienti ja tuonti
labels:
- sisäänluku
promoted: false
updated_at: '2026-11-04T13:46:56Z'
edited_at: '2026-11-04T13:39:56Z'
---

# Henkilöiden manuaalinen tuonti

Tämä artikkeli käsittelee yksittäisen henkilötietoja sisältävän tiedoston tuontia Nepton-palveluun. Lisätietoja eri tavoista tuoda henkilötietoja sekä teknisiä yksityiskohtia löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360003762577>).  
Teknisistä rajoituksista johtuen henkilön viennin ja tuonnin tukemien tietokenttien välillä on eroja. Tarkista aina ohjeista huolellisesti uusimmat tiedot.
### Pääsy toimintoon
Henkilötietoja voidaan manuaalisesti tuoda Neptoniin työsuhdeosion kautta. Henkilötuonti on käytössä vain Ylläpitäjä-roolissa oleville. Jos sinulla henkilötietoja sisältävä tiedosto tuetussa muodossa, voit tuoda henkilötiedot kohdassa **Työsuhde** > **Henkilöt** > **Tuo henkilöitä**.
![](https://support.nepton.com/hc/article_attachments/40414350498333)
Ensimmäisellä näytöllä valitaan tuotava tiedosto:
![](https://support.nepton.com/hc/article_attachments/40414338946717)
Voit pudottaa tiedoston laitteesi resurssienhallinnan avulla (näkymä riippuu laitteesi käyttöjärjestelmästä):
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360018590837)
Voit vaihtoehtoisesti napsauttaa Valitse tiedosto -painiketta ja avata tiedoston laitteeltasi (näkymä riippuu laitteesi käyttöjärjestelmästä):
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360018628098)
Tiedoston nimi näytetään valintasi jälkeen:
![mceclip5.png](https://support.nepton.com/hc/article_attachments/360018594557)
Jos valitsit väärän tiedoston, voit poistaa sen tiedostonimen viereisestä Poista-kuvakkeesta ja sen jälkeen valita oikean tiedoston. Voit myös valita uuden tiedoston poistamatta edellistä. Tällöin edellistä valittua tiedostoa ei tuoda - vain yksi tiedosto tuodaan kerrallaan.
Valittuasi tiedoston sinun on annettava tietoja, joita palvelu tarvitsee tulkitakseen tiedot oikein:
![](https://support.nepton.com/hc/article_attachments/36355663930269)
### Valitse merkistökoodaus
Merkistökoodauksen valinta näytetään vain, kun tuotava tiedosto on CSV-muotoinen. Tämä valinta määrittelee merkistön, jota käytetään tuotavassa tiedostossa. Mahdolliset valinnat ovat:
  * UTF-8
  * ISO-8859-1 


[UTF-8](<https://fi.wikipedia.org/wiki/Unicode#UTF-8>) on tapa koodata Unicode-merkistöä, [ISO-8859-1](<https://fi.wikipedia.org/wiki/ISO_8859-1>) on rajattu yleisiin eurooppalaisissa kielissä käytettyihin merkkeihin. Yleisesti ottaen sen ohjelman tai palvelun, jolla tuotat tiedoston, tulisi antaa tarvittavat tiedot merkistökoodauksesta. Jos valitset virheellisen tiedostomuodon, tarkkeet latinalaisten aakkosten yhteydessä (kuten suomen ä- ja ö-kirjaimissa) tai ei-latinalaisten aakkosten merkit näkyvät todennäköisesti väärin.
### Henkilötuonnin tyyppi 
Henkilötuonnin tyyppi määrittelee, miten tiedoston sisältö tulkitaan Neptonissa. Yleisesti Nepton suosittelee käyttämään **oletus** tuontityyppiä. Se tukee laajinta mahdollista joukkoa Neptonin henkilötietokentistä. Lisätietoja käytettävissä olevista kentistä oletustuontityypille löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360015933397>). Muut tyypit ovat tiettyjen ulkoisten järjestelmien liittymiä tai muita erityistarkoituksia varten. Lisätietoja tyypeistä löytyy alla olevista linkeistä. Mahdolliset valinnat ovat:
  * [Oletus](<https://support.nepton.com/hc/fi/articles/360015933397>)
  * [Jatka työsopimusten päiväyksiä](<https://support.nepton.com/hc/fi/articles/9003095125149>)
  * [Kieku (uudet tilit)](<https://support.nepton.com/hc/fi/articles/360005399958>)
  * [Kieku (työaikasäännöt)](<https://support.nepton.com/hc/fi/articles/360005401578>)
  * [Mepco](<https://support.nepton.com/hc/fi/articles/360005402338>)
  * [SAP](<https://support.nepton.com/hc/fi/articles/360005404298>)
  * [SAP SuccessFactors](<https://support.nepton.com/hc/fi/articles/360004051897>)
  * [Sympa](<https://support.nepton.com/hc/fi/articles/360003733858>)
  * [Sympa HR Integraatio API](<https://support.nepton.com/hc/fi/articles/360014650697>)


Valittuasi henkilötuonnin tyypin Nepton-palvelu tekee automaattisesti alustavan analyysin tuontitiedostosta ja näyttää sen tulokset valintojen alapuolella. Voit analysoinnista huolimatta vaihtaa seuraavassa kohdassa tyhjien kenttien käsittelytapaa.
### Henkilön tunniste
Henkilön tunniste tarkoittaa sitä henkilötietoa, jonka perusteella etsitään löytyykö tuotava henkilö jo olemassa olevista henkilöistä. Jos henkilö samalla henkilön tunnisteella löytyy, päivitetään tämän henkilön tietoja tuotavalla tiedolla.
Kun käytetään arvoa "Oletus", käytetään ensimmäistä näistä henkilötiedoista, jolle löytyy arvo tuotavista henkilötiedoista: Nepton-tunniste, Ulkoinen tunniste 1, Käyttäjätunnus, Henkilönumero.
Vinkki: Kun valitset muun arvon kuin "Oletus", voit päivittää tuotavan aineiston avulla näitä tunnisteita, "Ulkoinen tunniste 1", "Käyttäjätunnus" ja "Henkilönumero", lukuunottamatta tunnistetta jonka olet valinnut henkilön tunnisteeksi.
### Tyhjät arvot tuontitiedostossa
Oletusarvoisesti manuaalisessa henkilötuonnissa tyhjät kentät tuontitiedostossa eivät muuta olemassa olevien kenttien arvoja. Tätä valintaa käyttämällä kaikki olemassa olevat arvot henkilöille Nepton-palvelussa säilytetään kaikille kentille, joille on annettu tyhjä arvo tuontitiedostossa.
Valitsemalla vaihtoehdon "Olemassaolevat kenttien arvot poistetaan (tarkka)" voit pakottaa olemassa olevien arvojen poistamisen Nepton-palvelusta henkilöiltä, joille tuodaan tyhjiä arvoja kyseisille kentille.
### Alustava analyysi
Valittuasi henkilötuonnin tyypin Nepton-palvelu tekee automaattisesti alustavan analyysin tuontitiedostosta ja näyttää sen tulokset valintojen alapuolella:
![mceclip7.png](https://support.nepton.com/hc/article_attachments/360018597017)
Jos tuontitiedoston yhdessä tai useammassa kentässä on ongelmia, näistä esitetään samassa kohdassa varoitukset keltaisella värillä. Esimerkki:
![mceclip8.png](https://support.nepton.com/hc/article_attachments/360018634438)
Nämä varoitukset merkitsevät sitä, ettei joidenkin kenttien arvoja voida tuoda Neptoniin kyseistä tiedostoa käyttämällä. Jos mitään tietoa yhdestä tai useammasta henkilöstä ei voida tuoda, virheilmoitukset näytetään punaisella värillä. Esimerkki:
![mceclip9.png](https://support.nepton.com/hc/article_attachments/360018636138)
### Tuonnin aloittaminen
Kun olet tarkastanut alustavan analyysin ja hyväksynyt sen tulokset, voit aloittaa tuonnin käyttämällä Tuo henkilöt -painiketta:
![mceclip11.png](https://support.nepton.com/hc/article_attachments/360018639518)
Jos valitsit vaihtoehdon, jossa tyhjät arvot poistavat olemassa olevat arvot kentistä, sinun tulee vahvistaa valintasi Tuo henkilöt -painikkeen valinnan jälkeen.
![mceclip13.png](https://support.nepton.com/hc/article_attachments/360018640758)
Vahvista valinta -toiminto tuo tiedoston sisällön Neptoniin. Peru tuonti  
-toiminnolla voit vielä muuttaa valintojasi.
### Tulokset
Tuonnin valmistuttua näytetään tulokset jokaisesta tuodusta rivistä:
![mceclip10.png](https://support.nepton.com/hc/article_attachments/360018638618)
Jos tuonnissa ilmeni ongelmia, mutta ainakin jotain tietoa on tuotu onnistuneesti, varoitukset näytetään keltaisella:
![mceclip15.png](https://support.nepton.com/hc/article_attachments/360018606417)
Jos mitään tietoa yhdelle tai useammalle henkilölle ei voitu tuoda, virheilmoitukset näytetään punaisella:
![mceclip16.png](https://support.nepton.com/hc/article_attachments/360018606917)
### Esimerkkejä
#### Esimiestiedon massatuonti
Yksityiskohtaiset ohjeet esimiestiedon tuomiseksi taulukkolaskentaohjelman avulla löytyy [täältä](<https://support.nepton.com/hc/fi/articles/360002430658>).
#### Lisää vain uusia henkilöitä pakollisilla tiedoilla
Esimerkki CSV-tiedostosta, jolla tuodaan alustavat pakolliset tiedot uusille järjestelmään lisättäville henkilöille:
[code]
    Etunimi;Sukunimi;Palvelun käyttökieli;Rooli
    Hope;Hopeful;English;Työntekijä
    Dana;Dannerø;Danish;Esimies
    Matti;Meikäläinen;Finnish;Työntekijä
    Wojciech;Kozłowski;Polish;Työntekijä
    Sven;Svensson;Swedish;Työntekijä
    Ülle;Võsu;Estonian;Työntekijä
    Jakob;Hansen;Norwegian;Työntekijä
[/code]
Koska käyttäjätunnusta tai henkilönumeroa ei ole annettu, yllä oleva tuonti lisää aina henkilöt uusina Neptoniin, vaikka henkilöitä samankaltaisilla tiedoilla olisi aiemmin tallennettu järjestelmään.
#### Päivitä työajan asetusryhmäkoodit henkilöille
Esimerkki Excel-tiedostosta, jolla päivitetään henkilöille uudet työajan asetusryhmäkoodit henkilönumeroiden perusteella:
![mceclip18.png](https://support.nepton.com/hc/article_attachments/360018643998)
Yllä oleva etsii Neptoniin tallennettuja henkilöitä henkilönumeroilla 101, 104, 106, 147 ja 159 ja päivittää löytyneille henkilöille työajan asetusryhmäkoodiksi C100. Koska kaikkia pakollisia tietoja ei ole annettu, uutta henkilöä ei lisätä, mikäli henkilöä annetulla henkilönumerolla ei löydy. 
#### Tuo tyhjiä arvoja
Esimerkki tyhjien arvojen tuomisesta CSV-muodossa. Henkilöt tunnistetaan annetulla käyttäjätunnuksella. Kenttä Hallinnon lisätieto on annettu tyhjänä
[code]
    Käyttäjätunnus;Henkilönumero;Hallinnon lisätieto;Rooli
    Hope Hopeful;101;;Työntekijä
    Dana Dannerø;102;;Esimies
    Matti Meikäläinen;104;;Työntekijä
    Wojciech Kozłowski;106;;Työntekijä
    Sven Svensson;147;Sven;;Työntekijä
    Ülle Võsu;159;Ülle;Võsu;;Työntekijä
    Øyvind Thorsen;168;;Esimies
[/code]
Jos tämä tiedosto on tuotu oletusvalinnalla "Olemassaolevia kenttien arvoja ei muuteta (turvallisin)", ennestään olemassa olevat hallinnon lisätiedot löytyvät edelleen tuonnin jälkeen Neptonista. Jos kuitenkin Hallinnon lisätieto -kenttä on tyhjennettävä näille henkilöille, valinta "Olemassaolevat kenttien arvot poistetaan (tarkka)" on valittava tuontivalinnoissa.
