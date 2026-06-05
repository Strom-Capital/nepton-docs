---
id: 360005242897
title: Configure ADFS server
url: https://support.nepton.com/hc/en-gb/articles/360005242897-Configure-ADFS-server
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
updated_at: '2025-04-22T05:35:41Z'
edited_at: '2025-04-22T05:34:10Z'
---

# Configure ADFS server

Below are detailed technical instructions for configuration of a customers' ADFS server (Active Directory Federation Services) for SAML based SSO (Single Sign On) with the Nepton platform. These instructions are intended for individuals with experience in the area of ADFS server.
Please see other articles under the [Configuring SSO](<https://support.nepton.com/hc/en-gb/articles/360002590097>) section for more information on the topic of SSO configuration.
Nepton SP (Service Provider) metadata can be found here:
<https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml>
## Configure the Relying Party Trust (Service Provider)
choose one of the two options below:
### Import data online or on a local network 
  * Login to the ADFS server and open the management console.
  * Right-click on "Relying Party Trusts" under "Trust Relationships" > Add Relying Party Trust... > Start
  * Select "Import data about the relying party published online or on a local network"
  * Enter: 
    * https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml
  * Next
  * Enter a Display Name, eg: "go.nepton.com" > Next
  * Click Next to skip the Multi-factor Authentication
  * Select "Permit all users to access this relying party" (you can change this later) > Next
  * Click Next to continue
  * Uncheck "Open the claim rules dialog..." > Close
  * Right-click the new trust you just created > Properties
  * Advanced tab > Choose the desired algorithm, which will be set up also in Nepton
  * Click OK 


### Enter data manually
  * Login to the ADFS server and open the management console.
  * Right-click on "Relying Party Trusts" under "Trust Relationships" > Add Relying Party Trust... > Start
  * Select "Enter data about the relying party manually" > Next
  * Enter a Display Name, eg: "go.nepton.com" > Next
  * Click "AD FS 2 (or 3)" profile > Next
  * Click Next to skip the Token encryption certificate
  * Click Next to skip the Configure URL section
  * Enter following as the "Relying party trust identifier" 
    * **https://go.nepton.com/ExternalLogin/Saml**
  * Add > Next
  * Click Next to skip the Multi-factor Authentication
  * Select "Permit all users to access this relying party" (you can change this later) > Next
  * Click Next to skip
  * Uncheck "Open the claim rules dialog..." > Close
  * Right-click the new trust you just created > Properties 
    * Monitoring tab 
      * Enter following as Relying party's metadata URL 
        * <https://go.nepton.com/externallogin/metadata/EntityDescriptor_SP_go.nepton.com_V7_27_Apr_2025_26_Apr_2026.xml>
        * Add > Next
      * Check "Monitor Relying Party"
      * Check "Automatically update relying party"
    * Advanced tab > Choose the correct algorithm and **send the hash algorithm to Nepton**
    * Enter following on Endpoints tab > **SAML Assertion Consumer** , with **POST** binding 
      * **https://go.nepton.com/ExternalLogin/Saml2Consumer.aspx**
    * Click OK


## Ensure required certificates are set up
  1. Login to the ADFS server and open the management console.
  2. Ensure you have the **VRK Gov. Root CA - G2 **and **VRK CA for Service Providers - G4** Certificates installed in the Trusted Intermediate & Trusted Root stores. These certificates are available from <https://dvv.fi/en/ca-certificates>
  3. Import the go.nepton.com certificate 
     1. Right-click the Relying Party > Update from Federation Metadata 
        1. If this doesn't work, please check if you can from ADFS server access the metadata URL. If this is blocked, you might need to open the firewall accordingly.
     2. Verify the certificate's path is valid in the "Certificate Path" tab under the certificate's properties.
  4. Configuring the Claim Rules 
     1. Right-click the new trust you just created > Edit Claim Rules...
     2. Add Rule > **Send LDAP Attributes as Claims** > Next 
        1. Claim rule name > enter "Get LDAP Attributes"
        2. Attribute store > select Active Directory
        3. LDAP Attribute > Email Addresses
        4. Outgoing Claim Type > Email Address
        5. Finish
     3. Add Rule > **Transform an incoming claim** > Next 
        1. Claim rule name > enter "Convert Email to Name Id"
        2. Incoming claim type > Email Address
        3. Outgoing claim type > Name ID
        4. Outgoing Name ID format > Transient Identifier
        5. Finish
     4. Apply > OK


## Collect the Token-Signing Certificate
  * Login to the ADFS server and open the management console
  * Browse to Service > Certificates > Right-click the Token-Signing Certificate > View Certificate > Details Tab > Copy to File > Next 
    * Click "No, do not export the private key" > Next
    * Select "Base-64 encoded X.509" > Next
    * Pick a location to save the file > Next > Finish
    * You will need the certificate file on next step


## Creating the settings in Nepton
  * Add the SSO settings and certificate to Nepton. Guidance can be seen [here](<https://support.nepton.com/hc/en-gb/articles/360002590097>).
