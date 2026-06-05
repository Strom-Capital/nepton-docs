---
id: 360002562658
title: Projektikohdistuksen asetukset
url: https://support.nepton.com/hc/fi/articles/360002562658-Projektikohdistuksen-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Projektihallinta
section_id: 360000707398
section_path:
- Projektihallinta
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-05-22T07:34:17Z'
edited_at: '2026-05-21T05:13:24Z'
---

# Projektikohdistuksen asetukset

Projektien asetuksia voidaan määritellä sekä **Työyhteisö** -tasolla että **Asetusryhmät** -tasolla.
## Asetukset Työyhteisö-tasolla
### Projektit
Työyhteisö-tasolla projektien asetukset löytyvät valikosta **Työaika > Hallinta > Työyhteisön asetukset > Projektit.**
![](https://support.nepton.com/hc/article_attachments/36216427134237)
**Palvelu käytössä** \- Määrittää, onko projekteille kohdistaminen käytössä. Kun palvelu otetaan käyttöön, Projektit-valikko tulee näkyviin Työaika-osioon.
**Monta tasoa yläprojekteja sisällytetään projektin nimeen** \- Kuinka monta tasoa yläprojekteja sisällytetään projektin nimeen. Jos arvona on esimerkiksi 2, näytetään projektin yläprojektin ja yläprojektin yläprojektin nimi.  
Alla esimerkki siitä, miten yksi yläprojekti näytettäisiin:
![](https://support.nepton.com/hc/article_attachments/19188820800029)
**Näytä projektin kuvaus työajan tapahtumissa** \- Projektille annettu kuvaus näkyy sekä tapahtuman kirjauksessa, että Projektin tiedot -ikkunassa, kun tapahtuma avataan tarkasteltavaksi.
**Sisällytä projektin koodi projektin nimeen** \- Yli- ja aliprojektien koodit näkyvät projektien nimien etuliitteenä seuraavasti:
![](https://support.nepton.com/hc/article_attachments/19188835928349)
**Näytä tapahtuman kirjauksessa ainoastaan projektit jotka on kohdistettu kyseiselle henkilölle** \- Käyttäjä näkee tapahtumaa kirjatessaan vain häneen tai hänen käyttäjäryhmäänsä liittyvät projektit. Ohje: [Näin lisäät projektin henkilölle tai henkilöryhmälle](<https://support.nepton.com/hc/fi/articles/360006776758>).
  * Mikäli asetuksen arvona on "Ei", käyttäjä näkee tapahtumaa kirjatessaan kaikki työyhteisön projektit, jos projekteja on yhteensä 50 tai alle. Jos projekteja on yli 50, näytetään viimeksi käytetyt.
  * Oletusprojektiksi voi asettaa vain henkilöön tai henkilöryhmään liitetyn projektin. Ohje: [Henkilön oletusprojektin asettaminen](<https://support.nepton.com/hc/fi/articles/360002563098>).


**Lopeta aktiiviset projektit työaikapäätteeltä uloskirjauduttaessa** \- Projekti lopetetaan kirjauduttaessa työaikapäätteeltä ulos, jolloin sama projekti ei jatku automaattisesti enää seuraavan sisäänkirjautumisen jälkeen. Mikäli tässä asetuksessa on "Ei", jatkuu seuraavassa kirjauksessa joko oletusprojekti tai viimeisessä kirjauksessa ollut projekti, huolimatta siitä kuka kirjauksen on tehnyt ja onko se tehty päätteellä vai muuta kautta.
**Kohdista tapahtumakirjaus suunnitellun työvuoron projektiin** \- Kohdistetaanko työ suunnitellun työvuoron projektiin vai ei. Jos asetuksen arvona on "ei", käytetään henkilön oletusprojektia.
**Kuinka lähellä suunniteltua vuoroa tapahtumakirjauksen on oltava, jotta käytetään vuorolle suunniteltua projektia** \- Kun kirjataan uusi reaaliaikainen tapahtuma, henkilön oletusprojekti muodostuu sille automaattisesti. Tällä asetuksella voidaan valita, että tapahtuman projektiksi muodostuu se projekti jolle henkilön työaika on suunniteltu, silloin kun henkilö aloittaa työvuoronsa ajallisesti tarpeeksi lähellä suunniteltua vuoroa. Projekti tulee silloin vuorosta. Asetukseen asetetaan se määrä aikaa, jonka sisällä aloitettu työ ohjaa projektin muodostumista.
Asetuksen arvolla ei ole merkitystä jos "Kohdista työ suunnitellun vuoron projektiin" asetuksen arvona on "ei".
**Projektien vähimmäismäärä tapahtumalla -** mikäli tähän merkitään nollaa suurempi arvo, tulee projektin valinnasta työmerkinnän yhteydessä pakollista.
**Projektien enimmäismäärä tapahtumalla -** määrittää, montako projektia voidaan enintään kirjata per työmerkintä.
**Näytä projektin kestokenttä -** Määrittää, voivatko henkilöt syöttää projektin keston tapahtumille. Kesto voidaan määritellä tunteina tai prosentteina:
![mceclip4.png](https://support.nepton.com/hc/article_attachments/360004641677)
Tarkempi kuvaus tapahtuman kohdistamiselle usealle projektille löytyy [täältä](<https://support.nepton.com/hc/fi/articles/4411705615377>).
### Projektityypit
**Projektityypit** ja niiden lisääminen on kuvattu [tässä artikkelissa.](<https://support.nepton.com/hc/fi/articles/360002562338>)
Asetuksissa eri projektityypeille voidaan antaa käännökset Neptonin eri käyttökielille. Lisäksi projektyypille voidaan antaa aputeksti, joka näkyy käyttäjille projektikirjauksen yhteydessä projektit-otsikon alla.
![](https://support.nepton.com/hc/article_attachments/36216427136797)
## Asetukset asetusryhmä-tasolla
Asetusryhmä-tasolla projektien asetukset löytyvät valikosta **Työaika > Hallinta > Asetusryhmät > Asetusryhmä: Haluttu asetusryhmä > Toiminto: Asetusryhmän asetukset > Projektit.**
Asetusryhmäkohtaisesti projektien asetukset ovat työyhteisön asetuksia suppeammat. Asetusryhmälle voidaan projektien asetuksissa määritellä projektin nimessä näytettävien yläprojektien määrä, tapahtumakirjauksen kohdistaminen työvuoron projektiin sekä tarkkuus, jolla tapahtumakirjaus kohdistetaan suunnitellun työvuoron projektiin.
Lisäksi voidaan määritellä minimi- ja maksimiprojektimäärä kirjauksille sekä näytetäänkö projektien kestokenttä.
![](https://support.nepton.com/hc/article_attachments/36216427137309)
## Nykytila
Valikossa **Työaika > Hallinta > Työyhteisön asetukset > Nykytila** määritellään näkyvätkö projektit työaikapäätteellä ja Nykytila-näkymässä. Kun tämä on asetettu arvoon 'Kyllä', tapahtumalle tulee automaattisesti käyttäjän oletusprojekti tai vaihtoehtoisesti suunnitellun vuoron projekti, jos tämä on asetettu päälle.
![](https://support.nepton.com/hc/article_attachments/31526767435933)
