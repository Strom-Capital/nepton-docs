---
id: 360002559178
title: Laskenta-asetusten hierarkia
url: https://support.nepton.com/hc/fi/articles/360002559178-Laskenta-asetusten-hierarkia
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- NEPTONNEEDSREVIEW
- hierarkiatasot
- asetushierarkia
- periytyminen
- periminen
promoted: false
updated_at: '2026-04-01T07:09:15Z'
edited_at: '2026-04-01T07:09:14Z'
---

# Laskenta-asetusten hierarkia

Asetukset on luotu palveluun eri asetustasojen mukaan niin, että asetustasoilla on hierarkia, jonka mukaan asetukset periytyvät ylhäältä alaspäin. Alkuasetukset tehdään jo käyttöönoton aikana valmiiksi, eli ne on kustomoitu omalle työyhteisöllenne ja niitä tarvitsee muuttaa vain tarvittaessa.
Hierarkia ja asetusten periytyminen tasojen mukaan on kuvattu alla. Periytymisen voi tarvittaessa myös estää.
## Työyhteisön asetukset
Kaikkia käyttäjiä koskevat, työyhteisön yleisimmin noudatetut säännöt, ns. ylin taso. Työyhteisön asetukset löytyvät **Työaika > Hallinta > Työyhteisön asetukset**.
## Asetusryhmän asetukset
Asetusryhmää koskevat asetukset, joilla voidaan tehdä poikkeuksia työyhteisön asetuksiin. Asetusryhmät tehdään usein esim. käytettävien TESsien mukaan, jolloin jokaisessa asetusryhmässä on TESin mukaiset asetukset. Lisäksi usein tehdään yksi ylätason asetusryhmä, esimerkiksi 'Finland', johon voi määrittää koko työyhteisöä koskevia asetuksia sen sijaan, että nämä määritykset tehtäisiin suoraan työyhteisötasolla.
Asetusryhmät löytyvät valikosta **Työaika > Hallinta > Asetusryhmät**.
Asetusryhmään tehdyt asetukset koskevat kaikkia sen jäseniä, ellei heillä ole alemmalla tasolla (käyttäjän asetuksissa) poikkeavia asetuksia.
Asetukset periytyvät ylemmältä asetusryhmätasolta alemmalle asetusryhmälle, ellei alemmalla tasolla olla toisin määritelty. Asetusryhmähierarkia esitetään asetusryhmälistauksessa niin, että alemmat asetusryhmät on sisennetty ylemmän alle. Esimerkkikuvassa ylimpänä on Finland-tason asetusryhmä ja sen alla on asetusryhmätaso "7,5h kuukausipalkkainen, tunti-tunnista saldoon" ja sen alla asetusryhmä kolme eri osa-aikaisten asetusryhmää. 
![](https://support.nepton.com/hc/article_attachments/28384939623197)
Kuvan esimerkissä asetukset valuvat ylemmästä asetusryhmästä kaikkiin osa-aika -ryhmiin, ellei näissä asetusryhmissä olla määritelty poikkeavia asetuksia. Asetusryhmä "8h kuukausipalkkainen ma-su" on taas saman tasoinen kuin "7,5h kuukausipalkkainen, tunti-tunnista saldoon" sekä listan loput asetusryhmät, joten niistä ei periydy asetuksia toisiinsa, vaan näiden kaikkien asetusryhmän ylempi taso on Finland, jonka ylätaso taas on Työyhteisö.
## Käyttäjän asetukset
Yksittäisten käyttäjien taakse ei suositella tehtävän asetuksia, sillä asetusten hallinta menee hankalaksi, mitä enemmän niitä on ripoteltu. Pääosin kaikkien asetusten tulisi tulla henkilön asetusryhmästä. Vain tiettyä käyttäjää koskevat poikkeussäännöt, esimerkiksi työsuhteen alussa oleva pienempi vuosilomakertymä tai väliaikaisesti sovittu lyhyempi työvelvoite voidaan asettaa henkilön taakse käyttäen [voimassaolotoimintoa](<https://support.nepton.com/hc/fi/articles/360002559358>). Käyttäjän asetukset löytyvät **Työaika > Hallinta > Henkilöt > Toiminto: Henkilön asetukset.**
Asetusten periytyminen yllä kuvatun hierarkian mukaisesti toimii käytännössä niin, että kun palvelu tarkastaa asetuksia se etsii ensin, löytyykö asetusta käyttäjätasolta. Jos asetusta ei ole määritelty käyttäjätasolle, palvelu siirtyy etsimään sitä asetusryhmätasolta. Jos asetusta ei ole asetusryhmätasoltakaan, käytetty asetus tulee työyhteisötasolta.
## Periytymisen estäminen
Periytymisen voi estää asetuksesta riippuen monella eri tavalla.
  * "Käytössä" -asetus: Joillain asetuksilla on "käytössä"-asetus. Tällä voidaan estää ylemmältä tasolta periytyvät asetukset määrittämällä asetusryhmään halutun asetuksen kenttään "Käytössä: Ei". Esimerkkinä: Ylemmällä asetusryhmätasolla on käytössä sallitut työajat, mutta niiden ei haluta olevan voimassa alemmalla asetusryhmätasolla. Tällöin alemmalle asetusryhmätasolle voidaan määrittää, että ne eivät ole käytössä kyseisellä asetusryhmätasolla.  
![](https://support.nepton.com/hc/article_attachments/29753748417309)
  * Joillain asetuksilla on valinta "Älä käytä ylemmän tason ryhmän asetusta":![](https://support.nepton.com/hc/article_attachments/29753719177501)
  * Tekstikenttämuotoisen asetuksen periytyminen voidaan estää tallentamalla tyhjä arvo kyseisen kentän otsikkoon. Esimerkiksi jos halutaan estää työkorotuksen nimen periytyminen alemmalle tasolle, voidaan nimikenttään kirjoittaa alemmalle tasolle joku toinen teksti, tai tallentaa tyhjä kenttä:  
![](https://support.nepton.com/hc/article_attachments/29753748419357)
Poikkeuksena integraation sääntöjoukot (Liittymät), joissa periytyminen estetään tallentamalla tyhjä arvo kaikkiin kolmeen kenttään: Kuvaus, palkkalajikoodi ja poimintasääntö.
  * Numeeristen kenttien periytyminen voidaan estää painamalla kenttään ilmestyvää ruksi-kuvaketta. Esimerkiksi työpäivän pituuden periytyminen voidaan estää tällä tavoin. Kuvan esimerkissä näkyy maanantain kohdalla ruksi, jota painamalla periytyminen estetään. Torstaina näkyy miltä asetus näyttää, kun periytyminen on estetty.![](https://support.nepton.com/hc/article_attachments/29753748420253)


Huom: Muistathan tehdä aina kaikki asetukset [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
Jos periytyminen estetään, käytetään asetuksessa arvoa, joka on palvelussa oletusarvona. Oletusarvo riippuu siitä mikä kenttä on kyseessä. Oletusarvo voi olla numeerinen arvo (esimerkiksi työpäivän pituus on oletuksena 0 tuntia, jos muuta ei ole määritelty) tai se voi tarkoittaa, että ko. määritys ei ole lainkaan voimassa. Useat oletusarvot ovat työaikalain mukaisia. HUOM: Oletusarvo ei aina välttämättä ole 0.
## Poikkeusasetusten periytyminen
Mikäli ylätasolle on tehty asetus ja sille on tehty poikkeusasetus, periytyvät nämä kumpikin alaspäin seuraaville tasoille. Periytyminen jatkuu niin pitkään, kunnes jollekin tasolle on asetukseen tallennettu jotain muuta - siis jos pääasetukseen tallennetaan jotain, katkeaa periytyminen, eikä pelkkä poikkeusasetus periydy. Periytyminen jatkuu vain niin kauan, kun alatasolle ei olla samassa asetuksessa tallennettu mitään.
Mikäli ylätasolle on tehty pelkkä poikkeusasetus, periytyy tämä alaspäin. Jos alatasolle on tehty myös poikkeusasetus, tämä ei estä ylätason poikkeuksen periytymistä, vaan alatasolla on voimassa kumpikin poikkeus (sekä periytyvä että itse asetusryhmätasolle tehty asetus). Periytyminen voidaan estää vain antamalla pääasetukselle jokin arvo, tai kumoamalla ylätasolta tuleva poikkeus laittamalla alatasolle sama poikkeus eri arvolla.
