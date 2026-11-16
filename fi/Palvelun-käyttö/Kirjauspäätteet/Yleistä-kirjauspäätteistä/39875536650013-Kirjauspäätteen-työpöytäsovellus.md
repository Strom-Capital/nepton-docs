---
id: 39875536650013
title: Kirjauspäätteen työpöytäsovellus
url: https://support.nepton.com/hc/fi/articles/39875536650013-Kirjausp%C3%A4%C3%A4tteen-ty%C3%B6p%C3%B6yt%C3%A4sovellus
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleistä kirjauspäätteistä
section_id: 360005942558
section_path:
- Kirjauspäätteet
- Yleistä kirjauspäätteistä
labels: []
promoted: false
updated_at: '2026-10-13T13:13:16Z'
edited_at: '2026-10-13T13:13:16Z'
---

# Kirjauspäätteen työpöytäsovellus

Kirjauspäätteen työpöytäsovellus on erikseen tilattava ja veloitettava tuote. Mikäli organisaationne haluaa ottaa työpöytäsovelluksen käyttöön, olethan ensin yhteydessä palvelun toimittajaasi.  
Kirjauspäätteen työpöytäsovellus on nopea asentaa ja helppo käyttää. Tämä on ratkaisu tapahtumien tallentamiseen minimaalisilla vaatimuksilla ja on tarkoitettu jaetuille laitteille ja/tai ryhmille. Sovelluksen käyttöönotto vaatii PIN-koodin ja/tai RFID-tunnisteen (vaatii ulkoisen RFID-lukijan). Palvelu päivittää sovelluksen automaattisesti ja sallii myös lyhytaikaisen käytön offline-tilassa.
Katso myös: [Kirjauspäätteen käyttöönotto](<https://support.nepton.com/hc/fi/articles/360003461977>) ja [Kirjauspäätemallit](<https://support.nepton.com/hc/fi/articles/360003685277-Kirjausp%C3%A4%C3%A4temallit>)
## Vaatimukset
1\. Asiakasympäristö, jossa on määritetty työpöytäpäätteet käyttöön
2\. Microsoft Windows 7 tai uudempi
3\. Pääsy internetiin
4\. Paikalliset järjestelmänvalvojan oikeudet (tarvitset oikeudet sovelluksen kansioiden luomiseen ja tiedostojen lukemiseen/kirjoittamiseen tähän kansioon)
## Käyttöönotto
  1. Pura toimitettu zip-tiedosto 
  2. Yksi puretun kansion sisällä olevista tiedostoista on sovelluksen käynnistysohjelma TyötehoTerminalLauncher. Kopioi se työpöydälle pikakuvakkeeksi.
  3. Nimen voi muuttaa esimerkiksi NeptonTerminalLauncher
  4. Varmista, että internet yhteys toimii
  5. Käynnistä TyotehoTerminalLauncher.exe
     * Sovellus saattaa pyytää lataamaan .NET Framework 3.5 -sovelluksen. Valitse 'Download and install this feature'.
     * Tuplaklikkaa käynnistysohjelmaa (Launcher), jolloin se lataa uusimman version ja luo kirjauspäätteelle tunnuksen. Ota tunnus talteen.
     * Seuraavaksi sovellus kehottaa ottamaan yhteyttä palveluntarjoajaan tai määrittämään laitteen asiakasympäristöösi itse. Laite määritetään palveluun kirjautumisen jälkeen valikossa **Työsuhde - > Hallinta -> Kirjauspäätteet -> Lisää**. Kirjoita **Päätteen tunnus** -kohtaan talteenottamasi tunnus (ID) ja paina **Tallenna**.
     * Kun yhteys ympäristöön on muodostettu, kirjauspäätteen asetukset ladataan automaattisesti
  6. Käyttäjille on annettava PIN-koodi ja/tai RFID-tunniste ennen päätelaitteen käyttöä. Nämä tiedot on tallennettava heidän [henkilökohtaisiin tietoihinsa](<https://support.nepton.com/hc/fi/articles/360002425517-RFID-tunnisteen-lis%C3%A4%C3%A4minen-henkil%C3%B6lle>) Työsuhde-osiossa.
  7. Jos käytetään RFID-tunnisteita tunnistatumiseen, olethan yhteydessä asiakaspalveluun.
  8. Kirjauspääte on nyt käyttövalmis kohdassa 2 luomastasi pikakuvakkeesta
  9. Sovellus käynnistyy koko ruudun -tilassa. Jos haluat, että sovellus käynnistyy pienempään ikkunaan tai haluat muuttaa muita asetuksia, olethan yhteydessä asiakaspalveluun.
  10. Sovellus voidaan sammuttaa klikkaamalla hiiren osoittimella kaikkia neljää kulmaa näytöllä alkaen vasemmasta yläkulmasta, oikea yläkulma, oikea alakulma ja vasen alakulma. Nyt sovelluksen pitäisi sammua ja sinulla tulisi olla Windowsin työpöytänäkymä.


**Huomaathan:** Tuntemattomat RFID-tunnisteet sallivat kirjautumisen ja tapahtumien tallentamisen ennen kuin tunniste on määritetty tietylle henkilölle. Tallennetut tiedot kohdennetaan henkilöön, kun RFID-tunnisteen numero lisätään kyseisen henkilön tietoihin Työsuhde-osiossa.
Jos RFID-lukijan alustus epäonnistui, kyse on mahdollisesti COM portin määrityksistä, ota yhteyttä asiakaspalveluumme.
