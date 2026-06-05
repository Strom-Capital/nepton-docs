---
id: 360002559857
title: Vuosivapaan asetusten määrittely
url: https://support.nepton.com/hc/fi/articles/360002559857-Vuosivapaan-asetusten-m%C3%A4%C3%A4rittely
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Esimerkkejä asetusryhmien perustamiseksi
section_id: 360001483898
section_path:
- Työajan laskenta ja hallinta
- Asetusryhmät
- Esimerkkejä asetusryhmien perustamiseksi
labels:
- NEPTONNEEDSREVIEW
- Vuosivapaan ansaitseminen
promoted: false
updated_at: '2024-09-25T05:30:12Z'
edited_at: '2024-09-25T05:30:11Z'
---

# Vuosivapaan asetusten määrittely

## Yleistä vuosivapaasta
Vuosivapaata kertyy vain Työ ja Ylityö -tapahtumatyypeistä. Vuosivapaat pidetään ensisijaisesti ansaintavuoden aikana, kuitenkin viimeistään ansaintavuotta seuraavan vuoden huhtikuun loppuun mennessä.
## Vuosivapaan määritykset
Palvelu laskee vuosivapaata tässä kappaleessa kuvattujen määritysten mukaisesti. Vuosivapaan kertymään huomioidaan valituista tapahtumatyypeistä muodostuva työaika (myös ylityö).
Asetuksissa on mahdollista valita tapahtumatyyppikohtaisesti sen huomiointi vuosivapaan ansaintaan. Mikäli tapahtumatyypille ei ole toisin asetettu, niin vuosivapaata ansaitaan kaikista tapahtumatyypeistä pois lukien:
  * palkaton poissaolo
  * palkaton sairausloma
  * vuosiloma
  * saldovapaa
  * työajan lyhennysvapaa
  * vuosivapaa


