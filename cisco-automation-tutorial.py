# Command to run the program:   python cisco-automation-tutorial.py

# Print Pretty

import xmltodict
import xml.dom.minidom

# Import the required dependencies
from ncclient import manager
from jinja2 import Template
# Establish our NETCONF Session
m = manager.connect(host='192.168.0.87', port='830', username='admin',
                    password='admin', device_params={'name': 'csr'})

# Create a configuration filter
interface_filter = '''
  <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
          <interface>
            <GigabitEthernet>
              <name>1</name>
            </GigabitEthernet>
          </interface>
      </native>
  </filter>
'''

# Execute the get-config RPC
result = m.get_config('running', interface_filter)
# Print Pretty
print(xml.dom.minidom.parseString(str(result)).toprettyxml())

# Render our Jinja template
interface_template = Template(open('/usr/git_projects/pynet-script/interface.xml').read())
interface_rendered = interface_template.render(
  INTERFACE_INDEX='2', 
  IP_ADDRESS='10.0.0.1', 
  SUBNET_MASK='255.255.255.252'
)
# Execute the edit-config RPC
result = m.edit_config(target='running', config=interface_rendered)
# Print Pretty
print(xml.dom.minidom.parseString(str(result)).toprettyxml())