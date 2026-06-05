---
id: 360002590097
title: Configuring SAML SSO
url: https://support.nepton.com/hc/en-gb/articles/360002590097-Configuring-SAML-SSO
locale: en-gb
category: Support
category_id: 360000446658
section: SAML Login
section_id: 360004542757
section_path:
- Login
- Single Sign-on (SSO)
- SAML Login
labels:
- NEPTONNEEDSREVIEW
promoted: false
updated_at: '2025-03-28T08:16:19Z'
edited_at: '2024-09-16T10:52:12Z'
---

# Configuring SAML SSO

Administrator can manage SSO configuration on **Employees - Administration - Single Sign-on (SSO)** section. New SSO configuration can be added under SAML by clicking **Add**. It's possible to configure multiple simultaneous SSO logins. All login options are show on service login page.
Identity provider (IdP) platform will provide necessary configuration details. IdP provides this information as XML formatted metadata. Based on this information, you can input the relevant details into Nepton.
If you are using Active Directory, please review [Configure ADFS server](<https://support.nepton.com/hc/en-gb/articles/360005242897>)
If you are using OKTA, please review [Configure OKTA service](<https://support.nepton.com/hc/en-gb/articles/5115492518301>)
![Capture_3.PNG](https://support.nepton.com/hc/article_attachments/360010905658)
**Disabled** allows temporary disablement of SSO login. Standard password login to Nepton will still function in normal fashion. It's also recommended practice to temporarily disable SSO login while SSO configurations are being created.
**Name** defines the name/text shown to users in the login page SSO button.
User can also login to the service with direct login link, so that separate SSO login is never shown. This direct link can be constructed with following procedure: [https://go.nepton.com/Portal/ExternalLogin/Saml2Login.aspx?deploymentID=XXXX&cc=YYYYY](<https://go.nepton.com/Portal/ExternalLogin/Saml2Login.aspx?deploymentID=XXXX&cc=YYYYY.>). Replace values XXXX and YYYY with actual values for your organization. These organization-specific values can be found on <https://go.nepton.com> after you have written your organization name, searched for the organization and found it. The values can now be seen on the address bar of your browser.
**Start use** enables scheduling the date when SSO becomes active.  
  
**End use** enables scheduling the date when SSO becomes inactive. This is particularly useful when switching to another identity service provider or certificate and it's necessary to schedule the roll-over date to be on specific date.  
  
**Management** defines if the SSO configuration is defined manually or if the configuration is automatically fetched from the metadata source. For automatic option, the metadata source must be compatible with Nepton. If automatic option is selected, most of the configurations will be automatically filled with correct values. You still need to define the correct configurations for those fields which were not automatically filled.  
  
**Identity provider identifier (Entity Id)** is the unique identifier for the IdP. Each IdP has this unique identifier. This value can be found from the IdP generated metadata XML.  
  
**Organization name** defines the organization or unit which is responsible for SSO IdP.  
  
**Contact person(s)** defines the persons responsible for SSO and IdP in the organization. Please include contact details here if available.  
  
**Sign on service URL** defines the IdP login page of your organization. This value can be found from the IdP generated metadata XML.  
  
**Sign on service URL binding** value can be found from the IdP generated metadata XML.  
  
**Certificate hash algorithm** value can be found from the IdP generated metadata XML.
**Nameid format** value can be found from the IdP generated metadata XML. This value is typically Transient or Unspecified.
**Use Nameid for person identification** In case of Yes, persons in the identity provider are identified by their NameId identifier and you do not need to specify person identification attributes below.
**Person identification** **attribute(s)** value can be found from the IdP generated metadata XML. The attribute can for example be name or email address. This is used to identify person.
Each attribute code can be found from IdP XML metadata. For example email address could have one code in the metadata, which alone could be sufficient attribute in case email address is the desired person identification method.
In some cases the desired identification attribute must be constructed from multiple attribute components. For example if email address is the desired person identification method, but such attribute does not exist in the IdP XML metadata, the desired attribute can be constructed by appending the desired extra text strings to the full name attribute. The full name could for example be defined by code “urn:oid:0.1.1234.56789100.100.1.1” which could be used as a basis for desired identification attribute by appending the desired email extension string to the end. In this example case, the full identification attribute could be "urn:oid:0.1.1234.56789100.100.1.1\@xycorp.com" and the corresponding email address would, be "fullname@xycorp.com". This email address would when be used as login identifier for Nepton and compared to person email address in Nepton.
**Identify person by** is the HR field saved to Nepton, which is in turn used to identify a person during SSO. Possible options are email, username, employee number and personal identification code.
  
When all necessary configuration information has been provided, press **Save** to save these configurations.
Add the IdP provided certificate and possible additional certificates.
![Capture_7.PNG](https://support.nepton.com/hc/article_attachments/360010905858)
![Capture_8.PNG](https://support.nepton.com/hc/article_attachments/360010905878)
Certificate information can be acquired from identity service (IdP) or the party the certificate was acquired from. Define the Base64 encoded certificate text to the **Add certificate** text field. You can find the Base64 text by:
a) Viewing the certificate file with text editor and by copying this text
b) Viewing the metadata URL with browser and by copying the the relevant text. The text typically begins with **MII** characters and ends with **=** character.
![mceclip0.png](https://support.nepton.com/hc/article_attachments/4412502889745)
After copying the value to the text area, press **Save**. Nepton will validate the certificate, which might take few minutes. After validation, the certificate is shown under certificates section. In case the validated certificate is currently in effect and there are no other certificates, the new certificate is immediately taken into use. 
Please note that customer can use different certificates for information encryption and signing. In this case there can be two different certificate texts in the metadata URL. Both should be added separately to Nepton.
Single SSO login can include multiple certificates. Only one of these certificates is in effect at any time. Defining multiple certificates enables scheduling future certificate changes to happen on desired date. In case the new certificate validity is overlapping with existing certificate validity, service will automatically propose a roll-over date, which administrator can approve. Administrator can also change the rollover date manually.
Some certificates can require multiple certificates in certificate chain (**supporting certificates**) to be considered as trustworthy. Service allows administrators to also define such supporting certificates.
Please note that possible encryption certificates need to added via the S**upporting certificates** section.
![Capture_8.PNG](https://support.nepton.com/hc/article_attachments/360010905878)
Under certificates section, each certificate can display various alerts. These are shown if for example the certificate is expired or expiring soon, there is a gap between validity dates of two certificates, or supporting certificates are not fully defined.
If you now enable SSO login, it should become visible on the login page. Click this SSO Login button. In case everything has been correctly defined, the browser will now move to IdP identity providing server, which might request some identification information. After this, the browser will move back to Nepton and automatically log into the service.
After the initial login, users will be logged in to Nepton until users log out by clicking the logout link. Please make sure users in your organization are informed about this, and understand to logout when necessary. Logout URL is <https://go.nepton.com/logout.aspx>
