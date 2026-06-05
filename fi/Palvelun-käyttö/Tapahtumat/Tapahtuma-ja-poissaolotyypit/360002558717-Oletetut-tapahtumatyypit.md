---
id: 360002558717
title: Oletetut tapahtumatyypit
url: https://support.nepton.com/hc/fi/articles/360002558717-Oletetut-tapahtumatyypit
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Tapahtuma- ja poissaolotyypit
section_id: 360005841257
section_path:
- Tapahtumat
- Tapahtuma- ja poissaolotyypit
labels:
- automaattinen tapahtuma
- automaattikirjaus
- automaatti
- oletustyöaika
- oletus
- oletustapahtuma
- etukäteisleimaus
- ennakkoleima
- automaattileimaus
- työajan automatisointi
- työajan automaattinen täyttö
promoted: false
updated_at: '2026-01-12T11:45:40Z'
edited_at: '2026-01-02T08:34:09Z'
---

# Oletetut tapahtumatyypit

Palveluun voidaan määritellä millaisia oletettuja eli automaattisia tapahtumia luodaan erilaisissa tilanteissa. 
Oletettuja tapahtumatyyppejä voidaan määritellä Työaika-osiossa joko **Työyhteisö** \- tai **Asetusryhmät** -tason asetuksissa valikossa **Työaika > Hallinta > Työyhteisön/Asetusryhmän asetukset > Työtunnit > Tapahtumatyypit. **Määrityksen voi tehdä myös Henkilöt-tasolla (Työaika > Hallinta > Henkilöt). Emme kuitenkaan suosittele määritysten tekemistä henkilötasolle, koska niiden hallinta on silloin haastavaa.
Oletetut tapahtumatyypit löytyvät edellä mainittua polkua seuraamalla tapahtumatyyppilistauksen alapuolelta. Oletettuja tapahtumatyyppejä on kahdenlaisia: 
![](https://support.nepton.com/hc/article_attachments/32927120133789)  
**1\. Oletettu tapahtumatyyppi uutta tapahtumaa luodessa**  
Määrittelee, mikä tapahtumatyyppi näkyy oletuksena, kun uutta tapahtumaa luodaan. Jos asetukseen ei olla muuta määritelty, oletuksena esitetään Työ-tapahtumaa. Tämä tapahtumatyyppi on myös mobiilin pika-aloituksen tapahtumatyyppinä Ruokatauon lisäksi. Lue [tästä artikkelista](<https://support.nepton.com/hc/fi/articles/360009193677>) tarkempi ohje miten voit muokata mobiilinäkymän pika-aloitusta.
**2\. Oletettu tapahtumatyyppi tyhjinä työpäivinä**  
Määrittelee, mikä tapahtumatyyppi luodaan henkilön työaikakalenteriin niinä päivinä, kun henkilöllä on työvelvoite (työpäivän pituus), mutta henkilö ei kirjaa kyseiselle päivälle mitään tapahtumaa. HUOM: Oletettua tapahtumatyyppiä ei saa automaattisesti luotua juhlapyhille, vaikka kyseisellä päivällä olisi työvelvoite. Automaattinen tapahtuma merkitään kellonajoille, jotka on määritelty [näytön asetuksissa.](<https://support.nepton.com/hc/fi/articles/360008777997>) Jos näytön asetuksiin ei ole määritelty mitään, tulee automaattinen tapahtuma ajalle 8:00-16:00. Tapahtuman luojaksi muodostuu tapahtuman hyväksyjä, kun tapahtuma on hyväksytty.
Oletettua tapahtumatyyppiä tyhjinä työpäivinä voidaan hyödyntää esimerkiksi seuraavissa tilanteissa:
  * Henkilöille, jotka tekevät samaa tehtävää samaan aikaan joka päivä. Tällöin henkilön ei tarvitse tehdä kirjauksia manuaalisesti, vaan ne tulevat automaattisesti henkilön kalenteriin. 
  * Henkilöille, joilla ei varsinaisesti ole työajan leimaamisvelvollisuutta (=kiinteä työaika), mutta halutaan kuitenkin saada raportoitua kokonaistyöaikaa
  * Henkilöille, jotka tekevät osa-aikaisuutta siten, että heillä on viikolla koko päivän poissaoloja ja poissaolopäivä vaihtelee. Tällöin voidaan asettaa, että poissaolopäiville tulee esimerkiksi 'Osa-aikavapaa'-tapahtuma automaattisesti. Voit lukea lisää osa-aikaisuuden perustamisesta erillisestä artikkelista [täältä](<https://support.nepton.com/hc/fi/articles/360002559018-Osa-aikaisuuden-perustaminen>). 


Mikäli tiettyinä päivinä halutaan käyttää eri oletustapahtumatyyppiä, se voidaan toteuttaa [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta [poikkeusasetuksella](<https://support.nepton.com/hc/fi/articles/360002560677>) esim. seuraavasti:
![](https://support.nepton.com/hc/article_attachments/32927108761885)
Esimerkissä lauantaisin ja sunnuntaisin Etätyö on oletustapahtumatyyppi. Tarkemmin mahdollisista poikkeusasetuksista on kerrottu ohjeessa [Poikkeusasetusten määrittely. ](<https://support.nepton.com/hc/fi/articles/360002560677>) HUOM: Oletettua tapahtumatyyppiä ei saa luotua juhlapyhille, ei edes poikkeusasetuksella.
Oletettu tapahtumatyyppi on myös mahdollista luoda suunnitellun työvuoron mukaisesti:
![](https://support.nepton.com/hc/article_attachments/32927120134685)
Tällöin oletettu tapahtumatyyppi luodaan vuoron kellonajoilla ja tapahtumatyyppinä on työvuorolla suunniteltu tapahtumatyyppi. Poikkeusasetuksilla voidaan myös määrittää, että oletettu tapahtumatyyppi tulee vain tietynlaisista vuoroista. Määritys voidaan tehdä vuoron lyhenteen tai suunnitellun tapahtumatyypin perusteella.
Jos **Oletettu tapahtumatyyppi tyhjinä työpäivinä** on asetettu työsuhteen ensimmäisestä päivästä alkaen, eikä henkilö ole leimannut yhtään Työ-tapahtumaa kalenteriinsa, on henkilölle asetettava jokin palkanlaskennan käynnistävä tapahtuma (kuten esimerkiksi työ, saldon muutos tai saldon asetus) sille päivälle, josta lähtien oletetun tapahtumatyypin halutaan täyttävän kalenteria. Jos esimerkiksi halutaan, että oletettu tapahtumatyyppi tyhjinä työpäivinä täyttää henkilön kalenteria 15.5.2024 alkaen, on kyseiselle päivälle merkittävä esimerkiksi tapahtuma ''Työ'', jonka kesto on 08.00-08.00, jonka myötä oletettu tapahtumatyyppi merkitään tyhjille työpäiville tästä lähtien. 
Suosittelemme kaikkien määritysten tekemistä kaikissa tilanteissa [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta.
