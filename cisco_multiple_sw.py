from netmiko import ConnectHandler

iosv2_l2_s1 = {
	"device_type" : "cisco_ios",
	"ip" : "192.168.245.129",
	"username" : "cisco",
	"password" : "cisco123"
}

iosv2_l2_s2 = {
	"device_type" : "cisco_ios",
	"ip" : "192.168.245.130",
	"username" : "cisco",
	"password" : "cisco123"
}

iosv2_l2_s3 = {
	"device_type" : "cisco_ios",
	"ip" : "192.168.245.131",
	"username" : "cisco",
	"password" : "cisco123"
}

all_switches = [iosv2_l2_s1, iosv2_l2_s2, iosv2_l2_s3]

#network_connect = ConnectHandler(**devices)

for devices in all_switches:
	network_connect = ConnectHandler(**devices)
	for n in range (2,21):
		print ("Creating VLAN " + str(n))
		vlan_create_cmd = ["vlan " + str(n), "name Python Vlan" + str(n)]
		output = network_connect.send_config_set(vlan_create_cmd)
		print(output)
	
