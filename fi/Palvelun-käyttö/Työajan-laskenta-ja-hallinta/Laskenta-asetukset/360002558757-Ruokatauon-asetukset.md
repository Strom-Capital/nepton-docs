---
id: 360002558757
title: Ruokatauon asetukset
url: https://support.nepton.com/hc/fi/articles/360002558757-Ruokatauon-asetukset
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Laskenta-asetukset
section_id: 360005872258
section_path:
- Työajan laskenta ja hallinta
- Laskenta-asetukset
labels:
- ruoka
- lounas
- lounaan
- lounastauko
- lounaskirjaus
- työnantajan tarjoama lounas
promoted: false
updated_at: '2026-03-12T08:57:56Z'
edited_at: '2024-08-20T04:52:56Z'
---

# Ruokatauon asetukset

Ruokatauon asetukset voidaan määritellä Työyhteisö- tai Asetusryhmä-tasolla. Asetusryhmän osalta määritykset löytyvät kohdasta **Työaika > Hallinta > Asetusryhmät >Toimintavalikosta: Asetusryhmän asetukset > Työtunnit > Ruokatauko.**
Työyhteisö-tason osalta määritykset löytyvät kohdasta **Työaika > Hallinta > Työyhteisön asetukset > Työtunnit > Ruokatauko. **
Mikäli käytössä on**[Vuorosuunnittelu-toiminnallisuus](<https://support.nepton.com/hc/fi/articles/360011258978>)** , voidaan ruokatauon asetukset määritellä Toimipiste (Suunnittelutaso)-kohtaisesti. Tällöin niitä ei tarvitse välttämättä määritellä lainkaan Työyhteisötason tai Asetusryhmän asetuksissa. Ohje löytyy [täältä.](<https://support.nepton.com/hc/fi/articles/360015675918>) Kaikkia vuorosuunnittelun alaisuudessa olevia henkilöitä koskeva ohjeistus löytyy puolestaan [täältä.](<https://support.nepton.com/hc/fi/articles/360016244837>) Vuorosuunnitteluun tehdyt ruokatauon vähennysmääritykset ohittavat työyhteisötasolla, asetusryhmässä, henkilöasetuksissa tehdyt ruokataukomääritykset.
Määrityksiä voidaan tehdä myös käyttäjäkohtaisiin asetuksiin. Suosittelemme kuitenkin tekemään kaikki määritykset aina Työyhteisö- tai Asetusryhmät-tasoille.
## Ruokatunnin oletuskeston määrittäminen ja vähentäminen työajasta automaattisesti
Jos halutaan määritellä ruokatunnille oletuskesto, voidaan ruokatunnin oletuskestoon määritellä ruokatauon pituus, joka vähennetään työpäivän pituudesta automaattisesti, mikäli ruokataukoa ei kirjata manuaalisesti työajan kalenteriin. Tämä määritys tehdään kentässä **Ruokatunnin oletuskesto**.
Oletuskestolle voidaan merkitä myös poikkeusmäärityksiä, jos keston halutaan poikkeavan normaalista esimerkiksi tiettynä päivänä. Valitse tällöin **Poikkeukset**.
Poikkeusasetuksissa voidaan määrittää automaattiseen ruokatunnin vähentämiseen poikkeuksia, jos päivän ensimmäinen työtapahtuma (tai Työ-tapahtumatyypin kaltainen tapahtuma) aloitetaan tiettynä aikana tai tietyn ajan jälkeen, tai tarkalleen tiettynä ajankohtana.
On myös mahdollista asettaa vähimmäismäärä tehdylle työajalle, jonka jälkeen oletettu ruokatauko vähennetään. Esimerkiksi jos **Vähimmäistyöaika, jonka jälkeen ruokatauko voidaan olettaa** _-_ asetukseen on asetettu 6:00h ja henkilö kirjaa työaikaa 5:59h, oletettua ruokataukoa ei lisätä tälle päivälle. Jos henkilö kirjaa päivälle työaikaa 6:00h, eikä päivällä ole käsin lisättyjä ruokataukoja, vähennetään työajasta oletettu ruokatauko ja työajaksi jää 5:30h (jos on asetettu, että oletuksena ruokatauon kesto on 0:30h).
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4410077319825)
Huom! Jos ruokatunnin ja sitä edeltävän tai sen jälkeen tulevan työtapahtuman välissä on minuutin tai pidempi väli ilman kirjausta, leimauksia ei lasketa yhdeksi työvuoroksi ilman suunniteltua työvuoroa tai oletettuja työaikoja. Tässä tapauksessa ruokatunnin täytyy alkaa heti edeltävän työtapahtuman jälkeen ja ruokatunnin jälkeisen työtapahtuman heti ruokatunnin päättymisen jälkeen.
Huom! Palvelu laskee kaikki tapahtumat yhtäjaksoiseksi tapahtumaksi, jos tapahtumat on merkitty yhtäjaksoisesti ilman minuutinkaan väliä tapahtumien välissä. Esimerkiksi siis tapahtumat, jotka on merkitty erillisinä 4 tunnin tapahtumina klo 8:00-12:00 ja klo 12:00-16:00 lasketaan yhtäjaksoiseksi 8 tunnin tapahtumaksi. Jos tapahtumien väliin jää minuutinkin tauko palvelu katsoo tapahtumien olevan erillisiä tapahtumia/vuoroja ja niitä ei lasketa yhtäjaksoiseksi tapahtumaksi. Tämä voi vaikuttaa ruokatauon automaattisen vähennyksen kynnykseen.
## Ruokatunnin oletuskeston määrityksen ja automaattisen työajasta vähentämisen poistaminen
Ruokatunnin oletuskesto ja automaattinen vähennys työajasta voidaan poistaa käytöstä syöttämällä arvoiksi 0 minuuttia ja Ei asetettu/Peri ylemmältä tasolta (tällöin tulee huolehtia, ettei määritystä ole tehty myös ylemmälle tasolle, josta se periytyisi Neptonin toimintaperiaatteen mukaisesti myös alempiin asetusryhmiin).
## Ruokatuntien pidentäminen haluttuun pituuteen
Lyhyiden ruokataukojen leimaukset voidaan pidentää haluttuun pituuteen kohdassa **Pidennä lyhyet ruokatauot pituuteen.** Alempaan kenttään voidaan myös määrittää, että nollaminuuttiset ruokatauon leimaukset pidennetään tähän samaan pituuteen. Jos määritetään, että nollapituista ei pidennetä, voidaan estää automaattisesti muodostuva Ruokatauko kirjaamalla nollapituinen Ruokatauko.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/4410060851857)
Huom! Ruokataukoa ei pidennetä asetettuun pituuteen jos työajan/poissaoloajan määrä ei ylitä kynnysarvoa, joka on asetettu asetuksessa **Vähimmäistyöaika, jonka jälkeen lyhyet ruokatauot pidennetään.** Esimerkiksi, jos kynnysarvoksi on asetettu 6:00h ja **Pidennä lyhyet ruokatauot pituuteen** -asetukselle on asetettu 0:30h, ja henkilöllä on kuuden tunnin pituinen työtapahtuma, jonka yhteydessä on 10 minuutin lounas, lounasta ei pidennetä koska henkilö on tehnyt töitä vain 5:50h edestä. Jos esimerkin henkilöllä on 6:10h pituinen työtapahtuma, jonka yhteydessä 10 minuutin ruokatauko, kynnys ylittyy, ruokataukoa pidennetään 20 minuutilla (ruokatauon lopusta) ja henkilölle kirjataan työaikaa 5:40h.
## Ruokatauon pituuden rajaaminen
Pitkien ruokataukojen leimaukset voidaan lyhentään haluttuun pituuteen kohdassa **Lyhennä pitkät ruokatauot pituuteen.** Tällöin työvuoron ruokatauko ei voi ylittää määritettyä pituutta.
Huom! Tämä vaikuttaa myös ruokatauosta ansaittaviin työkorotuksiin. Esimerkiksi, jos halutaan, että ainoastaan palkallisesta ruokatauosta ansaitaan työkorotuksia, niin ruokatauot lyhennetään siihen pituuteen mikä palkalliselle ruokatauolle on määritelty, jolloin pidempiä ruokataukoja pidettäessä sen ylittävä osuus on työntekijän omaa aikaa eikä siitä ansaita työkorotuksia.
![mceclip3.png](https://support.nepton.com/hc/article_attachments/4410077597585)
## Palkallisen ruokatunnin kesto
Palkallisen ruokatunnin kesto määrittää ruokatauon palkallisen pituuden. Ylittävää aikaa ei lasketa normaaliksi työajaksi ja se ei kerrytä esimerkiksi saldokertymää.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/4410069283473)
Palkalliset ruokatunnit voidaan asettaa myös siten, että ne ansaitaan vasta kun tietty määrä työaikaa tai poissaoloa on toteutunut kyseisenä päivänä asetuksella **Vähimmäistyöaika, jonka jälkeen palkallinen ruokatauko ansaitaan.** Tämä kynnysarvo tarkistetaan sen jälkeen, kun työajasta on vähennetty mahdolliset ruokatauot, oletetut ruokatauot ja pidennetyt ruokatauot. Esimerkiksi jos palkallinen ruokatunti ansaitaan vasta kun päivässä on tehty työtä 6:00h ja henkilö kirjaa kuuden (6) tunnin työtapahtuman jonka perusteella vähennetään 30 minuutin oletettu ruokatauko, ruokatunti ei ole palkallinen koska kuuden (6) tunnin työaika ei täyty. Jos taas henkilö kirjaa 6:30h kestoisen työtapahtuman ja tästä muodostuu 30 minuutin oletettu ruokatauko, ruokatauko on palkallinen koska tehtyä työtä on kuusi (6) tuntia ja kynnysarvo ylittyy.
## Ruokatunnin oletusajankohta
Ruokatunnin oletusajankohta näkyy kalenterinäkymässä ruokatauon ajankohtana, mikäli ruokataukoa ei ole kirjattu.
![mceclip1.png](https://support.nepton.com/hc/article_attachments/4406965878417)
## Maksimimäärä mitä oletusruokatauosta voi ansaita kertymään jos tehdään töitä
Tällä asetuksella voidaan määrittää, kuinka paljon Ruokatauko-tapahtumatyypin tapahtumasta voidaan ansaita joko saldo-, pankki-, jousto-, ylityösaldo- tai työajan lyhennysvapaan kertymään.  
  
![20210223-lunch-settings.PNG](https://support.nepton.com/hc/article_attachments/360017196897)
## Oletettu ruokatauko tapahtumatyypeistä
Tällä asetuksella voidaan määrittää mistä tapahtumatyypeistä automaattinen ruokatunti vähennetään. Oletusmääritykset on kerrottu tapahtumatyypeittäin suoraan näkymässä. Oletusmääritystä käytetään, jos määrityksenä on Peri ylemmältä tasolta ja ylemmälläkään tasolla ei ole määritystä tehty. Jos halutaan määrittää jokin tapahtumatyyppi ensisijaiseksi, jonka aikana Oletettu ruokatauko merkitään, määritetään sille Korkea prioriteetti. Millään tapahtumatyypillä ei ole määritettynä oletuksena Korkea prioriteetti. Työ-tyyppisillä tapahtumatyypeillä on Normaali prioriteetti. Ei ansaita tarkoittaa Ei vähennetä.
  * **Korkea prioriteetti:** Ruokatauko vähennetään päivältä aina kyseisen tapahtumatyypin aikana.
  * **Normaali prioriteetti:** Ruokatauko vähennetään noin 3h 30min kuluttua työpäivän alusta, tai oletusajankohtana, jos se on määritetty.
  * **Matala prioriteetti:** Ruokatauko vähennetään ensisijaisesti päivältä jostakin muusta tapahtumatyypistä, jos päivälle on kirjattu muita tapahtumatyyppejä.
  * **Ei ansaita:** Tapahtumatyypistä ei vähennetä ruokataukoa.


![Annotation_2020-03-20_102819_6.png](https://support.nepton.com/hc/article_attachments/360007195618)
Muista kirjata kaikki asetusmuutokset [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta, jotta mahdolliset aiempien asetusten mukaiset laskennat eivät mene väärin.
