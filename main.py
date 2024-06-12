import os
import re
import psutil
from scapy.all import sniff
from colorama import init, Fore
from ascii import *

# Initialize colorama
init(autoreset=True)


def packet_callback(packet):
    print(Fore.GREEN + packet.summary())  # Print a summary of the packet in green

def start_sniffer(interface):
    print(f"Starting sniffing on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Intro screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX + ascii_art)  # Print ASCII art in yellow
    print(Fore.LIGHTYELLOW_EX + ascii_art2)  # Print ASCII art in yellow
    print(Fore.LIGHTWHITE_EX + ascii_art3)  # Print ASCII art in yellow

    input(Fore.CYAN + "Press Enter to start the network sniffer...")  # Print prompt in cyan

    # Get and print the list of available network interfaces
    interfaces = psutil.net_if_addrs()
    wifi_interfaces = []

    print(Fore.MAGENTA + "Available network interfaces:")  # Print header in magenta
    for iface in interfaces:
        print(iface)
        if re.search(r"Wi-Fi|Wireless|wlan", iface, re.IGNORECASE):
            wifi_interfaces.append(iface)

    # Show the available Wi-Fi interfaces
    print(Fore.BLUE + "\nAvailable Wi-Fi interfaces:")  # Print header in blue
    for iface in wifi_interfaces:
        print(iface)

    # Specify the network interface to use for sniffing packets
    if wifi_interfaces:
        interface = wifi_interfaces[0]  # Select the first available Wi-Fi interface
        start_sniffer(interface)
    else:
        print(Fore.RED + "No Wi-Fi interfaces found.")  # Print error message in red