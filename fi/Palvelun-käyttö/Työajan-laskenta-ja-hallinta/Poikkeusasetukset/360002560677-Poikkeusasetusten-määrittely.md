---
id: 360002560677
title: Poikkeusasetusten määrittely
url: https://support.nepton.com/hc/fi/articles/360002560677-Poikkeusasetusten-m%C3%A4%C3%A4rittely
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: 'Poikkeusasetukset '
section_id: 360000708398
section_path:
- Työajan laskenta ja hallinta
- 'Poikkeusasetukset '
labels:
- sdsql
- pyhäkalenteri
- mayday
- sääntöeditori
- juhannus
- pääsiäissunnuntai
- poikkeusase
promoted: false
updated_at: '2026-07-14T07:16:46Z'
edited_at: '2026-07-14T07:16:46Z'
---

# Poikkeusasetusten määrittely

Asetusten [voimassaolotoiminnolla](<https://support.nepton.com/hc/fi/articles/360002559358>) voidaan määrittää poikkeuksia käytössä oleviin asetuksiin. Asetuspoikkeus voidaan asettaa erikseen määritettävillä **sääntökomennoilla** mm. juhlapyhille tai vapaasti mille tahansa päivälle tai päiville. Sääntökomentoja käydään tarkemmin läpi tämän ohjeen alaosassa esimerkkien avulla.
Mikäli poikkeuksia on asetettu, tulkitaan poikkeusten säännöt ennen asetuksen arvon käyttämistä. 
  * Asetuksella voi olla useita poikkeuksia ja ne käsitellään järjestyksessä ylhäältä alas.
  * Ensimmäinen sääntö, jonka arvo on tosi, tulee voimaan.
  * Säännöt voidaan siirtää hiirellä toiseen järjestykseen käyttämällä ikonia, joka ilmestyy vasemmalle, kun hiiren kohdistin viedään säännön päälle.
  * Jokainen päivä arvioidaan sitä sääntöä vasten erillisenä. 


Mikäli asetukselle ei ole asetettu arvoa tai mikään poikkeus ei ole voimassa, haetaan palvelun käyttämä asetuksen arvo yläryhmästä. Mikäli ala-asetusryhmätasolle on määritelty pelkkä poikkeus, on kyseisessä asetusryhmässä voimassa sekä tämä poikkeus, että mahdolliset ylemmältä tasolta perityt poikkeussäännöt. Poikkeussäännön periytyminen voidaan estää antamalla eri arvo samaan poikkeussääntöön, tai antamalla arvo itse pääasetukseen.
## Asetusarvon poikkeuksen määrittäminen
Poikkeus asetusarvoon määritetään aina [voimassaolotoiminnon](<https://support.nepton.com/hc/fi/articles/360002559358>) kautta. Poikkeus asetukseen lisätään valitsemalla **Lisää poikkeus.**
  * **Arvo-** kenttään määritetään poikkeava asetusarvo.
  * **Sääntö-** kenttään määritetään alta löytyvillä sääntökomennoilla ehdot, jolloin poikkeusasetus halutaan olevan voimassa.
  * **Voimassa alkaen ja Voimassa saakka -** kenttiin voidaan määrittää päivämäärät esimerkiksi tilanteessa, jossa asetus on voimassa vain jonkin tietyn ajanjakson, esimerkiksi käytössä olevan työehtosopimuksen määrittelemän ajan.


Alla olevassa esimerkissä työpäivän pituus on 7,5 tuntia, paitsi jouluaaton aattona, jolloin se on 4 tuntia.
![](https://support.nepton.com/hc/article_attachments/35359393028637)
Sääntö-kentän vieressä olevasta taikasauva-painikkeesta aukeaa lista valittavista valmiista sääntökomennoista. Yleisimmät sääntökomennot, kuten komennot jotka perustuvat päivämääriin, juhlapyhiin tai tapahtumatyyppeihin, voidaan hakea ja valita painamalla taikasauva-kuvaketta sääntökentän oikealla puolella. Tämä avaa valintaikkunan alla olevan kuvan mukaisesti.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4972671302045)
Jokainen sääntöön lisätty sääntökomento vaikuttaa säännön ehtojen täyttymiseen. Jos esimerkiksi valitaan "[CHRISTMAS-DAY]" ja "Monday", sääntö toteutuu vain jos on sekä joulupäivä että Maanantai.  
Jos halutaan että joku sääntökomennoista toteutuu, ne eritellään pilkulla kuten esimerkiksi "[CHRISTMAS-DAY], Monday", jolloin sääntö toteutuu jos on joulupäivä TAI maanantai.
Tiettyjen sääntökomentojen valinta pyytää käyttäjältä lisätietoa, jos esimerkiksi halutaan että sääntö toteutuu kun tiettyjä tapahtumatyyppejä on merkitty kyseiselle päivälle, voidaan valita "[WORK-DAY-HAS-ANY-OF-EVENT-TYPES]" komento ja valintatyökalu kysyy tämän jälkeen mitä tapahtumatyyppejä säännön halutaan koskevan. Kun halutut tapahtumatyypit on valittu, painetaan "Ok" ja sääntö lisätään halutuilla tapahtumatyypeillä, esim. "[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|100|101|jne]"
Käytössä saattaa olla myös sääntökomento [WORK-DAY-HAS-ANY-EVENT-TYPE**-IDS** | -- ], jossa piippumerkin jälkeen on käytetty tapahtumatyyppien ID:tä. ID on aiemmin käytössä ollut tunniste, jota ei tule enää käyttää.
Huom: tämä ei tue SQL-pohjaisia sääntöjä kuten esim. "FROM UserEventData WHERE..."
### Asetukset, jotka eivät tue poikkeuksia
Poikkeusasetukset eivät toimi kaikissa asetuksissa. Mikäli poikkeuksia ei tueta, näytetään asetuksen muokkausikkunassa seuraavanlainen ilmoitus:  
![](https://support.nepton.com/hc/article_attachments/35359393030685)
Jotkut asetukset voivat tukea poikkeuksia rajallisesti, jolloin näkyy seuraava ilmoitus:
![](https://support.nepton.com/hc/article_attachments/35359393031453)
Jos yritetään tehdä poikkeusta, jota kyseinen asetus ei tue, ei palvelu anna tallentaa asetusta.
## Päivämäärän sääntökomennot
Sääntökomennot määritetään englanniksi mutta ne käyttäytyvät suomalaisten juhlapyhien sekä joidenkin muiden maiden juhlapyhien mukaisesti. Käytettävissä olevat sääntökomennot (hakasuluissa) ovat:
  * `[ANY-PUBLIC-HOLIDAY]` \- Mikä tahansa juhlapyhäksi laskettu päivä (eli asetuksissa juhlapyhälle on asetettu että lasketaan juhlapyhäksi, riippumatta siitä lyhentääkö se työviikon pituutta) Sääntö ei tue - 1 day tai + 1 day-ehtoa.
  * `[ANY-PUBLIC-HOLIDAY-IN|HOLIDAYNAME]` \- Mikä tahansa juhlapyhäksi laskettu päivä (eli asetuksissa juhlapyhälle on asetettu että lasketaan juhlapyhäksi, riippumatta siitä lyhentääkö se työviikon pituutta) joka on määritetty IN| - merkin jälkeen. Juhlapyhät kirjataan alla luetellun listan mukaisesti ilman hakasulkeita | merkillä eroteltuna. Esim. jos halutaan että sääntö on voimassa loppiaisena ja helatorstaina, asetetaan säännöksi [ANY-PUBLIC-HOLIDAY-IN|ASCENSION-DAY-GREGORIAN|EPIPHANY]. Sääntö ei tue - 1 day tai + 1 day-ehtoa, nämä aattopoikkeukset tulee määrittää erikseen ilman IN|-ehtoa. 
  * `[ANY-PUBLIC-HOLIDAY-EXCEPT|HOLIDAYNAME]` \- Mikä tahansa juhlapyhäksi laskettu päivä (eli asetuksissa juhlapyhälle on asetettu että lasketaan juhlapyhäksi, riippumatta siitä lyhentääkö se työviikon pituutta) paitsi ne jotka on määritetty EXCEPT| - merkin jälkeen. Juhlapyhät kirjataan alla luetellun listan mukaisesti ilman hakasulkeita | merkillä eroteltuna. Esim. jos halutaan että sääntö on voimassa kaikkina juhlapyhinä paitsi loppiaisena ja helatorstaina, asetetaan säännöksi [ANY-PUBLIC-HOLIDAY-EXCEPT|ASCENSION-DAY-GREGORIAN|EPIPHANY]. Sääntö ei tue - 1 day tai + 1 day-ehtoa. 
  * `[ALL-SAINTS-DAY]` \- Pyhäinpäivä
  * `[ANNIVERSARY-OF-THE-CORONATION-OF-KING-MINDAUGAS]` \- Valtion päivä Liettuassa (kuningas Mindaugasin kruunajaiset) (6.7.)
  * `[ARMISTICE-DAY]` \- Maailmansodan päättymisen muistopäivä (11.11.)
  * `[ASCENSION-DAY-GREGORIAN]` \- Helatorstai
  * `[ASSUMPTION-DAY]` \- Marian taivaaseenottamisen juhlapäivä (15.8.)
  * `[AUSTRIAN-NATIONAL-DAY]` \- Itävallan kansallispäivä (26.10.)
  * `[BELGIAN-ALL-SAINTS-DAY]` \- Pyhäinpäivä Belgiassa (1.11.)
  * `[BELGIAN-NATIONAL-DAY]` \- Belgian kansallispäivä (21.7.)
  * `[BOXING-DAY]` \- Tapaninpäivä
  * `[CHRISTMAS-DAY]` \- Joulupäivä
  * `[CHRISTMAS-EVE]` \- Jouluaatto
  * `[EASTER-JULIAN]` \- Pääsiäispäivä Juliaanisen kalenterin mukaan. Ortodoksisen (paitsi Suomen) kirkon pääsiäispäivä tulee Juliaanisen kalenterin mukaan.
  * `[EASTER-MONDAY-GREGORIAN]` \- Toinen pääsiäispäivä
  * `[EASTER-SUNDAY-GREGORIAN]` \- Pääsiäispäivä
  * `[EPIPHANY]` \- Loppiainen
  * `[ESTONIAN-INDEPENDENCE-DAY]` \- Viron itsenäisyyspäivä (24.2.)
  * `[ESTONIAN-INDEPENDENCE-DAY-EVE]` \- Viron itsenäisyyspäivän aatto (23.2.)
  * `[ESTONIAN-INDEPENDENCE-RESTORATION-DAY]` \- Viron uudelleenitsenäistymispäivä (20.8.)
  * `[ESTONIAN-ST-JOHNS-DAY-EVE]` \- Viron voitonpyhän aatto (22.6.)
  * `[ESTONIAN-VICTORY-DAY]` \- Viron voitonpyhä (23.6.)
  * `[FATHERS-DAY]` \- Isänpäivä
  * `[FEAST-OF-CORPUS-CHRISTI]` \- Pyhän ruumiin juhlapäivä (60 päivää pääsiäisen jälkeen)
  * `[GERMAN-ALL-SAINTS-DAY]` \- Pyhäinpäivä Saksassa (1.11.)
  * `[GOOD-FRIDAY-GREGORIAN]` \- Pitkäperjantai
  * `[GREAT-PRAYER-DAY]` \- Tanskan suuri rukouspäivä (4. lauantai pääsiäisen jälkeen)
  * `[HOLY-SATURDAY-GREGORIAN]` \- Pääsiäislauantai
  * `[INDEPENDENCE-DAY]` \- Itsenäisyyspäivä
  * `[INDEPENDENCE-DAY-EVE]` \- Itsenäisyyspäivän aatto (5.12.)
  * `[LITHUANIAN-ALL-SAINTS-DAY]` \- Pyhäinpäivä Liettuassa (1.11.)
  * `[LITHUANIAN-FATHERS-DAY]` \- Isänpäivä Liettuassa (kesäkuun ensimmäinen sunnuntai)
  * `[LITHUANIAN-INDEPENDENCE-RESTORATION-DAY]` \- Liettuan itsenäisyyden palauttamisen päivä (11.3.)
  * `[LITHUANIAN-MOTHERS-DAY]` \- Äitienpäivä Liettuassa (toukokuun ensimmäinen sunnuntai)
  * `[LITHUANIAN-RESTORATION-OF-THE-STATE-DAY]` \- Liettuan itsenäisyyspäivä (16.2.)
  * `[MAUNDY-THURSDAY-GREGORIAN]` \- Kiirastorstai
  * `[MAY-DAY]` \- Vappupäivä
  * `[MAY-DAY-EVE]` \- Vappuaatto
  * `[MIDSUMMERS-DAY]` \- Juhannuspäivä
  * `[MIDSUMMERS-EVE]` \- Juhannusaatto
  * `[MOTHERS-DAY]` \- Äitienpäivä
  * `[NEW-YEARS-DAY]` \- Uudenvuodenpäivä
  * `[NEW-YEARS-EVE]` \- Uudenvuodenaatto
  * `[NORWEGIAN-CONSTITUTION-DAY]` \- Norjan kansallispäivä (17.5.)
  * `[ST-JOHNS-DAY]` \- Johannes Kastajan päivä (24.6.)
  * `[ST-JOHNS-DAY-EVE]` \- Johannes Kastajan päivän aatto (23.6.)
  * `[SWEDISH-NATIONAL-DAY]` \- Ruotsin kansallispäivä (6.6.)
  * `[WHIT-SUNDAY-GREGORIAN]` \- Helluntai
  * `[WHIT-MONDAY]` \- Toinen helluntaipäivä
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]` \- Sääntö on voimassa koko viikolla, jos jollain viikon päivänä on työviikkoa lyhentävä juhlapyhä. Asetuksissa asetettu työviikon aloituspäivä otetaan huomioon, eli viikko voi olla esimerkiksi keskiviikosta tiistaihin.
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|COMPENSATED]` \- Sääntö on voimassa koko viikolla, jos jollain viikon päivänä on juhlapyhä josta ansaitaan juhlapyhäkorvaus. Asetuksissa asetettu työviikon aloituspäivä otetaan huomioon, eli viikko voi olla esimerkiksi keskiviikosta tiistaihin.
  * `[WEEK-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]` \- Sääntö on voimassa koko viikolla, jos jollain viikon päivänä on juhlapyhä. Juhlapyhän katsotaan olevan viikolla, vaikka siitä ei ansaita korvausta eikä se lyhennä työviikkoa. Asetuksissa asetettu työviikon aloituspäivä otetaan huomioon, eli viikko voi olla esimerkiksi keskiviikosta tiistaihin.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHORTENS-WEEK]` \- Sääntö on voimassa koko tasoittumisjaksolla, jos jollain tasoittumisjakson työpäivänä on työviikkoa lyhentävä juhlapyhä.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|COMPENSATED]` \- Sääntö on voimassa koko tasoittumisjaksolla, jos jollain tasoittumisjakson työpäivänä on juhlapyhä josta ansaitaan juhlapyhäkorvaus.
  * `[LEVELLING-PERIOD-HAS-PUBLIC-HOLIDAYS|SHOWN-AS-PUBLIC-HOLIDAY]` \- Sääntö on voimassa koko tasoittumisjaksolla, jos jollain tasoittumisjakson päivänä on juhlapyhä. Juhlapyhän katsotaan olevan tasoittumisjaksolla, vaikka siitä ei ansaita korvausta eikä se lyhennä työviikkoa.
  * `[EMPLOYMENT-LASTED-LESS-THAN-12-MONTHS-AT-END-OF-ANNUAL-HOLIDAY-YEAR]` \- Sääntö on voimassa, kun halutaan, että henkilö ei ansaitse täyttä vuosilomapäivien määrää, jos työsuhde on kestänyt alle 12 kuukautta lomanansaintakauden päättyessä (31.3.). Jos henkilön työsuhteen päättymispäivä ei ole tiedossa palvelu olettaa henkilön työsuhteen jatkuvan myös seuraavalle lomanansaintakaudelle.
    * Jos henkilön työsuhteen alkamispäivä on 1.4. ja työsuhteen päättymispäivää ei ole asetettu, tämä poikkeussääntö ei tee mitään.
      * Jos tässä esimerkissä henkilön työsuhteen päättymispäiväksi merkitäänkin tämän poikkeusasetuksen asettamisen jälkeen huhtikuussa tai myöhemmin oleva päivä tulee henkilön laskenta päivittää, jotta tämä poikkeusasetus tulee voimaan.
    * Jos henkilön työsuhteen aloituspäivä on edellisen vuoden tammikuussa ja työsuhteen päättymispäivä on tyhjä, tämä poikkeusasetus on voimassa tammikuusta seuraavan lomanansaitavuoden alkuun. Tällöin oletetaan, että henkilö työskentelee myös seuraavan lomanansaintakauden, jolloin ansaitaan normaali määrä vuosilomaa (eli tämä poikkeusasetus ei ole voimassa seuraavalla lomanansaintakaudella).
      * Jos tässä esimerkissä henkilölle lisätään työsuhteen päättymispäivä elokuulle, ei henkilön ansainta ole oikein huhtikuusta elokuuhun. Tällöin henkilön laskenta tulee päivittää, jotta laskenta menee halutusti.
  * `[ACCRUAL-EARNING-PERIOD-START-DATE|ACCRUALNAME]` \- Sääntö on voimassa määritetyn kertymän ansaintakauden alkupäivämäärinä. Tällä hetkellä järjestelmä tukee tätä sääntöä seuraavissa kertymissä:
    * Tasoittumisjakso
      * asetetaan _[ACCRUAL-EARNING-PERIOD-START-DATE|levellingperiodhours]_
    * Joustotyötunnit
      * asetetaan _[ACCRUAL-EARNING-PERIOD-START-DATE|flexibleworkhours]_
    * Sääntöä voidaan hyödyntää useassa kertymässä, esimerkiksi:
      * _[ACCRUAL-EARNING-PERIOD-START-DATE|flexibleworkhours|levellingperiodhours]_
  * `[ACCRUAL-EARNING-PERIOD-END-DATE|ACCRUALNAME]` \- Sääntö on voimassa määritetyn kertymän ansaintakauden loppupäivämäärinä. Tällä hetkellä järjestelmä tukee tätä sääntöä seuraavissa kertymissä:
    * Tasoittumisjakso
      * asetetaan _[ACCRUAL-EARNING-PERIOD-END-DATE|levellingperiodhours]_
    * Joustotyötunnit
      * asetetaan _[ACCRUAL-EARNING-PERIOD-END-DATE|flexibleworkhours]_
    * Sääntöä voidaan hyödyntää useassa kertymässä, esimerkiksi:
      * _[ACCRUAL-EARNING-PERIOD-END-DATE|flexibleworkhours|levellingperiodhours]_


Jos poikkeusasetus halutaan määrittää koskemaan kaikkia suomalaisia **arkipyhiä** , voidaan käyttää seuraavaa poikkeusasetusta:
[ANY-PUBLIC-HOLIDAY-IN|EPIPHANY|GOOD-FRIDAY-GREGORIAN|EASTER-MONDAY-GREGORIAN|ASCENSION-DAY-GREGORIAN|MAY-DAY|MIDSUMMERS-EVE|INDEPENDENCE-DAY|CHRISTMAS-EVE|CHRISTMAS-DAY|BOXING-DAY|NEW-YEARS-DAY]
Jos poikkeusasetus halutaan määrittää koskemaan kaikkia suomalaisia **pyhäpäiviä** , voidaan käyttää seuraavaa poikkeusasetusta:
[ANY-PUBLIC-HOLIDAY-IN|EPIPHANY|GOOD-FRIDAY-GREGORIAN|HOLY-SATURDAY-GREGORIAN|EASTER-SUNDAY-GREGORIAN|EASTER-MONDAY-GREGORIAN|ASCENSION-DAY-GREGORIAN|MAY-DAY|WHIT-SUNDAY-GREGORIAN|MOTHERS-DAY|MIDSUMMERS-EVE|MIDSUMMERS-DAY|ALL-SAINTS-DAY|FATHERS-DAY|INDEPENDENCE-DAY|CHRISTMAS-EVE|CHRISTMAS-DAY|BOXING-DAY|NEW-YEARS-DAY]
Tutustu myös [juhla- ja arkipyhien käsittelyn asetuksiin](<https://support.nepton.com/hc/fi/articles/360002558797>).
Juhlapyhien lisäksi käytettävissä on seuraavat sääntökomennot:
  * `[YEAR]` \- Käytetään vuoden korvaamiseen päivämäärässä, jolloin vastaavuus on minä tahansa vuonna
  * `[MONTH]` \- Käytetään kuukauden korvaamiseen päivämäärässä, jolloin vastaavuus on minä tahansa kuukautena annettuna vuotena
  * `[DAY]` \- Käytetään päivän korvaamiseen päivämäärässä, jolloin vastaavuus on minä tahansa päivänä annettuna kuukautena ja vuotena
  * `[YEAR-EPIPHANY-ON-WEEKEND]` \- Käytetään vuoden korvaamiseen päivämäärässä, vastaavuus vuosina, jolloin Loppiainen on viikonloppuna
  * `[YEAR-EPIPHANY-NOT-ON-WEEKEND]` \- Käytetään vuoden korvaamiseen päivämäärässä, vastaavuus vuosina, jolloin Loppiainen ei ole viikonloppuna
  * `[YEAR-LEAP-YEAR]` \- Käytetään vuoden korvaamiseen päivämäärässä, vastaavuus vuosina jotka ovat karkausvuosia
  * `[YEAR-NOT-LEAP-YEAR]` \- Käytetään vuoden korvaamiseen päivämäärässä, vastaavuus vuosina jotka eivät ole karkausvuosia
  * `[LAST-FRIDAY-IF-ON-WEEKEND]` \- Käytetään päivämäärän tai juhlapyhän sääntökomennon lisänä, vastaavuus päivästä edellisenaä perjantaina, jos päivä on viikonloppuna
  * `[NEXT-MONDAY-IF-ON-WEEKEND]` \- Käytetään päivämäärän tai juhlapyhän sääntökomennon lisänä, vastaavuus päivästä seuraavana maanantaina, jos päivä on viikonloppuna
  * `[ODD-WEEK-NUMBERS]` \- Käytetään tarkistamaan onko päivä viikolla jonka viikkonumero on pariton
  * `[EVEN-WEEK-NUMBERS]` \- Käytetään tarkistamaan onko päivä viikolla jonka viikkonumero on parilllinen
  * `[WEEK-NUMBERS|1|2|5]` \- Käytetään tarkistamaan onko päivä viikolla jolla on tietty viikkonumero. Viikkonumerot joita tarkistetaan asetetaan eriteltynä | merkillä, esimerkkikomennossa sääntö toteutuu viikoilla joiden viikkonumero on 1, 2 tai 5.
  * `[WEEKDAY|1|2]` \- Käytetään poikkeussäännössä triggeröitymään kuukauden ensimmäisenä (tai tosena, jne) päivänä joka osuu muulle kuin lauantaille tai sunnuntaille. Jos haluat säännön, joka muuttaa säännön arvoa vain arkipäivinä, eikä arkipyhinä, sinun tulee tehdä kaksi poikkeussääntöä, joista ensimmäinen pitää käyttäytymisen normaalina, jos päivällä on arkipyhä. Näiden poikkeussääntöjen tulee siis olla juuri allaolevassa järjestyksessä, tai poikkeussäännöt eivät toimi halutusti:  
  
![](https://support.nepton.com/hc/article_attachments/34607391953437)


Poikkeusasetus voidaan asettaa joko ylläolevilla sääntökomennoilla tai suoraan päivämäärämuotoisena (pp.kk.vvvv). Säännön perään voidaan myös asettaa komentoja, joilla määritetään poikkeusasetuksen voimassaolopäivä juhlapyhästä laskettuna:
  * **+1 day** poikkeus on voimassa juhlapyhän jälkeisenä päivänä (esim. `[BOXING-DAY] +1 day`)
  * **-1 day** poikkeus on voimassa päivää ennen juhlapyhää (esim. `[ASCENSION-DAY-GREGORIAN] -1 day`)
  * **+1 week** poikkeus on voimassa viikon kuluttua (7 päivää) juhlapyhästä
  * **-1 week** poikkeus on voimassa viikkoa aiemmin (7 päivää) ennen juhlapyhää
  * **next Saturday** poikkeus on voimassa seuraavana lauantaina (esim. `[NEW-YEARS-EVE] next Saturday`). Sääntö toimii kaikilla viikonpäivän nimillä. Viikonpäivän nimen täytyy olla englanniksi.
  * **previous Saturday** poikkeus on voimassa edellisenä lauantaina (esim. `[MAY-DAY] previous Saturday`). Sääntö toimii kaikilla viikonpäivän nimillä. Viikonpäivän nimen täytyy olla englanniksi.


Day-arvo voi olla mikä tahansa luku riippuen siitä, kuinka monta päivää eteenpäin tai taaksepäin poikkeus on tarkoitus määrittää.
Nämä komennot ovat hyödyllisiä tilanteissa, jossa esimerkiksi loppiaista edeltävälle päivälle halutaan antaa jokin poikkeusasetus, esimerkiksi työpäivän pituus. Tällöin poikkeukselle asetettava sääntö olisi muotoa `[EPIPHANY] -1 day`.
Poikkeusasetuksella voidaan asettaa muutos koskemaan jonkin viikon päiviä. Esimerkiksi poikkeuksen, joka on voimassa jouluaattoviikolla voi asettaa seuraavalla säännöllä.
`23.12.[YEAR] monday this week,`  
`23.12.[YEAR] tuesday this week,`  
`23.12.[YEAR] wednesday this week,`  
`23.12.[YEAR] thursday this week, `  
`23.12.[YEAR] friday this week,`  
`23.12.[YEAR] saturday this week,`  
`23.12.[YEAR] sunday this week`
Viikonpäiviä koskevia asetuksia voidaan käyttää myös sääntöjen `[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS]` ja `[WORK-WEEK-HAS-PUBLIC-HOLIDAYS]` kanssa. Koska asetuksissa asetettu työviikon aloituspäivä otetaan huomioon, ei ole syytä käyttää esimerkiksi määritteitä 'next' tai 'this week', vaan käyttää vain viikonpäiviä. Esimerkiksi poikkeukset kullekin viikonpäivälle viikkoina joilla on juhlapyhä voidaan määrittää seuraavasti.
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Monday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Tuesday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Wednesday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Thursday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Friday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Saturday`  
`[CALENDAR-WEEK-HAS-PUBLIC-HOLIDAYS] Sunday`
## Tapahtumatyypin sääntökomennot
Nämä komennot mahdollistavat poikkeusasetusten määrittämisen perustuen tapahtumatyyppeihin joita päivälle on merkitty.
Sääntö-ikkunan vieressä olevaa taikasauva-ikonia klikkaamalla aukeaa työkalu, joka auttaa tapahtumatyyppien ja tapahtumatyyppien kategorioiden sääntökomentojen asettamisessa.
Alla kuvaus tapahtumatyyppeihin ja niiden kategorioihin perustuvista komennoista.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|101|102]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtumia joiden tapahtumatyypin koodi on 101 tai 102.
  * `[WORK-DAY-HAS-ALL-OF-EVENT-TYPES|101|102]`
    * Sääntö toteutuu jos työpäivän¹ aikana on sekä tapahtumia joiden tapahtumatyypin koodi on 101 että tapahtumia joiden tapahtumakoodi on 102.
  * `[WORK-DAY-HAS-NONE-OF-EVENT-TYPES|101|102]`
    * Sääntö toteutuu jos työpäivän¹ aikana ei ole tapahtumia joiden tapahtumatyypin koodi on 101 tai 102.
  * `[WORK-DAY-HAS-EVENT-TYPES-OTHER-THAN|101|102]`
    * Sääntö toteutuu jos työpäivän¹ aikana on jotain muita tapahtumia kuin sellaisia joiden tapahtumatyypin koodi on 101 tai 102.
  * `[WORK-DAY-HAS-ANY-OF-ABSENCE-TYPES|1|2]`
    * Sääntö toteutuu jos työpäivän¹ aikana on poissaolotapahtumia, joiden poissaolotyypin koodi on 1 tai 2
  * `[WORK-DAY-HAS-ABSENCE-TYPES-OTHER-THAN|1|2]`
    * Sääntö toteutuu jos työpäivän¹ aikana on jotain muita poissaolotapahtumia kuin sellaisia joiden poissaolotyypin koodi on 1 tai 2.
  * `[WORK-DAY-HAS-ANY-OF-PLANNED-EVENT-TYPES|101|102]`
    * Sääntö toteutuu jos työpäivän¹ aikana on vuorokalenterin suunniteltuja työvuoroja joiden suunnitellun tapahtumatyypin koodi on esimerkiksi 101 tai 102.
  * `[WORK-DAY-HAS-ANY-OF-PLANNED-EVENT-ALIASES|A|Y]`
    * Sääntö toteutuu jos työpäivän¹ aikana on vuorokalenterin suunniteltuja vuorotyyppejä joiden lyhenne on esimerkiksi A tai Y
  * `[WORK-DAY-SHIFT-TYPE-ADDITIONAL-INFO-CONTAINS-ANY|I1430-2230]`
    * Sääntö toteutuu jos työpäivän¹ aikana on vuorokalenterin suunniteltuja vuorotyyppejä joiden vuorotyypin lisätiedoissa on merkkijono `I1430-2230`.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-CATEGORIES|WORK|ABSENCE]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtumia joiden tapahtumatyypin kategoria on työtä (WORK) tai poissaolo (ABSENCE). Kategorioita ovat työ, poissaolo, hallinta ja muut. Komennot tulee olla englanniksi isoilla kirjaimilla, eli "WORK", "ABSENCE", "ADMINISTRATION" ja "OTHER". Se mikä tapahtumatyyppi kuuluu mihinkin kategoriaan näkyy tapahtuman muokkauksen yhteydessä.
  * `[WORK-DAY-HAS-NONE-OF-EVENT-CATEGORIES|ABSENCE]`
    * Sääntö toteutuu jos työpäivän¹ aikana ei ole mitään poissaolo-kategorian (ABSENCE) tapahtumatyypin tapahtumaa kuten sairausloma, poissaolo tms.
  * `[WORK-DAY-HAS-EVENTS-WITH-BASE-PART|balance|bank]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma jolle on kirjattaessa merkitty ylityön perusosan kohdenteeksi saldo ("balance") tai pankki ("bank").
    * Tämän ohjeen alussa kuvattua taikasauvatyökalua voi käyttää apuna oikeiden ylityön kohdennetyyppien valitsemisessa.
  * `[WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART|balance|bank]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma jolle on kirjattaessa merkitty ylityön korotusosan kohdenteeksi saldo ("balance") tai pankki ("bank").
    * Tämän ohjeen alussa kuvattua taikasauvatyökalua voi käyttää apuna oikeiden ylityön kohdennetyyppien valitsemisessa.
  * `[WORK-DAY-BEGINS-BEFORE|06:00]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma joka alkaa ennen klo 06:00. 06:00 tilalla voi olla mikä tahansa kellonaika jota halutaan verrata tapahtuman aloitusaikaan. Mikä tahansa kirjattu tapahtuma aktivoi poikkeusasetuksen, myös esimerkiksi Huomautus-tapahtuma tai Korjaus-tapahtuma. 
    * Määritettävä alkamisajan arvo voi olla negatiivinen jos halutaan kohdentaa tarkistus tapahtumiin jotka alkavat edeltävänä päivänä. Esimerkiksi jos halutaan tarkistaa alkaako työ edeltävänä päivänä ennen klo 22:00, säännöksi kirjoitetaan [WORK-DAY-BEGINS-BEFORE|-02:00].
    * Määritettävä alkamisajan arvo voi olla yli 24 jos halutaan kohdentaa tarkistus tapahtumiin jotka alkavat seuraavana päivänä. Esimerkiksi jos halutaan tarkistaa alkaako työ seuraavana päivänä ennen klo 2:00, säännöksi kirjoitetaan [WORK-DAY-BEGINS-BEFORE|26:00].
  * `[WORK-DAY-BEGINS-AFTER|06:00]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma joka alkaa klo 06:00 tai sen jälkeen. 06:00 tilalla voi olla mikä tahansa kellonaika jota halutaan verrata tapahtuman aloitusaikaan. Mikä tahansa kirjattu tapahtuma aktivoi poikkeusasetuksen, myös esimerkiksi Huomautus-tapahtuma tai Korjaus-tapahtuma. 
    * Määritettävä alkamisajan arvo voi olla negatiivinen jos halutaan kohdentaa tarkistus tapahtumiin jotka alkavat edeltävänä päivänä. Esimerkiksi jos halutaan tarkistaa alkaako työ edeltävänä päivänä klo 22:00 tai sen jälkeen, säännöksi kirjoitetaan [WORK-DAY-BEGINS-AFTER|-02:00].
    * Määritettävä alkamisajan arvo voi olla yli 24 jos halutaan kohdentaa tarkistus tapahtumiin jotka alkavat seuraavana päivänä. Esimerkiksi jos halutaan tarkistaa alkaako työ seuraavana päivänä klo 2:00 tai sen jälkeen, säännöksi kirjoitetaan [WORK-DAY-BEGINS-AFTER|26:00].
  * `[WORK-DAY-BEGINS-BEFORE-BY-CATEGORY|06:00|WORK|ABSENCE]`
    * Toimii kuten `[WORK-DAY-BEGINS-BEFORE|06:00]`, mutta päivän pitää alkaa tapahtumatyypillä joka kuuluu yhteen säännössä määritetyistä kategorioista.
  * `[WORK-DAY-BEGINS-AFTER-BY-CATEGORY|07:00|WORK]`
    * Toimii kuten `[WORK-DAY-BEGINS-AFTER|06:00]`, mutta päivän pitää alkaa tapahtumatyypillä joka kuuluu yhteen säännössä määritetyistä kategorioista.
  * `[WORK-DAY-BEGINS-BEFORE-BY-EVENT-TYPE|06:00|101|102]`
    * Toimii kuten `[WORK-DAY-BEGINS-BEFORE|06:00]`, mutta päivän pitää alkaa tapahtumatyypillä jonka koodi on yksi määritetyistä tapahtumatyypin koodeista.
  * `[WORK-DAY-BEGINS-AFTER-BY-EVENT-TYPE|06:00|101]`
    * Toimii kuten `[WORK-DAY-BEGINS-AFTER|06:00]`, mutta päivän pitää alkaa tapahtumatyypillä jonka koodi on yksi määritetyistä tapahtumatyypin koodeista.


Näitä komentoja voidaan yhdistellä keskenään sekä useimpien päivämääräkomentojen kanssa, esim.
  * `[WORK-DAY-HAS-ANY-OF-EVENT-TYPES|101] Monday`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma jonka tapahtumatyyppi on 101 ja on maanantai.
  * `[WORK-DAY-HAS-EVENTS-WITH-BASE-PART|salary|bank] [WORK-DAY-HAS-EVENTS-WITH-OVERTIME-PART|salary|bank]`
    * Sääntö toteutuu jos työpäivän¹ aikana on tapahtuma jonka ylityön perusosan kohdenteeksi on kirjattu palkka ("salary") tai pankki ("bank") JA työpäivän¹ aikana on tapahtuma jonka ylityön korotusosan kohdenteeksi on kirjattu palkka ("salary") tai pankki ("bank").


¹Työpäivä tässä kontekstissa tarkoittaa kaikkia tapahtumia jotka kuuluvat siihen päivään perustuen "TES" -> "Työviikon aloitusaika" asetuksessa asetettuun arvoon, joka on oletuksena keskiyö. Huom: Tietyt asetukset kuten sallitut työajat, odotetut työajat ja työkorotusten ajat eivät tue täysin "Työpäivän" konseptia koska nämä asetukset muodostavat osan laskennasta jonka perusteella työpäivä määritetään. Tätä tullaan parantamaan tulevissa versioissa.
## Poissaolotyypin sääntökomennot
Poissaolotyypin voi määritellä poikkeusasetuksessa seuraavalla SQL-lausekkeella:
FROM  
UserEventData  
WHERE  
ActivityTypeCode = 4  
AND AbsenceTypeId = halutun poissaolotyypin ID
tai jos halutaan määritellä useampi poissaolotyyppi (123 ja 124 ovat kuvitteellisia koodeja):  
FROM  
UserEventData  
WHERE  
ActivityTypeCode = 4  
AND AbsenceTypeId IN (123, 124)  
  

## Esimerkkejä mahdollisista poikkeusasetuksista
Suoraan juhlapyhiin kohdistuvien sääntökomentojen lisäksi poikkeus on mahdollista määrittää päivään, kuukauteen tai vuoteen kohdistuvilla komennoilla. 
  * Jos asetusarvo on muuten aina sama, paitsi **jonain tiettynä päivänä** , voidaan säännöksi määrittää päivämäärä esimerkiksi:  
`19.2.2017`  
Päivämäärän tulee olla muodossa `pp.kk.vvvv`


  * Jos asetusarvo on muuten aina sama, paitsi **jonain tiettynä päivänä joka vuosi** , voidaan säännöksi määrittää esimerkiksi:  
`25.12.[YEAR]`


  * Jos asetusarvo on muuten aina sama, paitsi **joka kuukauden 5. päivä** , voidaan säännöksi määrittää esimerkiksi:  
`05.[MONTH].[YEAR]`


  * Jos asetusarvo on muuten aina sama, paitsi **kuukauden minä tahansa päivänä** , voidaan säännöksi määrittää esimerkiksi:  
`[DAY].01.2016`


  * Jos asetusarvon halutaan olevan aina sama, paitsi **karkauspäivänä** , voidaan säännöksi määrittää:  
`29.02.[YEAR-LEAP-YEAR]`


  * Jos asetusarvon halutaan olevan aina sama, paitsi **helmikuun viimeinen päivä vuosina, jotka eivät ole karkausvuosia** , voidaan säännöksi määrittää:  
`28.02.[YEAR-NOT-LEAP-YEAR]`


  * Jos asetusarvon halutaan olevan aina sama, mutta vain **loppiaisena, joka on viikonloppuna** , voidaan säännöksi määrittää:  
`06.01.[YEAR-EPIPHANY-ON-WEEKEND]`


  * Jos asetusarvon halutaan olevan aina sama, paitsi **loppiaisena, joka ei ole viikonloppuna** , voidaan säännöksi määrittää:  
`06.01.[YEAR-EPIPHANY-NOT-ON-WEEKEND]`


  * Jos asetusarvon halutaan olevan aina sama, paitsi **edeltävänä perjantaina kun jouluaatto on viikonloppuna** , voidaan säännöksi määrittää:  
`[CHRISTMAS-EVE] [LAST-FRIDAY-IF-ON-WEEKEND]`


  * Jos asetusarvon halutaan olevan aina sama, paitsi **seuraavana maanantaina kun itsenäisyyspäivä on viikonloppuna** , voidaan säännöksi määrittää:  
`[INDEPENDENCE-DAY] [NEXT-MONDAY-IF-ON-WEEKEND]`


  * Jos asetusarvo on muuten aina sama, paitsi **tiettynä viikonpäivänä tai viikonpäivinä** , voidaan säännöksi määrittää esimerkiksi:  
`Sunday` tai `Monday,Tuesday,Wednesday,Thursday,Friday`  
HUOM! Viikonpäivien yhteydessä ei käytetä hakasulkuja.


  * Jos asetusarvo on muuten aina sama, paitsi **joka kuukauden viimeisenä päivänä,** voidaan säännöksi määrittää:  
`[DAY].[MONTH].[YEAR] last day of this month`


  * Jos asetusarvo on muuten aina sama, paitsi **lauantaina ja sunnuntaina viikoilla, joilla jollain viikon työpäivänä on juhlapyhä** , voidaan säännöksi määrittää:  
`[WORK-WEEK-HAS-PUBLIC-HOLIDAYS] Saturday, [WORK-WEEK-HAS-PUBLIC-HOLIDAYS] Sunday`


## Poikkeuksen asettaminen SQL -lausekkeena
Poikkeusasetuksen voi tehdä myös **SQL -lausekkeena**. Tämä on tarkoitettu käytettäväksi tilanteissa, jolloin poikkeusasetusta ei muuten saada määritettyä. Asetuksen tekeminen tällä tavalla edellyttää SQL-kielen riittävää osaamista.
SQL -lauseketta käyttävät poikkeukset ovat suorituskyvyltään raskaampia kuin sääntökomennot, ja voivat aiheuttaa hitautta palvelun käytössä, joten SQL -lausekkeiden käyttö ei ole suositeltavaa, ellei haluttua asetusta ole mahdollista saada millään muulla tavalla.
![](https://support.nepton.com/hc/article_attachments/35359370054813)
Poikkeuksia voidaan tehdä esimerkiksi niissä tapauksissa, kun asetuksen arvon halutaan olevan erilainen perustuen palveluun kirjattuihin tapahtumiin tai henkilön tietoihin. Mahdollisina poikkeuksina voidaan kirjoittaa mikä tahansa SQL -lauseke, joka hyödyntää UserEventData, UserData ja UserInfoData - taulujen rakennetta. SQL -lauseke kirjoitetaan FROM avainsanasta alkaen.
Tarkemmat ohjeet taulujen sisältöön ja käytettävissä oleviin funktioihin on esitetty ohjesivulla [Sääntöjoukon poimintasääntöjen muodostaminen](<https://support.nepton.com/hc/fi/articles/360002489257>). Esitetyn rakenteen lisäksi voi käyttää avainsanaa ':SalaryRenderingDate', joka korvataan SQL lausekkeessa sillä vuorokauden päivämäärällä (YYYY-MM-DD), jonka päivän sääntöjä päätellään.
Esimerkki, jossa poikkeuksella voidaan ohjata käyttämään tiettyä sääntöä, kun työleimaus alkaa samana päivänä (eli aloitus aikaisintaan saman päivän keskiyönä tai sen jälkeen) ja aloitus on tapahtunut ennen kello 22:00 tai tasan kello 22:00.
Suositeltava tapa tällaisessa tilanteessa on käyttää sääntökomentoja commands WORK-DAY-HAS-ANY-OF-EVENT-TYPES ja WORK-DAY-BEGINS-BEFORE
Huomioi että WORK-DAY-BEGINS-BEFORE - komento koskee aikoja ennen annettua arvoja, eli jos halutaan tarkistaa tapahtumia jotka alkavat **ennen klo 22:00 tai tarkalleen 22:00** , sääntökomennolle määritetään haettavan tapahtumia ennen 22:01, eli [WORK-DAY-BEGINS-BEFORE|22:01] kuten alla:
[code]
    [WORK-DAY-HAS-ANY-OF-EVENT-TYPES|1] 
    [WORK-DAY-BEGINS-AFTER|00:00] 
    [WORK-DAY-BEGINS-BEFORE|22:01]
[/code]
Sama esimerkki SQL lausekkeena. Tällaisissa esimerkeissä on syytä määritellä myös tapahtuman alkuajan rajaus, jotta edelliseltä päivällä jatkuva leimaus ei vaikuta säännön tuloksiin.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND StartDateTime <= :SalaryRenderingDate || ' ' || '22:00'
      AND StartDateTime >= :SalaryRenderingDate || ' ' || '00:00'
[/code]
Esimerkki, jossa poikkeuksella voidaan ohjata käyttämään tiettyä sääntöä, kun työleimaus alkaa jälkeen 22:00 ja ennen 24:00 tai tarkalleen 24:00:
Suositeltava tapa tällaisessa tilanteessa on käyttää sääntökomentoja commands WORK-DAY-HAS-ANY-OF-EVENT-TYPES ja WORK-DAY-BEGINS-BEFORE
Huomioi että WORK-DAY-BEGINS-BEFORE - komento koskee aikoja ennen annettua arvoja, eli jos halutaan tarkistaa tapahtumia jotka alkavat **ennen klo 24:00 tai tarkalleen 24:00** , sääntökomennolle määritetään haettavan tapahtumia ennen 24:01, eli [WORK-DAY-BEGINS-BEFORE|24:01]. Tämä on mahdollista koska sääntökomento tukee arvoja yli 24 tunnin jolloin tarkastelujakso siirtyy seuraavalle päivälle. Sääntö kirjoitetaan tässä tapauksessa kuten alla:
[code]
    [WORK-DAY-HAS-ANY-OF-EVENT-TYPES|1] 
    [WORK-DAY-BEGINS-AFTER|22:00] 
    [WORK-DAY-BEGINS-BEFORE|24:01]
[/code]
Sama esimerkki SQL-lausekkeella:
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND StartDateTime >= :SalaryRenderingDate || ' ' || '22:00'
      AND StartDateTime <= :SalaryRenderingDate || ' ' || '24:00'
[/code]
Esimerkki, jossa poikkeuksella voidaan ohjata käyttämään tiettyä sääntöä, kun henkilön oletuskalleusluokan arvo kyseisenä päivänä on 1011:
[code]
    FROM
      UserInfoData
    WHERE
      datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND InfoTypeName = 'DefaultCostGroupCode'
      AND Value = 1011
[/code]
Esimerkki, jota käytetään vain, kun päivälle on kirjattu tiettyä tapahtumatyyppiä ja viikonpäivä on lauantai tai sunnuntai. Viikonpäivä on 0-6, jossa sunnuntai = 0.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 100
      AND strftime('%w',:SalaryRenderingDate) IN (0, 6)
[/code]
Esimerkki, jossa määritellään milloin ansaitaan vuosilomalain mukainen 2.5 vuosilomapäivää kuukaudessa.
Valmista sääntökomentoa käyttäen:
![](https://support.nepton.com/hc/article_attachments/35359393032221)
SQL -lauseketta käyttäen 2.5 pv/kk (huomioithan, että tässä ei oteta huomioon työsuhteen päättymispäivää):   

[code] 
    FROM
      UserInfoData
    WHERE
      InfoTypeName = 'LastWorkingContractBeginDate'
      AND datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND
       ((Value <= substr(:SalaryRenderingDate, 1,4) || '-04-01' -- contract starts earlier than 1.4 or exactly on 1.4 the salaryRenderingDate year
         AND :SalaryRenderingDate >= substr(:SalaryRenderingDate, 1,4) || '-04-01') -- and we live date exact or later than 1.4 on the salaryRenderingdate
        OR
        (Value < CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 1 AS Char(4)) || '-04-01')) -- contract starts earlier than last year 1.4
     
    
[/code]
Esimerkki, jossa määritellään milloin ansaitaan esim. KVTES-mukainen 3 vuosilomapäivää kuukaudessa (vähintään 15 vuoden työsuhde). Huom! Jos käytät myös 2.5 vuosilomapäivän poikkeussääntöä yllä, lisää tämä poikkeusasetus poikkeuslistalle ennen sitä, jotta tätä sääntöä sovelletaan ensisijaisesti, jos molemmat säännöt toteutuvat.
[code]
    FROM
      UserInfoData
    WHERE
      InfoTypeName = 'LastWorkingContractBeginDate'
      AND datetime(:SalaryRenderingDate) BETWEEN ValidFrom AND ValidTo
      AND
       ((Value <= CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 14 AS Char(4)) || '-04-01' -- contract starts 1.4. or earlier on a year 14 years ago from day we are calculating earned annual leave days for
         AND :SalaryRenderingDate >= substr(:SalaryRenderingDate, 1,4) || '-04-01') -- and day we are getting this setting for is 1.4. or later
        OR
        (Value <= CAST(CAST(substr(:SalaryRenderingDate, 1,4) AS Integer) - 15 AS Char(4)) || '-04-01')) -- contract started earlier or on 1.4. on a year 15 years ago from day we are calculating earned annual leave days for
    
    
    
[/code]
Esimerkki, jota käytetään vain, kun päivälle on kirjattu tiettyä tapahtumatyyppiä ja vuoden ja viikon numero on määritellyllä listalla. Viikonnumerot ovat 00-53:
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 100
      AND strftime('%Y',:startdatetime) = 2019
      AND strftime('%W',:startdatetime) IN ('00','01','10','11')
[/code]
Esimerkki, jossa poikkeus on voimassa, kun päivälle on kirjattu tapahtumatyyppiä työ, jonka kirjattu aika ylittää 3 tuntia:
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 1
      AND DATE(startDateTime) = :SalaryRenderingDate
    GROUP BY
      ActivityTypeCode
    HAVING
      SUM(Amount) >= 3 * 3600
[/code]
HUOM! Ylläoleva poikkeussääntö on hyödyllinen esimerkiksi ruokatauon tulkinnassa. Poikkeusäännön myötä päivällä voi olla työaikaa yhteensä esim. 10 tuntia muilla tapahtumatyypeillä kirjattuna, mutta jos poikkeussäännössä olevalla tapahtumatyypillä kirjattu työaika ei ylitä 3 tuntia, ruokataukoa ei automaattisesti vähennetä. 
Esimerkki, jossa poikkeus on voimassa viikoilla, joilla on pariton viikkonumero. Esimerkiksi viikot numeroilla 1, 3, 5, jne.
[code]
    [ODD-WEEK-NUMBERS]
[/code]
Esimerkki, jossa poikkeus on voimassa viikoilla, joilla on parillinen viikkonumero. Esimerkiksi viikot numeroilla 2, 4, 6, jne.
[code]
    [EVEN-WEEK-NUMBERS]
[/code]
Esimerkki, jossa poikkeus on voimassa itsenäisyyspäivän viikolla, kun itsenäisyyspäivä on arkipäivänä (ma-pe).
[code]
    FROM
      UserData
    WHERE
      strftime('%W', :salaryRenderingDate) = strftime('%W', strftime('%Y', :salaryRenderingDate) || '-12-06')
      AND CAST(strftime('%w', strftime('%Y', :salaryRenderingDate) || '-12-06') AS INTEGER) IN (1,2,3,4,5)
      /* this will set the rule to apply on the week of independence day if the independence
      day is on monday-friday */
      
[/code]
Esimerkki, jossa poikkeus on voimassa jos henkilön työsuhteen alkupäivästä on kulunut alle 3 kuukautta siitä päivästä jolloin sääntöä käsitellään. Vertailuarvossa date(:SalaryRenderingDate, '**-3 months** '). Viimeinen **korostettu** osa voidaan korvata halutulla arvolla.
[code]
    FROM 
      UserInfoData 
    WHERE 
      InfoTypeName = 'LastWorkingContractBeginDate' 
      AND Value > date(:SalaryRenderingDate, '-3 months')
[/code]
Esimerkki, jossa valitaan mikä tahansa henkilötiedoissa oleva kenttä. Tehdään sääntö, jossa poikkeus on voimassa jos kenttään syötetty päivämäärän arvo on pienempi kuin tarkasteltava päivä +3 kuukautta. Tälläista esimerkkiä voi käyttää tilanteessa, jossa henkilön tietokenttään perustetaan viimeisimmän työsuhteen alkupäivä. Tätä tietoa voidaan käyttää poikkeussäännössä, jos ei haluta työkorotuksen (esim arkipyhäkorvauksen) olevan voimassa silloin kun viimeisimmän työsuhteen alkupäivästä on alle 3kk. UserInfoTypeName tulee esimerkissä korvata sillä tietokentällä, johon tieto on syötetty. Jos kenttänä käytetään jotain muuta kuin päivämääräkenttää, tulee arvo syöttää amerikkalaisessa päivämäärämuodossa '2022-06-01'.
[code]
    FROM 
      UserInfoData 
    WHERE 
      UserInfoData.InfoTypeName = '236_ViimeisinTyosuhdeAlkoi' 
      AND  :salaryrenderingdate >= UserInfoData.ValidFrom
      AND :salaryrenderingdate <= UserInfoData.ValidTo 
      AND Value > date(:SalaryRenderingDate, '-3 months')
    
[/code]
Esimerkki, jossa poikkeus on voimassa, kun henkilö on leimannut päivälle tapahtumatyypillä Vuosiloma ja viikonpäivä on lauantai. Weekday-funktio palauttaa arvon 0-6, jossa 0 on maanantai ja 6 on sunnuntai.
[code]
    FROM
      UserEventData
    WHERE
      ActivityTypeCode = 'VL'
      AND Weekday(Startdatetime) = 5
[/code]
## Ongelmien tarkistaminen
Jos näet alla olevan kuvakkeen asetussivulla, tarkoittaa se, että poikkeusasetuksen säännön määrityksissä on ongelma. Ongelmaa voi tutkia avaamalla poikkeusasetuksen määritystyökalun ja etsimällä "INVALID" - mainintaa, esimerkiksi "INVALID-CODE: 123".
![mceclip0.png](https://support.nepton.com/hc/article_attachments/21080302725021)
