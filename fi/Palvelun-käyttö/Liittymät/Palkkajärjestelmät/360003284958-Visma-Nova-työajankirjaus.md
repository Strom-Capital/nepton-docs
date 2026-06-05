---
id: 360003284958
title: Visma Nova työajankirjaus
url: https://support.nepton.com/hc/fi/articles/360003284958-Visma-Nova-ty%C3%B6ajankirjaus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- nova
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2022-02-24T09:23:45Z'
---

# Visma Nova työajankirjaus

## Tiedostomuoto   
Työaikakirjaukset tuodaan Työaika-ohjelmasta.
  * Puolipiste-eroteltu tiedosto
  * Desimaalierottimena käytetään pilkkua
  * Jokaisen tietueen lopussa oltava puolipiste


##  Aineiston tietueet
Vain tietuetyyppi Tuntikirjaukset siirretään.
**Tietuetyypit:**
0 - Tuntikirjaukset
1 - Vaihetunnit
**Mallitiedosto:**
**Tyyppi 0**
TYYPPI0;HNRO;PVM;PROJEKTI;KP;ANUMERO;PLAJI;STUNNIT;TTUNNIT;LTUNNIT;SELITE;TIETUEPVM;TIETUEUSER;TIETUEMPVM;TIETUEMUSER;ALKU;LOPPU;PSELITE;SIIRTOPVM;LITTERA;YKSIKKO;LASKUTUSPVM;LASKUNRO;KOODI;TYONUMERO;TYOVAIHE;MAARA;URAKKAHINTA;TYOVAIHEVALMIS;AHINTA;OVH;SIIRRETTY;PROJEKTISELITE;GUID;EDITSTAMP;EDITUSER;TOSITE;LAJI;TYOSELITE;MINVALUE;TVR;SEASON  
0;123;2022-02-01 08:00:00;Projekti1;Cost center;;12345;;7,50;;Some description;2022-02-23 17:17:53;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  
0;456;2022-02-01 09:45:00;Projekti2;Cost center;;12345;;0,25;;Some description;2022-02-23 17:18:19;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
**Tyyppi 1**
TYYPPI1;tyonumero;vaihenumero;aloitus;lopetus;kesto;henkilo;plaji;koodi;maara;  
1;9;1;01.07.2008 02:36:00;01.07.2008 03:12:00;0,6;2;;00001769;;
**9.1.1 Tyyppi0: Tuntikirjaukset**
**Kenttä** |  **Sääntöjoukon kentän nimi** |  **Tyyppi/pituus** |  **Selite**  
---|---|---|---  
**0** |  **** |  int |  Tyyppimääritys  
**Hnro** |  _Lisätään automaattisesti, ei korvattavissa_ |  int |  Henkilönumero  
Pvm |  StartDateTime |  datetime |  Tekopäivä, korvattavissa  
Projekti |  ProjectCode1 |  20 |  Projektikoodi1, korvattavissa  
Kp |  VismaCostCentre |  20 |  Kustannuspaikan tunnus, kustannuspaikka haetaan henkilön asetuksista tai tyhjä jos ei ole asetettu, korvattavissa  
Anumero |  VismaNovaCustomerNo |  int |  Asiakasnumero, siirretään tyhjänä  
Plaji |  SalaryCode |  smallint |  Palkkalaji, korvattavissa  
Stunnit |  |  money |  vapaa / ei käytössä, siirretään tyhjänä  
Ttunnit |  Amount |  money |  Toteutunut työaika / h, korvattavissa  
Ltunnit |  VismaNovaBillableHours |  money |  Laskutettava työaika / h, siirretään tyhjänä, korvattavissa  
Selite |  VismaNovaDescription |  50 |  Selite / nimike, siirretään oletuksena tyhjänä, korvattavissa  
Tietuepvm |  |  smalldatetime |  Tietueen/tiedoston luontipvm  
Tietueuser |  VismaNovaCreatedBy |  20 |  Tietueen perustaja, siirretään oletuksena tyhjänä, korvattavissa  
Tietuempvm |  VismaNovaModifiedDateTime |  smalldatetime |  Tietueen muutospvm, siirretään oletuksena tyhjänä, korvattavissa  
Tietuemuser |  VismaNovaModifiedBy |  20 |  Tietueen muuttaja, siirretään oletuksena tyhjänä, korvattavissa  
Alku |  |  smalldatetime |  Työn aloitus kellonaika, ei käytössä, siirretään tyhjänä  
Loppu |  |  smalldatetime |  Työn lopetus kellonaika, ei käytössä, siirretään tyhjänä  
Pselite |  VismaNovaActivityCodeDescription |  40 |  Palkkalajin selite, siirretään oletuksena tyhjänä, korvattavissa  
Siirtopvm |  VismaNovaTransferDateTime |  smalldatetime |  Siirretty palkanlaskentaan, siirretään oletuksena tyhjänä, korvattavissa  
Littera |  VismaNovaLetter |  10 |  Projektivaihe, siirretään oletuksena tyhjänä, korvattavissa  
Yksikko |  VismaNovaUnit |  5 |  Yksikkö (kpl,H yms), siirretään oletuksena tyhjänä, korvattavissa  
Laskutuspvm |  VismaNovaInvoiceDatetime |  smalldatetime |  Siirretty laskutukseen, siirretään oletuksena tyhjänä, korvattavissa  
Laskunro |  VismaNovaInvoiceNo |  int |  Laskun numero, siirretään oletuksena tyhjänä, korvattavissa  
Koodi |  VismaNovaProductCode |  30 |  Tuotekoodi, siirretään oletuksena tyhjänä, korvattavissa  
Tyonumero |  VismaNovaWorkNo |  int |  Työnumero jolle kirjattu, siirretään oletuksena tyhjänä, korvattavissa  
Työvaihe |  VismaNovaWorkStage |  smallint |  Työnumeron työvaihe, siirretään oletuksena tyhjänä, korvattavissa  
Maara |  VismaNovaAmount |  money |  Tehty määrä, siirretään oletuksena tyhjänä, korvattavissa  
Urakkahinta |  |  money |  ei käytössä, siirretään tyhjänä  
Tyovaihevalmis |  VismaNovaWorkStageReady |  bit |  Onko työvaihe valmis, siirretään oletuksena tyhjänä, korvattavissa  
Ahinta |  VismaNovaUnitPrice |  money |  Yksikköhinta, siirretään oletuksena tyhjänä, korvattavissa  
Ovh |  VismaNovaInvoicePrice |  money |  laskutukseen yhteishinta, siirretään oletuksena tyhjänä, korvattavissa  
Siirretty |  |  smalldatetime |  ei käytössä, siirretään tyhjänä  
Projektiselite |  VismaNovaProjectName |  30 |  Projektinnimi, siirretään oletuksena tyhjänä, korvattavissa  
Guid |  VismaNovaGuid |  ?? |  Projektinnimi, siirretään oletuksena tyhjänä, korvattavissa  
Editstamp |  VismaNovaEditStamp |  ?? |  Editstamp, siirretään oletuksena tyhjänä, korvattavissa  
Edituser |  VismaNovaEditUser |  ?? |  Edituser, siirretään oletuksena tyhjänä, korvattavissa  
Tosite |  VismaNovaReceipt |  int |  Kirjauksen yksilöllinen tosite, siirretään oletuksena tyhjänä, korvattavissa  
Laji |  VismaNovaRegistrationType |  int |  Kirjauslaji 1,3,4, siirretään oletuksena tyhjänä, korvattavissa  
Työselite |  VismaNovaWorkDescription |  1000 |  Vapaa teksti, siirretään oletuksena tyhjänä, korvattavissa  
Minvalue |  VismaNovaMinValue |  int |  Urakkatunnit käyttää, siirretään oletuksena tyhjänä, korvattavissa  
Tvr |  VismaNovaTvr |  int |  Informatiivinen urakkatunnit, siirretään oletuksena tyhjänä, korvattavissa  
Season |  VismaNovaSeason |  ?? |  Season, siirretään oletuksena tyhjänä, korvattavissa  
**Tyyppi1: Vaihekirjaukset (EI MAHDOLLISTA SIIRTÄÄ TOISTAISEKSI)  
**
**Kenttä** |  **Tyyppi/pituus** |  **Selite** |  **Pakollinen**  
---|---|---|---  
**1** |  int |  Tyyppimääritys |  X  
**Tyonumero** |  int |  Työnumero |  X  
Tila |  smallint |  Vapaa  
**Vaihenumero** |  smallint |  Työvaiheennumero |  X  
Aloitus |  datetime |  Aloitusaika (pvm + klo)  
Lopetus |  datetime |  Lopetusaika (pvm + klo)  
Kesto |  money |  Kestoaika  
**Henkilo** |  int |  Työntekijä numero |  X  
Plaji |  int |  Palkkalajin numero  
Koodi |  30 |  Tuotekoodi  
Määrä |  money |  Tehty määrä  
Vialliset |  money |  Susikappaleet  
Kpaikka |  20 |  Kustannuspaikka
