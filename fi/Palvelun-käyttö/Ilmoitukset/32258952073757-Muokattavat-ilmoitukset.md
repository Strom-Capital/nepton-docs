---
id: 32258952073757
title: Muokattavat ilmoitukset
url: https://support.nepton.com/hc/fi/articles/32258952073757-Muokattavat-ilmoitukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Ilmoitukset
section_id: 32229019276445
section_path:
- Ilmoitukset
labels: []
promoted: false
updated_at: '2026-01-08T11:41:44Z'
edited_at: '2026-01-08T11:41:06Z'
---

# Muokattavat ilmoitukset

[**Valmiit i****lmoitukset**](<https://support.nepton.com/hc/fi/articles/32229098583965>) ovat käytettävissä Työaika Pro -palvelutasolla sekä tätä ylemmillä työajan palvelutasoilla. Muokattavat ilmoitukset ovat käytettävissä Työaika Complete -palvelutasolla.
Tämä artikkeli koskee muokattavia ilmoituksia. Lisätietoja ilmoitukset-näkymästä ja ilmoituksien luomisesta löytyy artikkelista [**Ilmoituksen luominen**.](<https://support.nepton.com/hc/fi/articles/32259026029213>)
## Mitä ovat muokattavat ilmoitukset?
Muokattavat ilmoitukset mahdollistavat organisaation omien tarpeiden mukaiset ilmoitukset. Ne perustuvat poimintasääntöihin (SQL), joilla määritetään, ketkä henkilöt ja mitkä tapahtumat sisältyvät ilmoitukseen. Poimintasäännöllä voidaan joustavasti määritellä:
  * Haettavat tiedot ilmoituksen kohteista (esim. henkilöt, tapahtumat, saldot).
  * Määritellä ehdot, joiden täyttyessä ilmoitus lähetetään.
  * Rajata tietoja henkilöstöryhmän, maksuryhmän tai muiden kriteerien perusteella.


Koska muokattavien ilmoitusten sisältö määräytyy sääntöjoukon mukaan, ja ne voivat sisältää mahdollisesti arkaluonteisia tietoja (esim. sairaslomat). Varmista aina, ettei ilmoitus paljasta tietoja, joita organisaatiossa ei saa välittää sähköpostitse, eivätkä käyttäjät normaalisti näe asiakasympäristössä.
## Muokattavan ilmoituksen määrittely
Muokattava ilmoitus määritellään **lisäasetukset** -välilehdellä, jossa hallitaan ilmoituksen poimintasääntöjä. Poimintasäännöt määrittävät, millä perusteella ilmoitukseen sisältyvät tiedot valitaan. Näkymässä voidaan muokata SQL-pohjaista sääntöä, joka hakee tarvittavat tapahtumat, henkilöt ja ryhmät järjestelmän tietokantatauluista.
**Lisäasetukset-näkymä:**
  * **Poimintasääntö:** Näyttää SQL-kyselyn, joka määrittää ilmoituksen sisällön. Kyselyssä voidaan käyttää valmiita muuttujia ja lisätä asiakaskohtaisia sääntöjä.
  * **Painikkeet**
    * **Katso säännön tulokset:** Aukaisee uuden ikkunan, jossa voi testata säännön toimintaa.
    * **Tallenna** : Tallentaa tehdyt muutokset poimintasääntöön.
    * **Peruuta** : Sulkee näkymän tallentamatta muutoksia.
    * **Poista** : Poistaa ilmoituksen kokonaan.

![lisäasetukset.png](https://support.nepton.com/hc/article_attachments/32478963293469)
## Poimintasäännön rakenne
Tyypillinen poimintasääntö sisältää seuraavat osat:
  * **SELECT** \- Määrittää, mitä tietoja ilmoitukseen sisällytetään (esim. käyttäjän tunniste, nimi, tapahtumien määrä). Jokaiselle kannattaa antaa alias (**AS**), jotta tieto voidaan käyttää ilmoituksen sähköpostiviestissä.
  * **FROM** ja**JOIN** \- Yhdistää tarvittavat taulut, kuten tapahtumat (`UserEventData`) ja käyttäjät (`UserData`). Lisätietoja voidaan hakea muista tauluista, kuten `UserInfoData`.
  * **WHERE** \- Rajaa mukaan vain tietyt tiedot (esim. hyväksymättömät tapahtumat, tietyt ryhmät).
  * **GROUP BY** \- Ryhmittelee tiedot henkilöittäin tai muulla logiikalla.
  * **HAVING** \- Määrittää ehdon ryhmitellyille tiedoille (esim. tapahtumien määrä > 0).


## Yleisimmät taulut ja kentät
Tässä perustietoa yleisimmistä tiedoista, joita tarvitaan ilmoitusten sääntöjoukkojen rakentamiseen. Kaikki tietokantataulujen sisällöt on kerrottu artikkelissa [**Tietokantataulujen sisältö**](<https://support.nepton.com/hc/fi/articles/360002489257>).
**UserEventData**
  * `ActivityId` – tapahtuman tunniste
  * `StartDatetime` – tapahtuman aloitusaika
  * `isApproved` – hyväksyntästatus (N = ei hyväksytty)


**UserData**
  * `UserId` – henkilön tunniste
  * `firstName`, `lastName` – nimi
  * `UserGroupCode` – henkilöryhmä


**UserSalaryData**
  * `Amount` – arvo sekunteina
  * `CompensationType` – kertoo rivin tyypin (esim. `Accrual` = kertymä)
  * `AccrualType` – kertoo kertymän kohteen (esim. `Balance` = työaikasaldo)
  * `SalaryRenderingDate` – päivämäärä, johon tapahtuma tai kertymä liittyy


## Henkilöryhmä- ja maksuryhmäsuodatus
Ilmoitusten sääntöjoukoissa voidaan rajata kohteet henkilöstöryhmän tai maksuryhmän perusteella. Rajausehdot lisätään **WHERE-osioon** poimintasäännössä, koska ne rajaavat mukaan otettavia rivejä ennen ryhmittelyä. Näiden sääntöjen lisääminen sääntöön luo käyttöliittymään valitsimen henkilöryhmälle tai maksuryhmälle.
### Henkilöryhmäsuodatus
Lisää seuraava ehto sääntöön. Säännön parametri luo Ilmoitus-näkymän käyttöliittymään valinnan, jossa voidaan valita henkilöryhmät.
[code]
    WHERE 
      ued.isApproved = 'N'  -- hyväksymättömät tapahtumat, korvaa omalla rajausehdollasi
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ]
      )  -- henkilöryhmäsuodatus
[/code]
### Maksuryhmäsuodatus
Lisää seuraava ehto sääntöön. Säännön parametri luo Ilmoitus-näkymän käyttöliittymään valinnan maksuryhmille.
[code]
    WHERE 
      ued.isApproved = 'N'  -- hyväksymättömät tapahtumat, korvaa omalla rajausehdollasi
      AND uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL'
      AND uid.Value IN (
        [notificationPersonFilter | {Valitse maksuryhmät} | paymentgroupselect | ]
      )  -- maksuryhmäsuodatus
[/code]
## Valmiiden ilmoitusten muokkaaminen
Valmiiden ilmoitusten poimintasääntöjen yläosassa on kohta, mihin asiakaskohtaiset muokkaukset tulee lisätä. Mikäli näin ei tee, asiakaskohtaiset muokkaukset katoavat, mikäli Nepton päivittää ilmoituksen toimintaa kaikille asiakkaille.
Jos on tarpeen muokata valmiita ilmoituksia laajemmin, tulee luoda muokattava ilmoitus ja kopioida valmiin ilmoituksen sääntö sen pohjaksi.
[code]
    /* --- Add customer-specific notification rules BELOW this line --- */
      
     
    /* --- Add customer-specific notification rules ABOVE this line --- */
[/code]
## Esimerkkejä poimintasäännöistä
### Muokattava ilmoitus: Saldoa yli 40 tuntia
Ilmoitus listaa henkilöt, joiden työaikasaldo ylittää määritetyn raja-arvon ajojakson päättymispäivänä. Saldon arvo poimitaan kertymätiedoista (`AccrualType = Balance`) suoraan ajojakson viimeiseltä päivältä, jolloin ilmoitus näyttää ajantasaisen saldon tilanteen.
  * Poimintasääntö **summaa saldon (Amount)** sekunteina ja muuntaa sen tunneiksi.
  * Viimeisellä rivillä asetetaan **saldoilmoituksen raja-arvo (40 tuntia = 14400 sekuntia)**


[code] 
    SELECT 
      usd.UserId AS 'affectedUserId', 
      -- Ilmoituksen kohteena olevan henkilön tunniste
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      -- Henkilön nimi ilmoitusta varten
      ROUND(
        SUM(usd.Amount) / 3600.0, 
        2
      ) AS 'BalanceHours' -- Lasketaan saldo tunneissa. Amount on sekunteina, joten jaetaan 3600:lla ja pyöristetään kahteen desimaaliin.
    FROM 
      UserSalaryData usd -- Taulu, jossa on tulkitut tapahtumat ja saldotiedot.
      INNER JOIN UserData ud ON ud.UserId = usd.UserId -- Liitetään henkilön perustiedot (nimi, ryhmän koodi)
    WHERE 
      usd.CompensationType = 'Accrual' -- Rajataan kertymäriveihin
      AND usd.AccrualType = 'Balance' -- Valitaan nimenomaan saldokertymä
      AND usd.SalaryRenderingDate = DATE(:ExportPeriodEnd) -- Poimitaan ajojakson viimeisen päivän arvo (snapshot)
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ] 
        ) -- Aktivoidaan ilmoitukseen henkilöryhmäsuodatus, ilmoitus koskee vain valittuja henkilöryhmiä.
    GROUP BY 
      usd.UserId -- Yksi rivi per henkilö
    HAVING 
      SUM(usd.Amount) > 144000 -- Lähetetään ilmoitus, jos saldo ylittää 40 tuntia (144000 sekuntia)