Vuosivapaan määritykset voidaan määrittää joko **Työyhteisö** -tasolla tai **Asetusryhmät** -tasolla. Mikäli vuosivapaan ansaintaperuste on pääsääntöisesti kaikilla yrityksen työntekijöillä samanlainen, ansainnan perusteet on helpointa määrittää Työyhteisö-tason asetuksiin, jolloin ne koskevat myös kaikkia asetusryhmiä. 
**Työaika > Hallinta > Työyhteisön asetukset > Työtunnit > Kertymät ja ylityötunnit**  
tai  
**Hallinta > Asetusryhmät > Asetusryhmä-valikko: Haluttu asetusryhmä >Toiminto-valikko: Asetusryhmän asetukset > Työtunnit > Kertymät ja ylityötunnit**
### Yleiset asetukset
Kertymä asetetaan päälle **Kertymä käytössä** -kohdasta **Vuosi****vapaa: Asetus päällä**.  
  
  
![](https://support.nepton.com/hc/article_attachments/20392473121693)  
**Laskennan asetukset** > **Vuosivapaa** -otsikon alla määritellään vuosivapaan ansainnan asetukset.
**Näkyvissä viikkotauluissa** \- Näytetäänkö kertymän tilanne Työajan kalenterissa ja Tapahtumat taulukossa - näkymässä. Oletusarvo on "Kyllä", jos mitään ei ole asetettu.
**Laske kertymän ennuste tulevaisuudessa** \- Ennustaako järjestelmä kertymän arvon tulevaisuuteen. Oletusarvo on "Kyllä", jos mitään ei ole asetettu.
**Koodi** \- Tarvitaan, mikäli vuosivapaa-tietoja siirretään integraatioissa Neptonista muihin järjestelmiin. (Koodi löytyy vain Työyhteisötasolta).
### Lainaussäännöt
**Kertymä lainaa automaattisesti kertymän saldosta** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä, jos päivän työvelvoite ei ole täyttynyt.
**Älä lainaa saldosta, jos työvelvoite on käsinasetettu** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä, jos päivän työvelvoite on asetettu manuaalisesti. Työvelvoite voidaan asettaa manuaalisesti kalenterinäkymässä muuttamalla päivän "Työpäivän pituus" - arvoa.
**Täytä työviikon tunnit saldosta työviikon viimeisenä päivänä** \- "Kyllä/Ei" - valinta sille, lainataanko aikaa kertymästä viikon päätteeksi, jos viikon työvelvoite ei ole täyttynyt.
### Ansainnan säännöt
**Ansaintakausi** \- Joko kuukausi tai vuosi
**Ansaintaperuste** voidaan määritellä joko tunteina, päivinä tai kuukausina.
Jos ansaintaperuste on kuukausina, vuosiloma-ajan laskennan työpäivien määrää tai työtuntien määrää käytetään katsomaan, ansaitaanko työkuukaudelta vuosivapaata. Lue lisää vuosiloman ansainnan käyttöönotosta [täällä](<https://support.nepton.com/hc/fi/articles/360002560698>).
Jos ansaintaperuste on tunteina, ansaintakynnys voidaan asettaa minuuttien tarkkuudella.
Huom! Ansaintaperusteena ei voi käyttää kuukausina, jos ansaintakautena on kuukausi. Jos näin on asetettu, vuosivapaata ei ansaita lainkaan.
**Ansaitaan** -kohtaan valitaan ansaitaanko vapaat tunteina vai päivinä. 
**Vapaa/loma jätetään huomiotta juhlapyhinä** \- Jos on asetettu "Kyllä", juhlapyhä estää vuosivapaan käyttämisen tai sen vähentämisen kertymän saldosta. Oletuksena "Ei".
**Ansaitse jos työsuhteen kesto ylittää** -kohdassa voidaan määritellä työsuhteen vähimmäiskesto vuosivapaan ansaitsemiselle. Tämä on käytössä vain, jos Työsuhde-osiossa on määritelty työsuhteen alkamispäivä.
**Ansaitaan vain säännölliseltä työajalta** -kohdassa voidaan määrittää, että työajan lyhennysvapaata ansaitaan vain säännölliseltä työajalta, eli siten että ylityötä ei oteta huomioon.
**Ansaitse kertymästä lainatusta ajasta** -kohdassa voidaan määrittää, ansaitaanko kertymää ajasta joka on lainattu kertymästä, kuten esimerkiksi aika joka on lainattu saldosta.
**Ansaitaan työsuhteen alusta** -kohdassa voidaan määrittää, että vuosivapaata ansaitaan työsuhteen alusta kun työsuhde on kestänyt "ansaitse jos työsuhteen kesto ylittää" -kohdassa määritettyjen kuukausien verran. Jos arvona on "Ei" tai arvoa ei ole asetettu, vuosivapaan ansainta alkaa vasta sen jälkeen kun työsuhde on kestänyt määritettyjen kuukausien verran.
Jos vuosivapaan ansainnan määrä ei ole sama joka kuukausi, esimerkiksi työsuhteen ja kalenterivuoden ensimmäisenä kuukautena ansaitaan enemmän kuin muina kuukausina, tällöin palvelun **käyttöönoton** yhteydessä Neptoniin tulee tuoda aikaisemmasta työnajanhallintajärjestelmästä tehdyt tapahtumat vuoden alusta. Tällöin Nepton tietää henkilön työskentelyn kalenterivuoden alusta alkaen ja voi laskea oikean ansainnan määrän käyttöönoton alkaessa.  
  

![](https://support.nepton.com/hc/article_attachments/21806963521949)
**Tapahtumatyyppi (Palkallinen)** ja **Tapahtumatyyppi (Palkaton)** -kohdissa voidaan määritellä tapahtumatyyppikohtaisesti, ansaitaanko tapahtumista työajan lyhennysvapaata. Muista kuin luetelluista palkallisista tapahtumatyypeistä ansaitaan oletusarvoisesti työajan lyhennysvapaata. Tapahtumatyyppi (Palkaton) -kohdassa luetelluille tapahtumatyypeille ei oletusarvoisesti ansaita työajan lyhennysvapaata ellei asetusta erikseen laiteta päälle.
![](https://support.nepton.com/hc/article_attachments/21806947598877)
## Vuosivapaan ansainta ja käyttö
Palvelu laskee vuosivapaan ansaintaa voimassa olevien asetuksien mukaan automaattisesti. Kun vuosivapaan kertymisen peruste, esimerkiksi tietty työskentelymäärä on ansaittu, tulee vuosivapaa-kertymään sille päivälle automaattisesti plussaa.
Vuosivapaata käytetään tapahtumatyypillä 'Vuosivapaa'. Tämä tapahtumatyyppi vähentää automaattisesti tapahtumapäivältä vuosivapaan kertymää.
Jos vuosivapaata ansaitaan päivinä, ja vapaata halutaan pitää puoli päivää, vuosivapaan kestoksi merkitään puolet työpäivän kestosta. Järjestelmä pyöristää käytetyn vapaan sille annetun keston mukaisesti puolikkaisiin päiviin. Eli esimerkiksi jos työpäivän pituus on 8 tuntia, jos vuosivapaan kestoksi merkitään 3,5 tuntia, tämä pyöristyy niin että vuosivapaata käytetään puoli päivää.
Jos vuosivapaata halutaan pitää puolikkaita päiviä yli yhden vuorokauden keston, tulee puolikkaan päivän vuosivapaa merkitä omana tapahtumanaan. Eli esimerkiksi jos halutaan pitää 1,5 päivää vuosivapaata, merkitään yksi päivän mittainen vuosivapaa ja yksi puolen päivän mittainen vuosivapaa.
## Vuosivapaan raportointi
Vuosivapaan sekä muiden kertymien raportoinnista on kerrottu lisää [täällä](<https://support.nepton.com/hc/fi/articles/4410571913873>).
