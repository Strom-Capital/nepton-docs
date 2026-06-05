---
id: 8700440260637
title: Talenom palkanlaskenta
url: https://support.nepton.com/hc/fi/articles/8700440260637-Talenom-palkanlaskenta
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-02-16T17:15:02Z'
---

# Talenom palkanlaskenta

## Yleinen kuvaus
Talenom ja Nepton ovat muodostaneet yhdessä parhaat käytännöt palveluiden liittämiseen toisiinsa. Mikäli käytössäsi on kumpikin palvelu, niin voit hyötyä ratkaisusta jossa palveluiden välinen tiedonsiirto on toteuttu mahdollisimman sujuvaksi.
  * Työaikakirjausten tulkinta siirtyy Talenomin Mepco järjestelmään poissaoloineen. Tämä mahdollistaa sujuvan ja laadukkaan palkanlaskennan prosessin.
  * Henkilö- ja työsuhdetiedot siirtyvät Talenomin Mepco järjestelmästä Neptoniin. Muutoksia ja lisäyksiä henkilö- ja työsuhdetietoihin ei tarvitse syöttää useaan paikkaan.


Palvelut liitetään toisiinsa käyttäen tässä kuvattua parasta käytäntöä, mikäli asiakaskohtaisesti ei sovita toisin. Mikäli käytössäsi ei ole vielä näitä liittymiä, niin voit sopia niiden käyttöönotosta ottamalla yhteyttä Neptoniin tai Talenomin palkanlaskennan yhteyshenkilöösi.
## Tekninen toteutus
Kun palveluja liitetään toisiinsa, niin tekninen toteutus tehdään alla kuvatulla tavalla. Asiakaskohtaiset poikkeukset ovat mahdollisia, mutta niistä tulee sopia erikseen liittymän toteutusvaiheessa.
### Palkka-, poissaolo- ja lomatiedosto Neptonista Talenomiin
Neptoniin muodostetaan 3 [sääntöjoukkoa](<https://support.nepton.com/hc/fi/articles/360002492278>), jolla palkka-, loma- ja poissaolo-aineistot muodostuvat. Aineistot ladataan Talenomiin Mepco-muotoisena [palkka,](<https://support.nepton.com/hc/fi/articles/360003473498>) [poissaolo, ja loma-tiedostona](<https://support.nepton.com/hc/fi/articles/360003515257>). Poissaolot- ja lomat-tiedostot ovat saman muotoisia. Poissaolo-tiedostossa kesto siirretään tunteina. Loma-tiedostossa kestoa ei siirretä.
Tiedostojen nimiksi määritellään alla olevat.
  * Palkkatapahtumatiedosto: "#RYHMA_TAPA_ToTalenom_YYYYMMDD_HHmm.csv"
  * Lomatiedosto: "#RYHMA_LOMA_ToTalenom_YYYYMMDD_HHmm.csv"
  * Poissaolotiedosto: "#RYHMA_POLO_ToTalenom_YYYYMMDD_HHmm.csv"


Merkkijono #RYHMÄ korvataan siirrettävällä maksuryhmän koodilla. Aineiston poiminta ryhmitellään poimintasäännön asetuksissa, siten että maksuryhmä on poiminnan [SPLITTINGVALUE], kuten on kuvattu [Sääntöjoukon siirron automatisoinnin ohjeessa](<https://support.nepton.com/hc/fi/articles/360002492458>).
Asiakkaan henkilöstö hyväksyy Neptonissa kirjatut tapahtumat, jonka jälkeen aineistot ladataan Neptonista SFTP-palvelimelle sovittuna ajankohtana asiakkaan palkkayhteyshenkilön toimesta.
Siirrettävät palkkalajit ovat asiakaskohtaisia ja niiden määrittely tehdään Neptonin sääntöjoukkoihin.
### Henkilö- ja työsuhdetiedot Talenomista Neptoniin
Talenom muodostaa aineiston SFTP-palvelimelle kerran yössä, jossa siirretään työntekijöiden henkilö- ja työsuhdetiedot Neptoniin. SFTP-palvelimena käytetään Talenomin palvelinta.
Talenomista muodostuneessa aineistossa siirtyvien tietojen voimassa alkaen päivämäärät siirtyvät työsuhteen alkupäivämäärän mukaisena. Muutokset työsuhteen aikana tulee syöttää Neptoniin oikealla voimassa alkaen päivämäärällä.
Neptoniin tehdään ajastus henkilö-ja työsuhdetietojen lukemiseksi [tämän](<https://support.nepton.com/hc/fi/articles/360002489317>) ohjeen mukaisesti.
Voimassa alkaen – arvona käytetään työsuhteen alkupäivää.
Henkilöryhmä – arvona käytetään kustannuspaikkaa.
Sarakejärjestys
”HENKILÖNUMERO;ETUNIMI;SUKUNIMI;SÄHKÖPOSTI;PUHELINNUMERO;ENSISIJAINEN ESIMIES;HENKILÖRYHMÄ;TYÖAIKA PROSENTTEINA;MAKSURYHMÄ;VOIMASSA ALKAEN”
