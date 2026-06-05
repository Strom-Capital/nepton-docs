---
id: 360016216278
title: Sääntöjoukon esimerkit - tapahtumahistoria
url: https://support.nepton.com/hc/fi/articles/360016216278-S%C3%A4%C3%A4nt%C3%B6joukon-esimerkit-tapahtumahistoria
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sääntöjoukot
section_id: 360000827378
section_path:
- Liittymät
- Sääntöjoukot
labels: []
promoted: false
updated_at: '2025-05-06T11:35:20Z'
edited_at: '2025-05-06T11:26:23Z'
---

# Sääntöjoukon esimerkit - tapahtumahistoria

**UserEventHistoryData** -taulu mahdollistaa poiminnat tapahtumista mukaan lukien poistetut tapahtumat ja muokkaukset halutulla aikavälillä. Tähän artikkeliin on koottu esimerkkejä tiedon hakemisesta.
Tapahtumia voidaan rajata :exportPeriodStart ja :exportPeriodEnd -muuttujilla. :exportPeriodStart korvataan kyselyä suoritettaessa käsiteltävän jakson alkupäivällä YYYY-MM-DD HH:MM:SS -muotoisena. Käsiteltävän jakson alkupäivä määritellään viennin asetuksissa kuten ohjeistettu [Sääntöjoukon siirron automatisointi -artikkelissa](<https://support.nepton.com/hc/fi/articles/360002492458>). Vastaavasti :exportPeriodEnd korvataan vietävän jakson loppupäivällä.
Löydät tietokantataulujen sarakekuvaukset [täältä](<https://support.nepton.com/hc/fi/articles/360002489257>)
Siisti/muotoile -kysely -toiminnallisuutta ei tueta tietokyselyiden testaus- ja kehitystyökalussa kun käytetään muuttujia :exportPeriodStart ja :exportPeriodEnd.
### Poimitaan kaikki käsiteltävän jakson tapahtumat, mukaan lukien muutetut ja poistetut tapahtumat
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE   
      (StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)   
      OR   
      (EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)
[/code]
### Poimitaan kaikki käsiteltävän jakson aikana muokatut tapahtumat, mukaan lukien muutetut ja poistetut tapahtumat
Tätä esimerkkiä voidaan käyttää poimimaan esimerkiksi kaikki eilen tehdyt muutokset tapahtumiin riippumatta muokattujen tapahtumien alku- tai loppupäivistä.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE  
      ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd
[/code]
### Poimitaan kaikki käsiteltävän jakson aikana muokatut tapahtumat ja liitetään tapahtuman uusimman version tiedot
Tätä esimerkkiä voidaan laajentaa hakuehdoin siten, että poimitaan tietyt muutokset silloin kuin tapahtuman uusin versio sisältää tai ei sisällä tiettyjä tietoja.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData AS ModifiedEventData   
    LEFT JOIN UserEventHistoryData AS CurrentEventData   
      ON ModifiedEventData.OriginalActivityId = CurrentEventData.ActivityId   
    WHERE   
      ModifiedEventData.ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd
[/code]
### Poimitaan kaikki käsiteltävän jakson ajalle sijoittuvat poistetut tapahtumat
Tämä kysely poimii kaikki tapahtumat, jotka on poistettu ja joiden tapahtuman alku- ja tai loppupäivä on käsiteltävän jakson sisällä. Tapahtumien aiempia versioita ei poimita.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE   
      (StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd  
       OR   
       EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)  
      AND IsActive = 'N'  
      AND OriginalActivityId IS NULL
[/code]
### Poimitaan käsiteltävän jakson aikana muokatut tapahtumat
Tämä kysely poimii kaikki tapahtumat, jotka poistettiin annetulla aikavälillä riippumatta tapahtuma-ajasta. Tapahtumien aiempia versioita ei poimita.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData   
    WHERE   
      ModifiedDateTime BETWEEN :exportPeriodStart AND :exportPeriodEnd  
      AND IsActive = 'N'  
      AND OriginalActivityId IS NULL
[/code]
### Poimitaan käsiteltävän jakson ajalta kaikki tapahtumat, joiden viimeisen versio on poistettu
Tapahtuma on poistettu silloin kun sen viimeisin versio on poistettu, eikä siitä ole tehty uusia muokkauksia.
Tapahtuma, jonka aikaa on muutettu tai jota on muuten muokattu, saattaa olla poistettu myöhemmässä muokkauksessa. Tämä kysely poimii tapahtumat, joiden tapahtuma-aika on annetulla aikavälillä ja jotka on lopulta poistettu.
[code] 
    SELECT  
      *   
    FROM  
      UserEventHistoryData AS ModifiedEventData   
    LEFT JOIN UserEventHistoryData AS CurrentEventData   
      ON ModifiedEventData.OriginalActivityId = CurrentEventData.ActivityId   
    WHERE   
      (ModifiedEventData.StartDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd  
       OR   
       ModifiedEventData.EndDatetime BETWEEN :exportPeriodStart AND :exportPeriodEnd)  
      AND ((ModifiedEventData.IsActive = 'N'  
            AND ModifiedEventData.OriginalActivityId IS NULL)  
           OR  
            CurrentEventData.IsActive = 'N')
[/code]
