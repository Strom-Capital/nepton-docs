---
id: 360017908457
title: Laskenta suunnittelunäkymässä
url: https://support.nepton.com/hc/fi/articles/360017908457-Laskenta-suunnittelun%C3%A4kym%C3%A4ss%C3%A4
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Yleiset työajan laskennan asetukset
section_id: 19210968853277
section_path:
- Vuorosuunnittelu ja vuorokalenterit
- Yleiset työajan laskennan asetukset
labels: []
promoted: false
updated_at: '2024-08-23T11:23:40Z'
edited_at: '2024-02-21T07:13:48Z'
---

# Laskenta suunnittelunäkymässä

Kun luodaan työvuorosuunnitelma Vuorosuunnittelu > Suunnittelunäkymässä, palvelu tukee suunnittelua näyttämällä työn kokonaismäärän. Tähän on mukaanluettu suunnitellut sekä tallennetut tapahtumat, joita verrataan henkilön tavoitetunteihin. Tässä artikkelissa kuvataan, mitä arvot ja niiden värikoodaukset tarkoittavat.
## Yhteensä sarakkeet
Oletuksena suunnittelunäkymässä on vain yksi yhteensä-sarake nimeltä "Näkymä". Siinä näytetään valitun näkymän ja suodatettujen arvojen kokonaismäärä.
Näkymä-sarakkeessa on kaksi arvoa. Ensimmäinen on henkilölle asetettu tavoite ja toinen on henkilölle suunnitellut ja / tai toteutuneet kokonaistyötunnit.
Huomaa: Toteutuneet tapahtumat ovat niitä, jotka on merkitty työaikaan ja määritetty näkymään suunnittelussa kohdassa Työaika-Hallinta-Työyhteisön asetukset-Työtunnit-Tapahtumatyypit.
![WSP_06.png](https://support.nepton.com/hc/article_attachments/360018245258)
Voit sisällyttää lisätietoja ja loppusummia suunnittelunäkymään käyttämällä Näkymän asetukset -valikon vaihtoehtoja. Avautuvasta valikosta voit valita tiedot, jotka haluat sisällyttää näkymään, kuten tasoittusmisjakso. Ota muutokset käyttöön napsauttamalla Käytä.
![](https://support.nepton.com/hc/article_attachments/16916467715613)
Suodattimien perusteella näkymään lisätyt tiedot näkyvät Näkymä-sarakkeessa.
##  Sovittujen tuntien määritteleminen henkilölle (eli Tavoite)
Tavoite-arvo on henkilölle asetettu viikoittainen työvelvoite tunteina. Viikkotyövelvoitteet asetetaan vähimmäis- ja enimmäistyötunteina viikossa. Viikon vähimmäis- ja enimmäistyötunnit voidaan asettaa jokaisen henkilön tiedoista Työsuhde>Henkilöt.
![WSP_14.png](https://support.nepton.com/hc/article_attachments/360018245358)
## Tavoitetyötunnit
Henkilön tavoitearvot näkyvät kolmessa eri värissä suunnittelunäkymässä.
### Sininen - Suunniteltuja tunteja on vähemmän kuin tavoite
Jos henkilön kokonaistyötunnit ovat pienempiä kuin vähimmäistyötunnit viikossa, tavoitearvo näytetään sinisellä värillä. Tavoitearvo näyttää vähimmäistyötuntien erotuksen vähennettynä kokonaistyötunneilla (vähimmäistyöajat viikossa - kokonaistyötunnit). Esimerkiksi alla olevassa kuvassa vähimmäistyötuntien viikossa asetettu arvo on 32h ja kokonaistyötunnit 30h, joten tavoitearvo on 2:00h.
![WSP_01.png](https://support.nepton.com/hc/article_attachments/360018245178)
### Vihreä - Suunnitellut tunnit ovat tavoitearvojen välissä Min/Max
Jos kokonaistyötunnit ovat vähimmäistyötuntien ja enimmäistyötuntien välillä viikossa, tavoitearvo näytetään vihreällä ja plusmerkillä. Tavoitearvo osoittaa kokonaistyötuntien vähennettynä vähimmäistyötunneilla viikossa (kokonaistyötunnit - vähimmäistyötunnit viikossa). Esimerkiksi asetetun arvon alapuolella vähimmäistyötunnit viikossa on 32h ja kokonaistyötunnit 37:30h, joten tavoitearvo on +5:30h.
![WSP_02.png](https://support.nepton.com/hc/article_attachments/360018245198)
### Punainen - Suunniteltuja tunteja on enemmän kuin tavoite
Jos kokonaistyötunteja ovat enemmän kuin viikon enimmäistyötunnit, tavoitearvo näytetään punaisella ja plusmerkillä. Tavoitearvo näyttää kokonaistyötuntien erotuksen enimmäistyötunneista viikossa (kokonaistyötunnit - enimmäistyötunnit viikossa). Esimerkiksi asetetun arvon alapuolella enimmäistyötunnit viikossa on 40 h ja kokonaistyötunnit ovat 45:30 h, joten tavoitearvo on +5:30h.
![WSP_03.png](https://support.nepton.com/hc/article_attachments/360018185597)
### Musta viiva – henkilölle ei ole asetettu tavoitearvoja
Jos henkilölle ei ole asetettu tavoitearvoja, näytetään musta viiva (”-”) ja hiiren ollessa sen päällä näkyy teksti: ”Tavoite: Ei asetettu”.
![WSP_17.png](https://support.nepton.com/hc/article_attachments/360018185757)
## Suunnitellut työtunnit
Toinen arvo Näkymä-sarakkeessa on henkilölle suunniteltu työaika. Tuntitiedot näytetään eriteltynä, kun viet hiiren kokonaistuntien päälle.
![WSP_04.png](https://support.nepton.com/hc/article_attachments/360018245238)
### Juhlapyhät
Jos juhlapyhäpäivälle ei ole suunniteltu työvuoroa, sen pituus lisätään normaalisti kokonaistyötunteihin. Juhlapyhien pituus voidaan asettaa osiossa Työsuhde>Hallinta>Vuorosuunnittelu.
![WSP_13.png](https://support.nepton.com/hc/article_attachments/360018245338)
Jos juhlapyhälle on suunniteltu työvuoro, voidaan määrittää, kuinka juhlapyhä lisätään suunniteltuihin työtunteihin. Asetus voidaan tehdä kohdassa Työsuhde>Hallinta>Vuorosuunnittelu.
![WSP_19.png](https://support.nepton.com/hc/article_attachments/360018185797)
**Esimerkki 1**
Juhlapyhän pituus: **8h**
Suunnitellun työvuoron pituus juhlapyhänä: **8h**
Juhlapyhinä päivittäinen työvelvoite lisätään työtunteihin päivälle suunnitellun työn lisäksi = (**ei valittu**)**  
**
Kokonaistyötunnit = **8h** (ainoastaan suunnitellun vuoron pituus (8h) lisätään kokonaistyötunteihin)
![WSP_21.png](https://support.nepton.com/hc/article_attachments/360018185817)
**Esimerkki 2  
**
Juhlapyhän pituus: **8h**
Suunnitellun työvuoron pituus juhlapyhänä:**8h**
Juhlapyhinä päivittäinen työvelvoite lisätään työtunteihin päivälle suunnitellun työn lisäksi = (**valittu**)
Kokonaistyötunnit = **16h**(juhlapyhän pituus (8h) + suunnitellun vuoron pituus (8h) lisätään kokonaistyötunteihin)
![WSP_22.png](https://support.nepton.com/hc/article_attachments/360018185837)
### Tapahtumatyypit, jotka eivät koskaan lisää suunniteltuja työtunteja
Seuraavat tapahtumatyypit eivät koskaan lisää suunnittelun kokonaistunteja:
  * Sairausloma
  * Vuosivapaa
  * Poissaolo
  * Ruokailu
  * Saldovapaa
