---
id: 360003473498
title: Mepco palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003473498-Mepco-palkkatapahtumat
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
- S365
promoted: false
updated_at: '2025-08-06T07:55:18Z'
edited_at: '2025-08-06T07:55:14Z'
---

# Mepco palkkatapahtumat

## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360017695558)
Jos henkilön Mepco-tunnusta ei ole asetettu, käytetään henkilön henkilönumeroa.
**2\. Liittymän asetukset**
Liittymässä käytettävän sovelluksen tunnuksen, ilmoittajan käyttäjätunnuksen ja palkanlaskentayksikön voi määrittää liittymän asetuksista, Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Accountor Mepco HRM.
Aineistossa käytettävän päivämäärän voi myös asettaa asetuksista:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360017694858)
Esimerkiksi jos päivämäärän halutaan olevan muotoa PP.KK.VVVV, annetaan asetuksen arvoksi "d.m.Y"
Jos asetukselle ei ole annettu arvoa tai arvona on tyhjä, päivämäärän muotona on VVVV-KK-PP
**3\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-k%C3%A4sittely>).
## Tiedostomuoto
Siirtotiedosto on UTF-8 muotoista puolipisteellä (;) eroteltua tekstimuotoista dataa (.csv-tiedosto). Kenttien pituuksille ei ole määritelty ylärajaa. Mepcoon määritellään tiedoston luentaan tätä aineistoa vastaavat sarakkeet ja käsittelysäännöt.
Palvelun työyhteisön asetuksissa (Liittymät > Accountor Mepco HRM > Yleiset asetukset) on asetus "Sisällytä viisi projektitasoa palkka-aineistoon". Jos asetus on päällä, aineistoon muodostuu 5 projektitasoa. Jos asetus ei ole päällä, projektitasoja muodostuu vain yksi. **"Sisällytä viisi projektitasoa palkka-aineistoon" - tulee olla päällä uusissa toteutuksissa. Yhden tason siirtämisen mahdollisuus tullaan poistamaan palvelusta.**
Mepcon tuonnissa voidaan määritellä ylimääräiset sarakkeet ohitettavaksi. Tällä tavalla toimimalla useiden projektikohteiden lisääminen ei aiheuta aineistossa muiden tietosarakkeiden sarakejärjestyksen siirtymistä. Tässä ohjeessa on kuvattu suositeltu viiden projektitason tietuemuoto.  
Asetuksella 'Jaa projektikoodi useisiin koodeihin kauttaviivalla (/)' voidaan projektikoodi jakaa automaattisesti osiin kauttaviivan perusteella. Esim. projektikoodi1 1234/5678/90 jaettaisiin automaattisesti osiin ja siitä muodostuisi projektikoodi1='1234', projektikoodi2='5678' ja projektikoodi3='90'.
Osiossa Työaika > Hallina > Työyhteisön asetukset > Liittymät > Accountor Mepco HRM asetuksella 'Sisällytä rivinvaihtomerkki vientitiedoston viimeiselle riville' voidaan määrittää, muodostuuko tiedoston loppuun yksi tyhjä rivi. Joihinkin Mepcon formaattia hyödyntäviin järjestelmiin tietoa siirrettäessä voi olla välttämätöntä käyttää tätä asetusta. 
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa
  * Jos projektikoodilla ei ole arvoa eli se on NULL siirtyy projektikoodit vasemmalle. Esim. projektikoodeilla 1 ja 3 on arvo ja projektikoodi 2 on NULL, niin projektikoodin 3 arvo on kohdassa projektikoodi 2. Asettamalla projektikoodille 2 arvon "", saadaan projektikoodit omiin sarakkeisiinsa.


