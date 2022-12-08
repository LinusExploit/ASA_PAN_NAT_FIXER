# ASA_PAN_NAT_FIXER
Check Expedition Migrated Configuration to Validate IP translation in Security Policies
<br>
This Script will iterate over PAN OS config that is the output of expedition and it will has the NAT rules input as an excel sheet. The script will validate ip addresses in the security policies to ensure they are mapped properly. 
<br>

Required Packages:
<br>
pan-os-python
<br>
pandas
<br>

Please be aware of the following:
<br>
The script uses pan-os-python package and does not rely on manual parsing.
<br>
The script should be run after expedition migration is completed and config is exported to an xml file. 
<br>
The script does a level 1 nesting check for object groups so it does not only check the address usage directly but it also check the address groups used in policies. 
<br>
Work is still in Progress and the following can be added:
<br>
More beautified output
<br>
Format output to reflect exact nat rule affected by the security policy 
<br>
Auto Fix for the affected security policies which can be done easily as pan-os-python is used 
<br>
Output of a configuration file that has the fix 
<br>
The support to push the fix directly to the firewall via API 
<br>



Example of Initial Run:
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
Fetching Security Rules from the Configuration File
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
Fetching Addresses from the Configuration File
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
Fetching Address Groups from the Configuration File
<br>
address XXXXX exists in address group XXXXX
<br>
address XXXXX exists in address group XXXXX
<br>
address XXXXX exists in address group XXXXX
<br>
address XXXXX exists in address group XXXXX
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
Found an IP address XXXXX that is used in policy XXXXX
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
<br>
Found an address group  XXXXX that is used in policy XXXXX
<br>
Found an address group  XXXXX that is used in policy XXXXX
<br>
Found an address group  XXXXX that is used in policy XXXXX
<br>
Found an address group  XXXXX that is used in policy XXXXX
<br>
Found an address group  XXXXX that is used in policy XXXXX
<br>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

