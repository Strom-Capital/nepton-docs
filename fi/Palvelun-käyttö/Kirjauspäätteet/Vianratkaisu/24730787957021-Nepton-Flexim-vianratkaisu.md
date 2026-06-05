---
id: 24730787957021
title: Nepton Flexim vianratkaisu
url: https://support.nepton.com/hc/fi/articles/24730787957021-Nepton-Flexim-vianratkaisu
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Vianratkaisu
section_id: 360005896337
section_path:
- Kirjauspäätteet
- Vianratkaisu
labels: []
promoted: false
updated_at: '2026-04-27T09:46:19Z'
edited_at: '2026-04-27T09:46:19Z'
---

# Nepton Flexim vianratkaisu

Tämä ohje auttaa sinua ratkaisemaan yleisimmät Nepton Flexim ‑kirjauspäätteisiin liittyvät ongelmat nopeasti ja turvallisesti.
### Näin käytät tätä ohjetta
  1. Kohdatessasi vikatilanteen, tunnista ensin, **mikä oire kirjauspäätteessä näkyy**
  2. Noudata kohdan **”Toimi näin”** ohjeita ylhäältä alas
  3. Jos ongelma ei ratkea, ohje kertoo **milloin ja keneen** kannattaa olla yhteydessä


## Kirjauspääte on offline-tilassa (punainen palkki ruudun alareunassa)
**Miltä tämä näyttää?**
Kirjauspäätteen näytön alareunassa näkyy **punainen palkki** , ja kirjauksia ei voi tehdä normaalisti.
> Huom: Pikakirjaustoimintoa voi käyttää myös offline-tilassa.
**Mitä tämä tarkoittaa?**
Kirjauspääte ei saa tällä hetkellä yhteyttä Nepton-palveluun. Usein kyse on **tilapäisestä verkkokatkoksesta** , joka korjaantuu itsestään.
**Toimi näin**
  1. **Odota hetki**
     * Kirjauspääte yrittää automaattisesti muodostaa yhteyden uudelleen.
     * Monesti offline-tila poistuu muutamassa minuutissa.
  2. **Jos yhteys ei palaudu itsestään, testaa verkkoyhteys**
     * Kokeile toimiiko sama verkkoyhteys (käytä samaa kaapelia kuin kirjauspäätteessä) esimerkiksi tietokoneella.
     * Jos käyttämäsi toinen laite ei saa verkkoyhteyttä, kyse voi olla laajemmasta verkkoviasta. Näissä tapauksissa ole yhteydessä oman organisaatiosi IT-tukeen tai tietoliikenteestä vastaavaan tahoon. 
  3. **Jos ongelma jatkuu**
     * Ole yhteydessä organisaatiosi IT-tukeen, esihenkilöösi tai organisaatiosi henkilöstöhallintoon. Jokaisella organisaatiolla on omat käytänteensä tilanteessa toimimiselle, varmista oman organisaatiosi käytänteet esihenkilöltäsi tai henkilöstöhallinnolta. 
  4. **Ohje IT-tuelle ongelmanratkaisuun**
     * Seuraavat toimenpiteet vaativat IT-oikeudet:
       * Jos palomuuri muodostaa HTTPS-yhteydet uudelleen, kirjauspäätteen asetuksissa tulee sallia sertifikaattivirheet. Katso tarkemmat ohjeet tätä toimenpidettä varten [päätteen hallinta-asetuksista ](<https://support.nepton.com/hc/fi/articles/24730505042077>).
       * Mikäli yhteys `time.nepton.com` ‑palvelimeen on hidas, yhteyden aikakatkaisua (REQUESTTIMEOUT) voidaan kasvattaa.
         * Esimerkki: 15000 ms = 15 sekuntia (oletusarvo on 5000 ms)


## Kirjauspääte ei reagoi mihinkään (laite on jumissa)
**Miltä tämä näyttää?**
Kosketusnäyttö ei vastaa painalluksiin eikä laitteella voi tehdä kirjauksia.
**Mitä tämä tarkoittaa?**
Kirjauspääte on käytännössä tietokone, ja kuten muutkin tietokoneet, se voi joskus **jumiutua**.
**Toimi näin – virran katkaisu**
  1. Irrota kirjauspääte seinätelineestä
     * Avaa laitteen alaosassa oleva ruuvi.
  2. Käännä laite niin, että pääset käsiksi virtajohtoon.
  3. Irrota virtajohto laitteesta.
  4. Odota hetki (n. 10–20 sekuntia).
  5. Kytke virtajohto takaisin ja aseta laite paikoilleen.


> Huom: Laite voi olla kytketty joko
>   * yhdellä PoE-kaapelilla (Power over Ethernet) tai
>   * erillisellä virtajohdolla ja verkkokaapelilla
> 

## Kirjauspääte reagoi hitaasti
**Miltä tämä näyttää?**
  * Kirjaukset viivästyvät
  * Näkymien avautuminen kestää tavallista kauemmin


**Mahdolliset syyt**
  * Laitteen ohjelmisto
  * Verkkoyhteyden hitaus


**Toimi näin**
  1. **Käynnistä kirjauspääte uudelleen**
     * Paina päätteen näytöltä **kysymysmerkki (?),** tämän jälkeen pääset alla olevan kuvan mukaiseen näkymään
     * Valitse **Käynnistä uudelleen**
     * Tämä onnistuu ilman hallinta‑PIN‑koodia
     * Käynnistys kestää muutaman minuutin
  2. **Tarkista verkkoyhteys**
     * Testaa verkkoyhteys toisella laitteella samaa verkkokaapelia käyttäen
  3. **Tarkista ohjelmistoversio**
     * Ohjelmistoversio näkyy kysymysmerkin takana olevassa valikossa
     * Ota päätteen versionumero (alla olevassa esimerkkikuvassa 5.1.2) talteen ja toimita se tarvittaessa omalle esihenkilöllesi, IT-tuelle tai organisaatiosi henkilöstöhallintoon. Organisaatiosi Nepton-pääkäyttäjä voi pyytää kirjauspäätteen päivittämistä etäyhteyden avulla Neptonin asiakaspalvelusta.   
  
![](https://support.nepton.com/hc/article_attachments/24888662947613)


## Vikailmoituksen teko - näin nopeutat ja helpotat tilanteen käsittelyä
Jos laite ei lähde tämän artikkelin ohjeiden suorittamisen jälkeenkään toimimaan, seuraa [tätä ](<https://support.nepton.com/hc/fi/articles/360002588797-Vikailmoituksen-teko-ja-tarvittavat-tiedot>)ohjetta välittääksesi oikeat tiedot eteenpäin joko organisaatiosi sisällä tai Neptonin asiakaspalveluun. 
## Ohjeet asiakkaan IT:lle
  * Kirjaudu päätteelle SSH:lla: root / (organisaation määrittämä salasana) 
  * Testaa verkon toiminta 
    * Nimipalvelu: nslookup google.com
    * ![](https://support.nepton.com/hc/article_attachments/24896548209693)
    * Aikapalvelu: date
    * ![](https://support.nepton.com/hc/article_attachments/24896548213533)
    * ntpq -p
    * ![](https://support.nepton.com/hc/article_attachments/24896539116317)
    * Verkko


traceroute -I elisa.fi
traceroute to elisa.fi (195.197.95.175), 30 hops max, 38 byte packets
1 * * *
2 * * *
3 * * *
4 * * *
5 * * *
6 * * *
7 * * *
8 * * *
9 elisa.fi (195.197.95.175) 7.531 ms (246) 7.437 ms (246) 4.281 ms (246)
  * Palvelinyhteys ja kirjautumisongelmat


Lokitiedoista näkee saako palvelin yhteyttä ja mitä kirjautuessa tapahtuu. Lokit voi toimittaa Neptonille tutkintaan
/tmp/ita.log   
/tmp/itaio.log  
/var/local/ita/ita.log.0  
/var/local/ita/itaio.log.0  
/var/local/ita/itaupgrade/itaupgrade.log
``
