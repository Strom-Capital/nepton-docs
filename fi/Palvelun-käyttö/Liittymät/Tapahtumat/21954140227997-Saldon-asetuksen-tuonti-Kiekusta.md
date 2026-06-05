---
id: 21954140227997
title: Saldon asetuksen tuonti Kiekusta
url: https://support.nepton.com/hc/fi/articles/21954140227997-Saldon-asetuksen-tuonti-Kiekusta
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
updated_at: '2024-10-02T06:06:29Z'
edited_at: '2024-10-02T06:05:50Z'
---

# Saldon asetuksen tuonti Kiekusta

Palveluun voidaan tuoda saldon asetukset Kieku-järjestelmästä. Tuotavan tiedoston tulee olla XML-muodossa ja se ladataan SFTP-palvelimelta. Liittymä tukee vain saldon asetuksen tuontia, ei muita kertymiä tai tapahtumatyyppejä.
## Tuonnin asetukset
**Henkilö, joka näytetään tapahtumien luojana** | Käyttäjä, joka merkitään tuotujen tapahtumien luojaksi. **Huom:** tuonnille on hyvä luoda oma ylläpitäjä-käyttäjä joka suorittaa tuonnin. Lisätietoja henkilöstä joka näytetään tapahtumien luojana [täällä](<https://support.nepton.com/hc/fi/articles/4403974690321>).  
---|---  
**Tuontitiedoston nimi** | Palvelimelta haettavan tuontitiedoston nimi  
**SFTP-palvelimen osoite** | Osoite SFTP-palvelimelle josta tiedosto haetaan. Palvelimen tulee pystyä hyväksymään SFTP-yhteyksiä.  
**SFTP-käyttäjätunnus** | Käyttäjätunnus SFTP-palvelimelle kirjautumista varten.  
**Käytä public key -autentikointia** | Jos SFTP-palvelimelle käytetään autentikointia julkisilla avaimilla, asetetaan tähän valinnaksi "Kyllä".   
Lisätietoa public key-autentikoinnista: [https://support.nepton.com/hc/fi/articles/360015591697-Public-key-autentikointi](<https://support.nepton.com/hc/fi/articles/360015591697>).  
**SFTP salasana** | Salasana SFTP-palvelimelle kirjautumista varten.  
**SFTP suhteellisen hakemiston polku** | Hakemistopolku josta tuotavia tiedostoja haetaan. Tämä on suhteellinen suhteessa oletushakemistoon joka avataan kun SFTP-palvelimelle otetaan yhteys, esimerkiksi transfers/to-nepton/  
**SFTP arkistoinnin suhteellisen hakemiston polku** | Kun tuotava tiedosto on käsitelty, se poistetaan noutokansiosta, jotta sitä ei käsitellä enää uudestaan. Suosittelemme arkistoimaan tiedostot asettamalla arkistointikansion, esim. transfers/to-nepton/processed. Tiedostot arkistoidaan päivämäärän mukaan. Jos arkistointia ei oteta käyttöön, tämä kohta jätetään tyhjäksi.  
**Hyväksy tapahtumat tuonnin yhteydessä** | Jos valinnaksi on annettu "Kyllä", tapahtumat hyväksytään tuonnin yhteydessä.  
********
![](https://support.nepton.com/hc/article_attachments/21954180192541)
Jos liittymä löytää henkilöltä aiemman saldoasetuksen samalle päivämäärälle, kuin johon ollaan tuomassa uusi saldoasetus, ei liittymä tee uutta saldoasetusta vaan päivitää vanhan saldoasetuksen uuden määrän mukaisesti. Saldoasetus päivittyy riippumatta siitä, onko sen tehnyt eri käyttäjä kuin käyttäjä joka on asetettu tapahtumien luojaksi.
## Tuontitiedoston rakenne
Saldot | Juurielementti joka sisältää saldotiedot  
---|---  
Yritystunnuskoodi | Yrityksen tunnus, ei käytetä tuonnissa  
SaldoTyyppi | Elementti joka sisältää yhden saldoasetuksen tiedot  
HenkiloNro | Henkilönumero jolle saldon asetus tehdään  
SaldoPvm | Saldon asetuksen päivämäärä muodossa vvvvkkpp. **Huom:** Johtuen erilaisesta merkintätavasta, saldoasetus asetetaan Neptonissa seuraavalle päivälle kuin mitä kentässä asetettu. Esim. 20241001 tarkoittaa että asetus luodaan Neptoniin seuraavalle päivälle 2.10.2024.  
SaldoMaara | Saldon määrä hh:mm, positiivisella saldolla etumerkki + ja negatiivisella saldolla etumerkki -  
## Tuontitiedoston esimerkki
Esimerkki tiedostosta, jolla tuodaan henkilönumerolle 10 saldoksi +10 tuntia päivämäärälle 2.10.204 ja henkilönumerolle 11 saldoksi -5:34 päivämäärälle 3.12.2024.
[code] 
    <Saldot>  
      <YritysTunnusKoodi>1234567</YritysTunnusKoodi>  
      <SaldoTyyppi>  
        <HenkiloNro>10</HenkiloNro>  
        <SaldoPvm>20241001</SaldoPvm>  
        <SaldoMaara>+10:00</SaldoMaara>  
      </SaldoTyyppi>  
      <SaldoTyyppi>  
        <HenkiloNro>11</HenkiloNro>  
        <SaldoPvm>20241202</SaldoPvm>  
        <SaldoMaara>-5:34</SaldoMaara>  
      </SaldoTyyppi>  
    </Saldot>
[/code]
