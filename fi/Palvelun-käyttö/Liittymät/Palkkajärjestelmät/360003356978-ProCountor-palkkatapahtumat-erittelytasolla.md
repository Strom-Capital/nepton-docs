---
id: 360003356978
title: ProCountor palkkatapahtumat erittelytasolla
url: https://support.nepton.com/hc/fi/articles/360003356978-ProCountor-palkkatapahtumat-erittelytasolla
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
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-06-08T11:09:25Z'
---

# ProCountor palkkatapahtumat erittelytasolla

## Tiedostomuoto
Siirtotiedosto on csv-muotoinen ProCountor – vakiomallin mukainen tiedosto. Tiedostossa siirretään tapahtumien tulkittu palkka-aineisto.
Rivityyppi E, tapahtumat erittelytasolla
**Column** |  **Field** |  **Integration query field  
** |  **Type** |  **Notes**  
---|---|---|---|---  
A |  Rivityyppi |  Asetetaan automaattisesti |  merkki |  Aina "E"  
B |  Henkilötunnus |  Asetetaan automaattisesti |  merkki |   
C |  Palkkalajin koodi |  SalaryCode |  merkki |  Palkkalajikoodi  
D |  Palkkalajin nimi |  ProcountorERowPaygradeName |  merkki |  Oletuksena tyhjä, voidaan korvata kentällä ProcountorERowPaygradeName  
E |  Määrä |  Amount |  desimaali, pilkku (,) desimaalierottimena |   
F |  Yksikköhinta |  ProcounterERowRate |  desimaali, pilkku (,) desimaalierottimena |  Oletuksena tyhjä, voidaan korvata kentällä ProcounterERowRate  
G |  Projektin 1 nimi |  ProjectName1 |  merkki |   
H |  Projektin 1 koodi |  ProjectCode1 |  merkki |   
I |  Projektin 2 nimi |  ProjectName2 |  merkki |   
J |  Projektin 2 koodi |  ProjectCode2 |  merkki |   
K |  Projektin 3 nimi |  ProjectName3 |  merkki |   
L |  Projektin 3 koodi |  ProjectCode3 |  merkki |   
M |  Projektin 4 nimi |  ProjectName4 |  merkki |   
N |  Projektin 4 koodi |  ProjectCode4 |  merkki |   
O |  Projektin 5 nimi |  ProjectName5 |  merkki |   
P |  Projektin 5 koodi |  ProjectCode5 |  merkki |   
Q |  Projektin 6 nimi |  ProjectName6 |  merkki |   
R |  Projektin 6 koodi |  ProjectCode6 |  merkki |