## Aineiston tietueet
Asetettu poimintasääntö täyttää aineiston tietueet automaattisesti. Mikäli halutaan kentän arvoon poikkeava sisältö, niin kenttänimi voidaan korvata poimimalla säännön sarakkeeksi tieto jonka nimenä on 'Override' sekä sarakkeen nimi. Override-kentän nimi on esitetty alla olevassa taulukossa. Esimerkiksi säännössä poimimalla kentän 'AS OverrideSalaryCode', poimittu arvo korvaa automaattisesti muodostuneen SalaryCode-kentän. Lisää tietoja [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>).
Sarakenumero | Sarakkeen sisältö | Säännön poiminnassa käytettävä kenttänimi | Muoto | Kuvaus  
---|---|---|---|---  
1 | Employee integration ID | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) | Henkilön Mepco-tunniste tai henkilönumero, jos Mepco-kenttää ei ole asetettu  
2 | Employee name | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) |   
3 | Event begin date | OverrideStartDateTime | päivämäärä | Päiväysmuoto on päivämäärämuodon asetuksen mukaan, oletuksena `VVVV-KK-PP`  
4 | Event end date | OverrideEndDateTime | päivämäärä | Päiväysmuoto on päivämäärämuodon asetuksen mukaan, oletuksena `VVVV-KK-PP`  
5 | Amount | OverrideAmount | desimaaliluku | Piste desimaalierottimena, kaksi desimaalia. Esim. 12.50  
6 | Salary code | OverrideSalaryCode | merkkijono  
nvarchar(max) | Sääntöjoukon säännön palkkalajikoodi  
7 | Project code 1 | OverrideProjectCode1 | merkkijono  
nvarchar(255) | Projektikoodi 1  
8 | Project code 2 | OverrideProjectCode2 | merkkijono  
nvarchar(255) | Projektikoodi 2. Huom: muodostetaan kun Mepcon vientiasetus 'Sisällytä viisi projektitasoa palkka-aineistoon' on päällä.  
9 | Project code 3 | OverrideProjectCode3 | merkkijono  
nvarchar(255) | Projektikoodi 3. Huom: muodostetaan kun Mepcon vientiasetus 'Sisällytä viisi projektitasoa palkka-aineistoon' on päällä.  
10 | Project code 4 | OverrideProjectCode4 | merkkijono  
nvarchar(255) | Projektikoodi 4. Huom: muodostetaan kun Mepcon vientiasetus 'Sisällytä viisi projektitasoa palkka-aineistoon' on päällä.  
11 | Project code 5 | OverrideProjectCode5 | merkkijono  
nvarchar(255) | Projektikoodi 5. Huom: muodostetaan kun Mepcon vientiasetus 'Sisällytä viisi projektitasoa palkka-aineistoon' on päällä.  
12 | Ruleset rule name | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) | Sääntöjoukon säännön nimi  
13 | Project IDs | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) |  Kauttaviivoilla eroteltu lista sisäisistä projektitunnuksista, esim: 1234/4342/5343  
14 | Project ID of related project | Automaattisesti asetettu, ei voida korvata | kokonaisluku | Ensimmäisen liitännäisprojektin projektitunnus (saatetaan tarvita joissakin ERP-järjestelmissä)  
15 | Project names | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) | Kauttaviivoilla eroteltu lista projektinimiä  
16 | Cost group | OverrideUserCostGroup | merkkijono  
nvarchar(max) | Voidaan korvata OverrideUserCostGroup-kentän avulla  
17 | Setting group code | Automaattisesti asetettu, ei voida korvata | merkkijono  
nvarchar(max) | Asetusryhmän koodi  
18 | Custom data 1 | CustomData1 | merkkijono  
nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi1' as CustomData1  
19 | Custom data 2 | CustomData2 | merkkijono  
nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi2' as CustomData2  
20 | Custom data 3 | CustomData3 | merkkijono  
nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi3' as CustomData3  
21 | Custom data 4 | CustomData4 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi4' as CustomData4  
22 | Custom data 5 | CustomData5 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi5' as CustomData5  
23 | Custom data 6 | CustomData6 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi6' as CustomData6  
24 | Custom data 7 | CustomData7 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi7' as CustomData7  
25 | Custom data 8 | CustomData8 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi8' as CustomData8  
26 | Custom data 9 | CustomData9 |  merkkijono nvarchar(max) | Voidaan käyttää itse valittujen lisätietojen lisäämiseksi vientiin, esim. 'testi9' as CustomData9  
CustomData4-CustomData9 sarakkeet lisätään vientitiedostoon vain jos ne ovat lisätty valittaviksi sääntöjoukon säännössä. Jos jokin CustomData4 - CustomData9 kentistä on lisätty valittavaksi sääntöjoukossa, sisällytetään kaikki CustomData4 - CustomData9 sarakkeet tiedostoon, ja ne CustomDatat joiden arvoa ei ole määritetty siirtyvät tyhjinä kenttinä. Tietueen viimeisen kentän jälkeen aineistoon muodostuu vielä puolipiste (;) ja tyhjä kenttä, jos CustomData4 - CustomData9 ei käytetä.
###  Esimerkki
Alla esimerkki tiedostosta, jossa on yhden henkilön palkkalajit kahdelle päivälle
[code] 
    72144; Elisa Esimerkki;2011-01-03;2011-01-03;4.00;1012;16141;20234;;;;Säännöllinen työaika;10437;10437;20234/Pakkaamo;200;500;;;;
    72144; Elisa Esimerkki;2011-01-04;2011-01-04;3.50;1012;16141;20234;;;;Säännöllinen työaika;10437;10437;20234/Pakkaamo;200;500;;;;
    
[/code]
