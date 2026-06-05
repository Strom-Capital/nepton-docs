---
id: 360003357238
title: Microsoft AX myyntilaskut
url: https://support.nepton.com/hc/fi/articles/360003357238-Microsoft-AX-myyntilaskut
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2020-02-13T06:55:26Z'
---

# Microsoft AX myyntilaskut

## Tiedostomuoto
Siirtotiedosto on positioeroteltua tekstimuotoista dataa. Rivinvaihtona on CRLF. Siirretään aineiston jokaiselle kustannuspaikalle (cost group) yksi laskurivi ja 0..n laskuriviä.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Otsikkorivi
Tieto | Positio | Pituus | Huom. | Esim.  
---|---|---|---|---  
Yritysnumero | 1 | 2 | MicrosoftAxHeaderCompanyNumber | 11, 19, 29, …  
_Tyhjä_ | 3 | 6 |  |   
Rivityyppi | 9 | 1 | 1 = otsikko | 1  
Asiakasnumero | 10 | 8 | MicrosoftAxHeaderCustomerNumber | 10000141  
_Tyhjä_ | 18 | 12 |  |   
Laskutuspäivä | 30 | 8 |  Laskun muodostuspäivä, `YYYYMMDD` MicrosoftAxGenerationDate | 20130627  
_Tyhjä_ | 38 | 52 |  |   
Valuutta | 90 | 3 |  EUR MicrosoftAxHeaderCurrency | EUR  
_Tyhjä_ | 93 | 6 |  |   
## Laskurivi
Tieto | Positio | Pituus | Huom. | Esim.  
---|---|---|---|---  
Yritysnumero | 1 | 2 |  Yhtiökoodi ProjectCode1 | 11, 19, 29, …  
_Tyhjä_ | 3 | 6 |  |   
Rivityyppi | 9 | 1 | 2 = rivi | 2  
Tuotenumero | 10 | 5 | MicrosoftAxProductCode | 99003  
_Tyhjä_ | 15 | 15 |  |   
Tuotenimi | 30 | 60 |  Tuotteen nimi MicrosoftAxProductName | Toimistohenkilöstö  
Määrä | 90 | 9 | Kappalemäärä etunollilla, ilman desimaalierotinta | 000000750  
Etumerkki | 99 | 1 |  +'= myyntilasku, '-'=hyvityslasku \+ or 1 sent based on if Määrä is positive or negative | +  
Hinta | 100 | 20 |  Kappalehinta etunollilla, ilman desimaalierotinta MicrosoftAxPrice | 00000000000000002500  
_Tyhjä_ | 120 | 25 |  |   
Alv | 145 | 3 |  ALV-kanta etunollalla MicrosoftAxVatPercentage | 024  
_Tyhjä_ | 148 | 2 |  |   
Kirjanpitotili | 150 | 4 |  Myyntitili MicrosoftAxAccountingAccount | 3910  
_Tyhjä_ | 154 | 1 |  |   
Vastuualue | 155 | 4 |  Henkilöä lainannut kustannuspaikka MicrosoftAxAreaOfResponsibility | 4703  
_Tyhjä_ | 159 | 6 |  |   
Laskutettava yhtiökoodi | 165 | 2 | MicrosoftAxCompanyToInvoice | 11, 19, 29, …  
_Tyhjä_ | 167 | 3 |  |   
Laskuriviviite | 170 | 25 |  Laskutettava kustannuspaikka, laskutettava kk/vvvv ja hlö TAI Laskutettava kustannuspaikka, laskutettava kk/vvvv MicrosoftAxReference |   
_Tyhjä_ | 195 | 145 |  |   
Shipment date | 340 | 8 |  Laskutettava päivämäärä, YYYYMMDD SalaryRendergingDate | 20130429  
_Tyhjä_ | 348 | 2 |  |   
## Esimerkki
[code] 
    11      14400                20180801                                                    EUR      
    11      29900                Toimistohenkilöstö                                          000000250+00000000000000000000                         024  3910 50        23   238 03/2016 602027                                                                                                                                                        20160307  
    11      29900                Toimistohenkilöstö                                          000000350+00000000000000000000                         024  3910 50        23   238 03/2016 602027                                                                                                                                                        20160308  
[/code]
