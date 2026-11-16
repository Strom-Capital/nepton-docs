---
id: 360004051897
title: Henkilötietojen tuonti - SAP Success Factors
url: https://support.nepton.com/hc/fi/articles/360004051897-Henkil%C3%B6tietojen-tuonti-SAP-Success-Factors
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Järjestelmäkohtaiset henkilötietojen tuonnit
section_id: 7976634441629
section_path:
- Liittymät
- Henkilötiedot
- Järjestelmäkohtaiset henkilötietojen tuonnit
labels: []
promoted: false
updated_at: '2026-10-07T06:11:24Z'
edited_at: '2026-10-07T06:06:12Z'
---

# Henkilötietojen tuonti - SAP Success Factors

Ei pidä sekoittaa samannimiseen [SAP](<https://support.nepton.com/hc/fi/articles/360005404298>)-tuontiin. Tämä tuontitapa on erityisesti suunniteltu SAP Success Factors -lähdejärjestelmälle. Se laajentaa yleisiä tuontisääntöjä erityisellä liiketoimintalogiikalla ja data-tunnisteilla.
Tämä tapa on ensisijaisesti tarkoitettu XML-tiedostomuodolle, eikä siinä siksi ole määritelty sarakkeiden järjestystä. Tämä tekee solmun nimistä pakollisia (tai sarakeotsikoista, jos käytetään muita tiedostotyyppejä kuin XML).
## Kentät
Alla on luettelo erityisistä tunnisteista ja kenttien käyttäytymisestä, jotka liittyvät tähän tuontitapaan. Myös muita henkilötuonnin kenttiä on mahdollista tuoda käyttämällä [tässä artikkelissa](<https://support.nepton.com/hc/fi/articles/360015933397>) listattuja XML kenttä -tunnisteita.
Tunniste | Vastaa Neptonin kenttää | Kuvaus  
---|---|---  
person_id_external | Henkilönumero | Henkilln henkilönumero  
surrogate_id | Käyttäjätunnus | Käyttäjätunnus  
first_name | Etunimi | Etunimi(t)  
last_name | Sukunimi | Sukunimi  
business_email_address | Sähköposti | Sähköposti  
business_phone_number | Puhelin | Puhelinnumero  
emp_start_date | Työsuhteen alkupäivä | Työsuhteen alkamispäivä  
emp_end_date | Työsuhteen loppupäivä | Työsuhteen päättymispäivä  
emp_status | Henkilö poistettu / Tili aktiivinen |  Arvot: A,P,F,U,D - Aktiivinen Arvot: R,S,T,O - Poistettu  
company_code | Yksikkö | Yksikkö  
manager_person_id_external | Ensisijainen esimies | Ensisijainen esimies  
grouping_code segment_code business_area_code department_code business_unit_code team_code group_code sub_team_code | Henkilöryhmän koodikentät |  Käytetään määrittämään käyttäjän henkilöryhmä(t) ja henkilöryhmän hierarkia. Voidaan käyttää mitä tahansa luetelluista kentistä. Lisätietoja löytyy alla olevasta **Henkilöryhmän kentät (koodit ja nimet)** osiosta.  
grouping_name segment_name business_area_name department_name business_unit_name team_name group_name sub_team_name | Henkilöryhmän nimikentät |  Käytetään määrittämään käyttäjän työaikakäyttäjäryhmät ja käyttäjäryhmien hierarkia. Voidaan käyttää mitä tahansa luetelluista kentistä. Lisätietoja löytyy alla olevasta **Henkilöryhmän kentät (koodit ja nimet)** osiosta.  
## Liiketoimintalogiikka
  * **Tuontidata voi sisältää useita käyttäjäelementtejä/rivejä per henkilö**  
Kuitenkin vain yksi tuodaan per tuonti
    * Tuotava elementti/rivi valitaan "emp_status"-kentän arvon perusteella, prioriteetti korkeimmasta alkaen
      * Prioriteetti korkeimmasta matalimpaan: A,P,F,U,D,R,S,T,O
      * Jos useammalla rivillä on sama prioriteetti, valitaan ensimmäinen esiintymä
  * **Työsopimuksen pituuden pidentäminen**  
Tarkemmat tiedot [täällä](<https://support.nepton.com/hc/fi/articles/13129687045789>)


## Henkilöryhmän kentät (koodit ja nimet)
Käytetään henkilön henkilöryhmän asettamiseen ja henkilöryhmähierarkian tuontiin
**Kaksi tapaa tuoda**
  * **Kahden kentän ja putkierottimien käyttäminen**
    * **Koodikenttä** sisältää putkella (|) erotetun listan henkilöryhmien koodeista. Oikeanpuoleisin koodi on henkilön henkilöryhmän koodi ja vasemmalla olevat koodit määrittelevät henkilöryhmähierarkian
    * **Nimikenttä** toimii samalla tavalla kuin koodikenttä, mutta se sisältää henkilöryhmien nimet. Nimikentän käyttö on vapaaehtoista ja se on lisätieto koodeille. Jos määritellään vain koodit, uusilla ryhmillä nimi on sama kuin koodi
    * Esimerkkinä:  
<grouping_code>S1|P1|E1</grouping_code>  
<grouping_name>Suomi|Pääkaupunkiseutu|Espoo</grouping_name>  

  * **Useiden kenttien käyttäminen ilman erotinta**
    * Kenttien järjestys on tärkeä, ei kenttien nimet
    * Viimeisin kenttä on henkilön henkilöryhmän koodi/nimi ja sen edellä olevat kentät määrittelevät henkilöryhmähierarkian
    * Esimerkkinä:  
<grouping_code>Lvl1</grouping_code>  
<grouping_name>Group - Level 1</grouping_name>  
<segment_code>Lvl2</segment_code>  
<segment_name>Group - Level 2</segment_name>  
<business_area_code>Lvl3</business_area_code>  
<business_area_name>Group - Level 3</business_area_name>  
<department_code>Lvl4</department_code>  
<department_name>Group - Level 4</department_name>


  * **Jos tuonnissa määritelty käyttäjäryhmähierarkia ei ole olemassa, se luodaan**
    * Jos tuonnissa ensimmäisenä määritelty vasemmanpuoleista ryhmää ei ole olemassa, se luodaan juureen
      * Tuonnissa ensimmäisen vasemmanpuoleisen ryhmän jälkeen määritellyt ryhmät luodaan sen alle, ellei vastaavia olemassa olevia ryhmiä löydy, jolloin olemassa olevat ryhmät, joilla on jäseniä, siirretään uuteen sijaintiin hierarkiassa
    * Jos tuonnissa määritelty ensimmäinen vasemmanpuoleinen ryhmä on olemassa, tuonnissa määritelty hierarkia luodaan sen alle, jos sitä ei vielä ole
