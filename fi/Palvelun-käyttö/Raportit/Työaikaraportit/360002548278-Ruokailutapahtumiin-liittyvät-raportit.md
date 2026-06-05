---
id: 360002548278
title: Ruokailutapahtumiin liittyvät raportit
url: https://support.nepton.com/hc/fi/articles/360002548278-Ruokailutapahtumiin-liittyv%C3%A4t-raportit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Työaikaraportit
section_id: 360005870318
section_path:
- Raportit
- Työaikaraportit
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-05-13T09:00:16Z'
edited_at: '2025-05-13T09:00:16Z'
---

# Ruokailutapahtumiin liittyvät raportit

Ruokailuraportointi liittyy ruokalapäätteen tai selaimen kautta merkittyihin ruokailu-työlisiin. Kyseiset merkinnät kertovat, mitä henkilöt ovat ostaneet ruokalasta. Artikkelissa kuvataan, millaisia ruokailuun liittyviä raportteja on saatavilla ja mitä tietoa ne sisältävät. 
## Ruokailut henkilöittäin
Raportilla näytetään henkilöiden ruokailu-tapahtumien työlisät päivätasolla. Työlisät kuvaavat, millaisesta ruokailusta on kyse. Raportti voidaan tulostaa ja viedä Exceliin.
![](https://support.nepton.com/hc/article_attachments/25691958077469)
## Ruokailujen yhteenveto henkilöittäin
Raportilla näytetään henkilöiden ruokailutapahtumien yhteismäärä ruokailutyypeittäin.
Raportti voidaan tulostaa ja viedä Exceliin.
![](https://support.nepton.com/hc/article_attachments/25691958077725)
## Ruokailuraportti ravintolahenkilökunnalle tai muille kolmansille osapuolille
Tietyissä tilanteissa on hyödyllistä, että kolmas osapuoli, jolla ei ole pääsyä Neptoniin, voi nähdä ruokailutapahtumien työlisiä näkemättä kuitenkaan käyttäjien henkilökohtaisia tietoja.
Tämä onnistuu ajastetulla [mukautetun viennin raportilla](<https://support.nepton.com/hc/fi/articles/10758741671581>), joka lähettää raportin taulukkotiedostona sähköpostiin.
Ohjeet asetuksiin:
  1. Luo integraation sääntöjoukko sekä kysely, joka hakee vain kolmannen osapuolen tarvitsemat tiedot. Alla suositeltu kysely, joka ei sisällytä mukaan arkaluonteista tietoa: 
[code]SELECT   
         s.startDateTime, s.WorkIncrementName as SupplementName, s.Amount, s.UnitType, e.TerminalId   
         FROM UserSalaryData s   
         INNER JOIN UserEventData e ON s.activityId = e.activityid   
         WHERE s.CompensationType = 'WorkIncrement'   
         and TerminalId IS NOT NULL 
[/code]
  2. Määritä sääntöjoukolle haettua tietoa vastaavat sarakkeet. Otsikkorivi kannattaa sisällyttää vientiin. Alla suositeltu esimerkki asetuksista. Tarkempia ohjeita [tässä artikkelissa](<https://support.nepton.com/hc/fi/articles/10758741671581>).  
![](https://support.nepton.com/hc/article_attachments/10767697772317)
  3. Nyt vienti voidaan ajastaa lähettämään tiedosto päivittäin kolmannen osapuolen sähköpostiosoitteisiin. Lisätietoa ajastuksesta [tästä artikkelista](<https://support.nepton.com/hc/fi/articles/10510800700573>).
