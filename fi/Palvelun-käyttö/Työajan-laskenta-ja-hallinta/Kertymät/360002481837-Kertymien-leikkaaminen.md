---
id: 360002481837
title: Kertymien leikkaaminen
url: https://support.nepton.com/hc/fi/articles/360002481837-Kertymien-leikkaaminen
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Kertymät
section_id: 360000705197
section_path:
- Työajan laskenta ja hallinta
- Kertymät
labels:
- liukumarajat
- liukumaraja
- saldonylitys
promoted: false
updated_at: '2025-06-09T08:08:19Z'
edited_at: '2025-06-09T05:53:23Z'
---

# Kertymien leikkaaminen

Kertymän arvon leikkaaminen on tarpeellista, jos kertymän arvon kertymiselle halutaan määritellä maksimi- ja/tai minimimäärä (liukumarajat). Määrittely tehdään Työaika-osiossa joko Työyhteisön tai asetusryhmän asetuksissa. Käytetään esimerkkinä saldo-kertymää (samat asetukset löytyvät jokaisen kertymän alta):
Navigoi kohtaan **Työaika >** **Hallinta > Työyhteisön / Asetusryhmän asetukset > Työtunnit > Kertymät > Laskennan asetukset > Saldo** **> Saldo saa tippua arvoon ja Saldo saa nousta arvoon. **
  
![](https://support.nepton.com/hc/article_attachments/27939626624413)   
Saldon arvon maksimi- ja minimimäärän rajaus tehdään ennen työpäivän saldolaskentaa, jos asetukset on määritelty päivän alussa -kohtaan. Käytännössä rajaus tehdään siis edellisen päivän loppusaldon arvolle.
Mikäli taas arvon maksimi- ja minimimäärän rajaus tehdään koskemaan päivän loppua, tehdään rajaus kyseisen päivän saldolaskennan jälkeen. Tällöin menetetään tieto saldon muutoksesta kyseisenä päivänä, eikä arvoa päivän lopussa pystytä hakemaan esimerkiksi palkka-aineistolle.
## Kertymän leikkaamiselle asetettu tietty päivämäärä
[Voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta voidaan määrittää joustavasti poikkeusasetuksella päivä, jona kertymän arvo leikataan. Tällöin voidaan määritellä, että kertymä leikataan aina tiettynä päivänä, esimerkiksi joka kuun ensimmäinen päivä.
Käytetään taas esimerkkinä saldo-kertymää. Valitse voimassaolotoiminnosta määritys auki. Valitse Lisää asetusarvon poikkeus ja lisää haluamasi arvo ja sääntö-kenttään leikkauksen ajankohta.
Alla esimerkkinä määritys, jonka myötä saldo tulisi aina leikatuksi nollaan tuntiin huhtikuun ensimmäisenä päivänä joka vuosi päivän aluksi:
![](https://support.nepton.com/hc/article_attachments/27939626626589)
Toisena esimerkkinä määritys, jonka myötä saldo tulisi leikatuksi useampana päivänä vuodessa:
![](https://support.nepton.com/hc/article_attachments/27939636266525)
Saldon leikkauksen päivämäärä voidaan määrittää joustavasti erilaisten poikkeussääntöjen avulla. Tarkemmin poikkeussäännöistä ja niiden käytöstä on kerrottu ohjeessa [Poikkeusasetusten määrittely. ](<https://support.nepton.com/hc/fi/articles/360002560677>)
