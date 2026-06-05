---
id: 21954560152477
title: Kieku tapahtumien vienti
url: https://support.nepton.com/hc/fi/articles/21954560152477-Kieku-tapahtumien-vienti
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtumat
section_id: 360001061298
section_path:
- Liittymät
- Tapahtumat
labels: []
promoted: false
updated_at: '2024-10-02T06:47:39Z'
edited_at: '2024-10-02T06:47:38Z'
---

# Kieku tapahtumien vienti

Neptonista voidaan viedä tapahtumia Kieku-järjestelmään vakiomuotoisella liittymällä.
## Tapahtumien vientimuoto
Kieku käsittelee työtapahtumia erilailla kuin Nepton. Neptonissa tapahtumat ovat tietyllä tapahtumatyypillä ja niillä on alku- ja loppuaika. Kiekussa tapahtumat ovat joko aloitus- tai lopetustapahtumia yhdellä ajalla.
Nepton tekee tätä varten muunnoksia. Esimerkiksi seuraavat Neptoniin kirjatut tapahtumat:
  * 08:00 - 13:00 Työ
  * 13:00 - 14:00 Koulutus
  * 14:00 - 16:00 Työ


Muutetaan seuraavaan muotoon, jonka Kieku ymmärtää:
  * 08:00 Aloitus (ei syykoodia)
  * 13:00 Lopetus (koulutus)
  * 14:00 Aloitus (ei syykoodia)
  * 16:00 Lopetus (ei syykoodia)


## Määrittäminen
### Henkilöiden tunnusten määrittäminen
Kieku käyttää henkilön tunnisteena joko Kieku-kenttään tallennettua tunnistetta, tai henkilötunnusta, mikäli Kieku-tunnustetta ei olla tallennettu henkilön tietoihin. Kieku-tunniste sekä henkilön henkilönumero voidaan määrittää muokkaamalla henkilötietoja Työsuhde > Henkilön tiedot -näkymässä, Tunnisteet -osiossa.
![](https://support.nepton.com/hc/article_attachments/21954574052253)
### Tapahtumatyyppien koodien ja käyttäytymisen määrittäminen
Nämä voidaan määritellä Kiekuliittymän asetuksista: Työaika > Hallinta > Työyhteisön asetukset > Liittymät > Tapahtumat: Kieku (vienti).
![](https://support.nepton.com/hc/article_attachments/21968559868957)
Kaikille tapahtumatyypeille voi määrittää seuraavat tiedot:
  * **Tapahtumatyypin syykoodi** \- Kieku käyttää tätä tunnistamaan, mistä tapahtumasta on kyse
  * **Käsittele tapahtumatyyppi** \- Onko tapahtumatyypillä kirjattu tapahtuman alku joko sisään (aloitus) vai ulos (lopetus) leimaus. Asetuksen alla kerrotaan, mikä on tapahtumatyypin oletuskäsittelytapa, jos asetusta ei ole asetettu.
  * **Käsittele tapahtumatyyppi ylityönä** \- Onko tapahtuma ylityötä vai ei. Tämä asetus on asetettavissa vain työtä vastaaville tapahtumille, sitä ei esimerkiksi voi asettaa poissaoloille.


Oletuksena kaikki tapahtumatyypit viedään vaikka niille ei olisi määritetty syykoodia. Jos halutaan että tiettyä tapahtumatyyppiä ei viedä, sen syykoodiksi määritetään 0.
### Viennin asetukset
Nepton luo määritysten mukaan Kiekuun sisäänluettavan tiedoston, joka viedään SFTP-palvelimelle [ajastetusti](<https://support.nepton.com/hc/fi/articles/10510800700573>) tai manuaalisesti vastaanottavan järjestelmän noudettavaksi. Siirtoa varten tulee täyttää Viennin asetukset -kenttiin tarvittavat tiedot.
![](https://support.nepton.com/hc/article_attachments/21968584020381)
## Vientitiedoston rakenne
**Tyoaikakirjaukset** | Juurielementti joka sisältää leimaustapahtumat  
---|---  
**TyoaikakirjausTyyppi** | Elementti joka sisältää yksittäisen leimaustapahtuman  
**Leimaustapahtumakoodi** | Leimaustapahtuman koodi, 001 = Sisään, 002 = Ulos  
**HenkiloNro** | Henkilön tunniste  
**LeimausHetki** | Leimauksen hetki  
**Syykoodi** | Leimauksen syykoodi  
**YksikkoKoodi** | Yksikön koodi, viedään tyhjänä  
**LahdeKoodi** | Lähteen koodi, käytetään asetuksen ”Kieku lähdekoodi” arvoa  
### Vientitiedoston esimerkki
[code] 
    <?xml version="1.0" encoding="utf-8"?>  
    <Tyoaikakirjaukset xmlns="http://www.kiekuhanke.fi/kieku/tyoaikakirjaukset">  
        <TyoaikakirjausTyyppi xmlns="">  
            <LeimaustapahtumaKoodi>001</LeimaustapahtumaKoodi>  
            <HenkiloNro>1</HenkiloNro>  
            <LeimausHetki>04-10-2024 08:00:00</LeimausHetki>  
            <SyyKoodi>1234</SyyKoodi>  
            <YksikkoKoodi/>  
            <LahdeKoodi>ABC</LahdeKoodi>  
        </TyoaikakirjausTyyppi>  
        <TyoaikakirjausTyyppi xmlns="">  
            <LeimaustapahtumaKoodi>002</LeimaustapahtumaKoodi>  
            <HenkiloNro>1</HenkiloNro>  
            <LeimausHetki>04-10-2024 16:00:00</LeimausHetki>  
            <SyyKoodi>1234</SyyKoodi>  
            <YksikkoKoodi/>  
            <LahdeKoodi>ABC</LahdeKoodi>  
        </TyoaikakirjausTyyppi>  
    </Tyoaikakirjaukset>
[/code]
