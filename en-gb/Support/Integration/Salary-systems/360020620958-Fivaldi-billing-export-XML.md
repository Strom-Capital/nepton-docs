---
id: 360020620958
title: Fivaldi billing export XML
url: https://support.nepton.com/hc/en-gb/articles/360020620958-Fivaldi-billing-export-XML
locale: en-gb
category: Support
category_id: 360000446658
section: Salary systems
section_id: 360000964297
section_path:
- Integration
- Salary systems
labels: []
promoted: false
updated_at: '2024-12-18T15:10:08Z'
edited_at: '2023-09-21T07:16:18Z'
---

# Fivaldi billing export XML

## File type  
Export file is in XML form. See file structure below.
## Limitations
  * Fivaldi Business ID must be set in Nepton in _Worktime - Administration - Working community settings - Integrations - Fivaldi - Payroll system ID._
  * Persons with personnel number 0 will not be exported.


![mceclip0.png](https://support.nepton.com/hc/article_attachments/360020429138)
## File structure
Taso | Kentän nimi | Muoto | Esiintymiskerrat | Selite  
---|---|---|---|---  
Root | FivaldiXML | XML element | 1 |   
1 | FVBusinessId | XML element | 1 | Fivaldi Business ID from settings  
1 | SalesOrder | XML element | 0...n |   
2 | SalesOrderNo | string | 1 | Generated unique numerical ID  
2 | SalesOrderExecutor | XML element | 1 | Person's data  
3 | FVSalesmanName | string | 1 | Full name of the person   
3 | FVSalesmanTelephone | string | 1 | Empty field  
3 | FVSalesmanEmail | string | 1 | Empty field  
2 | SalesOrderCompanyId | string | 1 | Populated with `ProjectCode1`. Can be overridden with ruleset field `OverrideProjectCode1`  
2 | SalesOrderName1 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderName1`  
2 | SalesOrderName2 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderName2`  
2 | SalesOrderStreetAddress | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderStreetAddress`  
2 | SalesOrderStreetAddress2 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderStreetAddress2`  
2 | SalesOrderPostalAddress | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderPostalAddress`  
2 | SalesOrderCountry | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderCountry`  
2 | SalesOrderReference | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderReference`  
2 | SalesOrderDate | date | 1 | Date of the event. Last day if event spans multiple days. In the format `YYYY-MM-DD`.  
2 | SalesOrderWarehouseCode | number | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderWarehouseCode`  
2 | SalesOrderWarehouseName | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderWarehouseName`  
2 | SalesOrderAdditionalInfo | string | 1 | Comments for the event, can be overridden with field `Comment`  
2 | SalesOrderDeliveryDate | date | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryDate`  
2 | SalesOrderTaxableTotal | decimal | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderTaxableTotal`  
2 | SalesOrderTotalIncludingTax | decimal | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderTotalIncludingTax`  
2 | SalesOrderDeliveryName1 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryName1`  
2 | SalesOrderDeliveryName2 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryName2`  
2 | SalesOrderDeliveryStreetAddr | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryStreetAddr`  
2 | SalesOrderDeliveryStreetAddr2 | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryStreetAddr2`  
2 | SalesOrderDeliveryPostalAddr | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryPostalAddr`  
2 | SalesOrderDeliveryCountry | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderDeliveryCountry`  
2 | SalesOrderCurrency | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderCurrency`  
2 | SalesOrderExchangeRate | decimal | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderExchangeRate`  
2 | SalesOrderCashDate | date | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderCashDate`  
2 | SalesOrderCashPercent | number | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderCashPercent`  
2 | SalesOrderNetDate | date | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderNetDate`  
2 | SalesOrderInvoicingPermit | XML element | 0...1 | Empty element. Nepton does not create the element unless field `SalesOrderInvoicingPermit` is set.  
attribute | Value | boolean | 1 | Attribute to `SalesOrderInvoicingPermit` Nepton does not set this attribute by default. Possible values: 
  * `0`
  * `1`

Can be set with ruleset field `SalesOrderInvoicingPermit `  
2 | SalesOrderOfferEffectiveDate | date | 0...1 | Nepton does not add this field by default. Can be set with ruleset field`SalesOrderOfferEffectiveDate`  
2 | SalesOrderOrderer | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderOrderer`  
2 | SalesOrderPostingGroupId | string | 0...1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderPostingGroupId`  
2 | SalesOrderInternalInfo | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderInternalInfo`  
2 | SalesOrderRow | string | 1 |   
3 | SalesOrderRowNo | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowNo`  
3 | SalesOrderRowProductId | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowProductId`  
3 | SalesOrderRowQuantity | decimal | 0..1 | Event duration in hours. Can be overridden with ruleset field `Amount`  
3 | SalesOrderRowProductType | number | 0..1 | Nepton does not add this field by default. Can be set with ruleset fieldä `SalesOrderRowProductType`  
3 | SalesOrderRowProductName | string | 1 | Salary code. Can be set with ruleset field `SalaryCode`  
3 | SalesOrderRowDiscountPercent1 | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowDiscountPercent1`  
3 | SalesOrderRowDiscountPercent2 | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowDiscountPercent2`  
3 | SalesOrderRowTaxableUnitPrice | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowTaxableUnitPrice`  
3 | SalesOrderRowUnitPriceInclTax | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowUnitPriceInclTax`  
3 | SalesOrderRowDeliveryDate | date | 1 | Event date  
3 | SalesOrderRowVatDate | date | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowVatDate`  
3 | SalesOrderRowProductSupplierCompanyId | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowProductSupplierCompanyId`  
3 | SalesOrderRowTaxableCostPrice | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowTaxableCostPrice`  
3 | SalesOrderRowTaxableTotal | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowTaxableTotal`  
3 | SalesOrderRowTotalIncludingTax | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowTotalIncludingTax`  
3 | SalesOrderRowInvoicingChoice | XML element | 0...1 | Empty element. Nepton does not create the element unless field `SalesOrderRowInvoicingChoice ` is set.  
attribute | Value | boolean | 1 | Attribute to `SalesOrderRowInvoicingChoice`. Nepton does not set this attribute by default. Possible values: 
  * `0`
  * `1`

Can be set with ruleset field `SalesOrderRowInvoicingChoice `  
3 | SalesOrderRowWarehouseCode | number | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowWarehouseCode`  
3 | SalesOrderRowWarehouseName | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowWarehouseName`  
3 | SalesOrderRowWarehouseBatchId | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowWarehouseBatchId`  
3 | SalesOrderRowAdditionalInfo | string | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowAdditionalInfo`  
3 | SalesOrderRowStatisticsRow | XML element | 0...1 | Empty element. Nepton does not create the element unless field `SalesOrderRowStatisticsRow ` is set.  
attribute | Value | boolean | 1 | Attribute to `SalesOrderRowStatisticsRow `. Nepton does not set this attribute by default. Possible values: 
  * `0`
  * `1`

Can be set with ruleset field `SalesOrderRowStatisticsRow `  
3 | SalesOrderRowDeliveredQuantity | decimal | 0..1 | Nepton does not add this field by default. Can be set with ruleset field `SalesOrderRowDeliveredQuantity`  
### File example
Supported fields listed in example:
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
