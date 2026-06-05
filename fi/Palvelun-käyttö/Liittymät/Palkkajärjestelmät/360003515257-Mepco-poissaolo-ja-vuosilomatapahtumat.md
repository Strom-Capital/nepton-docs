---
id: 360003515257
title: Mepco poissaolo- ja vuosilomatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003515257-Mepco-poissaolo-ja-vuosilomatapahtumat
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-01-23T11:00:01Z'
edited_at: '2025-01-23T11:00:00Z'
---

# Mepco poissaolo- ja vuosilomatapahtumat

Tämä on vanha liittymä poissaolotapahtumien viemiseksi Mepcoon. On suositeltavaa käyttää uudempaa liittymää [Accountor Mepco HRM poissaolojen vienti](<https://support.nepton.com/hc/fi/articles/23700503323933>). Uusi liittymä käsittelee poissaolotapahtumat heti, kun ne merkitään kalenteriin. Tämä mahdollistaa reaaliaikaisen liittymän suorittamisen, kun poissaolotapahtumia luodaan, muokataan tai poistetaan. Olethan yhteydessä Nepton-yhteyshenkilöösi, mikäli haluat ottaa uuden liittymän käyttöön.
Poissaolotapahtumien viennissä voidaan hakea kaikki poissaolot tai vain vuosilomat.
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/11393128561181)
Jos henkilön Mepco-tunnusta ei ole asetettu, käytetään henkilön henkilönumeroa.
**2\. Liittymän asetukset**
Liittymässä käytettävän sovelluksen tunnuksen, ilmoittajan käyttäjätunnuksen ja palkanlaskentayksikön voi määrittää liittymän asetuksista, **Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Accountor Mepco HRM**
Aineistossa käytettävän päivämäärän voi myös asettaa asetuksista:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/11393128562077)
Esimerkiksi jos päivämäärän halutaan olevan muotoa PP.KK.VVVV, annetaan asetuksen arvoksi "d.m.Y"
Jos asetukselle ei ole annettu arvoa tai arvona on tyhjä, päivämäärän muotona käytetään:
  * Poissaoloaineistoissa VVVV-KK-PP
  * Vuosiloma-aineistossa PP.KK.VVVV


**3\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto
Siirtotiedosto on UTF-8 muotoista puolipisteellä (`;`) eroteltua tekstimuotoista dataa. Kenttien pituuksille ei ole määritelty ylärajaa. Mepcoon määritellään tiedoston luentaan tätä aineistoa vastaavat sarakkeet ja käsittelysäännöt.
Tiedonsiirto on mahdollista ottaa käyttöön myös vain yhdellä projektikohdenteella.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
Sarake | Kenttä | Sääntöjoukon kentän nimi | Muoto | Kuvaus  
---|---|---|---|---  
A | Henkilönumero | _Lisätään automaattisesti, ei korvattavissa_ | string | Henkilön Mepco-tunnus / henkilönumero  
B | Poissaolon alkamispvm | StartDateTime | date | Poissaolon alkamispäivämäärä. Päiväysmuoto on päivämäärämuodon asetuksen mukaan.  
C | Poissaolon päättymispvm | EndDateTime | date | Poissaolon päättymispäivämäärä. Päiväysmuoto on päivämäärämuodon asetuksen mukaan.  
D | Henkilön nimi | _Lisätään automaattisesti, ei korvattavissa_ | string | Henkilön suku- ja etunimet  
E | Projektikoodi 1 | ProjectCode1 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode1`  
F |  Projektikoodi 2 | ProjectCode2 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode2`  
G |  Projektikoodi 3 | ProjectCode3 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode3`  
H |  Projektikoodi 4 | ProjectCode4 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode4`  
I |  Projektikoodi 5 | ProjectCode5 | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode5`  
J | Palkkalajikoodi | SalaryCode | string | Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideSalaryCode`  
K | Määrä | Amount | decimal | Poissaolon pituus, voidaan esittää tunteina tai päivinä. Desimaalierottimena on piste (`.`)  
## Esimerkki
[code] 
    1918;2020-02-03;2020-02-04;Meikäläinen Matti;1001;0002;;;;418;2.00
    1918;2020-03-09;2020-03-09;Meikäläinen Matti;2002;;;;;404;3.50
[/code]
