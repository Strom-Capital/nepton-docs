---
id: 30528934209181
title: Project allocation using barcode reader
url: https://support.nepton.com/hc/en-gb/articles/30528934209181-Project-allocation-using-barcode-reader
locale: en-gb
category: Support
category_id: 360000446658
section: General information on terminals
section_id: 360005942558
section_path:
- Terminals
- General information on terminals
labels: []
promoted: false
updated_at: '2025-12-19T12:32:31Z'
edited_at: '2025-12-19T12:32:31Z'
---

# Project allocation using barcode reader

The service allows you to allocate work to a project using a barcode. This capability is available in Nepton Flexim terminals.
Projects that can be read using a barcode must be found in the service, or the user reading the bar codes must have correct permissions to create new projects via bar code reading. Projects can be brought to Nepton by:
  * integration : order
  * manually using Excel
  * manually in the user interface, in which case the project code can be read into the project code field with a barcode reader


## How does barcode allocation work with a Nepton Flexim terminal?
  * A person logs in with an identifier
  * The barcode of the project/task is read using a barcode reader
    * If a project corresponding to the barcode exists in the service
      * a possible ongoing project and event is terminated
      * the same event is started with the corresponding project read with the barcode
      * If a project code corresponding to the barcode is not found, a new project can be created and started. This requires that the person has the rights to do so.

![](https://support.nepton.com/hc/article_attachments/31490400532125)
## How can barcodes from projects be printed?
Investigate the customer's system: ERP, ordering system, job planning, etc.
  * Does the customer's system have the ability to create and print barcodes?
  * If not, the barcodes must be generated using an external program, such as Excel or an online barcode generator (project code needs to be transformed into a bar code).
  * The barcodes are printed as Code128B barcodes
