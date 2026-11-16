---
id: 360010602957
title: Microsoft-kirjautumisen määritys Neptonissa
url: https://support.nepton.com/hc/fi/articles/360010602957-Microsoft-kirjautumisen-m%C3%A4%C3%A4ritys-Neptonissa
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Microsoft-kirjautuminen
section_id: 360002832097
section_path:
- Kirjautuminen
- Kertakirjautuminen (SSO)
- Microsoft-kirjautuminen
labels:
- m365
promoted: false
updated_at: '2026-11-16T06:40:11Z'
edited_at: '2026-11-16T06:37:41Z'
---

# Microsoft-kirjautumisen määritys Neptonissa

Microsoft Azure Active Directory on nyt Microsoft Entra ID
Microsoft-kirjautuminen (Entra ID Single Sign-On) antaa työntekijöille pääsyn Nepton-palveluun organisaation vakiovaltuuksilla ja turvallisuuskäytännöillä. Tämä ohje kuvaa tarpeelliset määritysvaiheet Microsoft SSO:n käyttöönottamiseksi Azuressa. Tämä artikkeli on tarkoitettu organisaatiosi Microsoft Entra ID tai Microsoft 365 -järjestelmänvalvojille.
## Edellytykset
Organisaatiollasi on oltava aktiivinen Microsoft 365 tai Entra ID tilaus. Organisaatiollasi on oltava vähintään yksi vapaa Entra ID sovelluksen rekisteröintipaikka käytettävissä. Kaikki Microsoft 365 asiakkaat saivat vähintään 10 sovelluksen rekisteröintipaikkaa tilauksen alkaessa.
## Nouda kaksi Entra ID arvoa ja talleta ne Neptoniin
Hae kaksi arvoa **Application (client) ID** ja **Secret value** Entra ID palvelusta. Ohjeet nähtävissä [täältä](<https://support.nepton.com/hc/fi/articles/360009872457>)
Mene Työsuhde - Hallinta
Valitse osio Kertakirjautuminen (SSO) - Microsoft Login
Määritä tarvittavat tiedot ja paina Tallenna
  * **Nimi** : Sisäänkirjautumis-nappiin tuleva teksti
  * **Sovellustunnus** : Entra ID palvelusta saatava **Application (client) ID** teksti
  * **Salainen arvo** : Entra ID palvelusta saatava **secret value** teksti
  * Ohje arvojen noutamisesta Entra ID palvelusta on nähtävissä [täältä](<https://support.nepton.com/hc/fi/articles/360009872457>)
  * Varmistathan vielä että käytät **secret value** tekstiä etkä **secret ID** tekstiä


HUOM: Mikäli salaisella arvolla on vanhenemispäivä, tulee sinun ennen vanhenemispäivää aina luoda Entra ID palvelussa uusi secret value ja päivittää tämä secret value myös Neptoniin. Tämä on edellytys Microsoft-kirjautumisen keskeytymättömälle käytölle Neptonissa.
![](https://support.nepton.com/hc/article_attachments/14916316260637)
## Salaisen arvon vaihtaminen
Mikäli Microsoft login on ollut jo käytössä ja salainen arvo halutaan vaihtaa (esimerkiksi salaisen arvon vanhetessa), muuta uusi salainen arvo Microsoft Entra ID -riville painamalla ''Muokkaa'' painiketta, syötä uusi salainen arvo vanhan tilalle ja paina ''Tallenna''.
![](https://support.nepton.com/hc/article_attachments/17683671437213)
## Myönnä oikeudet ja testaa
Ensimmäisellä Microsoft-kirjautumiskerralla sinun täytyy mahdollisesti valtuuttaa SSO sovellus koko organisaatiosi puolesta. Jos näin tapahtuu, erillinen ponnahdusikkuna näytetään ensimmäiselle henkilölle, joka organisaatiostasi kirjautuu sisään.
Jos henkilö on Entra ID pääkäyttäjä, ponnahdusikkuna näyttää allakuvatun kaltaiselta, ja käyttäjä voi välittömästi hyväksyä valtuutuksen koko organisaation puolesta (Consent ja Accept). Tässä ei ikinä tulisi painaa Cancel.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/21078310213917)
Jos henkilö on normaali käyttäjä, hänelle näytetään erilainen ponnahdusikuuna, jossa hänen on mahdollista pyytää lupaa Entra ID pääkäyttäjältä. Tässä tapauksessa on suositeltavaa ottaa yhteyttä suoraan organisaation Entra ID pääkäyttäjään.
Microsoft-kirjautumisen toiminta edellyttää yllä kuvattujen oikeuksien myöntämistä.
Neptonin Microsoft-kirjautuminen (kertakirjautuminen) siirtyy käyttämään ensisijaisena tunnistautumismenetelmänä OpenID Connect (OIDC) v2.0 -päätepistettä, joka korvaa aiemmin käytetyn Microsoft Graph API -integraation.
Muutoksella vastataan Microsoftin tekemiin Conditional Access -käytäntöjen muutoksiin. Aiheesta lisää ohjeessa [Microsoft-kirjautuminen V2](<https://support.nepton.com/hc/fi/articles/40185048819485-Microsoft-kirjautuminen-V2>).
