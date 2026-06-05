---
id: 360003473518
title: Tikon palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003473518-Tikon-palkkatapahtumat
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
updated_at: '2025-08-06T09:02:58Z'
edited_at: '2020-10-05T12:07:54Z'
---

# Tikon palkkatapahtumat

## Tiedostomuoto  
Siirrettävässä tiedostossa kentät ovat määrämittaisia. Tieto viedään numeerisissa kentissä oikeaan laitaan ja täydennetään etunollilla (jos tietoa ei ole, koko kenttä täytetään nollilla). Muissa kentissä tieto viedään vasempaan laitaan ja loppu jätetään tyhjäksi. Tietueen pituus on 80 merkkiä.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet 
**Sijainti** |  **Tieto** |  **Muoto** |  **Sääntöjoukon kentän nimi**  
---|---|---|---  
1-4 |  Tapahtumapäivämäärä (pakollinen) |  PPKK | StartDateTime (date formatting automatic)  
5-8 |  Työntekijänumero (pakollinen) |  NNNN | _Lisätään automaattisesti, ei korvattavissa_  
9-12 |  Palkkalaji |  NNNN | SalaryCode  
13-14 |  Työnvaativuusryhmä. Siirtyy aina tyhjänä |  NN |   
15-23 |  Kappaleet (siirtyy arvo määrä) |  NNNNNN.NN | "Amount" field if unitType is 'U', or 'D'  
24-29 |  Aika tunteina ja tunnin osina |  NNN.NN | "Amount" field if unitType is 'H', or 'S' (conversion is automatic)  
30-34 |  Kellonaika mihin. Siirtyy aina tyhjänä |  NN.NN |   
35-45 |  Hinta. Siirtyy aina tyhjänä |  NNNNNN.NNNN | "Amount" field if unitType is 'C'  
46-53 |  Kustannuspaikka (osasto). Siirretään projektin koodi, mikäli asetuksissa ohjaus ’Vie projektikoodi kustannuspaikkana’. Muuten tyhjä. |  AAAAAAAA | ProjectCode1 (jos "Vie projektikoodi kustannuspaikkana")  
54-59 |  Kirjanpidontili / Kustannuslaji. Siirtyy aina tyhjänä. |  AAAAAA |   
60-67 |  Projekti. Siirretään projektin koodi mikäli ohjausta ’Vie projektikoodi kustannuspaikkana’ ei ole asetettu. Muuten tyhjä. |  AAAAAAAA | ProjectCode  
68-73 |  Projektilaji. Siirretään aina tyhjänä |  AAAAAA |   
74-79 |  Kustannuslaji (Jos kirjanpidontilillä ja kustannuslajilla on eri arvot, annetaan kustannuslaji tässä.). Siirretään aina tyhjänä |  AAAAAA |   
80 |  Varalla. Siirretään aina tyhjänä. |  |   
###  Esimerkki
15011001006000000000.00080.0000.00000000.00006010 5000 
15011001008000000000.00005.0000.00000000.00006010 5000 
15011001050000000100.00000.0000.00000000.00006010 7874 
15011002006000000000.00075.0000.00000000.00006020 5000
