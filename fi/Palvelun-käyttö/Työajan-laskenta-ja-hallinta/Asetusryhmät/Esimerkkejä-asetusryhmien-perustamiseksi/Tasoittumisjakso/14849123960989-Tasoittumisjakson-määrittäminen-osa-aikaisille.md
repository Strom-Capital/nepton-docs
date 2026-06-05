---
id: 14849123960989
title: Tasoittumisjakson määrittäminen osa-aikaisille
url: https://support.nepton.com/hc/fi/articles/14849123960989-Tasoittumisjakson-m%C3%A4%C3%A4ritt%C3%A4minen-osa-aikaisille
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
labels: []
promoted: false
updated_at: '2024-08-23T08:51:51Z'
edited_at: '2024-03-04T13:02:57Z'
---

# Tasoittumisjakson määrittäminen osa-aikaisille

Tasoittumisjakso on mahdollista määrittää noudattamaan osa-aikaisten työntekijöiden työaikaprosenttia. Tämä skaalaa lisätyön ansaintakynnyksen työaikaprosentin mukaisesti. Määrittäminen onnistuu asetuksista paikasta Työaika > Asetukset > Työtunnit > Tasoittumisjakso:
![](https://support.nepton.com/hc/article_attachments/14849225736605)
Jos työntekijä esimerkiksi on osa-aikainen 60% työaikaprosentilla ja yhden viikon tasoittumisjakson rajat asetuksissa ovat seuraavat:
![](https://support.nepton.com/hc/article_attachments/14849225738525)
Työntekijän koko jakson rajat olisivat seuraavat:
  * Enimmäistyöaika: 22,5 tuntia
  * Lisätyön enimmäismäärä: 17,5 tuntia
  * 50% ylityön enimmäismäärä: 10 tuntia


Jos työaikaprosenttia ei käytetä lisätyön ansaintakynnyksen laskemiseen, jakson rajat olisivat seuraavat:
  * Enimmäistyöaika: 37,5 tuntia
  * Lisätyön enimmäismäärä: 2,5 tuntia
  * 50% ylityön enimmäismäärä: 10 tuntia


## Lisätyön erittely 0% ja lisätyön korotusprosentin välillä
Palvelussa on mahdollista määrittää että lisätyö eritellään siten että 0% lisätyötä ansaitaan kunnes täysiaikainen työvelvoite täyttyy ja sen jälkeen lisätyötä ansaitaan TES lisätyön korotusprosentin mukaisesti. Tämä tapahtuu määrittämällä sekä "Käytä työaikaprosenttia lisätyön ansaintakynnyksen laskemiseen" että "Osa-aikaisten tulee ansaita 0% lisätyötä ennen täyden työaikakynnyksen täyttymistä" valintoihin "Kyllä".
![](https://support.nepton.com/hc/article_attachments/17293346214429)
Esimerkki: Lisätyötä ansaitaan 2 viikon tasoittumisjaksolla 72 tunnin jälkeen ja osa-aikaisen työaikaprosentti on 60%. Osa-aikainen alkaa ansaita lisätyötä 48 tunnin jälkeen, ja lisätyötä ansaitaan 0% niin kauan kunnes täysiaikaisen ansaintakynnys on täyttynyt eli 72 tuntiin asti. Eli esim. jos osa-aikaisen maksimityöaika jaksolla on 45 tuntia ja osa-aikainen on tehnyt töitä tasoittumisjakson aikana 79 tuntia, ansaitaan 0% lisätyötä 30 tuntia, ja sen jälkeen lisätyön korotusprosentilla ansaitaan 4 tuntia, koska täysiaikaisen lisätyön ansaintakynnys on täyttynyt 75 tunnin kohdalla ja tämän täyttymisen jälkeen on tehty vielä neljä tuntia töitä, eli 79h - (45h+30h)= 4h.
## Poissaolon lyhennyksen määrän määrittäminen
Poissaolot lyhentävät tasoittumisjakson enimmäistyöaikaa sen mukaan, mikä työvelvoite poissolopäivillä on.
Jos esimerkiksi työpäivän pituudeksi (ma-pe) on määritetty 7:30, 60% työaikaprosentilla poissaolot lyhentäisivät enimmäistyöaikaa 4,5 tuntia arkipäivinä.
![](https://support.nepton.com/hc/article_attachments/14849410553629)
Jos halutaan määrittää, mitkä kolme päivää ovat poissaolopäiviä viikolla, sen voi tehdä asettamalla työpäivän pituuden poikkeukset päiville.
![](https://support.nepton.com/hc/article_attachments/14849419803677)
## Juhlapyhän lyhennyksen määrän määrittäminen
Kuten poissaolotkin, juhlapyhät lyhentävät tasoittumisjaksoa työaikaprosentin mukaisesti. Eli esimerkiksi 60% työaikaprosentilla juhlapyhä lyhentäisi tasoittumisjakson enimmäistyöaikaa 4,5 tuntia.
Juhlapyhän lyhennyksen pituuden voi myös määrittää asettamalla päivälle työpäivän pituuden poikkeuksen.
