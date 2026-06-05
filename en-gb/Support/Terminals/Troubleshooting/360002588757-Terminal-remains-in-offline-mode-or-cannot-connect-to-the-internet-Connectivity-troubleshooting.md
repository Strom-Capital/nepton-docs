---
id: 360002588757
title: Terminal remains in offline mode, or cannot connect to the internet (Connectivity
  troubleshooting)
url: https://support.nepton.com/hc/en-gb/articles/360002588757-Terminal-remains-in-offline-mode-or-cannot-connect-to-the-internet-Connectivity-troubleshooting
locale: en-gb
category: Support
category_id: 360000446658
section: Troubleshooting
section_id: 360005896337
section_path:
- Terminals
- Troubleshooting
labels:
- NEPTONNEEDSREVIEW
- leimauslaite
- vianselvitys
promoted: false
updated_at: '2024-08-23T08:51:49Z'
edited_at: '2021-10-05T05:47:21Z'
---

# Terminal remains in offline mode, or cannot connect to the internet (Connectivity troubleshooting)

**Whoops!**  
This article has not been translated yet. 
Työaikapäätteet reagoivat verkkoyhteyden vikatilanteisiin välittömästi. Nämä vikatilanteet johtuvat usein hetkellisestä katkosta internet-yhteydessä. Usein nämä katkokset ovat niin lyhytaikaisia, ettei käyttäjä ehdi huomaamaan niitä. Katkosten aikana tehdyt kirjaukset jäävät laitteen muistiin ja ne lähetetään palveluun, kun laite on taas internet-yhteydessä.  
  
**Mikäli verkkoyhteys ei palaudu muutamassa minuutissa on hyvä suorittaa/tarkistaa seuraavat asiat.  
**  
-**Laite on hyvä käynnistää uudelleen.** Ohjeet laitteen uudelleenkäynnistykseen löydät [täältä](<https://support.nepton.com/hc/fi/articles/360002588737>).  
\- **Vilkkuuko päätteen ethernet-portissa valo?** Jos ei, on todennäköistä, että portti tai ethernet-kaapeli on vikaantunut, tai verkkoyhteys ei muusta syystä toimi ko. kaapelilla. Suosittelemme kokeilemaan laitteen yhdistämistä toisella verkkokaapelilla.  
\- **Saako toinen laite (esimerkiksi kannettava tietokone) internet-yhteyden samalla kaapelilla?**
Kannettavalla pitää testata yhteys osoitteeseen:
https://go.nepton.com/TerminalUpdateService/TerminalUpdateService.svc
Jos ko. yhteys toimii, tulee näytölle seuraava sivu:
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4407346444689/mceclip0.png)
Mikäli ko. sivu ei avaudu, vikatilanne johtuu todennäköisesti verkkoyhteydestä.  
  
\--  
  
**Alla on kuvattu menettely tilanteessa, jossa työaikapääte ilmoittaa seuraavaa häiriötä:**_**  
**Windows CE Networking  
_ _DHCP was unable to obtain an IP address. If the netcard is removable,__then you can remove/reinsert it to have DHCP make another attempt to_ _obtain an IP address for it. Otherwise you can statically assign an_ _address._
**1\. Jotta vikatilannetta voidaan korjata, tulee ensin poistua kirjausnäkymästä.**
\- Tarkista, että laitteessa on virrat päällä.
\- Paina sormella tai kosketusnäyttökynällä laitteen kosketusnäytön jokaista neljää kulmaa kerran jämäkästi mahdollisimman läheltä reunaa järjestyksessä**vasen yläkulma - oikea yläkulma - oikea alakulma - vasen alakulma.  
  
2\. Vikatilanteen toteaminen ja ratkaisu  
**  
\- Kun työpöytänäkymä on näkyvissä, näkyy Windowsin työkalupalkin vasemmassa reunassa seuraavanlainen kuvake. Tämä kertoo, että laitteessa ei ole verkkoyhteyttä.  
  
![mceclip0.png](https://support.nepton.com/hc/article_attachments/360004646577/mceclip0.png)  
  
\- Klikkaamalla kuvaketta aukeaa ikkuna, jossa on mahdollista päivittää päätteen käyttämät IP-osoitteet.  
  
![mceclip1.png](https://support.nepton.com/hc/article_attachments/360004711238/mceclip1.png)  
  
Klikkaamalla **Renew** -painiketta pääte hakee uudet IP-osoitteet. Onnistuneen IP-osoitteiden haun pystyy todentamaan sillä, että aiemmassa kuvassa näkyvän verkkoyhteys-kuvakkeen päällä oleva punainen raksi katoaa. Tällöin verkkoyhteys toimii normaalisti.
**3\. Palaaminen kirjausnäkymään, jotta työaikaa voi taas kirjata.  
**
\- Kun halutut asetukset on määritelty tulee Terminal Launcher käynnistää uudelleen, jotta työaikaa voi taas kirjata. Työpöytänäkymästä löytyy **Nepton Terminal Launcher -kuvake** , jota tuplaklikkaamalla palvelu käynnistyy. Kun palvelua käynnistetään saattaa se käynnistyä itsestään useamman kerran uudelleen. Tämä on normaalia ja saattaa kestää jopa 10 minuuttia. Kannattaa odottaa rauhassa, että palvelu käynnistyy.  
  
\- Joissain laiteversioissa Terminal Launcher ei ole työpöydällä, vaan se tulee käynnistää valitsemalla työpöydältä kansio My device. Kansiosta valitaan Storage Card - Release - Työteho (tuplaklikataan). Kirjausnäkymä avautuu automaattisesti ja laite on valmis vastaanottamaan kirjauksia. Tässäkin tapauksessa palvelu saattaa käynnistyä uudelleen useita kertoja ja käynnistyksessä saattaa kestää useita minuutteja.
