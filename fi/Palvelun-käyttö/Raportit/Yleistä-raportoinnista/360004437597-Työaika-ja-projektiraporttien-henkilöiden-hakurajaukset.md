---
id: 360004437597
title: Työaika- ja projektiraporttien henkilöiden hakurajaukset
url: https://support.nepton.com/hc/fi/articles/360004437597-Ty%C3%B6aika-ja-projektiraporttien-henkil%C3%B6iden-hakurajaukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä raportoinnista
section_id: 360005870478
section_path:
- Raportit
- Yleistä raportoinnista
labels: []
promoted: false
updated_at: '2026-02-03T06:07:06Z'
edited_at: '2025-04-24T11:49:30Z'
---

# Työaika- ja projektiraporttien henkilöiden hakurajaukset

Kaikissa työaika- ja projektiraporttien sekä integraatioaineistojen henkilövalinnoissa, voidaan käyttää erilaisia henkilöiden valinnan asetuksia rajamaan raporttien sisältämää tietoa.
Henkilöiden rajaus valitaan suoraan avautumasta näkymästä kohdasta **Henkilöt**. Lisärajauksia voidaan tehdä oikeassa yläkulmassa olevan hammasrattaan takaa. Raportin luojalla tulee olla vähintään omien alaisten tapahtumien tarkasteluoikeus, jotta henkilöitä voi rajata.
![](https://support.nepton.com/hc/article_attachments/25691914390941)
## Henkilöiden valinnan asetukset
Kun halutut rajaukset on tehty, valinta vahvistetaan **Tallenna** -painikkeesta. Tällöin henkilölistaus päivittyy rajauksen mukaiseksi.
![](https://support.nepton.com/hc/article_attachments/25691958076061)
## Lataa henkilöt ajanjaksolta
Tällä rajauksella voidaan hakea raportille henkilöitä, joiden työsuhde on päättynyt ennen raportille valittua ajanjaksoa tai heidät halutaan jättää pois raportilta, vaikka työsuhde olisi raportin ajoajanjakson aikana ollut aktiivinen. 
**Esimerkki:** Henkilön työsuhde on asetettu tämän tiedoissa päättyneeksi 15.1.2025. Raportin ajanjakso on 1.2.2025-28.2.2025. Kun**lataa henkilöt ajanjaksolta** -kohtaan otetaan mukaan myös tammikuu, henkilö tulee valittavaksi Henkilöt -osioon vaikka tämän työsuhde ei ole enää helmikuussa aktiivinen. Vastaavasti myös työsuhteensa jo päättäneen henkilön jättäminen pois raportilta onnistuu, vaikka hän olisikin ollut työsuhteessa raportin ajoajanjakson aikana. 
## Ryhmittele
Oletuksena raporttien henkilövalinnat tehdään **henkilöryhmien** perusteella. Vaihtamalla rajaukseksi **Asetusryhmittäin** , henkilövalinnat voidaan tehdä käytännössä työaikamuodon perusteella. Vaihtamalla rajaukseksi **Maksuryhmittäin** , henkilövalinnat voidaan tehdä maksuryhmien perusteella.
**Esimerkki:** Raportointi halutaan kohdistaa liukuvaa työaikaa tekeviin työntekijöihin. Valinta voidaan tehdä tällöin asetusryhmän/ryhmien perusteella. 
## Rajaa esimiehen alaisiin
Henkilövalinnat voidaan rajata vain tietyn esimiehen alaisiin. 
**Esimerkki:** Raportointi halutaan kohdistaa ainoastaan valitun Testi Esihenkilön alaisiin. 
## Rajaa henkilöitä
**Kaikki henkilöt** : Henkilövalintaan tulee valittavaksi kaikki mahdolliset valittavina olevat henkilöt. Ylläpitäjä-oikeustasolla kohdalla tämä tarkoittaa käytännössä kaikkia aktiivisia henkilöitä. Esimies-oikeustasolla puolestaan kaikkia esimiehen alaisia. 
**Kaikki alaiset** : Henkilövalintaan tulee valittavaksi kaikki ne alaiset, joiden ensisijainen tai toissijainen esimies raportin ottaja on. 
**Ensisijaiset alaiset** : Henkilövalintaan tulee valittavaksi vain ne alaiset, joiden ensisijainen esimies raportin ottaja on. 
**Toissijaiset alaiset** _:_ Henkilövalintaan tulee valittavaksi vain ne alaiset, joiden toissijainen esimies raportin ottaja on. 
## Rajaa palkkauksen mukaan
Henkilövalintaan tulee valittavaksi henkilöt, joiden asetusryhmässä on määritetty palkkaustieto **Kuukausipalkka** tai **Tuntipalkka** (asetusryhmän asetuksissa Työtunnit -> TES -> Palkkaus). 
**Esimerkki:** Tunnit palkkalajeittain -raportti halutaan kohdistaa ainoastaan tuntipalkkaisiin työntekijöihin. Työntekijät kuuluvat asetusryhmään, jossa palkkaustieto on määritetty. Henkilövalintaan tulee valittavaksi ainoastaan tämän rajauskriteerin täyttävät henkilöt, ts. tuntipalkkaiset työntekijät.
