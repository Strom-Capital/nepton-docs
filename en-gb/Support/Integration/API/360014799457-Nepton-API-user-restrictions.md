---
id: 360014799457
title: Nepton API user restrictions
url: https://support.nepton.com/hc/en-gb/articles/360014799457-Nepton-API-user-restrictions
locale: en-gb
category: Support
category_id: 360000446658
section: API
section_id: 360000921798
section_path:
- Integration
- API
labels: []
promoted: false
updated_at: '2025-09-08T07:24:57Z'
edited_at: '2025-09-08T07:24:57Z'
---

# Nepton API user restrictions

By default, the features of Nepton API can be used by all properly authenticated users. If desired, users of Nepton API can be restricted to limit usage or to increase data security. Restricting users is possible based on IP addresses.
You can enable the restrictions by logging into the service and going to **Employees > Administration > Settings: Security > Limit Nepton API access** and adding the IP addresses from which the use of Nepton API is allowed. Add a name describing the allowed IP address(es) in the name field, add comments if desired, and set the validity period for the access. Once you have defined the allowed IP addresses, enable the restrictions by pressing "Allow calls to Nepton API web services only from IP addresses listed below ".
Note: In the "Allowed IP addresses" field, you can specify not only individual IP addresses, but also a set of IP addresses. Below are descriptions of the rules in use.
**1\. Individual IP address**
For example 83.150.75.169
**2\. IP-address range**
For example 83.150.75.165-83.150.75.175
**3\. IP-address and asterisk**
When using asterisk, the following ways to define IP addresses are allowed (numbers can be anything between 0-255):
83.150.75.*  
83.150.*  
83.*  
*
For example. 80.150.*.169 is not allowed.
**4\. A combination of the above expressions, separated by a comma**
For example 83.150.75.169, 83.150.75.180-83.150.75.190, 83.150.78.*, 83.150.90.155
![](https://support.nepton.com/hc/article_attachments/30163367036061)
