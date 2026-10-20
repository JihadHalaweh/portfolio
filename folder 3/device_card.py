""" device_card this program is meant to to give the details of a port """
MAX_CONNECTIONS = 100 
device_name = " Web_server-03"
device_ip = " 192.168.1.3"
service = " HTTP"
open_port =  443
print("device name: ", device_name)
print("ip address: ", device_ip)
print("service: ", service)
print("port : ", open_port)
print("max connections: ", MAX_CONNECTIONS)
service = "SSH"
open_port = 83 
print("updated services : ", service,"on port",open_port)
