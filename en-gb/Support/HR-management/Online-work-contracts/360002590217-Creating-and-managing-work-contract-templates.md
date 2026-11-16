---
id: 360002590217
title: Creating and managing work contract templates
url: https://support.nepton.com/hc/en-gb/articles/360002590217-Creating-and-managing-work-contract-templates
locale: en-gb
category: Support
category_id: 360000446658
section: Online work contracts
section_id: 360000708617
section_path:
- HR management
- Online work contracts
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2026-11-16T13:54:48Z'
edited_at: '2026-11-16T13:54:48Z'
---

# Creating and managing work contract templates

In Nepton, electronic work contracts are created based on fillable work contract templates. Work contract templates can be customised to meet the organisation's needs, and their fields can be linked to employee information.
Work contract templates are managed under **Employment > Contracts > Work contract templates**.
Creating and editing work contract templates requires **Administrator** permissions.
We have created a general example work contract template to make it easier to start using the feature. We recommend using the example template as the basis for a new work contract template. You can download the template [here](<https://support.nepton.com/hc/fi/article_attachments/11444518799389/working-contract.zip>) and customise it to meet your organisation's needs using these instructions.
Completed work contract templates can be used to create [work contract packages](<https://support.nepton.com/hc/fi/articles/360002590237>), which are then used to create, complete and sign the actual work contract.
## Work contract templates and attachments
Work contract templates and files attached to them are managed under **Employment > Contracts > Work contract templates**.
The following template types are available:
  * **Work contract**
    * A fillable HTML work contract form. It is used as the basis for creating an electronic fillable work contract in Nepton.
  * **Work contract attachment**
    * A static file that can be attached to a work contract. A work contract attachment can, for example, be a confidentiality agreement or remote working agreement.
  * **Commission attachment**
    * A static file that can be attached to a work contract.


The actual fillable work contract template is an HTML file. Static attachments can, for example, be PDF files.
## Creating a work contract template
  1. Go to **Employment > Contracts > Work contract templates**.
  2. Select **Add work contract template**.
  3. Enter a name and description for the template.
  4. Select the template type.
  5. Select the required file from your computer.
  6. Select **Save**.


When creating a fillable work contract, select **Work contract** as the type and use an **HTML file**.
A new work contract template does not usually need to be built from scratch. You can use [Nepton's example template](<https://support.nepton.com/hc/fi/article_attachments/11444518799389/working-contract.zip>) as a starting point and customise it to meet your organisation's needs.
![](https://support.nepton.com/hc/article_attachments/40704907807133)
## Editing a work contract template
To edit the basic information of a work contract template:
  1. Go to **Employment > Contracts > Work contract templates**.
  2. Select the **pencil icon** next to the required work contract template.
  3. Edit the template's name, description or type as required.
  4. Select **Save**.


![](https://support.nepton.com/hc/article_attachments/40704880285085)
If the template is a fillable **Work contract** template, its contents can be edited by selecting **Edit template**.
A work contract template can be edited either using the graphical editor or directly in the HTML code.
![](https://support.nepton.com/hc/article_attachments/40704880286621)
### Using the graphical editor
The graphical editor is particularly suitable for editing text, headings and other simple content, as well as adding new fillable text fields.
![Graphical work contract template editor](https://support.nepton.com/hc/article_attachments/5136665766045)
To add a new fillable text field:
  1. Place the cursor at the point in the work contract template where you want to add the field.
  2. Open the form field menu in the toolbar and select **Insert Textbox**.
  3. Define the field name (**Name**).
  4. Define the field completion permission (**ID**).
  5. Add the field by selecting **OK**.
  6. Finally, save the changes you have made to the work contract template.


If the contents of the field are to be linked to employee information, the field name must correspond to a data field identifier supported by Nepton. The identifiers are described in more detail at the end of this article.
![Insert Textbox menu option](https://support.nepton.com/hc/article_attachments/5136632492061)
### Using the HTML editor
More advanced changes should be made directly in the HTML code.
To open the HTML view, select **HTML** at the bottom of the editor.
![HTML editor tab](https://support.nepton.com/hc/article_attachments/5136701281565)
The HTML editor can be used, for example, to:
  * edit existing form fields
  * add new HTML elements
  * define field properties
  * change the appearance of the contract using inline CSS
  * add images in Base64 format


Using the HTML editor requires a basic understanding of HTML.
HTML code can be edited directly in Nepton. The template's HTML code can also be copied and saved to your computer as an `.html` file, which can then be edited using a separate text editor.
## Work contract template data fields
In addition to regular fields, work contract templates can contain fields that are linked to employee information in Nepton.
You only need to define the form fields into which information is entered. Nepton adds the other structures and elements required for the form to function, such as save buttons.
A fillable form field must include at least a field name (`name`) and completion permission (`id`).
When a Nepton-defined `data_` identifier is used for a field, the field value can be pre-filled using employee information. When the work contract is approved, the information entered in the field can also be saved to the employee's information.
A field can, for example, be defined as follows:
[code] 
    <input type="text" name="data_etunimi" size="40" id="tt">
[/code]
Here, `data_etunimi` links the field to the employee's first name, while `tt` specifies that the field is completed by the employee.
The available identifiers are listed under **Data fields linked to employee information** later in this article.
Custom fields created in the service can also be assigned their own `data_` identifier.
### Field name
The field's `name` value defines the form field name.
When a Nepton-defined `data_` identifier is used as the `name` value, the field can be linked to the corresponding employee information.
If information is collected on the work contract but does not need to be linked to employee information, the field can be given a freely defined name.
Do not use spaces, Scandinavian characters or other special characters in the field name.
### Field completion permissions
The form field's `id` attribute determines who can complete the field.
The available completion permissions are:
  * `id="ta"` = the employer completes the field
  * `id="tt"` = the employee completes the field
  * `id="ta,tt"` = both the employer and employee can complete the field


The `opt_` modifier can also be applied when completing the field is optional. Otherwise, the field must be completed before the work contract can be approved.
### Supported form field types
Fillable text fields can be used in work contract templates.
Radio-type form fields and drop-down lists are not supported. Instead of a drop-down list, a text field can be used in which the user types the required selection according to the instructions on the form.
## Styles, formatting and images
The HTML structure of a work contract template should be kept as simple as possible. A simple table-based layout is well suited to a work contract template.
The following are removed from HTML code imported into Nepton:
  * `<style>` elements
  * references to external CSS stylesheets
  * content outside the `<body>` element


The appearance of a work contract template can be modified using **inline CSS** , where formatting is defined directly in the HTML element's `style` attribute.
For example:
[code] 
    <table style="font-family: Arial, Helvetica, sans-serif; color: #000;">
[/code]
Inline CSS can be used to define, for example:
  * font
  * text size and colour
  * background colour
  * element width
  * borders
  * alignment
  * spacing and margins


### Adding images and a logo
Images, such as your organisation's logo, can be added to a work contract template. The image is added to the HTML file as **Base64-encoded data** , which embeds the image directly in the work contract template so that it does not need to be loaded from an external image file.
#### Converting an image to Base64
First, convert the required image to Base64 format using a suitable tool. The conversion produces a Base64 string representing the image contents.
It is recommended that you resize and optimise the image before conversion so that the work contract template does not become unnecessarily large. Base64 encoding typically increases the size of the data by approximately one third.
#### Adding a Base64 image to the HTML code
A Base64-encoded image is added to the `src` attribute of the HTML `<img>` element.
For example, a PNG image:
[code] 
    <img src="data:image/png;base64,BASE64-ENCODED-IMAGE" alt="Logo">
[/code]
The `src` attribute value is structured as follows:
[code] 
    data:image/png;base64,BASE64-ENCODED-IMAGE
[/code]
In this value:
  * `image/png` defines the image file type
  * `base64` indicates that the content is Base64 encoded
  * the actual Base64 string for the image is added after the comma


This follows the Data URL structure used in HTML: `data:[mediatype];base64,[data]`.
Use the media type that corresponds to the image file format. For example:
  * PNG: `image/png`
  * JPEG/JPG: `image/jpeg`


A Base64 string can be very long. This is normal. The entire string must be included in the `src` attribute after `base64,`.
#### Changing the image size
The image size can be defined using inline CSS. For example, the logo width can be set to 180 pixels:
[code] 
    <img src="data:image/png;base64,BASE64-ENCODED-IMAGE"
         style="width: 180px; height: auto;"
         alt="Logo">
[/code]
`width: 180px` sets the image width to 180 pixels, while `height: auto` preserves the image's original aspect ratio.
## Using an existing work contract template as the basis for a new template
If a new work contract template differs only slightly from an existing template, there is no need to build it entirely from scratch. An existing template can be used as the starting point for the new template.
  1. Open the existing work contract template for editing.
  2. Open the **HTML** view.
  3. Copy the template's HTML code.
  4. Paste the HTML code into a text editor.
  5. Make the required changes.
  6. Save the file in `.html` format.
  7. Return to **Employment > Contracts > Work contract templates**.
  8. Select **Add work contract template** and add the saved HTML file as a new template.


This allows the structure and formatting of an existing template to be reused without building a new template from scratch.
## Data fields linked to employee information
When one of the identifiers below is used as the `name` value of a field on a work contract, the field can be linked to the corresponding employee information.
When a work contract is created, these fields can be pre-filled using the employee's information. When the work contract is approved, the values entered in the fields can be saved to the employee's information.
Data field | Identifier  
---|---  
First name | `data_etunimi`  
Last name | `data_lastname`  
Personal identity code | `data_hetu`  
Email address | `data_email`  
Phone number | `data_puhelinnumero`  
Bank account number (IBAN) | `data_tilinumero`  
BIC | `data_BIC`  
Street address | `data_katuosoite`  
Postcode | `data_postinumero`  
City | `data_kaupunki`  
Employment start date | `data_aloituspvm`  
Employment end date | `data_lopetuspvm`  
Weekly working time | `data_viikkotunnit`  
Hourly pay | `data_tuntipalkka`  
Default cost centre | `data_oletuskustannuspaikka`  
Probation end date | `data_koeaika_paattyy`  
Job title | `data_jobtitle`  
Working area | `data_alue`  
Working time percentage | `data_worktimepercentage`  
Custom fields created in the service can also be used on work contracts. A custom `data_` identifier can be defined when the custom field is created.
## Next steps
Once the required work contract templates and attachments have been created, they are combined into a **work contract package**. The work contract package defines the template and attachments used when creating the actual electronic work contract.
See also:
  * [Work contract packages](<https://support.nepton.com/hc/fi/articles/360002590237>)
  * [Completing and signing a work contract](<https://support.nepton.com/hc/fi/articles/360002590277>)
