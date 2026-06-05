---
id: 10067038494621
title: Normaalin työajan ansainta työvelvoitteen jälkeen
url: https://support.nepton.com/hc/fi/articles/10067038494621-Normaalin-ty%C3%B6ajan-ansainta-ty%C3%B6velvoitteen-j%C3%A4lkeen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels: []
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-10-03T12:25:37Z'
---

# Normaalin työajan ansainta työvelvoitteen jälkeen

Neptonin asetuksissa on [Työpäivän pituuden](<https://support.nepton.com/hc/fi/articles/360002558417>) määrittämisen alla asetus "Normaalin työajan ansainta työvelvoitteen jälkeen" (Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Työpäivän pituus), joka voidaan määrittää [tapahtumatyyppikohtaisesti](<https://support.nepton.com/hc/fi/articles/360002520778>). Asetuksen tyypillinen käyttötilanne on sellaisten tapahtumatyyppien kanssa, jotka kerryttävät normaalisti työtunteja ja säännöllistä työaikaa vain työpäivän pituuteen saakka, esim. sairausloma ja matka-aika. Asetuksella voidaan määrittää esimerkiksi, että sairauslomasta voidaan ansaita 9h työaikaa, vaikka työpäivän pituudeksi olisi määritetty 7h 30min. Asetuksella voidaan rajata kuinka paljon työaikaa voidaan maksimissaan ansaita. Toinen tyypillinen käyttötilanne asetukselle on Matka-aika -tapahtumatyyppi, kun halutaan korvata säännöllisen työajan ylittävä [matka-aika saldoon](<https://support.nepton.com/hc/fi/articles/360002559737>).
## Määritykset
Asetukseen ilmaantuu oma kenttä jokaiselle ympäristössä käytössä olevalle tapahtumatyypille.
![](https://support.nepton.com/hc/article_attachments/22001619945757)
**Normaalin työajan ansainta työvelvoitteen jälkeen - "tapahtumatyyppi"** asetukseen määritellään se arvo, mikä on päivän maksimityöaika kyseisen tapahtumatyypin ansainnassa. Esimerkiksi jos kyseessä on matka-aika tapahtumatyyppi, ja siitä halutaan ansaita 2h säännöllisen työajan ylitettyä, laitetaan kentän arvoksi 2h + säännöllinen työaika, esim. 7,5h = 9,5h. Tällöin matka-ajasta voidaan ansaita työaikaa niin kauan, kunnes päivän työaika on saavuttanut 9,5h.
**Josta palkatonta aikaa** määrittää kuinka monta palkatonta tuntia on, ennen kuin ansaitaan normaalia työaikaa työvelvoitteen jälkeen.
Asetus ei siis mahdollista jostain tapahtumatyypistä ansaittavaa kiinteää tuntien määrää, vaan asetus antaa ansaita tietystä tapahtumatyypistä työaikaa siihen asti, kunnes koko päivän työtunnit saavuttavat määritetyn rajan. Eli jos päivällä on tehty velvoitteen lisäksi esimerkiksi tunti-tunnista työtä, vähenee tapahtumatyypistä ansaittava aika sen mukaan.
## Esimerkkejä käytöstä
Alla kuvattu tyypillisiä asetuksen käyttötapoja.
### Matka-aika
Oletuksena tapahtumatyypistä "matka-aika" ansaitaan vain säännöllistä työaikaa. Jos halutaan, että työaikaa voi myös kertyä päivän velvoitteen täyttymisen jälkeen, täytyy sen kohdalle määrittää haluttu arvo. Esimerkkinä tapaus, jossa matka-ajasta voi ansaita 3h arkena ja 12h viikonloppuna saldoon. Työpäivän pituus on 7,5h, joten määritykset laitettaisiin seuraavasti:  
![](https://support.nepton.com/hc/article_attachments/22001619949981)
Tällöin arkena matka-ajasta ei korvata enää mitään kun päivän työaika saavuttaa 10,5h, ja viikonloppuisin 12h:
![](https://support.nepton.com/hc/article_attachments/22001619953309)
  * Torstai 10.10.: Ensin on tehty normaali 7,5h työpäivä, jonka jälkeen matka-aikaa 2h. Tunteja ei olla rajattu pois, koska päivän työaika ei ylitä 10,5h.
  * Perjantai 11.10.: Ensin on tehty normaali työpäivä 7,5h, ja sen jälkeen 5h matka-aikaa. Matka-ajasta ansaitaan vain 3h, sillä siinä kohtaa päivän enimmäistunnit 10,5h on täynnä.
  * Lauantai 12.10.: Päivällä on pelkkää matka-aikaa 14h. Tästä saldoon menee vain maksimimäärä, eli 12h.


### Sairausloma
Oletuksena sairauslomasta ansaitaan vain säännöllistä työaikaa. Jos halutaan, että sairauslomasta voi ansaita työtunteja päivän velvoitteen ollessa täynnä, täytyy sen kohdalle määrittää haluttu arvo. Esimerkkinä tapaus, jossa työpäivän pituus on 7,5h, mutta sairauslomasta voi ansaita yhdeksään tuntiin asti. Yksi tunti on palkatonta aikaa.
![](https://support.nepton.com/hc/article_attachments/10066607924125)
  * Normaalin työajan ansainta työvelvoitteen jälkeen = 9:00
  * Josta palkatonta aikaa = 1:00


Sairausloman ansainta toimisi tässä esimerkissä seuraavalla tavalla:
  * 07:00 - 15:00 -> 7,5 normaalin työvelvoitteen mukaan (sisältää 30 min palkattoman ruokatauon)
  * 15:00 - 16:00 -> Asetuksen mukainen 1h palkatonta aikaa
  * 16:00 - 17:00 -> 1h normaalin työajan ansainta työvelvoitteen jälkeen. Työaikaa voidaan ansaita asetusmäärityksen mukaan 9h asti


![](https://support.nepton.com/hc/article_attachments/22005744262813)
