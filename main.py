import os
import re
import psutil
from scapy.all import sniff

# ASCII Art for the intro screen
ascii_art = r"""

  _____            ____               ____  _____   ______          ____   ____         _____     ____   ____  _____   ______        _____   
 |\    \   _____  |    |         ____|\   \|\    \ |\     \        |    | |    |   ____|\    \   |    | |    ||\    \ |\     \   ___|\    \  
 | |    | /    /| |    |        /    /\    \\\    \| \     \       |    | |    |  /     /\    \  |    | |    | \\    \| \     \ |    |\    \ 
 \/     / |    || |    |       |    |  |    |\|    \  \     |      |    |_|    | /     /  \    \ |    | |    |  \|    \  \     ||    | |    |
 /     /_  \   \/ |    |  ____ |    |__|    | |     \  |    |      |    .-.    ||     |    |    ||    | |    |   |     \  |    ||    | |    |
|     // \  \   \ |    | |    ||    .--.    | |      \ |    |      |    | |    ||     |    |    ||    | |    |   |      \ |    ||    | |    |
|    |/   \ |    ||    | |    ||    |  |    | |    |\ \|    |      |    | |    ||\     \  /    /||    | |    |   |    |\ \|    ||    | |    |
|\ ___/\   \|   /||____|/____/||____|  |____| |____||\_____/|      |____| |____|| \_____\/____/ ||\___\_|____|   |____||\_____/||____|/____/|
| |   | \______/ ||    |     |||    |  |    | |    |/ \|   ||      |    | |    | \ |    ||    | /| |    |    |   |    |/ \|   |||    /    | |
 \|___|/\ |    | ||____|_____|/|____|  |____| |____|   |___|/      |____| |____|  \|____||____|/  \|____|____|   |____|   |___|/|____|____|/ 
    \(   \|____|/   \(    )/     \(      )/     \(       )/          \(     )/       \(    )/        \(   )/       \(       )/    \(    )/   
     '      )/       '    '       '      '       '       '            '     '         '    '          '   '         '       '      '    '    
            '                                                                                                                                
    Wlan Hound by G#sh                                                                                           Wi-Fi Network Packet Sniffer

                                                           |\|\
                                                          ..    \       .
                                                        o--     \\    / @)
                                                         v__///\\\\__/ @
                                                           {           }
                                                            {  } \\\{  }
                                                            <_|      <_|                                                                

                                                         github.link.link                     
                                                                                    
"""


def packet_callback(packet):
    print(packet.summary())  # Print a summary of the packet


def start_sniffer(interface):
    print(f"Starting sniffing on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)


if __name__ == "__main__":
    # Intro screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_art)

    input("Press Enter to start the network sniffer...")

    # Get and print the list of available network interfaces
    interfaces = psutil.net_if_addrs()
    wifi_interfaces = []

    print("Available network interfaces:")
    for iface in interfaces:
        print(iface)
        if re.search(r"Wi-Fi|Wireless|wlan", iface, re.IGNORECASE):
            wifi_interfaces.append(iface)

    # Show the available Wi-Fi interfaces
    print("\nAvailable Wi-Fi interfaces:")
    for iface in wifi_interfaces:
        print(iface)

    # Specify the network interface to use for sniffing packets
    if wifi_interfaces:
        interface = wifi_interfaces[0]  # Select the first available Wi-Fi interface
        start_sniffer(interface)
    else:
        print("No Wi-Fi interfaces found.")
