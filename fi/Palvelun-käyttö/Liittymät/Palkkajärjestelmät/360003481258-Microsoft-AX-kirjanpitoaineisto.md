---
id: 360003481258
title: Microsoft AX kirjanpitoaineisto
url: https://support.nepton.com/hc/fi/articles/360003481258-Microsoft-AX-kirjanpitoaineisto
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
edited_at: '2021-11-08T13:41:15Z'
---

# Microsoft AX kirjanpitoaineisto

## Tiedostomuoto
Siirtotiedosto on positioeroteltua tekstimuotoista dataa. Rivinvaihtona on CRLF.
## Rajaukset
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


## Aineiston tietueet
Tieto | Positio | Pituus | Huom. | Esim  
---|---|---|---|---  
Yritysnumero | 1 | 3 | Voidaan asettaa poimimalla tulokset kenttään MicrosoftAxCompanyNumber | 11, 19, 29, …  
_Tyhjä_ | 4 | 17 |  |   
Tositepvm | 21 | 8 |  Aineiston luontipäivämäärä `DDMMYYYY`. Voidaan asettaa poimimalla tulokset kenttäänMicrosoftAxGenerationDate | 03022018  
_Tyhjä_ | 29 | 4 |  |   
Selite | 33 | 30 | Voidaan asettaa poimimalla tulokset kenttään MicrosoftAxReference | "12042013 447 Lehtinen"  
_Tyhjä_ | 63 | 11 |  |   
Henkilönumero | 74 | 4 | Person number | 447  
_Tyhjä_ | 79 | 10 |  |   
Kirjanpitotili | 89 | 4 | Voidaan asettaa poimimalla tulokset kenttään MicrosoftAxAccountingAccount | 9000  
_Tyhjä_ | 93 | 4 |  |   
Vastuualue | 97 | 4 | Voidaan asettaa poimimalla tulokset kenttään MicrosoftAxAreaOfResponsibility | 4012  
_Tyhjä_ | 101 | 38 |  |   
Summa | 139 | 12 | Summa etunollilla ja kahdella desimaalilla | 000000300,00  
_Tyhjä_ | 151 | 1 |  |   
Etumerkki | 152 | 1 | \+ = Debit/- = Credit. Muodostuu automaattisesti miinusmerkkinä negatiivisiin summin ja plusmerkkinä positiivisiin summin. | +  
## Esimerkki
[code] 
    011                 20082018    07032016 60202 Sukunimi                  60202          9000    238                                       000000050,00  
    011                 20082018    07032016 60202 Sukunimi                  60202          9500    238                                       000000050,00 -
    011                 20082018    07032016 60202 Sukunimi                  60202          9000    238                                       000000040,00  
[/code]
