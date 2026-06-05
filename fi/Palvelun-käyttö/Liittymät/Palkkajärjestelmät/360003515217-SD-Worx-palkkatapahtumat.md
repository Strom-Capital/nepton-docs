---
id: 360003515217
title: SD Worx palkkatapahtumat
url: https://support.nepton.com/hc/fi/articles/360003515217-SD-Worx-palkkatapahtumat
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- sdworks
- sdworx
- SD worx
promoted: false
updated_at: '2026-06-04T12:09:17Z'
edited_at: '2026-06-04T12:08:49Z'
---

# SD Worx palkkatapahtumat

SD Worx oli aiemmin nimellä Personec W.
## Tiedostomuoto
Siirtotiedosto on ISO-8859-1 muotoista puolipisteellä (;) eroteltua tekstimuotoista dataa. Aineisto ei sisällä otsikoita. Kenttien pituuksille ei ole määritelty ylärajaa. Palkka-aineiston schema-tiedoston voi ladata palvelusta.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa
  * Tyhjät projektikoodit korvataan seuraavasti. Projektikoodit 1 ja 2: arvoa ei korvata, vaikka niiden arvo olisi NULL. Projektikoodit 3-5: jos arvo on NULL, niin arvo korvataan seuraavan projektikoodin arvolla. Esim. Projektikoodi3 = NULL, projektikoodi4 = 123 ja projektikoodi5 = NULL, on arvot projektikoodi3 = 123, projektikoodi4 = NULL ja projektikoodi5 = NULL.


## Aineiston tietueet
Asetettu poimintasääntö täyttää aineiston tietueet automaattisesti. Mikäli halutaan kentän arvoon poikkeava sisältö, niin osa kenttänimistä voidaan korvata poimimalla säännön sarakkeeksi tieto jonka nimenä on 'Override' sekä sarakkeen nimi. Override-kentän nimi on esitetty alla olevassa taulukossa. Esimerkiksi säännössä poimimalla kentän 'AS OverrideSalaryCode', poimittu arvo korvaa automaattisesti muodostuneen SalaryCode-kentän. Seuraaviin kenttiin voidaan käyttää Override-sääntöä: Salary code, Unit type, Amount, Project codes 1-5, StartDateTime ja EndDateTime. Lisää tietoja [täältä](<https://support.nepton.com/hc/fi/articles/360002489257-S%C3%A4%C3%A4nt%C3%B6joukon-poimintas%C3%A4%C3%A4nt%C3%B6jen-muodostaminen>).  

**Sarake** |  **Kuvaus** |  **Integraatiokyselyn kenttä  
** |  **Formaatti** |  **Huom**  
---|---|---|---|---  
A |  Henkilönumero |  Asetetaan automaattisesti, ei voi muuttaa |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin. Jos liittymän ID on tyhjä, käytetään henkilönumeroa.  
B |  Palkkalajikoodi |  SalaryCode |  merkki |   
C |  Alkupäivä |  StartDateTime |  merkki |  Formaatti DD.MM.YYYY  
D |  Loppupäivä |  EndDateTime |  merkki |  Formaatti DD.MM.YYYY  
E |  Määrä, tunteja |  Määrä-kenttä, jos UnitType on 'H' tai 'S', muuten 0 |  desimaali |  Määrä tunteina kahdella desimaalilla. , desimaalierottimena. Tässä kentässä on arvo, jos määrä siirretään tunteina.  
F |  Määrä, päiviä |  Määrä-kenttä, jos UnitType on 'J', muuten 0 |  desimaali |  Määrä päivinä kahdella desimaalilla. , desimaalierottimena. Tässä kentässä on arvo, jos määrä siirretään päivinä.  
G |  Määrä, desimaali/yksikkö |  Määrä-kenttä, jos UnitType on 'U' tai 'D', muuten 0 |  desimaali |  Määrä kahdella desimaalilla. , desimaalierottimena. Tässä kentässä on arvo, jos määrä siirretään desimaalina tai kappaleina.  
H |  Projektikoodi1 |  ProjectCode1 |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin  
I |  Projektikoodi2 |  ProjectCode2 |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin  
J |  Projektikoodi3 |  ProjectCode3 |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin  
K |  Projektikoodi4 |  ProjectCode4 |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin  
L |  Projektikoodi5 |  ProjectCode5 |  merkki |  Kentän sisältö sijoitetaan lainausmerkkien (") väliin  
M |  Määrä,valuutta |  Määrä-kenttä, jos UnitType on 'C', muuten 0 |  desimaali |  Määrä valuuttana kahdella desimaalilla. , desimaalierottimena. Tässä kentässä on arvo, jos määrä siirretään valuuttana.