[/code]
### Valmis ilmoitus: Hyväksymättömät tapahtumat henkilöryhmittäin
[code]
    /* --- Update this rule with the latest from the notification integration (unapproved events) template:[Yes] --- */
    
    SELECT 
      ued.userId as 'affectedUserId', 
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      COUNT(ued.ActivityId) AS 'UnapprovedCount' 
     
      /* --- Add customer-specific notification rules BELOW this line --- */
    
      
     
      /* --- Add customer-specific notification rules ABOVE this line --- */
    
    FROM 
      UserEventData ued 
      INNER JOIN UserData ud ON ued.UserId = ud.UserId 
    WHERE 
      ued.isApproved = 'N' 
      AND ud.UserGroupCode IN (
        [notificationPersonFilter | {select_user_groups} | persongroupselect | ]
      ) 
    GROUP BY 
      affectedUserId 
    HAVING 
      UnapprovedCount > 0
[/code]
### Valmis ilmoitus: Hyväksymättömät tapahtumat maksuryhmittäin
[code]
    /* --- Update this rule with the latest from the notification integration (unapproved events) template:[Yes] --- */
    
    SELECT 
      ued.userId as 'affectedUserId', 
      CONCAT(ud.firstName, " ", ud.lastName) AS 'PersonName', 
      COUNT(ued.ActivityId) AS 'UnapprovedCount' 
     
      /* --- Add customer-specific notification rules BELOW this line --- */
    
      
     
      /* --- Add customer-specific notification rules ABOVE this line --- */
    
    FROM 
      UserEventData ued 
      INNER JOIN UserData ud ON ued.UserId = ud.UserId 
      LEFT JOIN UserInfoData uid ON ued.UserId = uid.UserId 
      AND datetime(ued.StartDatetime) BETWEEN uid.ValidFrom 
      AND uid.ValidTo 
    WHERE 
      ued.isApproved = 'N' 
      AND uid.InfoTypeName = 'NeptonPaymentGroupCode_SDSQL' 
      AND uid.Value IN (
        [notificationPersonFilter | {select_groups_of_persons_to_check_for_unapproved_events} | paymentgroupselect | ]
      ) 
    GROUP BY 
      affectedUserId 
    HAVING 
      UnapprovedCount > 0
[/code]
## Säännön tietojen käyttäminen ilmoituksen sähköpostiviestissä
Poimintasäännössä **AS** -aliaksella määriteltyjä tietoja voidaan käyttää viestissä kirjoittamalla ne hakasulkujen väliin Ilmoitus-välilehdellä, kun muokkaat viestin sisältöä. Esimerkiksi näin: `Hei [PersonName], saldosi on [BalanceHours] tuntia.`
Tiedot nimetään **AS** -aliaksella, kuten alla olevassa poimintasäännössä on tehty `'PersonName'` sekä `'BalanceHours'` kohdalla.
![](https://support.nepton.com/hc/article_attachments/32385489454621)
Tämän jälkeen poimintasäännössä määriteltyjä **AS** -aliaksia voidaan käyttää viestissä kirjoittamalla ne hakasulkujen väliin esim. `[PersonName]`, jolloin viestin sisältö päivittyy automaattisesti viimeisimmillä tiedoilla.
![](https://support.nepton.com/hc/article_attachments/32274797644829)
