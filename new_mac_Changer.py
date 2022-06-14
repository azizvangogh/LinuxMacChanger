import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i" , "--interface" , dest="interface" , help="Example : python new_mac_changer -i eth0")
parse_object.add_option("-m" , "--mac", dest="mac_adress",help="Example : python new_mac_changer -i wlan0 -m 00:22:52:64:85:88")
(user_inputs,arguments) = parse_object.parse_args()

user_interface = user_inputs.interface
user_mac_adress = user_inputs.mac_adress
print("Your MacAdress has Changed")

subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether",user_mac_adress])
subprocess.call(["ifconfig","eth0","up"])
