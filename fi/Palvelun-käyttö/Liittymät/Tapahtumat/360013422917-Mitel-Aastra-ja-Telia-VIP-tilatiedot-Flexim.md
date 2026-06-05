---
id: 360013422917
title: Mitel Aastra ja Telia VIP-tilatiedot (Flexim)
url: https://support.nepton.com/hc/fi/articles/360013422917-Mitel-Aastra-ja-Telia-VIP-tilatiedot-Flexim
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
updated_at: '2026-05-12T06:32:17Z'
edited_at: '2026-05-12T06:31:48Z'
---

# Mitel Aastra ja Telia VIP-tilatiedot (Flexim)

Palvelusta voidaan lähettää henkilöiden tilatietoja Mitel Aastra ja Telia VIP (ent. Telia Merex) puhelinjärjestelmiin. Tiedot lähetetään Flexim-kulunvalvontajärjestelmään, jonka tietoja puhelinjärjestelmät hyödyntävät.
## Määrittäminen
### Henkilöiden tunnusten määrittäminen
Henkilöiden tunnisteet integraatiota varten voidaan määrittää muokkaamalla henkilötietoja **Työsuhde - Henkilön tiedot - Tunnisteet - Aastra**. Sekä Aastra- että VIP (Merex)-tiedonsiirtoa varten käytetään asetuksissa olevaa "Aastra"-tunnistetta.
![aastra-identifier.png](https://support.nepton.com/hc/article_attachments/360012739237)
### Tapahtumatyyppien koodien määrittäminen
Tapahtumatyyppien koodit voidaan määrittää työyhteisön asetuksista, **Työaika** \- **Hallinta** \- **Työyhteisön asetukset** \- **Liittymät**. Aastran asetukset löytyvät kohdasta Mitel Aastra ja Telia VIPin asetukset kohdasta Telia Merex.
![aastra-wt-settings.PNG](https://support.nepton.com/hc/article_attachments/360012857318)
### Tapahtumatyyppien koodit
Tapahtumatyypeille määritetään koodit alla olevan taulukon mukaisesti.
Koodi | Selite  
---|---  
1 | Kokous  
2 | Sisällä (vastaa työajan aloittamista)  
3 | Ulkona (vastaa työajan loppumista)  
5 | Matkatyö  
6 | Loma / Työajan lyhennysvapaa / Saldovapaa  
7 | Sairasloma  
8 | Koulutus  
9 | Työ muualla  
0 | Ulkona muu syy (vastaa työajan loppumista)  
a | Lounas  
### Tietojen lähettäminen
Aastran host-osoitteen ja muut viennin asetukset saa asetettua työyhteisön asetuksista, _**Työaika** -**Hallinta** -**Työyhteisön asetukset** -**Liittymät** -**Mitel Aastra**_ \- **Kokoonpano**.
![aastra-kokoonpano.PNG](https://support.nepton.com/hc/article_attachments/360012782957)
Telia VIPin host-osoitteen ja muut viennin asetukset saa asetettua työyhteisön asetuksista, _**Työaika** -**Hallinta** -**Työyhteisön asetukset** -**Liittymät** -**Telia Merex**_ \- **Kokoonpano**. Palvelimen osoite tulee olla muodossa ”123.456.78.9:1234”, eli IP-osoite ja TCP-portti kaksoispisteellä erotettuina.
![merex-kokoonpano.PNG](https://support.nepton.com/hc/article_attachments/360012857338)
Kummassakin integraatiossa tilapäivityksiä lähetetään oletuksena maksimissaan 100 minuutissa. Viive lähetettyjen tilarivien välissä on oletuksena 500 millisekuntia. Näitä voi muokata omista asetuskohdistaan.
### Rajaukset
  * Työntekijät henkilönumerolla 0 eivät tule osaksi aineistoa


## Liittymän tekninen toiminta
Tilatiedot lähetetään minuutin välein määritetyn palvelimen osoitteeseen sellaisenaan yksi kerrallaan. Lähetys tapahtuu avatun TCP socketin kautta eikä liittymä ei odota paluusanomaa lähetettyihin tietoihin.
### Sanoman sisältö
Liittymä on vakioitu eikä tietosisältöön ole tarvetta tehdä muutoksia. Tilatieto on tabulaattorimerkillä erotettua tekstimuotoista dataa. Merkistökoodauksena on `ASCII`. Lähetettävät tiedot ovat kuvattu alla.
Tieto | Selite  
---|---  
Aloitusmerkki | Aloitusmerkkinä käytetään aina `STX` -merkkiä (Start of Text), ASCII HEX `02`.  
Tapahtumatyypin koodi |   
_Tabulaattori_ |   
Henkilön Aastra -tunnus / henkilönumero | Maksimissaan 11 merkkiä pitkä.  
_Tabulaattori_ |   
Muu syykoodi | Maksimissaan 3 merkkiä pitkä. Tietoa ei käytetä.  
_Tabulaattori_ |   
Tapahtuman päättymispäivä | Jos tapahtumalla ei ole tiedossa olevaa päättymispäivää, tieto lähetetään tyhjänä. Muotona `PPKK`, esimerkiksi `3105`.  
_Tabulaattori_ |   
Tapahtuman päättymispäivä | Jos tapahtumalla ei ole tiedossa olevaa päättymisaikaa, tieto lähetetään tyhjänä. Muotona `HHMM`, esimerkiksi `1230`.  
Tilatiedon tarkistemerkki | Tarkiste lasketaan vain Telia VIPin tilatietoihin, Mitel Aastran tilatiedoissa se jätetään pois.  
Lopetusmerkki | Lopetusmerkkinä käytetään aina `CR` -merkkiä (carriage return), ASCII HEX `0D`.  
### Odotettu vastaus
Liittymä ei odota vastausta lähetettyihin tilatietoihin. Jos tilatiedon lähetys TCP socketiin onnistuu, tilatieto katsotaan onnistuneesti lähetetyksi.
### Tarkistemerkin laskukaava
  1. Jokaisen tilatiedossa olevan merkin sijainti ASCII-taulukossa lasketaan ja nämä arvot lasketaan yhteen. Vain merkit ennen tarkistemerkkiä katsotaan.
  2. Otetaan yhteen lasketun summan 7 alinta bittiä kokonaislukuna.
  3. Jos kokonaisluku on alle 32, arvoon lisätään 32.
  4. Laskentakaavan tulos kertoo tarkistemerkin sijainnin ASCII taulukossa.


PHP esimerkki:
[code]
    <?php
    
    function getChecksum(string $string): string
    {
        $sum = array_sum(
            array_map(
                static function (string $chr): int {
                    return ord($chr);
                },
                str_split($string)
            )
        );
        $sum &= hexdec('0x7f');
        if ($sum < hexdec('0x20')) {
            $sum += hexdec('0x20');
        }
        return chr($sum);
    }
[/code]
### Esimerkki
`STX`, `TAB`, tarkiste (`CHECKSUM`) ja `CR` merkit visualisoituna esimerkkisanomassa.
[code]
    STX
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    TAB
[/code]
[code]
    CHECKSUM
[/code]
[code]
    CR
[/code]
