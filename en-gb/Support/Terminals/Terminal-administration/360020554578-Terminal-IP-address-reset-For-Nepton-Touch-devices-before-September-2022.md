---
id: 360020554578
title: Terminal IP address reset (For Nepton Touch devices before September 2022)
url: https://support.nepton.com/hc/en-gb/articles/360020554578-Terminal-IP-address-reset-For-Nepton-Touch-devices-before-September-2022
locale: en-gb
category: Support
category_id: 360000446658
section: Terminal administration
section_id: 360005942618
section_path:
- Terminals
- Terminal administration
labels: []
promoted: false
updated_at: '2024-08-23T08:51:47Z'
edited_at: '2022-08-16T03:36:24Z'
---

# Terminal IP address reset (For Nepton Touch devices before September 2022)

**Sorry!**
This article has not been translated yet.
Huomioithan, että ohjeet saattaa poiketa hieman päätelaitteen tyypistä riippuen, mutta pääpiirteissään logiikka on kaikissa laitteissa sama. Olethan yhteydessä organisaationne palvelun pääkäyttäjään, mikäli tarvitset lisäapua.
Kiinteän IP-osoitteen määrittämistä varten tarvitaan vähintään seuraavat tiedot: IP-osoite (IP Address), aliverkon peite (Subnet Mask) sekä oletusyhdyskäytävä (Default Gateway).
Työaikapäätteen IP-osoitteen voi muuttaa seuraavasti:
**1\. Jotta laitteen IP-osoite voidaan asettaa uudelleen, tulee ensin poistua kirjausnäkymästä.**
\- Tarkista, että laitteessa on virrat päällä.
\- Paina sormella tai kosketusnäyttökynällä laitteen kosketusnäytön jokaista neljää kulmaa kerran jämäkästi mahdollisimman läheltä reunaa järjestyksessä**vasen yläkulma - oikea yläkulma - oikea alakulma - vasen alakulma.**
\- Näkymän pitäisi poistua ja nyt pitäisi näkyä perinteinen Windows-työpöytänäkymä, jolla on erilaisia kuvakkeita.
**2\. IP-osoitteen****muuttaminen  
****-** Tämä vaihe on helpointa toteuttaa liittämällä erillinen USB-liitännäinen hiiri laitteen USB-porttiin. Määritysten tekeminen onnistuu myös sormella tai joissain laitteissa mukana toimitettavalla kosketusnäyttökynällä (Olink-laitteessa laitteen takareunan oikeassa yläkulmassa sisällä, irtoaa vetämällä ylöspäin).
\- Valitse työpöytänäkymän vasemmasta alareunasta klikkaamalla Windows-kuvake - Settings - Control panel.
**![Terminal_IP_01.png](https://support.nepton.com/hc/article_attachments/360020367078/Terminal_IP_01.png)**
\- Tämän jälkeen valitse Network and Dial-up...
![Terminal_IP_02.png](https://support.nepton.com/hc/article_attachments/360020259937/Terminal_IP_02.png)
\- Seuraavaksi valitse DM9CE1 (Nepton Touch) tai ENET2 (Idesco), voi olla nimeltään myös joku toinen.
![Terminal_IP_03.png](https://support.nepton.com/hc/article_attachments/360020367098/Terminal_IP_03.png)
\- Aukeavasta ikkunasta pääset asettamaan IP-osoitteen (IP Address) sekä aliverkon (Subnet Mask) ja yhdyskäytävän (Default Gateway).
![Terminal_IP_04.png](https://support.nepton.com/hc/article_attachments/360020260017/Terminal_IP_04.png)
\- Seuraavaksi valitse välilehti Name Servers ja määritä sinne tarvittavat tiedot. Lopuksi paina oikean yläkulman OK-nappia.
![Terminal_IP_05.png](https://support.nepton.com/hc/article_attachments/360020260097/Terminal_IP_05.png)
\- Jos määritykset on tehty Idesco-työaikapäätteeseen, täytyy ne vielä tallentaa. Valitse Start-Programs-ColibriTools-SaveReg ja asetukset tallentuvat.
![Idesco_savereg.jpg](https://support.nepton.com/hc/article_attachments/4408956076561/Idesco_savereg.jpg)
**3\. Palaaminen kirjausnäkymään, jotta työaikaa voi taas kirjata.**
\- Sulje kaikki ikkunat ja palaat takaisin Windows-työpöytänäkymään.
\- Kun halutut asetukset on määritelty tulee Terminal Launcher käynnistää uudelleen, jotta työaikaa voi taas kirjata. Työpöytänäkymästä löytyy **Nepton Terminal Launcher -kuvake** , jota tuplaklikkaamalla palvelu käynnistyy. Kun palvelua käynnistetään saattaa se käynnistyä itsestään useamman kerran uudelleen. Tämä on normaalia ja saattaa kestää jopa 10 minuuttia. Odota rauhassa, että palvelu käynnistyy.
![Terminal_IP_06.png](https://support.nepton.com/hc/article_attachments/360020371678/Terminal_IP_06.png)
