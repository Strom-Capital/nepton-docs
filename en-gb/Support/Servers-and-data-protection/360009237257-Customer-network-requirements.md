---
id: 360009237257
title: Customer network requirements
url: https://support.nepton.com/hc/en-gb/articles/360009237257-Customer-network-requirements
locale: en-gb
category: Support
category_id: 360000446658
section: Servers and data protection
section_id: 360005870038
section_path:
- Servers and data protection
labels:
- palomuuri
- palomuuriportit
- verkkomääritykset
promoted: false
updated_at: '2026-10-16T09:58:43Z'
edited_at: '2026-10-16T09:58:43Z'
---

# Customer network requirements

To utilise the Nepton platform, customer networks must be able to connect to it via the public internet. Below is a collection of all network requirements, which can be used by a network specialist to ensure good connectivity.
Please make sure that devices connected to the network also have access to name servers.
Customers can configure their firewalls and other similar systems with either the DNS addresses listed below or the IP addresses listed below.
Our goal is to keep the IP addresses specified in this document valid for a long time or even indefinitely. However, it is possible that the addresses may change in the future. If the addresses change at some point in the future, we will communicate the changes well in advance of the change date.
## Nepton services
Below are the connectivity details for the Nepton platform and all of its services.
To avoid any issues with future upgrades or changes in your subscription, it is recommended to permit access to all of the domains and ports mentioned for each environment you will use (production or testing).
### Production use
The latest version of the Nepton platform and all of its features and services. These are the connectivity details that are relevant to you.
#### Employees (HR), management services and wall terminals
Notes | Mandatory for browsers, mobiles, wall terminals, API and automated integrations  
---|---  
Domain | go.nepton.com  
IP address | 83.150.75.175  
TCP Ports | 80 and 443  
#### Worktime and wall terminals
Notes | Mandatory for browsers, mobiles, wall terminals, API and automated integrations  
---|---  
Domain | time.nepton.com  
IP address | 83.150.75.169  
TCP Ports | 80 and 443  
#### Learning management
Notes | Mandatory for browsers, mobiles, API and automated integrations  
---|---  
Domain | priima.nepton.com  
IP address | 94.237.105.7  
TCP Ports | 80 and 443  
#### Employee survey and analytics
Notes | Mandatory for browsers, mobiles, API and automated integrations  
---|---  
Domain | kivawork.nepton.com  
IP address | 94.237.15.216  
TCP Ports | 80 and 443  
#### Wall terminals
Terminals do not support AD or proxy technologies.
Best practice is for customer to connect terminals into a separate (physical or virtualised VLAN) customer network. This ensures maximum separation between wall terminals and other customer networks.
Unless a bespoke configuration has been agreed, terminals fetch their IP addresses and DNS servers used by customer from the customer DHCP server.
Customer firewall must allow terminals to access the DNS servers used by the customer. In addition, firewalls must allow terminals to outbound access the below mentioned Windows update service, NTP time service, and Teamviewer service.
Nepton Touch terminals update themselves automatically. You can read more about this on the [Terminal automatic updates](<https://support.nepton.com/hc/en-gb/articles/7611101419037>) article.
Nepton Touch terminal uses Microsoft's update servers for security updates. Windows Update uses TCP ports 80, 443 and the following servers:
http://download.windowsupdate.com  
http://*.download.windowsupdate.com  
http://download.microsoft.com  
https://*.update.microsoft.com  
http://*.update.microsoft.com  
https://update.microsoft.com  
http://update.microsoft.com  
http://*.windowsupdate.com  
http://*.windowsupdate.microsoft.com  
http://windowsupdate.microsoft.com  
https://*.windowsupdate.microsoft.com  
http://ntservicepack.microsoft.com  
http://wustat.windows.com
Nepton Touch terminals have TeamViewer installed for remote connection in case of problem situations.  
Teamviewer uses TCP 5938 port by default and 443 port as a backup. The PTR records of Teamviewer's IP addresses are directed to *.teamviewer.com.  
Nepton Touch terminals use NTP (network time protocol) to connect time1.mikes.fi. This address should not be blocked on firewall.
Nepton Flexim terminals use NTP (network time protocol) to connect time.mikes.fi, time1.mikes.fi and time2.mikes.fi. These addresses should not be blocked on firewall.
In addition to general access to Nepton servers as detailed above, customers using Netpton Flexim terminals must enable the following network access to/from the devices.
  * Inbound TCP/IP ports 22, 443, 9021
  * Inbound & Outbound ICMP protocol message type echo-request and reply
  * Inbound & Outbound UDP/IP ports 53, 123


### Public testing
Available by special agreement, a testing environment can be used by customers via the public internet. This environment can be updated to any version of the platform, even including near-future changes.
#### Employees (HR) and management services
Notes | Mandatory for browsers, mobiles, terminals, API and automated integrations  
---|---  
Domain | publictesting-go.nepton.com  
IP address | 83.150.75.168  
TCP ports | 80 and 443  
#### Worktime and wall terminals
Notes | Mandatory for browsers, mobiles, wall terminals, API and automated integrations  
---|---  
Domain | publictesting-time.nepton.com  
IP address | 83.150.75.165  
TCP ports | 80 and 443  
## SFTP data transfers
### Nepton SFTP service
On request, Nepton can provide an SFTP service for integration purposes. Credentials are issued upon delivery of the account.
Description | Customer opens outbound connection to Nepton SFTP service. This can be used to transfer data in/out from Nepton  
---|---  
Customer IP address |  Customer must inform Nepton about the static IP address they use to interact with the Nepton SFTP service. Note that dynamic cloud IP addresses are not sufficient. Always use static cloud IP addresses instead
  * AZURE <https://docs.microsoft.com/en-us/azure/virtual-network/public-ip-addresses>

  
Nepton Domain | transfers.nepton.com  
Nepton IP address | 83.150.75.188  
Nepton TCP port | 22  
### Customer SFTP server
If customer wishes to use their own SFTP server for integrations, they should inform Nepton about their SFTP server Domain/IP, TCP port, and credentials. Nepton will allow necessary connections to the customer SFTP server. 
To authorize Nepton to access customer SFTP server, customer must allow connections in their firewall from Nepton IP addresses mentioned below.
#### Required for HR and management service to use
Description | Customer opens an inbound connection to their SFTP server. This can be used to transfer data in/out from Nepton  
---|---  
Nepton Domain | go.nepton.com  
Nepton IP address | 83.150.75.175  
Customer TCP port | 22  
####  Required for Worktime and management service to use
Description | Customer opens an inbound connection to their SFTP server. This can be used to transfer data in/out from Nepton  
---|---  
Nepton Domain | time.nepton.com  
Nepton IP address | 83.150.75.169  
Customer TCP port | 22  
#### Required for creating, testing and deploying integrations in more efficient manner
Description | Customer opens an inbound connection. This can be used to create, deploy and test integrations.  
---|---  
Nepton IP address | 79.134.102.194  
Customer TCP port | 22
