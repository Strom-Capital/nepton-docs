---
id: 23063634766493
title: Configure Entra ID service
url: https://support.nepton.com/hc/en-gb/articles/23063634766493-Configure-Entra-ID-service
locale: en-gb
category: Support
category_id: 360000446658
section: SAML Login
section_id: 360004542757
section_path:
- Login
- Single Sign-on (SSO)
- SAML Login
labels: []
promoted: false
updated_at: '2025-04-22T06:56:01Z'
edited_at: '2025-04-22T06:56:01Z'
---

# Configure Entra ID service

This approach should only be used if you can't use the recommended [Microsoft Login](<https://support.nepton.com/hc/en-gb/articles/360002590137>) method.
Below are detailed technical instructions for configuration of a customers' Entra ID service for SAML based SSO (Single Sign On) with the Nepton platform. These instructions are intended for individuals with experience in the Entra ID service.
Please see other articles under the [Configuring SSO](<https://support.nepton.com/hc/en-gb/articles/360002590097>) section for more information on the topic of SSO configuration.
## Entra ID configuration
1) Nepton SP (Service Provider) metadata can be found from the link below. Download this XML file and save it to your computer.
<https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml>
2) Sign in to the Microsoft Entra admin center with your admin credentials.
3) Go to Identity, Applications, Enterprise Applications, New application, Create your own application
4) Add a new application called "SSO Nepton SAML 2". Select the "Integrate any other application you don't find in the gallery (Non-gallery)". Click Create.
5) Go the "SSO Nepton SAML 2" application. Select Manage, Single-sign-on, and select the SAML method. In the "Set up Single Sign-On with SAML" select "Upload metadata file" and upload the the XML file you downloaded in step 1. Review settings. Save.
6) Copy following values to notepad:
  * App Federation Metadata Url
  * Login URL
  * Microsoft Entra Identififier


7) Go the "SSO Nepton SAML 2" application. Select Manage, Properties, and check that "Assignment required" is set to "No". Click Save.
## Nepton configuration
8) Sign in to Nepton with your admin credentials
9) Go the Employees, Administration, Single Sign-On (SSO)
10) Click "Add" to create new SSO
  * Management: manual
  * Entity Id: The "Microsoft Entra Identifier" value you copied to notepad in step 6
  * Sign on service Url: he "Login Url" value you copied to notepad in step 6
  * Sign on service url binding: HTTP-POST
  * Certificate hash-algorithm: SHA-256
  * Name id format: unspecified
  * Use NameId for person identification: Yes
  * Identify person by: Email


11) Save
12) Find the "App Federation Metadata URL" address you copied to notepad in step 6. Open this address. Look at the long text string between ds:X509Certificate tags and copy this long text string to notepad. Add the missing certificate (this long text string) to Nepton and save it.
