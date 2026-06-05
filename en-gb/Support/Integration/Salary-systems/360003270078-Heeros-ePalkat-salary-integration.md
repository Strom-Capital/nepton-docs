---
id: 360003270078
title: Heeros ePalkat, salary integration
url: https://support.nepton.com/hc/en-gb/articles/360003270078-Heeros-ePalkat-salary-integration
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-05-10T09:24:14Z'
---

# Heeros ePalkat, salary integration

**Sorry!**
This article has not been translated yet.
Nepton voidaan määrittää tuottamaan kirjatuista tapahtumista tulkittu palkka-aineisto Heeros ePalkat -järjestelmään.
Huom! Aineiston nimi on Neptonissa aiemmin ollut Aboa
## Määrittäminen
**1\. Henkilöiden tunnusten määrittäminen**
Henkilöiden henkilötunnisteet voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot > Tunnisteet -näkymässä.
Jos henkilön Heeros -tunnusta ei ole asetettu, käytetään henkilön henkilönumeroa.
**2\. Sääntöjoukon luominen**
Liittymässä voidaan käyttää integraation sääntöjoukkoja. Sääntöjoukon poiminnan ohje löytyy artikkelista [Sääntöjoukon poimintasääntöjen käsittely](<https://support.nepton.com/hc/fi/articles/360002489257>).
## Tiedostomuoto
Siirtotiedosto on tabulaattorilla erotettua tekstimuotoista dataa. Rivinvaihto on CR & LF. Merkistökoodaus on UTF-8.
Muodostettava aineisto on aina ryhmitelty per henkilö, per projekti, per palkkalaji
## Rajaukset
Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa
## Aineiston tietueet
Sarake | Tieto | Sääntöjoukon kentän nimi | Muoto | Kuvaus  
---|---|---|---|---  
A | Henkilönumero | OverrideUserIntegrationId | merkkijono | Henkilön Heeros-tunniste tai henkilönumero. Arvo voidaan myös antaa sääntöjoukon kentällä.  
B | Palkkalajikoodi |  _Saa arvonsa sääntöjoukon yksittäisen säännön Koodi-kentästä ja voidaan korvata käyttämällä kenttänimeä_ OverrideSalaryCode | merkkijono | Palkkalajin koodi, esimerkiksi `412`  
C | Määrä | Amount | desimaali | Määrä desimaalina. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
D | Rivi | RowDescription | merkkijono | Oletuksena tyhjä, arvo voidaan antaa sääntöjoukon kentällä.  
E | Hinta | UnitPrice | desimaali |  Oletuksena tyhjä, arvo voidaan antaa sääntöjoukon kentällä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
F | Kerroin | HeerosMultiplier | desimaali |  Oletuksena tyhjä, arvo voidaan antaa sääntöjoukon kentällä. Luku on kahden desimaalin tarkkuudella ja desimaalierottimena on pilkku (`,`).  
G | Työnumero | HeerosJobNumber | merkkijono | Oletuksena tyhjä, arvo voidaan antaa sääntöjoukon kentällä.  
H | Projekti |  | merkkijono | Jos projekteja on yksi, sen projektin projektikoodi. Jos projekteja on enemmän, projektikoodit järjestetääm aakkosjärjestyksen mukaan ja järjestyksessä viimeisenä oleva otetaan projektikoodiksi.
