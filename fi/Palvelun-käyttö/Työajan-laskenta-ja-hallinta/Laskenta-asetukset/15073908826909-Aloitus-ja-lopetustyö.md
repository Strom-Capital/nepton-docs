---
id: 15073908826909
title: Aloitus- ja lopetustyö
url: https://support.nepton.com/hc/fi/articles/15073908826909-Aloitus-ja-lopetusty%C3%B6
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels: []
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2025-05-23T09:21:24Z'
---

# Aloitus- ja lopetustyö

## Yleiskatsaus
Aloitustyö- ja lopetustyö voidaan ottaa käyttöön, kun käytössä on Neptonin Vuorosuunnittelu- toiminto.
Palvelu voidaan määrittää korvaamaan työntekijälle työaikaa, joka on tehty ennen työvuoron alkamista (Aloitustyö) tai työvuoron loppumisen jälkeen (Lopetustyö).
Aloitustyön tarkoitus on korvata työntekijöille ylimääräinen aika, jonka he käyttävät ennen vuoron varsinaista alkamisaikaa. Joskus tämä kirjataan työnä päätelaitteelta ja joissain tapauksissa työntekijä teki jo töitä ennen kuin pääsi päätelaitteelle kirjaamaan työn alkaneeksi (esim. kaivoksen sisäänkäynti vaatteiden vaihdon jälkeen).
Lopetustyön (ns. puhdistus/siivoustyö) tarkoitus on korvata työntekijöille ylimääräinen aika, jonka he käyttävät vuoron varsinaisen päättymisajan jälkeen. Esimerkiksi jos päätelaitteelta uloskirjaaminen on tehty ennen varsinaista töistä poistumista tai jos työtä on kirjattu tunteja vuoron päättymisen jälkeen.
Esimerkki työviikosta jolla on aloitus- ja lopetustyötä:
![](https://support.nepton.com/hc/article_attachments/19035795746845)
Huom! Jos tapahtumatyypiltä ansaitaan aloitus- tai lopetustyötä, rajataan tapahtumatyypiltä ansaittu aika ennen työvuoron alkua ja työvuoron päättymisen jälkeen aloitus- ja lopetustyön maksimimäärän mukaan. Rajaus tehdään, vaikka sallitut työajat eivät olisi käytössä.
Jos joltain tapahtumatyypiltä ei pitäisi ansaita aloitus- tai lopetustyötä, tämän voi määrittää asetuksissa. On myös mahdollista määrittää, että tapahtumatyypiltä ei ansaita aloitus- tai lopetustyötä tilanteissa kun tapahtumalla on määritetty jokin tietty ylityökohdenne.
## Aloitus- ja lopetustyön määritykset
Aloitus- ja lopetustyö voidaan määrittää joko työyhteisö- tai asetusryhmätasolla **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Aloitus- ja lopetustyö **\- osiossa.
Jotta aloitustyö tai lopetustyö lasketaan, tulee niillä olla asetettuna joko
  * Ansaitsemiseen vaadittava vähimmäismäärä sekä ansaitsemisen enimmäistyömäärä.
  * Kiinteän korvauksen määrä.


### Aloitustyö
![](https://support.nepton.com/hc/article_attachments/26899020856605)
  * **Vähimmäisaika ennen vuoroa, jotta aloitustyötä ansaitaan**  
Aika joka työntekijän on _vähintään_ pitänyt tehdä töitä jotta aloitustyötä ansaitaan. Esim. ylläolevan kuvan määritysten mukaan jos työntekijä on tehnyt töitä 29 minuuttia ennen työvuoron alkamisaikaa, aloitustyötä ei ansaita.
  * **Enimmäisaika, joka voidaan ansaita ennen vuoroa**  
Aika jonka työntekijä voi _enintään_ tehdä töitä niin että siitä ansaitaan aloitustyötä. Esim. ylläolevan kuvan määritysten mukaan jos työntekijä on tehnyt töitä 1h 30min ennen työvuoron alkamisaikaa, aloitustyötä ansaitaan 1 tunti.
  * **Kiinteä korvaus**  
Aloitustyö korvataan kiinteänä korvauksena. Kiinteä korvaus ansaitaan jos 
    * Työntekijä on tehnyt töitä ennen vuoron alkamista _vähintään_ aloitustyön ansaitsemiseen vaadittavan minimimäärän, tai
    * Suurin sallittu vaje vuoron alussa ei ole ylitetty. Jos esimerkiksi suurin sallittu vaje on 30 minuuttia ja työ aloitetaan 15 minuuttia myöhässä, kiinteä kovaus ansaitaan. Jos työntekijä samassa tilanteessa aloittaisi työn 31 minuuttia myöhässä, kiinteää korvausta ei ansaittaisi.
  * **Kiinteä korvaus ansaitaan ilman vuoroa** Jos asetukseen on määritelty kyllä, ansaitaan aloitustöitä kiinteän korvauksen verran myös päivinä, joilla ei ole suunniteltua työvuoroa.**  
**
  * **Suurin sallittu vaje vuoron alussa kiinteän korvauksen ansaintaan**  
Kuinka monta minuuttia myöhässä vuoron voi aloittaa ja silti ansaita aloitustyön kiinteä korvaus.
  * **Ohita tapahtuman ylityön perusosan kohdenne**  
Asettaa ylityön perusosan kohdenteen aloitustyölle, joka ohittaa tapahtumalla olevan kohdenteen.
  * **Ohita tapahtuman ylityön korotusosan kohdenne**  
Asettaa ylityön korotusosan kohdenteen aloitustyölle, joka ohittaa tapahtumalla olevan kohdenteen.
  * **Aloitustyö lyhentää kynnystä 100% viikkoylityön ansaintaan**  
Jos asetus on päällä, ansaittu aloitustyö lyhentää kynnystä 100% viikkoylityön ansaintaan. Jos viikottaisen 50% ylityön maksimimäärä on 8 tuntia ja viikolla on ollut 2 tuntia aloitustyötä, viikottaista 100% ylityötä ansaitaan sen jälkeen kun viikottaista 50% ylityötä on ansaittu 6 tuntia.
  * **Rajattu sallittujen työaikojen mukaan**


**Aloitustyötä ansaitaan tapahtumatyypistä**  
Tässä voit määrittää, miltä tapahtumatyypeiltä ansaitaa aloitustyötä. Oletuksena aloitustyötä ei ansaita miltään tapahtumatyypiltä.
**Aloitustyötä ansaitaan tapahtumatyypistä ja ylityökohdenteesta**  
Tässä voit määrittää, miltä tapahtumatyypin ja ylityökohdenteen yhdistelmät ansaitsevat aloitustyötä. Esimerkiksi:
-Jos "työ" tapahtumatyypiltä tulisi ansaita aloitustyötä muissa tapauksissa paitsi silloin kun tapahtuman ylityön kohdenne on "ylityö - palkkaan", saadaan se aikaisesti yllä olevan kuvan mukaisesti.
-Jos tapahtumatyypiltä tulisi ansaita aloitustyötä vain silloin kun tapahtuman ylityön kohdenteena on "tunti tunnista - palkkaan", tulisi tämä asetus lisätä arvolla "Kyllä".
### Lopetustyö
![](https://support.nepton.com/hc/article_attachments/26899020857245)
  * **Vähimmäisaika vuoron jälkeen, jotta lopettamistyötä ansaitaan**  
Aika joka työntekijän on _vähintään_ pitänyt tehdä töitä vuoron loppumisen jälkeen jotta lopetustyötä ansaitaan. Esim. ylläolevan kuvan määritysten mukaan jos työntekijä on tehnyt töitä 29 minuuttia työvuoron loppumisen jälkeen, lopetustyötä ei ansaita.
  * **Enimmäisaika, joka voidaan ansaita vuoron jälkeen**  
Aika jonka työntekijä voi _enintään_ tehdä töitä niin että siitä ansaitaan lopetustyötä. Esim. ylläolevan kuvan määritysten mukaan jos työntekijä on tehnyt töitä 1h 30min työvuoron loppumisen jälkeen, lopetustyötä ansaitaan 1 tunti.
  * **Suurin sallittu vaje työvuoron lopussa, joka voidaan täyttää**  
Vähimmäisaika työvuoron päättymisen jälkeen joka voidaan täyttää lopetustyöllä. Esim. ylläolevan kuvan määritysten mukaan jos työntekijän työvuoro on 8-16 ja työntekijä kirjaa työn loppuneeksi 15:29, jäljelle jäävää 31 minuuttia ei lasketa lopetustyöksi. Sen sijaan jos työntekijä kirjaa työn loppuneeksi 15:30, jäljelle jäävä 30 minuuttia lasketaan lopetustyöksi.
  * **Kiinteä korvaus**  
Lopetustyö korvataan kiinteänä korvauksena. Kiinteä korvaus ansaitaan jos 
    * Työntekijä on tehnyt töitä vuoron loppumisen jälkeen _vähintään_ lopetustyön ansaitsemiseen vaadittavan minimimäärän, tai
    * Suurin sallittu vaje vuoron lopussa ei ole ylitetty. Jos esimerkiksi suurin sallittu vaje on 30 minuuttia ja työ lopetetaan 15 minuuttia etuajassa, kiinteä kovaus ansaitaan. Jos työntekijä samassa tilanteessa lopettaisi työn 31 minuuttia etuajassa, kiinteää korvausta ei ansaittaisi.
  * **Kiinteä korvaus ansaitaan ilman vuoroa** Jos asetukseen on määritelty kyllä, ansaitaan lopetustöitä kiinteän korvauksen verran myös päivinä, joilla ei ole suunniteltua työvuoroa.
  * **Suurin sallittu vaje vuoron lopussa kiinteän korvauksen ansaintaan**  
Kuinka monta minuuttia etuajassa vuoron voi lopettaa ja silti ansaita lopetustyön kiinteä korvaus.
  * **Ohita tapahtuman ylityön perusosan kohdenne**  
Asettaa ylityön perusosan kohdenteen lopetustyölle, joka ohittaa tapahtumalla olevan kohdenteen.
  * **Ohita tapahtuman ylityön korotusosan kohdenne**  
Asettaa ylityön korotusosan kohdenteen lopetustyölle, joka ohittaa tapahtumalla olevan kohdenteen.
  * **Lopetustyö lyhentää kynnystä 100% viikkoylityön ansaintaan**  
Jos asetus on päällä, ansaittu lopetustyö lyhentää kynnystä 100% viikkoylityön ansaintaan. Jos viikottaisen 50% ylityön maksimimäärä on 8 tuntia ja viikolla on ollut 2 tuntia lopetustyötä, viikottaista 100% ylityötä ansaitaan sen jälkeen kun viikottaista 50% ylityötä on ansaittu 6 tuntia.
  * **Rajattu sallittujen työaikojen mukaan**


**Lopetustyötä ansaitaan tapahtumatyypistä**  
Tässä voit määrittää, miltä tapahtumatyypeiltä ansaitaan lopetustyötä. Oletuksena lopetustyötä ei ansaita miltään tapahtumatyypiltä.
**Lopetustyötä ansaitaan tapahtumatyypistä ja ylityökohdenteesta**  
Tässä voit määrittää, miltä tapahtumatyypin ja ylityökohdenteen yhdistelmät ansaitsevat lopetustyötä. Esimerkiksi:
-Jos "työ" tapahtumatyypiltä tulisi ansaita lopetustyötä muissa tapauksissa paitsi silloin kun tapahtuman ylityön kohdenne on "ylityö - palkkaan", saadaan se aikaisesti yllä olevan kuvan mukaisesti.
-Jos tapahtumatyypiltä tulisi ansaita lopetustyötä vain silloin kun tapahtuman ylityön kohdenteena on "tunti tunnista - palkkaan", tulisi tämä asetus lisätä arvolla "Kyllä".
## Työkorotukset
Aloitus- ja lopetustyöstä voidaan ansaita työkorotusta määrittämällä näille "Kyllä" kohdassa **Työaikahyvitystyypit joista ansaitaan korotusta**.
Työkorotuksen voin määrittää ansaittavaksi joko aloitustyöstä, lopetustyöstä tai molemmista. Määritys löytyy työyhteisötasolla tai asetusryhmätasolla **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Työkorotukset > Työkorotus > Työaikahyvitystyypit joista ansaitaan korotusta** \- osiosta.
## Raportointi
Aloitus- ja lopetustyö lasketaan **Toteutuneen työajan määrä** -raportilla mukaan sarakkeisiin **Työajan veroinen aika yhteensä** ja **Keskimääräinen työajan veroinen aika per viikko**. Lisäksi aloitus- ja lopetustyö näkyvät **Tunnit palkkalajjeittain, tunneittain** raportilla.
