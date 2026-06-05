---
id: 360014799457
title: Nepton API käyttäjien rajaaminen
url: https://support.nepton.com/hc/fi/articles/360014799457-Nepton-API-k%C3%A4ytt%C3%A4jien-rajaaminen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Sovellusliittymät (API)
section_id: 360000921798
section_path:
- Liittymät
- Sovellusliittymät (API)
labels: []
promoted: false
updated_at: '2025-09-08T07:24:57Z'
edited_at: '2025-09-08T05:01:52Z'
---

# Nepton API käyttäjien rajaaminen

Nepton API:n ominaisuuksia voi oletuksena käyttää kaikki asianmukaisesti tunnistautuneet tunnistetut käyttäjät. Nepton API:n käyttäjiä voidaan halutessa rajata käytön rajaamiseksi tai tietoturvan lisäämiseksi. Käyttäjien rajaaminen on mahdollista IP-osoitteiden perusteella.
Voit ottaa rajoitukset käyttöön kirjautumalla palveluun ja menemällä **Työsuhde > Hallinta > Turvallisuus > Rajaa Nepton API käyttäjiä** ja lisäämällä taulukkoon ne IP-osoitteet joista Nepton API:n käyttö halutaan sallia. Lisää nimi kenttään sallittua / sallittuja IP osoitteita kuvaava nimi, lisää halutessasi huomiot ja aseta API:n käyttöluvan voimassaoloaika. Kun olet määrittänyt sallitut IP-osoitteet, aseta rajoitukset käyttöön painamalla "Salli kutsut Nepton API web service rajapintaan vain alla listatuista IP osoitteista".
Huom. Kenttään "Sallitut IP-osoitteet", voidaan määrittää myös yksittäisten IP-osoitteiden lisäksi joukon IP-osoitteita määrittäviä ilmaisuja. Alla kuvaukset käytössä olevista säännöistä.
**1\. Yksittäinen IP-osoite**
Esim. 83.150.75.169
**2\. IP-osoiteväli**
Esim. 83.150.75.165-83.150.75.175
**3\. IP-osoite korvausmerkillä**
Korvausmerkkiä käytettäessä, seuraavat ilmaisut ovat hyväksyttyjä (numerot voivat olla väliltä 0-255 esimerkeissä). Esim.
83.150.75.*  
83.150.*  
83.*  
*
Esim. 80.150.*.169 ilmaisu ei ole sallittu.
**4\. Yhdistelmä edellä mainittuja ilmaisuja pilkulla erotettuna**
Esim. 83.150.75.169, 83.150.75.180-83.150.75.190, 83.150.78.*, 83.150.90.155
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21082156054685)
