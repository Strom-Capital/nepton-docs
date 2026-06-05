---
id: 360002558617
title: Oletetut työajat
url: https://support.nepton.com/hc/fi/articles/360002558617-Oletetut-ty%C3%B6ajat
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- NEPTONNEEDSREVIEW
- oletustyöaika
- oletustyöajat
promoted: false
updated_at: '2026-03-13T10:55:21Z'
edited_at: '2026-03-13T10:54:55Z'
---

# Oletetut työajat

Oletetut työajat määrittävät kellonajat, joilla voidaan mahdollistaa saldon tai ylityön kertyminen esimerkiksi tilanteissa, joissa henkilö jää kesken päivän sairaspoissaololle, tai jos töitä on tehty ennen varsinaisen työajan alkua. Työajan laskennassa säännöllinen työaika sijoittuu oletetun työajan sisällä. Siltä osin kuin työaika on oletettujen työaikojen ulkopuolella, se tulkitaan niillä säännöillä mitä säännöllisen työajan ylittävältä osalta on määritetty. Ylittävä aika korvataan sen mukaan, kuinka tapahtuman [ylityöohjauksella](<https://support.nepton.com/hc/fi/articles/360002481617>) asetetaan.
## Oletettujen työaikojen määrittely
Oletetut työajat voidaan määritellä Työaika-osiossa joko Työyhteisö- tai Asetusryhmät-tason asetuksissa: Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Oletetut työajat. Huomioithan, että kaikki määritykset on aina hyvä tehdä [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
Jotta oletetut työajat on käytössä, tulee Oletetut työajat käytössä -kohtaan valita Kyllä. Tämän jälkeen Oletetut Työajat määritellään jokaiselle päivälle, ma-su. Oletettujen työaikojen asetuksiin on mahdollista asettaa kaksi eri arvoa. Tämä on tarpeellista esim. silloin, kun tehdään töitä vuorokauden vaihtuessa. 
Alla olevassa esimerkkikuvassa asetusryhmään on määritelty oletetut työajat maanantaista perjantaihin klo 8-16.  
  
![](https://support.nepton.com/hc/article_attachments/19947426413725)
Mikäli henkilöllä on voimassa olevat työajat, näkyvät ne hänen kalenterinäkymässään päivän päivämäärää klikkaamalla:  
![](https://support.nepton.com/hc/article_attachments/19947415706397)
### Oletettujen työaikojen asettaminen yhdelle henkilölle tietylle päivälle
Joskus on tarpeen muokata oletettuja työaikoja jossain tietyssä tilanteessa. Yksittäiselle henkilölle voidaan luoda päivälle poikkeukselliset Oletetut työajat. Tämä tehdään henkilön kalenterinäkymässä, jossa klikataan oikeaa päivämäärää. Sen jälkeen klikataan auki Oletetut työajat. Tästä aukeaa uusi ikkuna, johon voidaan määrittää poikkeukselliset Oletetut työajat kyseiselle päivälle, koskemaan vain kyseistä henkilöä.
## Oletetut työajat ja ylityötulkinta
Nyt, kun määritykset ovat voimassa, voi henkilö ansaita ylitöitä, vaikka säännöllinen työaika ei olisi täyttynyt. Alla esimerkkitapauksia, joissa oletetut työajat on 8-16:
![](https://support.nepton.com/hc/article_attachments/19947426418077)
Tiistai 4.6. Työtä tehty klo 6-15. Ylityön ohjaus on "Ylityö palkkaan". Koska oletetut työajat alkavat klo 8, tulee kahdesta ensimmäisestä tunnista 2h ylitöitä. Klo 8 alkaen alkaa säännöllinen työaika täyttymään. Koska työt on lopetettu klo 15, ei päivän velvoite ole kuitenkaan tullut täyteen, vaan jää tunnin vajaaksi. Tästä syystä saldosta lainataan yksi tunti päivän päätteeksi.
![](https://support.nepton.com/hc/article_attachments/19947415712413)
Keskiviikko 5.6. Tehty samanpituinen työleimaus kun edellisenä päivänä, mutta tällä kertaa ylityön ohjauksena on "tunti-tunnista saldoon". Lopputulemana on, että saldoon lisätään päivän päätteeksi 1h, eikä ylitöitä muodostu.
![](https://support.nepton.com/hc/article_attachments/19947415714717)
Torstai 6.6. Töihin on tultu klo 7, ja työt on ohjattu "Ylityö palkkaan". Päivän aikana ollaan kuitenkin tultu sairaaksi, ja klo 12 alkaen on alkanut sairausloma. Koska Oletetut työajat alkavat klo 8, on ensimmäiseltä tunnilta ansaittu ylitöitä:  
![](https://support.nepton.com/hc/article_attachments/19947415718685)
Ilman oletettuja työaikoja kyseinen viikko näyttäisi tältä, eli ylitöitä ei ansaita ennen kuin varsinainen työaika on täynnä:  
![](https://support.nepton.com/hc/article_attachments/19947426435229)
