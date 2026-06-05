---
id: 360020620958
title: Fivaldi laskutusaineisto XML
url: https://support.nepton.com/hc/fi/articles/360020620958-Fivaldi-laskutusaineisto-XML
locale: fi
category: Palvelun käyttö
category_id: 360000446658
section: Palkkajärjestelmät
section_id: 360000964297
section_path:
- Liittymät
- Palkkajärjestelmät
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-09-11T12:16:21Z'
---

# Fivaldi laskutusaineisto XML

## Tiedostomuoto  
Siirtotiedosto on XML-muotoista tietoa.
## Rajaukset 
  * Fivaldi Business ID tulee olla syötetty Nepton-palveluun valikossa  _Työaika - Hallinta - Työyhteisön asetukset - Liittymät - Palkanlaskentajärjestelmän tunniste._
  * Työntekijät työntekijänumerolla 0 eivät tule osaksi aineistoa


![mceclip0.png](https://support.nepton.com/hc/article_attachments/13489626930205)
## Aineiston rakenne 
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Juuri | FivaldiXML | XML elementti | 1 |   
1 | FVBusinessId | XML elementti | 1 | Fivaldi Business ID asetuksista  
1 | SalesOrder | XML elementti | 0...n |   
2 | SalesOrderNo | merkkijono | 1 | Järjestelmän generoima yksilöllinen numeerinen tunniste  
2 | SalesOrderExecutor | XML elementti | 1 | Henkilön tiedot  
3 | FVSalesmanName | merkkijono | 1 | Henkilön koko nimi   
3 | FVSalesmanTelephone | merkkijono | 1 | Tyhjä kenttä  
3 | FVSalesmanEmail | merkkijono | 1 | Tyhjä kenttä  
2 | SalesOrderCompanyId | merkkijono | 1 | Täytetään `ProjectCode1` arvolla. Voidaan ohittaa sääntöjoukon säännössä kentällä `OverrideProjectCode1`  
2 | SalesOrderName1 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderName1`  
2 | SalesOrderName2 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderName2`  
2 | SalesOrderStreetAddress | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderStreetAddress`  
2 | SalesOrderStreetAddress2 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderStreetAddress2`  
2 | SalesOrderPostalAddress | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderPostalAddress`  
2 | SalesOrderCountry | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderCountry`  
2 | SalesOrderReference | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderReference`  
2 | SalesOrderDate | päivämäärä | 1 | Tapahtuman päivämäärä, loppupäivä, jos tapahtuma kestää useamman päivän. Muoto `YYYY-MM-DD`.  
2 | SalesOrderWarehouseCode | kokonaisluku | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderWarehouseCode`  
2 | SalesOrderWarehouseName | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderWarehouseName`  
2 | SalesOrderAdditionalInfo | merkkijono | 1 | Tapahtuman kommentit, voidaan ohittaa poimintasäännön kentällä `Comment`  
2 | SalesOrderDeliveryDate | päivämäärä | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryDate`  
2 | SalesOrderTaxableTotal | desimaali | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderTaxableTotal`  
2 | SalesOrderTotalIncludingTax | desimaali | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderTotalIncludingTax`  
2 | SalesOrderDeliveryName1 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryName1`  
2 | SalesOrderDeliveryName2 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryName2`  
2 | SalesOrderDeliveryStreetAddr | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryStreetAddr`  
2 | SalesOrderDeliveryStreetAddr2 | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryStreetAddr2`  
2 | SalesOrderDeliveryPostalAddr | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryPostalAddr`  
2 | SalesOrderDeliveryCountry | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderDeliveryCountry`  
2 | SalesOrderCurrency | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderCurrency`  
2 | SalesOrderExchangeRate | desimaali | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderExchangeRate`  
2 | SalesOrderCashDate | päivämäärä | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderCashDate`  
2 | SalesOrderCashPercent | kokonaisluku | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderCashPercent`  
2 | SalesOrderNetDate | päivämäärä | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderNetDate`  
2 | SalesOrderInvoicingPermit | XML elementti | 0...1 | Tyhjä elementti. Nepton ei oletuksena luo tätä elementtiä. Luodaan, jos poimintasäännön kentällä `SalesOrderInvoicingPermit` on arvo.  
attribuutti | Value | boolean | 1 |  `SalesOrderInvoicingPermit` -kentän attribuutti. Nepton ei oletuksena täytä tätä atribuuttia. Mahdolliset arvot: 
  * `0`
  * `1`

Voidaan asettaa poimintasäännön kentällä `SalesOrderInvoicingPermit `  
2 | SalesOrderOfferEffectiveDate | päivämäärä | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderOfferEffectiveDate`  
2 | SalesOrderOrderer | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderOrderer`  
2 | SalesOrderPostingGroupId | merkkijono | 0...1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderPostingGroupId`  
2 | SalesOrderInternalInfo | merkkijono | 0..1 |  Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderInternalInfo`  
2 | SalesOrderRow | merkkijono | 1 |   
3 | SalesOrderRowNo | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowNo`  
3 | SalesOrderRowProductId | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowProductId`  
3 | SalesOrderRowQuantity | desimaali | 0..1 | Tapahtuman kesto tunteina, Voidaan ohittaa poimintasäännön kentällä `Amount`  
3 | SalesOrderRowProductType | kokonaisluku | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowProductType`  
3 | SalesOrderRowProductName | merkkijono | 1 | Palkkalajikoodi. Voidaan ohittaa poimintasäännön kentällä `SalaryCode`  
3 | SalesOrderRowDiscountPercent1 | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowDiscountPercent1`  
3 | SalesOrderRowDiscountPercent2 | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowDiscountPercent2`  
3 | SalesOrderRowTaxableUnitPrice | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowTaxableUnitPrice`  
3 | SalesOrderRowUnitPriceInclTax | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowUnitPriceInclTax`  
3 | SalesOrderRowDeliveryDate | päivämäärä | 1 | Tapahtuman päivämäärä  
3 | SalesOrderRowVatDate | päivämäärä | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowVatDate`  
3 | SalesOrderRowProductSupplierCompanyId | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowProductSupplierCompanyId`  
3 | SalesOrderRowTaxableCostPrice | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowTaxableCostPrice`  
3 | SalesOrderRowTaxableTotal | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowTaxableTotal`  
3 | SalesOrderRowTotalIncludingTax | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowTotalIncludingTax`  
3 | SalesOrderRowInvoicingChoice | XML elementti | 0...1 | Tyhjä elementti. Nepton ei oletuksena luo tätä elementtiä. Luodaan, jos poimintasäännön kentällä `SalesOrderRowInvoicingChoice ` on arvo.  
attribuutti | Value | boolean | 1 |  `SalesOrderRowInvoicingChoice ` -kentän attribuutti. Nepton ei oletuksena täytä tätä -atribuuttia. Mahdolliset arvot: 
  * `0`
  * `1`

Voidaan asettaa poimintasäännön kentällä `SalesOrderRowInvoicingChoice `  
3 | SalesOrderRowWarehouseCode | kokonaisluku | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowWarehouseCode`  
3 | SalesOrderRowWarehouseName | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowWarehouseName`  
3 | SalesOrderRowWarehouseBatchId | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowWarehouseBatchId`  
3 | SalesOrderRowAdditionalInfo | merkkijono | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowAdditionalInfo`  
3 | SalesOrderRowStatisticsRow | XML elementti | 0...1 | Tyhjä elementti. Nepton ei oletuksena luo tätä elementtiä. Luodaan, jos poimintasäännön kentällä `SalesOrderRowStatisticsRow ` on arvo.  
attribuutti | Value | boolean | 1 |  `SalesOrderRowStatisticsRow ` -kentän attribuutti. Nepton ei oletuksena täytä tätä -atribuuttia. Mahdolliset arvot: 
  * `0`
  * `1`

Voidaan asettaa poimintasäännön kentällä `SalesOrderRowStatisticsRow `  
3 | SalesOrderRowDeliveredQuantity | desimaali | 0..1 | Nepton ei oletuksena täytä tätä kenttää. Voidaan asettaa poimintasäännön kentällä `SalesOrderRowDeliveredQuantity`  
### Aineiston esimerkki
Tuetut kentät listattu esimerkissä:
[code] 
    <?xml version="1.0" encoding="ISO-8859-15"?>  
    <FivaldiXML>  
      <!-- Fivaldi business id setting is used. Can be overridden with SQL rule. -->  
      <FVBusinessId>01010ÄÄ1-1</FVBusinessId>  
      <SalesOrder>  
        <!-- Unique identifier for the SalesOrder generated in export. -->  
        <SalesOrderNo>1234567890</SalesOrderNo>   
        <SalesOrderExecutor>  
          <!-- First name(s) last name of the employee whose data is exported. -->  
          <FVSalesmanName>Frankie Employee</FVSalesmanName>
          <FVSalesmanTelephone/>  
          <FVSalesmanEmail/>  
        </SalesOrderExecutor>  
        <!-- ProjectCode1, can be overridden. Max length 10 characters. -->  
        <SalesOrderCompanyId>12345</SalesOrderCompanyId>  
        <!-- optional, may be set with SQL -->  
        <SalesOrderName1>Name 1</SalesOrderName1>  
        <!-- optional, may be set with SQL -->  
        <SalesOrderName2>Name 2</SalesOrderName2>
        <!-- optional, may be set with SQL -->  
        <SalesOrderStreetAddress>Street Address</SalesOrderStreetAddress>
        <!-- optional, may be set with SQL -->  
        <SalesOrderStreetAddress2>Street Address 2</SalesOrderStreetAddress2>
        <!-- optional, may be set with SQL -->  
        <SalesOrderPostalAddress>Postal Address</SalesOrderPostalAddress>
        <!-- optional, may be set with SQL -->  
        <SalesOrderCountry>FI</SalesOrderCountry>
        <!-- optional, may be set with SQL -->  
        <SalesOrderReference>REF</SalesOrderReference>  
        <!-- Salary rendering date of the exported event -->
        <SalesOrderDate>2021-04-31</SalesOrderDate>  
        <!-- optional, may be set with SQL -->  
        <SalesOrderWarehouseCode>12</SalesOrderWarehouseCode>
        <!-- optional, may be set with SQL -->
        <SalesOrderWarehouseName>Name</SalesOrderWarehouseName>
        <!-- Exported event's notes, can be overridden. -->
        <SalesOrderAdditionalInfo>example note</SalesOrderAdditionalInfo>
        <!-- optional, may be set with SQL -->   
        <SalesOrderDeliveryDate>2021-11-12</SalesOrderDeliveryDate>
        <!-- optional, may be set with SQL -->   
        <SalesOrderTaxableTotal>1400000000.1511</SalesOrderTaxableTotal>
        <!-- optional, may be set with SQL -->   
        <SalesOrderTotalIncludingTax>10.12</SalesOrderTotalIncludingTax>
        <!-- optional, may be set with SQL -->   
        <SalesOrderDeliveryName1>Name</SalesOrderDeliveryName1>
        <!-- optional, may be set with SQL -->   
        <SalesOrderDeliveryName2>Name</SalesOrderDeliveryName2>
        <!-- optional, may be set with SQL --> 
        <SalesOrderDeliveryStreetAddr>Street Address</SalesOrderDeliveryStreetAddr>
        <!-- optional, may be set with SQL -->
        <SalesOrderDeliveryStreetAddr2>Street Address 2</SalesOrderDeliveryStreetAddr2>
        <!-- optional, may be set with SQL --> 
        <SalesOrderDeliveryPostalAddr>Postal Address</SalesOrderDeliveryPostalAddr>
        <!-- optional, may be set with SQL --> 
        <SalesOrderDeliveryCountry>SE</SalesOrderDeliveryCountry>
        <!-- optional, may be set with SQL --> 
        <SalesOrderCurrency>EUR</SalesOrderCurrency>  
        <!-- optional, may be set with SQL --> 
        <SalesOrderExchangeRate>1.1</SalesOrderExchangeRate>
        <!-- optional, may be set with SQL --> 
        <SalesOrderCashDate>2021-11-10</SalesOrderCashDate>
        <!-- optional, may be set with SQL --> 
        <SalesOrderCashPercent>12</SalesOrderCashPercent>  
        <!-- optional, may be set with SQL --> 
        <SalesOrderNetDate>2021-11-15</SalesOrderNetDate>  
        <!-- optional, may be set with SQL, value 0 or 1 -->
        <SalesOrderInvoicingPermit Value="1"/>  
        <!-- optional, may be set with SQL --> 
        <SalesOrderOfferEffectiveDate>2021-11-14</SalesOrderOfferEffectiveDate>
        <!-- optional, may be set with SQL --> 
        <SalesOrderOrderer>Orderer</SalesOrderOrderer>  
        <!-- optional, may be set with SQL --> 
        <SalesOrderPostingGroupId>GroupID</SalesOrderPostingGroupId>
        <!-- optional, may be set with SQL --> 
        <SalesOrderInternalInfo>Internal Info</SalesOrderInternalInfo>
        <SalesOrderRow>  
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowNo>13</SalesOrderRowNo>  
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowProductId>ID12314</SalesOrderRowProductId>
          <!-- Hours / pcs from the exported event / supplement etc. Can be overridden -->  
          <SalesOrderRowQuantity>9</SalesOrderRowQuantity>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowProductType>23</SalesOrderRowProductType>
          <!-- Salary code -->
          <SalesOrderRowProductName>Example987654321</SalesOrderRowProductName>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowDiscountPercent1>13.45</SalesOrderRowDiscountPercent1>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowDiscountPercent2>55.65</SalesOrderRowDiscountPercent2>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowTaxableUnitPrice>1234.234</SalesOrderRowTaxableUnitPrice>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowUnitPriceInclTax>23453.23</SalesOrderRowUnitPriceInclTax>
          <!-- Salary rendering date of the exported event -->
          <SalesOrderRowDeliveryDate>2021-05-31</SalesOrderRowDeliveryDate>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowVatDate>2021-12-22</SalesOrderRowVatDate>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowProductSupplierCompanyId>ID</SalesOrderRowProductSupplierCompanyId>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowTaxableCostPrice>342.56</SalesOrderRowTaxableCostPrice>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowTaxableTotal>342.23</SalesOrderRowTaxableTotal>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowTotalIncludingTax>2343.23</SalesOrderRowTotalIncludingTax>
          <!-- optional, may be set with SQL, value 0 or 1 -->
          <SalesOrderRowInvoicingChoice Value="1"/>  
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowWarehouseCode>23</SalesOrderRowWarehouseCode>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowWarehouseName>Name</SalesOrderRowWarehouseName>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowWarehouseBatchId>BatchId</SalesOrderRowWarehouseBatchId>
          <!-- optional, may be set with SQL --> 
          <SalesOrderRowAdditionalInfo>Additional Info</SalesOrderRowAdditionalInfo>
          <!-- optional, may be set with SQL, value 0 or 1 -->
          <SalesOrderRowStatisticsRow Value="0"/>  
          <!-- optional, may be set with SQL -->   
          <SalesOrderRowDeliveredQuantity>23.54</SalesOrderRowDeliveredQuantity>
        </SalesOrderRow>  
      </SalesOrder>  
    </FivaldiXML>
    
[/code]
