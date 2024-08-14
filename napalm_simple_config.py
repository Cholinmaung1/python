import json
from napalm import get_network_driver

driver = get_network_driver("ios")
iosvl2 = driver("192.168.245.129", "cisco", "cisco123")
iosvl2.open()

ios_output = iosvl2.get_facts()
print (ios_output)

#print output with json format
print (json.dumps(ios_output, indent=4))
