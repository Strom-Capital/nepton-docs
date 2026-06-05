---
id: 4411220910865
title: Takautuva asetusmuutos ja kertymän arvon uudelleenlasketus
url: https://support.nepton.com/hc/fi/articles/4411220910865-Takautuva-asetusmuutos-ja-kertym%C3%A4n-arvon-uudelleenlasketus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Kertymät
section_id: 360000705197
section_path:
- Työajan laskenta ja hallinta
- Kertymät
labels:
- kalenterin laskettaminen
- kalenterin päivittäminen
- kalenterin uudellenlaskettaminen
promoted: false
updated_at: '2025-07-10T08:28:50Z'
edited_at: '2025-07-10T08:12:50Z'
---

# Takautuva asetusmuutos ja kertymän arvon uudelleenlasketus

Tässä ohjeessa on kuvattu toimenpiteet tilanteessa, jossa on tehty takautuvasti minkä tahansa kertymän laskentaan vaikuttava asetusmuutos [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta. Esimerkkinä on käytetty saldo-kertymää, mutta samat toimintaperiaatteet pätevät myös muihin Neptonissa käytettäviin kertymiin (esim. pankki, ylityö, jousto). 
Vuosiloma-kertymästä ei tule huomatuskolmiota kalenterinäkymään.
## Mikä voi johtaa kertymän uudelleenlaskettamisen tarpeeseen?
Takautuvasti saldon kokonaisarvoon vaikuttava asetusmuutos voi koskea esimerkiksi
\- saldon kokonaisarvon enimmäis- tai vähimmäismäärää  
\- saldon enimmäismäärää per päivä  
\- henkilön työajan tulkintaa ( esim. asetusryhmän tai työaikaprosentin vaihto takautuvasti)  
\- asetusryhmässä määritettyä työpäivän pituutta
Minkä tahansa kertymän kokonaisarvoon vaikuttava asetusmuutos luo henkilön kalenteriin poikkeuksellisen kirjauksen huomiokolmion. Poikkeuksellisten kirjausten raportoinnista on kerrottu tarkemmin ohjeessa [täällä](<https://support.nepton.com/hc/fi/articles/360002548837>). 
## Esimerkki takautuvasti voimaan tulleesta asetusmuutoksesta
Alla olevassa esimerkissä henkilö on ollut työaikamuodoltaan kokoaikainen, mutta tälle on vaihdettu takautuvasti 80% osa-aikainen työajan laskenta. Säännöllinen päivittäinen työaika on aiemmin ollut 7h 30min mutta muutoksen jälkeen se on osa-aikaisuuden mukaisesti 6h. Takautuvasti voimaan tullut kertymään vaikuttava asetusmuutos muodostaa päivälle huomiokolmion, joka kertoo, että kertymän kokonaisarvo (23:30) ei täsmää päivälle lasketun arvon kanssa (+01:30).
![](https://support.nepton.com/hc/article_attachments/19914366171037)
## Kertymän kokonaisarvon uudelleenlasketuksen toimenpiteet
1\. Luo henkilölle myöhäisintään asetusmuutoksen voimaantulopäivälle Huomautus-tapahtuma tai tallenna uudestaan mikä tahansa tapahtuma asetusmuutoksen voimaantulopäivällä (tapahtuman muokkaus > tallenna). Jos haluat käyttää huomautus-tapahtumaa ja se ei ole organisaatiossanne käytössä tapahtumatyypeissä, saat sen käyttöön [tämän](<https://support.nepton.com/hc/fi/articles/360002519157-Tapahtumatyyppien-lis%C3%A4%C3%A4minen-k%C3%A4ytt%C3%B6%C3%B6notto-ja-muokkaaminen>) ohjeen mukaan.
2\. Huomautus-tapahtuman luominen laskettaa saldon kokonaisarvon uudestaan ko. päivästä eteenpäin suhteessa uuteen muuttuneeseen työpäivän pituuteen
3\. Poista Huomautus-tapahtuma henkilöltä
Esimerkissä osa-aikaisuus on tullut henkilölle voimaan maanantaina 10.6., jolloin myös Huomautus-tapahtuma on luotu tälle päivälle.
Huomautus-tapahtuman luomisen jälkeen em. tilanne on seuraavanlainen. Huomiokolmio on kadonnut ja saldon kokonaisarvo on suhteessa uuteen säännölliseen työaikaan ja päivällä tehtyyn työhön. 
![](https://support.nepton.com/hc/article_attachments/19914366172829)
## Kertymän uudelleenlasketus useammalle henkilölle samanaikaisesti
Takautuvasti voimaan tullut kertymän kokonaisarvoon vaikuttava asetusmuutos on saattanut toisinaan koskea myös useampaa kuin yhtä henkilöä esimerkiksi tilanteessa, jossa saldon ansainnan enimmäismäärä per päivä on muuttunut takautuvasti suuremmaksi. Tällaisessa tilanteessa on suositeltavaa luoda Huomautus-tapahtuma em. ohjeen mukaisesti ensin yhdelle henkilölle ja kopioida tämä tapahtuma kaikille niille henkilöille, joita asetusmuutos on koskenut. Tapahtuman kopiointiin löytyy tarkempi ohjeistus [täältä](<https://support.nepton.com/hc/fi/articles/360002521078>). 
Kun Huomautus-tapahtuma on kopioitu useammalle henkilölle, sen voi myös poistaa henkilöiltä samanaikaisesti. Kopioitujen tapahtumien poistoon löytyy tarkempi ohjeistus [täältä.](<https://support.nepton.com/hc/fi/articles/360002521118>)
Asetusmuutokset useammalle henkilölle koskevat usein saman asetusryhmän henkilöitä. Tapahtumien kopionnissa on mahdollista valita henkilöt asetusryhmän perusteella. Tästä toiminnallisuudesta on kerrottu tarkemmin [täällä](<https://support.nepton.com/hc/fi/articles/360004437597>).
