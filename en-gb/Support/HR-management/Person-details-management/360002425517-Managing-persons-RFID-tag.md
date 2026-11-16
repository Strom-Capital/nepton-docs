---
id: 360002425517
title: Managing persons RFID tag
url: https://support.nepton.com/hc/en-gb/articles/360002425517-Managing-persons-RFID-tag
locale: en-gb
category: Support
category_id: 360000446658
section: Person details management
section_id: 360004485937
section_path:
- HR management
- Person details management
labels:
- rfid
- rdif
- kortinlukija
- leimaustunniste
- lätkä
promoted: false
updated_at: '2026-11-06T10:36:08Z'
edited_at: '2026-10-28T11:51:49Z'
---

# Managing persons RFID tag

If RFID tags are used to record work hours, RFID tag identifier needs to be saved in person's information.
## Adding RFID tag identifier manually
RFID tag identifier can be saved in person's information in **Employees** section through **Persons > Person's information > Identifiers**.  
![](https://support.nepton.com/hc/article_attachments/40238496618653)  
One user can have multiple RFID identifiers. To save more than one, separate the identifiers with a pipe symbol (|). Once you have added the information, remember to save the changes from the Save-button at the bottom of the page. Please note, that the field is managed with [validity tools](<https://support.nepton.com/hc/en-gb/articles/360004856937>).
The same RFID tag identifier can only be saved for one person, so when an employee's contract ends, the RFID tag identifier needs to be removed from their information before [deactivating the user](<https://support.nepton.com/hc/en-gb/articles/360002424617>).
In some of the RFID tags the code that has been printed on the tag is actually not the identifier code. The right code can be seen when the tag is shown to the reader that's connected to a terminal. If the code is not set for another user, the terminal will inform that the code was not found, and will show the code on the screen. You can save this code into the user's details.
## Adding RFID tag identifier with reader
RFID tag identifier can also be added to the person's details by connecting a reader to the computer via USB port. By showing the person's RFID tag to the reader, the right code will be read straight from it to the person's information.
  1. Connect the reader to a computer via USB.


![mceclip0.png](https://support.nepton.com/hc/article_attachments/360009426478)
  2. Log in to Nepton.
  3. Open the right person's information.
  4. Click your mouse on the RFID tag identifier -field.


![mceclip2.png](https://support.nepton.com/hc/article_attachments/360008281197)
  5. Show the tag (picture below) to the reader.


![keyfob.jpg](https://support.nepton.com/hc/article_attachments/4402933069713)
  6. The code will appear on the field.


![mceclip4.png](https://support.nepton.com/hc/article_attachments/360008281237)
  7. Save the changes from the Save-button at the bottom of the page. 


The tag identifier has now been added to the user's information.
## Adding and removing RFID tags in bulk
### Adding RFID tags in bulk
RFID tags can also be imported into the service in bulk by using an Excel file. Our support article, "[Manual person import](<https://support.nepton.com/hc/en-gb/articles/360018767498>)" provides guidance on how to perform a bulk import.
### Removing RFID tags in bulk
RFID-tunnisteita voidaan poistaa massana henkilötietojen tuontia hyödyntäen. Valitse Työsuhde-osiosta koko henkilöstö (tai rajaa sitä haluamallasi tavalla) ja lataa henkilöstön tiedot sisäänluettavaan exceliin:
RFID tags can be removed in bulk by utilizing the manual person import. In the Employment section, select the entire staff (or filter the selection as desired) and export the results to importable Excel file for import:
![](https://support.nepton.com/hc/article_attachments/40238496619037)
Process the file in Excel by completely removing the RFID tag information from the RFID tag column for the relevant individuals. Save the file after making these changes. Import the edited data back into Nepton using the person import function (**Employees > Persons > Import persons**).
![](https://support.nepton.com/hc/article_attachments/40238496619293)
The person import type determines how the file content is interpreted in Nepton. In general, Nepton recommends selecting "Default" as the import type.
When importing person data manually, empty fields in the import file do not, by default, alter the values ​​of existing fields. To remove RFID tags, you must select "Existing field values ​​will be removed (exact match)," which forces the deletion of the data. Exercise caution when using this option, as it overwrites all fields included in the import.
### Reusing an RFID tag for another person
When an empty RFID field is submitted during a person import, the RFID tag’s history remains in the service. This means that if you wish to reassign an RFID tag—previously removed from another person’s record—to a different individual, you must add it to the new person using the validity function. You can add an RFID tag via the validity function by following this path: Employees > select the desired person > Identifiers: RFID tag identifier. The validity function (a button resembling a calendar icon) appears when you click on the text field (the field where the value is entered).
![](https://support.nepton.com/hc/article_attachments/40238496619549)
