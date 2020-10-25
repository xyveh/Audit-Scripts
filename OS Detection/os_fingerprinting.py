#
# File:        os_detection.py
# Author:      Jarryd Brits - ATHENA GROUP
# Description: Run Program; Enter IP address or range of IP addresses to
#              get probable OS through use of TTL Patterns. Uses Ping from Scapy.


import concurrent.futures
from scapy.all import *
from scapy.layers.inet import IP, ICMP
import sys
import re
import ipaddress

def banner():
    print( " \033[91m      /\      \033[0m\033[1;92m  --------   \033[0m\033[1;93m  __     __  \033[0m\033[1;94m  _______  \033[0m\033[1;95m  ___      __  \033[0m\033[1;96m      /\       \033[0m\n")
    print( " \033[91m     /  \     \033[0m\033[1;92m |__    __|  \033[0m\033[1;93m |  |   |  | \033[0m\033[1;94m |  _____| \033[0m\033[1;95m |    \   |  | \033[0m\033[1;96m     /  \      \033[0m\n")
    print( " \033[91m    / /\ \    \033[0m\033[1;92m    |  |     \033[0m\033[1;93m |  |___|  | \033[0m\033[1;94m |  |___   \033[0m\033[1;95m |  |\ \  |  | \033[0m\033[1;96m    / /\ \     \033[0m\n")
    print( " \033[91m   / /__\ \   \033[0m\033[1;92m    |  |     \033[0m\033[1;93m |   ___   | \033[0m\033[1;94m |  ____|  \033[0m\033[1;95m |  | \ \ |  | \033[0m\033[1;96m   / /__\ \    \033[0m\n")
    print( " \033[91m  / ______ \  \033[0m\033[1;92m    |  |     \033[0m\033[1;93m |  |   |  | \033[0m\033[1;94m |  |____  \033[0m\033[1;95m |  |  \ \|  | \033[0m\033[1;96m  / ______ \   \033[0m\n")
    print( " \033[91m /_/      \_\ \033[0m\033[1;92m    |__|     \033[0m\033[1;93m |__|   |__| \033[0m\033[1;94m |_______| \033[0m\033[1;95m |__|   \____| \033[0m\033[1;96m /_/      \_\  \033[0m\n")
    print( " \033[40;38;5;82m CSEC-472 ROCHESTER INSTITUTE OF TECHNOLOGY - DUBAI \033[0m\n")
    print(" \n")
    print(" \033[95m OS FINGERPRINT PROGRAM\033[0m\n")


def send_ping(ip):
    try:
        ip = ipaddress.ip_address(ip)
        packet = IP(dst=str(ip), ttl=20) / ICMP()
        ply = sr1(packet, timeout=2,verbose=False)
        if ply == None:
            return None
        if IP in ply:
            if ply.getlayer(IP).ttl <= 64 and ply.getlayer(IP).ttl >32:
                os = "Linux || Unix"
                return os
            if ply.getlayer(IP).ttl > 64 or ply.getlayer(IP).ttl == 32:
                os = "Windows"
                return os
    except:
        #print("Invalid IP")
        return None


def main():
    banner()
    while True:
        print("To start please make a selection:")
        print("""
            (a)     Input a single IP address
            (b)     Input a range of IP addresses
            (f)     File input
            (exit)  To exit program""")
        x = input("Selection: ")
        if x == 'a':
            while True:
                print("Enter a single IP address: ie. XXX.XXX.XXX.XXX\n")
                y = input("IP ADDRESS: ")
                print("-"*50)
                if(re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", y)):
                    os = send_ping(y)
                    print("IP: {}, OS: {}".format(y,os))
                    break
                elif y == 'exit' or y == 'Exit':
                    break
                else:
                    print("Entered Invalid IP Address")
        elif x == 'b':
            while True:
                print("Enter range IP address: ie. AAA.AAA.AAA.AAA-BBB.BBB.BBB.BBB")
                y = input("IP ADDRESS RANGE: ")
                print("-"*50)
                if(re.search("^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})-([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", y)):
                    start_ip = y.split("-")[0]
                    end_ip = y.split("-")[1]
                    increment = 0
                    while True:
                        ip = ipaddress.ip_address(start_ip + increment)
                        if ip == ipaddress.ip_address(end_ip):
                            y = send_ping(str(ip))
                            print("IP: {}, OS: {}".format(y,os))
                            break
                        else:
                            send_ping(str(ip))
                            print("IP: {}, OS: {}".format(y,os))
                    break
                elif y == 'exit' or y == 'Exit':
                    break
                else:
                    print("Entered Invalid IP Address")
        elif x == 'f':
            print("Enter file path or file name if in same directory: ")
            y = input("File: ")
            print("-"*50)
            ip_addresses = []
            f = open(y)
            for line in f:
                ip_addresses.append(line.strip())

            with concurrent.futures.ProcessPoolExecutor() as executor:
                for ip, os_result in zip(ip_addresses, executor.map(send_ping, ip_addresses)):
                    if os_result != None:
                        print("IP: {}, OS: {}".format(ip,os_result))
        elif x == 'exit' or x == 'Exit':
            print("------------GOODBYE------------")
            break
        else:
            print("Invalid option selected")
        print("-"*50)

main()
