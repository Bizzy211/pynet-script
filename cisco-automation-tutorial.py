# Command to run the program:   python cisco-automation-tutorial.py

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
print(result)