import subprocess
import argparse
import re

def create_ob():
    parse_object = argparse.ArgumentParser()
    parse_object.add_argument("-i","--interface",dest="interface",help="selection interface \n usage: python mac-changer.py -i eth0")
    parse_object.add_argument("-m","--mac_address",dest="mac_address",help="write mac-address: \n usage: python mac-changer.py -m 00:00:00:00:00:00")
    return parse_object.parse_args()

def proc():
    subprocess.run(["ifconfig",b.interface,"down"])
    subprocess.run(["ifconfig",b.interface,"hw","ether",b.mac_address])
    subprocess.run(["ifconfig",b.interface,"up"])

def check_mac_state():
    ipa = subprocess.check_output(["ifconfig",b.interface])
    dipa = ipa.decode('utf-8')
    rege = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",dipa)
    if rege.group(0) == b.mac_address:
        print("Mac address change !")
    else:
        print("Error")

b = create_ob()
proc()
check_mac_state()
