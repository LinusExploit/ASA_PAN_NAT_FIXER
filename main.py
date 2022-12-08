import pandas as pd
from panos.policies import Rulebase, SecurityRule
from panos.objects import AddressObject
from panos.objects import AddressGroup
import time
import xml.etree.ElementTree as ET

addresses_from_cfg = []
address_groups_from_cfg = []
nested_address_groups = []

# read the excel sheet to get the list of the source translated address
df = pd.read_excel("/users/malhyari/Desktop/mqasem/scriptfiles/snatrules.xlsx")

# print(df.columns)
destination_translated = df['SOURCE'].tolist()
print(destination_translated)

# create a rule base class

tree = ET.parse("/users/malhyari/Desktop/mqasem/scriptfiles/pan.xml")
root = tree.getroot()

# parsing security rules
rules_xml = root.find("./devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/rulebase/security/")
addresses_xml = root.find("./devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address")
addresses_group_xml = root.find(
    "./devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group")

# parsing addresses
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

rules = SecurityRule().refreshall_from_xml(rules_xml)
addresses = AddressObject().refreshall_from_xml(addresses_xml)
addresses_groups = AddressGroup().refreshall_from_xml(addresses_group_xml)

print('Fetching Security Rules from the Configuration File')

# for rule in rules:
# print(rule.destination)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

print('Fetching Addresses from the Configuration File')
for address in addresses:
    # print(address.name)
    # print(address.value)
    addresses_from_cfg.append({'name': address.name, 'value': address.value})

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('Fetching Address Groups from the Configuration File')

for address in addresses_groups:
    # print(address.name)
    # print(address.static_value)
    address_groups_from_cfg.append({'name': address.name, 'members': address.static_value})

# Now checking if one of the addresses used in NAT are members of address groups
for address in destination_translated:
    for address_group in address_groups_from_cfg:
        if address in address_group['members']:
            print("address {} exists in address group {}".format(address, address_group['name']))
            nested_address_groups.append(address_group['name'])

# Now working on the policy address check direct no address group
for address in destination_translated:
    for rule in rules:
        # exact match based on name
        if address in rule.destination:
            print("Found an IP address {} that is used in policy {}".format(address, rule.name))

# Now showing the address groups used in policies and these address groups have NAT addresses as members
for v in nested_address_groups:
    for rule in rules:
        if v in rule.destination:
            print("Found an address group  {} that is used in policy {}".format(v, rule.name))

# print(addresses_from_cfg)
# print(address_groups_from_cfg)
