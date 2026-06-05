---
id: 360005378238
title: Tapahtuman hyväksynnän määritykset
url: https://support.nepton.com/hc/fi/articles/360005378238-Tapahtuman-hyv%C3%A4ksynn%C3%A4n-m%C3%A4%C3%A4ritykset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumien hallinta
section_id: 360000667978
section_path:
- Tapahtumat
- Tapahtumien hallinta
labels:
- lukko
- hyväksyntä
- voimassaolotoiminto
- hyväksyminen
- projektien hyväksyminen
- lukitus
- lukitseminen
- validity function
- approval
- approving
- approve events
promoted: false
updated_at: '2026-04-02T11:40:09Z'
edited_at: '2026-02-24T08:21:27Z'
---

# Tapahtuman hyväksynnän määritykset

Palvelun **Työaika** -osiossa voidaan työyhteisö- ja asetusryhmätasolla määritellä tapahtumien hyväksymisen yleisiä asetuksia. Määritykset löytyvät valikosta **Työaika > Hallinta > Työyhteisön asetukset/Asetusryhmän asetukset > Työtunnit > Tapahtumien lukitseminen ja hyväksyntä. **
![](https://support.nepton.com/hc/article_attachments/34185876345117)
### Lukitse tapahtumat automaattisesti kun on kulunut
Määrittelee päivät lukittautumaan automaattisesti, kun on kulunut tietty aika. Automaattinen lukitus tehdään aina aamuyöstä.
Esimerkki: "Lukitse tapahtumat automaattisesti kun on kulunut"-asetus on 14pv. Kun eletään päivää 14.2., lukituksi tulee 31.1. Seuraavana päivänä 15.2. lukituksi tulee 1.2. ja niin edelleen.
### Hyväksy kokonaisia päiviä yksittäisten tapahtumien sijaan
Oletuksena palvelussa käsitellään tapahtumien hyväksyntää tapahtumatasolla. Tällä määrityksellä voidaan asettaa hyväksyntä tapahtuvaksi päivätasolla, eli kaikki päivän tapahtumat hyväksytään aina kerralla.
### Kun tapahtuman muokkaaminen poistaa sen hyväksynnän
Mahdollistaa muiden tapahtumien hyväksynnän automaattisen poistamisen, kun tapahtumaa muokataan ja sen hyväksyntä poistuu muokkauksen yhteydessä. Mahdollistaa hyväksynnän perumisen vain henkilöille, joilla on oikeus muokata jo hyväksyttyjä tapahtumia.
Vaihtoehtoina oletusarvo "Se ei vaikuta muihin tapahtumiin", "poista kaikkien saman päivän tapahtumien hyväksyntä" ja "poista kaikkien saman viikon tapahtumien hyväksyntä".
![](https://support.nepton.com/hc/article_attachments/34185876347933)
Huom! Muokatun tapahtuman hyväksyntä poistetaan aina, jos henkilöllä on oikeus muokata tapahtumaa, mutta ei oikeutta hyväksyä sitä.
### Tapahtuman hyväksyntä hyväksyy tapahtumaan liitetyt projektit
Määrittelee, hyväksytäänkö tapahtuman hyväksynnän yhteydessä myös siihen liittyvät projektitunnit. **Poikkeuksena matkalasku. Matkalaskun hyväksyminen hyväksyy** _**aina**_**myös sen projektitunnit.**
### Tapahtuman hyväksynnän poisto poistaa hyväksynnän myös liitetyiltä projekteilta
Määrittelee, poistetaanko tapahtuman hyväksynnän poiston yhteydessä hyväksyntä myös siihen liittyviltä projektitunneilta. **Poikkeuksena matkalasku. Matkalaskun hyväksynnän poisto poistaa hyväksynnän** _**aina**_**myös sen projektitunneilta.**
Huom! Tapahtuman projektituntien hyväksyntä poistetaan aina tapahtuman muokkauksen yhteydessä, ellei tapahtuma pysy hyväksyttynä ja tapahtuman hyväksyntä hyväksy siihen liittyviä projekteja.
### Kaikkien tapahtumaan liitettyjen projektien hyväksyntä hyväksyy tapahtuman
Määrittelee, hyväksytäänkö tapahtuman projektituntien hyväksynnän yhteydessä myös kyseisen tapahtuman tunnit. **Poikkeuksena matkalasku. Matkalaskun projektitunteja ei voi erikseen hyväksyä, vaan matkalaskun hyväksyntä hyväksyy myös sen projektitunnit.**
