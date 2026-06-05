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
updated_at: '2025-03-07T15:06:08Z'
edited_at: '2025-03-07T15:02:05Z'
---

# Creating and managing work contract templates

This functionality is available if you are using the HR Complete service level.
## What is the employment contract basis?
There are two basic types of employment contract bases that are used in nepton's Employment section:
  * **Employment contract**
    * Html employment contract form to be filled in
    * Also called "**the employment contract form to be filled out** "
  * **Employment Contract Supplement, Employment Certificate, Pay slip, Commission**
    * Employment Contract Supplement, Employment Certificate, Pay slip, Commission
    * The worker reads and accepts these attachments at the time of signature of the employment contract


Based on html employment contract forms to fill out, the service will be electronically fully filling employment contracts. You can download a generic the basis of the employment contract form to be filled in [here (extract the file before using it).](<https://support.nepton.com/hc/article_attachments/11444518799389>) By modifying the base, it can be personalized for customer-specific needs. Existing employment contract templates are attached [employment contract packages](<https://support.nepton.com/hc/fi/articles/360002590237>), joilla [creating electronic employment contracts for employees.](<https://support.nepton.com/hc/fi/articles/360002590277>)
### Employment contract form to be filled in
**You can download the generic employment contract form template at the bottom of the page.**
**Predefined form fields**  
When you create employment contracts, we recommend that you use predefined form fields. Using predefined form fields in employment template forms names, Nepton retrieves the person's information from the employment contract template, for example: Employment agreement information page.  
  
**Required form actions**  
You only need to mark the form fields in which you enter information in the employment template. The employment relationship completes the structures and elements required for the forms created, such as recording buttons. When you mark form fields, the required information is name and id, for example: <input type="text" name="data_kokonimi" size="20" id="tt,ta" >  
  
**Form field name**  
In the previous example, The employment retrieves the 'field' in the predefined form data_kokonimi' the name of the person when a new employment contract is created for him or her. If the employment contract collects: data for which there is no predefined form field, the field can be named in a free-form format. Do not use spaces and Scandinavian characters.  
  
**Form field fill permission**  
The ID value of the form field determines whether the employee has permission to fill the field, employer or both parties.  
Mark as needed: id="tt,ta" if both employee and employee can fill in the field. id="ta" if only the employer does.  
id="tt" if only the employee fills in.  
  
**Allowed form field types**
Radio or drop-down-fields are currently **not** supported on employment templates. Instead, you can use text fields where the employee fills in the chosen option based on given instructions.
**Styles and formatting**  
The best suited form for employment contract template is a simple stylized table. When drawing up the contract template, it is worth note that <style> elements, links to external CSS-files and all <body> elements are excluded from the imported HTML code. CSS formatting is possible by marking the formatting directly in the desired element, for example:  
<table style="font-family: Arial, Helvetica, sans-serif;color: #000;" > contract template creating / editing
The user must have: [Admin permission level](<https://support.nepton.com/hc/fi/articles/360002425637>) service.
## Managing templates
### Create an employment template
  1. Under Employees > Contracts > **Contract Templates**.
  2. At the top of the page, **Add work contract template** .
  3. Select the base file format 
     * A contract of employment means an HTML employment contract form to be filled in
     * Employment contract supplement, Employment certificate, Pay slip, Provisioliite means static file that cannot be edited, but are attachments to the employment contract when making
  4. On your computer, select the **file**. Put it on the bottom **name** and **description**. 
     * In the case of an employment contract, please note the generic employment contract form template that we offer (extract the file before using it). By modifying the template, it can be personalised to customer-specific needs.
  5. Press "**Save** "


![mceclip1.png](https://support.nepton.com/hc/article_attachments/5136507608733)
### Edit your employment template
  1. Go to Employment - & gt; Agreements - & gt; **Templates**
  2. You can change the employment template via the **pen icon** **Name,** **Description, and Template Type** **.**
  3. In the case of a **Employment Contract** , you can edit what needs to be filled out Press "**Edit template** " in the HTML form 
     * See "Creating a Completable Form (HTML) below" for more information and editing "
  4. After making changes, press **Save**.


![mceclip3.png](https://support.nepton.com/hc/article_attachments/4410543967121)
### Edit the employment contract form to fill out
  1. You can edit the employment contracts to be filled in on the Templates page **Edit Template** for the employment template, which opens the Employment Template edit view.
![mceclip2.png](https://support.nepton.com/hc/article_attachments/5136522871325)
  2. At the top of the page is a toolbar that lets you set up an employment contract template. The HTML Builder editor offers the ability to create and edit full HTML and the Page Properties dialog significantly facilitates the process of creation and formatting of complete html content
  3. To create a new text field to fill in, go to the one you want in the employment contract template and select the 'Textbox' / 'abc' button on the toolbar.
![mceclip4.png](https://support.nepton.com/hc/article_attachments/5136632492061)
  4. An INPUT window opens on top of the employment contract template, in which a text field must be defined Name and ID. If the contents of the data field are to be transferred person's data, the field name must be one of the predefined data fields names. The list of data fields to be used is shown below. 
     * **NOTE** : Scandinavian is not allowed in the field name or other special characters.
  5. Fill Rights (ID): The field must have a fill right that tells the program who is entitled to fill in that field. **ta** & nbsp; = employer meet, **tt** = employee meets **tt** = both can be filled.
  6. An additional attribute opt_ can be entered in the ID field, which means that the field may be waived by a supervisor or employee. In other case the field must be completed before the employment contract can be approved.
  7. A text field is created in the employment contract template by pressing the **OK** button.
  8. It's a good idea to edit existing fillable text fields in the source code view. 
     * The source code view is for more advanced users
     * To access the source code view, press the 'HTML' button at the bottom of the view
  9. When you're done, **be sure to** save your changes the **Save** button at the bottom of the page.


![mceclip3.png](https://support.nepton.com/hc/article_attachments/5136665766045)
### Copying a template
Copying a template can be a lot quicker than starting from scratch. Especially if you only want to make minor changes compared to an existing one. Follow the steps below to create a copy of an existing template.
  1. Go to the **Edit Template page  
**
  2. Go to the the HTML Builder 
  3. Select HTML mode
![mceclip5.png](https://support.nepton.com/hc/article_attachments/5136701281565)
  4. Copy the whole html inside the HTML Builder 
  5. Open a text editor like notepad or notepad++
  6. Past the the whole html inside the text editor
  7. Save the document as template.**html**
     * it is important to save the document as html file (.html)
  8. back nepton website and upload you document (see section 
Create an employment template)


## Data fields associated with employee information
If the name of the text field to be filled in the employment contract form to be filled in is used any of the following, the contents of the field are stored in the employee data when the employment contract accepted. When creating an employment contract, these data fields are pre-filled by the employee based on data fields.  
  
In addition to the list below, the employment contract is free to use for the service additional data fields created. When creating additional data fields in the field can enter its own data_ tag.  
  
  

**Name of the data field** | **Data field ID at the bottom**  
---|---  
First Name | data_etunimi  
Last Name | data_lastname  
Social security number | data_hetu  
Email | data_email  
Phone number | data_puhelinnumero  
Account number | data_tilinumero  
BIC | data_BIC  
Street address | data_katuosoite  
Postal Code | data_postinumero  
City | data_kaupunki  
Employment Start Date | data_aloituspvm  
Termination Date | data_lopetuspvm  
Weekly Hours | data_viikkotunnit  
Salary | data_tuntipalkka  
Your default destination | data_oletuskustannuspaikka
