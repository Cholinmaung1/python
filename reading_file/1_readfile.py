from netmiko import ConnectHandler

#with open("interface_assign", "r") as r:
#read = r.read()
#print(read)
file = open("bgp_peer_config", "r")
try:
    print("Opening File")
    content = file.read()
    print(content)
finally:
    print("Closing File")
    file.close()
