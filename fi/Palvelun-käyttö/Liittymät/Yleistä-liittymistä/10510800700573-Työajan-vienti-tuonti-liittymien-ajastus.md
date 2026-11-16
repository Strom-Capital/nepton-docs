---
id: 10510800700573
title: Työajan vienti/tuonti liittymien ajastus
url: https://support.nepton.com/hc/fi/articles/10510800700573-Ty%C3%B6ajan-vienti-tuonti-liittymien-ajastus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä liittymistä
section_id: 360002325398
section_path:
- Liittymät
- Yleistä liittymistä
labels: []
promoted: false
updated_at: '2026-08-14T10:05:38Z'
edited_at: '2025-09-08T12:45:20Z'
---

# Työajan vienti/tuonti liittymien ajastus

Tämä artikkeli koskee liittymiä, jotka löytyvät työaika-osion alta. Muiden osioiden liittymiä (Esim. henkilöiden tuonti työsuhde-osion alla) varten tarkista ko. liittymän ohjeesta, kuinka automaattiset ajastukset toimivat.
## Johdanto
Liittymien ajastusosiossa on mahdollista automatisoida tietojen tuonti tai vienti ulkoisista järjestelmistä tiettyinä päivinä ja aikoina.
Asetukset ajastuksia varten löytyvät Työaikaosiosta Hallinta > Työyhteisön asetukset > Liittymät > Liittymien ajastus. Ajastukset voi määritellä vain työyhteisön tasolle.
Tarkista myös ohje liittymälle, jota olet ajastamassa. Järjestelmä sisältää lukuisia liittymiä, jotka saattavat toimia hieman eri tavalla ja tukea eri ajastusvaihtoehtoja.
## Asetukset
Asetuksiin tulisi asettaa liittymä (sekä sääntöjoukko, mikäli valittu liittymä tukee tätä), jotka haluat ajastaa. On suositeltavaa tallentaa määritykset ennen kuin alat määrittää varsinaisia aikatauluja.
Jos olet tekemässä muutoksia tuleviin ajoihin, on suositeltavaa käyttää asetuksen historiatoimintoa (kalenteri-ikoni), jolloin muutos tulee voimaan vasta halutulla hetkellä.
![](https://support.nepton.com/hc/article_attachments/10920694616605)
**Ajastus voimassa alkaen** on pakollinen kenttä. Päivä ja aika voidaan määrittää nykyhetkeen, jos aikataulun tulee olla heti aktiivinen. Aikataulu voidaan aktivoida myös tulevana ajankohtana. Ajankohta on teknisesti mahdollista asettaa menneisyyteen, mutta aiheuttaa sen, että liittymä suoritetaan myös menneiden päivien osalta (maks. 3 päivää taaksepäin). Tämä ei ole tavanomainen käyttötapaus. Aikavyöhyke Europe/Helsinki.
Kun olet asettanut päiväyksen voimassa alkaen tai voimassa saakka -kenttiin, aseta vielä kellonaika. Ilman kellonaikaa palvelu ei tallenna tietoa. Huomaathan, että ajastusten voimassaoloajat tulee tallentaa erikseen asetussivun alaosasta löytyvästä Tallenna-painikkeesta. 
![](https://support.nepton.com/hc/article_attachments/20721149101469)
**Ajastus voimassa saakka** on vaihtoehtoinen kenttä. Jos kenttä on tyhjä, on ajastus voimassa toistaiseksi. Aikavyöhyke Europe/Helsinki.
**Kuvaus** voidaan vapaasti määrittää ajastukselle. Kuvaus näytetään ajastusten listalla ja se helpottaa tunnistamaan ajastukset.
**Liittymä** on pakollinen kenttä. Tämä määrittää, mitä liittymää käytetään, kun ajastus suoritetaan.
**Poimintasäännöt** antaa määrittää sääntöjoukon, mikäli valittu liittymä tukee sääntöjoukon käyttämistä. Osalle liittymistä on pakko määrittää sääntöjoukko. Jos sääntöjoukko on valittu, niin sääntöjoukon asetukset myös määrittävät palvelimen, jonne tiedot viedään tai jolta tiedot tuodaan.
**Ajastustapa** on joko päivä- tai minuuttiajastus. Myös nämä vaihtoehdot riippuvat valitusta liittymästä, sillä osa liittymistä saattaa tukea vain päivittäistä suoritusta.
**Minuuttiajastuksen sääntö** on käytössä vain minuuttiajastuksella ja on pakollinen jos ko. ajastustapaa käytetään. Kentässä määritetään, monenko minuutin välein suoritus tapahtuu. Suoritus ei voi tapahtua useammin kuin 15 minuutin välein. Taikasauva-ikonia painamalla saa auki työkalun, jolla voi valita valmiita sääntöjä.
**Päivittäisen ajastuksen sääntö** on käytössä vain päiväajastuksella ja se määrittää, minä päivinä suoritus tapahtuu. Taikasauva-ikonia painamalla saa auki työkalun, jolla voi valita valmiita sääntöjä listasta.
**Päivittäinen aloitusaika** on käytössä vain päiväajastuksella ja määrittää kellonajan, jolloin suoritus tapahtuu. Kellonajalle ei ole rajoitteita. On suositeltavaa välttää aikoja, jotka osuvat huoltoajankohtien päälle tai aikoja, jolloin järjestelmä on kuormituksen alla. Tiedot huoltoajankohdista löydät [täältä](<https://support.nepton.com/hc/fi/articles/360006554777>). Aikavyöhyke Europe/Helsinki.
**Tuonnin/viennin aloituspäivän sääntö** ja **Tuonnin/viennin lopetuspäivän sääntö** kentät määrittävät ajanjakson, joka tuodaan tai viedään. Nämä kentät eivät ole käytössä kaikilla liittymillä. Taikasauva-ikonia painamalla saa auki työkalun, jolla voi valita valmiita sääntöjä listasta.
**Lähetä sähköpostiraportti seuraaviin osoitteisiin** Antaa määrittää sähköpostiosoitteet, joihin lähetetään raportti jokaisesta ajastetusta suorituksesta. Voit antaa useamman osoitteen erottelemalla ne pilkulla(,). Suurin osa liittymistä asettaa viedyn/tuodun siirtotiedoston mukaan sähköpostiin. Sähköposti lähetetään riippumatta siitä oliko ajastuksen suoritus onnistunut vai ei. Huom: liittymän tai sääntöjoukon ei ole pakko määrittää palvelinasetuksia ja saat silti sähköpostiraportin.
## Ajastuksen määrittäminen, kun liittymän ajopäivä vaihtelee kuukausien välillä
Mikäli organisaatiollanne on vakioidut liittymän ajopäivät ja ne vaihtelevat kuukausittain, on liittymän ajastus tehtävä poikkeusasetuksella. Poikkeus on tehtävä Päivittäisen ajastuksen sääntö -asetukseen seuraavasti:
Jätä itse asetukseen määritettävä asetusarvo tyhjäksi. Pääset alla olevaan näkymään kalenterikuvakkeen näköisestä voimassaolotoimintopainikkeesta.![](https://support.nepton.com/hc/article_attachments/30173982021917)
Kirjoita Poikkeukset-osion Arvo-kohtaan [DAILY] ja Sääntö-kenttään ne päivät, jolloin ajo on suoritettava. Varmista, että voimassaoloaika on toivomanne jakson, esimerkiksi vuoden, mittainen. Huomioithan myös, että tätä ajastusmallia käytettäessä jokaiselle jaksolle on syötettävä omat ajastuspäivät erikseen. 
![](https://support.nepton.com/hc/article_attachments/30174011612829)
## Viivästyneet tai ajamatta jääneet suoritukset
Joissain tapauksissa voi esiintyä viivästyksiä ennen kuin järjestelmä alkaa suorittaa ajastettua liittymää esim. huoltoajankohdat. Jos liittymä viivästyy, mutta on edelleen päivällä, jolle se oli määritetty ajettavaksi, suoritus pysyy tilassa "Jonossa" ja tulee lopulta suoritetuksi.
Jos liittymää ei voida aloittaa samana päivänä pidentyneiden huoltotoimenpiteiden takia, suoritus näytetään historia taulussa epäonistuneena. Työ voidaan manuaalisesti suorittaa uudestaan, mutta tällöin tulisi varmistaa, että se on kyseisen liittymän kohdalla turvallista. Osa liittymistä saattaa siirtää kaikki tiedot joka suorituskerralla ja osa liittymistä vain aiemman siirron jälkeiset tapahtumat, missä on myös tärkeää että suoritukset tapahtuvat oikeassa järjestyksessä. Lue kohdasta "Ajastuksien aloittaminen tai uudelleen aloittaminen manuaalisesti" lisää tästä.
## Samanaikaisesti suoritettavat liittymät
Saman liittymän suorittaminen useampaan kertaan samanaikaisesti voi tuottaa odottamattomia seurauksia. esim. samojen tiedostojen luku/kirjoitus SFTP-palvelimella. Jos samassa asiakasympäristössä kaksi liittymää yrittää lukea tai kirjoittaa samalle SFTP-palvelimelle yhtä aikaa, järjestelmä odottaa, että ensimmäinen liittymä valmistuu ennen kuin seuraava aloitetaan.
Erilliset liittymät, jotka käyttävät samaa tiedostopalvelinta, tulisi määrittää niin etteivät ne aiheuta ristiriitoja keskenään. Esim. Jos liittymä lukee tiedostoja SFTP-palvelimelta ja toinen kirjoittaa tiedostoja samalle SFTP-palvelimelle, on suositeltavaa, että ne käyttävät eri hakemistoja palvelimella. Eri aloitusaikoihin ei kannata luottaa, sillä toisen suorituksen aloitus saattaa viivästyä, kuten oli kuvattu kohdassa "Viivästyneet tai ajamatta jääneet suoritukset"
## Ajastettujen suoritusten historia ja tila
![](https://support.nepton.com/hc/article_attachments/10720932866461)
Avatussa ajastusosiossa on historiataulu, joka näyttää kaikki aiemmat ajastuksen suoritukset, kaikki käynnissä olevat suoritukset sekä mahdolliset asetusvirheet, jotka aikataulussa tai liittymässä on havaittu.
Suorita nyt -painike mahdollistaa ajastetun liittymän manuaalisen suorituksen (lue kohta "Ajastuksien aloittaminen tai uudelleen aloittaminen manuaalisesti")
Taulu näyttää, milloin valittu ajastus suoritettiin ja oliko sen tulos onnistunut vai epäonnistunut. Useimpien liittymien kohdalla myös viennin/tuonnin siirtotiedosto on saatavilla.
Tila-sarekkeella voi näyttää jotakin seuraavista:
  * "Ajastettu" - Kuvastaa tulevaa ajastusta, joka suoritetaan mainittuna aikana (kts. Ajastettu-sarake).
  * "Jonossa" - Ajastettu työ alkaa heti, kun mahdollista. Viive voi johtua aktiivisesta huoltoikkunasta, useasta saman liittymän työn suorituksesta tai suuresta määrästä saman aloitusajankohdan ajastuksia.
  * "Käynnissä" - Ajastettu työ on parhaillaan käynnissä.
  * "Peruutettu" - Ajastettu työ on peruutettu ja sitä ei suoriteta ajastettuna ajankohtana. Tämä ei vaikuta tuleviin ajastuksiin.
  * "Päättynyt" - Ajastettu työ on päättynyt ja loki saatavilla.
  * "Aloitusaika umpeutunut" - Mikäli työtä ei pystytty aloittamaan ajastettuna ajankohtana, eikä siitä hetkestä tietyn ajan kuluessa, oletetaan sen suorittamisen olevan riskialtista ja käytetään "Aloitusaika umpeutunut" -tilaa.
  * "Aika loppui" - Ajastetun työn suoritus kesti yli 6 tuntia ja on todennäköistä, että suorituksessa on tapahtunut virhe. Tapahtuma merkitään virheelliseksi historianäkymään. Mikäli suoritus on yhä käynnissä ja kestänyt todella kauan, tila ja loki on hyvä tarkastaa myöhemmin uudelleen, kun ne ovat muodostuneet.


Kaikkien automaattisesti suoritettujen liittymien tilan näet myös [palvelulokista](<https://support.nepton.com/hc/fi/articles/360002575478>).
## Ajastuksien aloittaminen tai uudelleen aloittaminen manuaalisesti
Kun ajastus on määritetty, se tullaan suorittamaan automaattisesti. Joissain tapauksissa voi olla tarpeen manuaalisesti suorittaa ajastettu liittymä. Manuaalisessa suorituksessa huomioitavaa:
  * Manuaalisessa suorituksessa käytetään tapahtuman luojana asetuksissa määriteltyä henkilöä, mikäli liittymä tukee tätä toiminnallisuutta. Esim. asetus "Henkilö, joka näytetään tapahtumien luojana" tapahtumien tuonti -liittymässä. Muussa tapauksessa sisäänkirjautunut käyttäjä näytetään tapahtumien luojana.
  * Suorita nyt -painike historiatoiminnoissa suorittaa ajastuksen kuin se olisi ajastettu tapahtuvaksi nykyhetkellä ja asetukset poimitaan sen mukaisesti. Tämä voi aiheuttaa sen, että mikäli liittymä on asetettu poimimaan kahden edellisen päivän tapahtumat, manuaalinen suoritus saattaa poimia eri ajanjakson kuin automaattinen suoritus. 
  * Suorita uudestaan -painike näytetään, kun tarkastelet jonkin aikataulun suoritusta historiataulussa. Toiminnossa on eroja suorita nyt -painikkeeseen. Työ suoritetaan alkuperäisen aikataulun mukaisesti. Tuontiliittymän tapauksessa toiminto myös käyttää samaa tiedostoa, jos sellainen ladattiin aiemman suorituksen aikana. Viennissä tiedosto muodostetaan samalla tavalla.
