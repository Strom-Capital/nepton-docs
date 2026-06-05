---
id: 360008763537
title: Henkilön lisätietokenttien oletusarvojen hallinta
url: https://support.nepton.com/hc/fi/articles/360008763537-Henkil%C3%B6n-lis%C3%A4tietokenttien-oletusarvojen-hallinta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Hallinta
section_id: 360004488558
section_path:
- Henkilöstö
- Hallinta
labels: []
promoted: false
updated_at: '2024-08-23T10:03:02Z'
edited_at: '2021-07-22T12:41:27Z'
---

# Henkilön lisätietokenttien oletusarvojen hallinta

Asettamalla henkilön lisätietokentille oletusarvon, voit käyttää sitä kaikille uusille henkilöille. Tällä voidaan säästää paljon aikaa, jos kaikille uusille henkilöille halutaan sama tieto, lähtöarvo tai kyseinen tieto on suurimmalla osalla organisaation henkilöistä sama. Tätä voidaan hyödyntää myös henkilöiden tuonnissa, jos halutaan tiettyyn kenttään vakioarvo. Lisätietoja henkilönlisätietokenttien hallinnasta [täältä](<https://support.nepton.com/hc/fi/articles/360002430918>). 
## Oletusarvon asettaminen
Oletusarvo voidaan asettaa kaikille henkilön lisätietokentille, joille ei ole määrätty asetettavaksi yksilöllistä arvoa kaikille henkilöille. Voit katsoa ja muokata olemassa olevaa oletusarvoa valikossa **Työsuhde - > Hallinta -> Henkilön lisätietokentät**. 
Voit asettaa oletusarvon luodessasi uutta henkilön lisätietokenttää tai voit muokata olemassa olevaa arvoa klikkaamalla kynän kuvaketta kentän nimen vasemmalla puolella ja kirjoittamalla halutun oletusarvon sille varattuun kenttään. Kirjoittamasi arvon kelpoisuus tarkastetaan ennen tallentamista.
**Huomaathan** , että oletusarvot vaikuttavat vain uusiin henkilöihin. Oletusarvon asettaminen tai muuttaminen ei automaattisesti päivitä henkilöiden olemassa olevia tietoja. Katso alempaa 'Olemassa olevien henkilöiden tietojen massapäivitys uudella oletusarvolla', jos haluat päivittää uuden oletusarvon olemassa oleville henkilöille.
![Lisatieto_3__2020-05-19_130759.png](https://support.nepton.com/hc/article_attachments/360008491997/Lisatieto_3__2020-05-19_130759.png)
### Esimerkki
Kun uusi henkilö lisätään valikossa **Työsuhde - > Henkilöt -> Henkilöt -> Lisää henkilö**, tai [henkilöiden tuonnin](<https://support.nepton.com/hc/fi/articles/360003762577>) kautta, kaikki henkilön lisätietokentät, joilla on oletusarvo, täytetään automaattisesti. Esimerkiksi, alla olevassa kuvakaappauksessa 'Ensiapukoulutus suoritettu'-kentällä on oletusarvo 'Kyllä'. Kun uusi henkilö lisätään, saa kyseinen kenttä arvon 'Kyllä'.![Lisatieto_1__2020-05-19_130759.png](https://support.nepton.com/hc/article_attachments/360008586858/Lisatieto_1__2020-05-19_130759.png)
## Uuden oletusarvon päivittäminen olemassa oleville henkilöille
Kun lisätään tai muutetaan kentän oletusarvoa, on tärkeää huomata, että olemassa olevia arvoja henkilöiden lisätietokentissä ei päivitetä uudella/muutetulla oletusarvolla. Jos haluat asettaa uuden oletusarvon jo olemassa oleville henkilöille, voit tehdä sen henkilöiden tuonti-toiminnolla.
  1. Mene Työsuhde-välilehdelle
  2. Aseta haluamasi suodattimet valitaksesi päivitettävät henkilöt
  3. Klikkaa 'Vie sisäänluettavaan Exceliin' nappia  

     * Riippuen henkilöiden määrästä ympäristössäsi ja internet-yhteyden nopeudesta, saattaa kestää hetken luoda tiedosta ja ladata se
  4. Avaa ladattu Excel-tiedosto ja klikkaa 'Ota muokkaus käyttöön'-nappia
  5. Poista Excel-tiedostosta kaikki muut kentät paitsi Käyttäjätunnus ja lisätietokentät, joille haluat asettaa uuden oletusarvon 
     * Huomioithan, että kentät, joilla ei ole arvoa, on automaattisesti piilotettu Excel-tiedostossa. Löytääksesi nämä, valitse kaikki sarakkeet ja klikkaa hiiren oikealla näppäimellä ja valitse avautuvasta valikosta 'Näytä'.
  6. Lisää uusi oletusarvo kaikille riveille haluttuihin kenttiin
  7. Tallenna muutokset
  8. Palaa Neptoniin ja mene Työsuhde -> Henkilöt -> Tuo henkilöitä
  9. Seuraa ohjeita ja tarkasta, että tuotavien henkilöiden määrä täsmää ennen kuin painat 'Tuo henkilöt'-nappia


## Oletusarvot ja henkilöiden tuonti
Kun henkilöitä lisätään joko toiminnolla Työsuhde -> Henkilöt -> Tuo henkilöitä tai käyttämällä ajatettua henkilöiden tuontia, henkilön lisätietokenttien oletusarvot asetetaan tuotavien henkilöiden tietoihin, ellei kentälle ole määritetty arvoa tuontitiedostossa.
Tuontitiedostoon ei tarvitse sisällyttää kenttiä, joiden oletusarvot on asetettu palveluun, ellei ole tarpeen asettaa oletusarvosta poikkeavia arvoja henkilöiden tuonnissa.
