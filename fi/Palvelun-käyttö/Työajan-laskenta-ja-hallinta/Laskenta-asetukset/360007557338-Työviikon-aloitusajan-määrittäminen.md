---
id: 360007557338
title: Työviikon aloitusajan määrittäminen
url: https://support.nepton.com/hc/fi/articles/360007557338-Ty%C3%B6viikon-aloitusajan-m%C3%A4%C3%A4ritt%C3%A4minen
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
updated_at: '2026-04-14T07:00:14Z'
edited_at: '2026-04-14T06:09:10Z'
---

# Työviikon aloitusajan määrittäminen

Palvelussa voidaan määritellä haluttu työviikon aloitusaika. Työviikon aloituspäivä ja aloitusaika voi vaikuttaa [työkorotusten ](<https://support.nepton.com/hc/fi/articles/360002560978>)ja [viikkolepokorvauksen](<https://support.nepton.com/hc/fi/articles/360007389978>) maksuun tai [ylitöiden käsittelyyn](<https://support.nepton.com/hc/fi/articles/360002481617>).
Asetus löytyy valikosta **Työaika** > **Hallinta** > **Työyhteisön asetukset / Asetusryhmät** > **Työtunnit > TES.**
**Työviikon aloituspäivä** -asetus määrittää, minä viikonpäivänä työviikko katsotaan alkavan. Jos arvoa ei ole asetettu, oletusarvo on maanantai.
**Työviikon aloitusaika** -asetus määrittää, mihin kellonaikaan työviikon katsotaan alkavan. Määritys kertoo myös mihin aikaan vuorokausi laskennallisesti vaihtuu.
**![mceclip1.png](https://support.nepton.com/hc/article_attachments/4410478851985)**
Jos Työviikon aloitusaika -kenttään määritelty arvo on '00:00' alkaa työviikko ja jokainen työviikon päivä aina klo 00:00. Tällöin kukin vuorokausi katsotaan alkavaksi klo 00:00 ja päättyväksi klo 24:00.
Maanantai 00:00 – 24:00
Tiistai 00:00 – 24:00
Keskiviikko 00:00 – 24:00
Torstai 00:00 – 24:00
Perjantai 00:00 – 24:00
Lauantai 00:00 – 24:00
Sunnuntai 00:00 – 24:00
= 1 viikko
Jos taas työviikon aloitusaika -kenttään on määritelty arvoksi esimerkiksi '07:00', niin laskenta katsotaan seuraavasti:
Maanantai 07:00 – 07:00 (tiistaiaamuna)
Tiistai 07:00 – 07:00 (keskiviikkoaamuna)
Keskiviikko 07:00 – 07:00 (torstaiaamuna)
Torstai 07:00 – 07:00 (perjantaiaamuna)
Perjantai 07:00 – 07:00 (lauantaiaamuna)
Lauantai 07:00 – 07:00 (sunnuntaiaamuna)
Sunnuntai 07:00 – 07:00 (maanantaiaamuna)
= 1 viikko
Riippuen alkaako päivä ennen vai jälkeen puolen päivän (12:00), vaikuttaa myös viikon/päivän alkamisajankohtaan.
Esimerkiksi, jos viikko alkaa sunnuntaina klo 22:00:
  * Viikon ensimmäinen päivä on maanantaina/seuraavana päivänä (koska viikon alkamisaika on asetettu puolen päivän jälkeen), mutta maanantaipäivä alkaa sunnuntaina klo 22:00 ja päättyy maanantaina klo 22:00.
  * Viikon seuraava päivä on tiistai, mutta se alkaa maanantaina klo 22:00 ja päättyy tiistaina klo 22:00. Ja niin edelleen...
  * Työvuorot, jotka alkavat sunnuntaina klo 23:00, näytetään ja lasketaan työaikakalenterissa maanantain kohdalla, alkavan viikon vuorona.
  * Työvuorot, jotka alkavat sunnuntaina ennen klo 22:00, näytetään ja lasketaan työaikakalenterissa sunnuntain kohdalla, päättyvän viikon vuorona.


Esimerkiksi, jos viikko alkaa sunnuntaina klo 04:00:
  * Viikon ensimmäinen päivä on sunnuntaina/samana päivänä (koska viikon alkamisaika on asetettu ennen puolta päivää), jolloin sunnuntaipäivä alkaa sunnuntaina klo 04:00 ja päättyy maanantaina klo 04:00.
  * Viikon seuraava päivä on maanantaina, joka alkaa maanantaina klo 04:00 ja päättyy tiistaina klo 04:00. Ja niin edelleen...
  * Työvuorot, jotka alkavat sunnuntaina ennen klo 04:00, näytetään ja lasketaan työaikakalenterissa lauantain kohdalla, päättyvän viikon vuorona.
  * Työvuorot, jotka alkavat sunnuntaina klo 04:00 jälkeen, näytetään ja lasketaan työaikakalenterissa sunnuntain kohdalla, alkavan viikon vuorona.
  * Työvuorot, jotka alkavat maanantaina ennen klo 04:00, näytetään ja lasketaan työaikakalenterissa sunnuntaina kohdalla, jne.
