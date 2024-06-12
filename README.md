
# Wlan Hound Wi-Fi-Sniffer

## Overview
This Python script allows you to sniff network packets on your Wi-Fi network using Scapy. It provides a simple interface to capture and analyze network traffic.

## Purpose
Network sniffing is the process of intercepting and logging the traffic passing over a digital network. It can be useful for various purposes, including network troubleshooting, security analysis, and performance monitoring. 

## Usage
1. Install the required dependencies listed in `requirements.txt`.
   
 ```sh
   pip install -r requirements.txt
 ```

2. Run the sniffer.py script to start sniffing network packets.
   
 ```sh
  python sniffer.py
 ```

3. The script will display a summary of each packet captured, including information such as source and destination IP addresses, protocol, and payload.


## Interpreting the Results
**The output of the script provides information about each packet captured. Here's how to interpret each line:**

- **Ether / IP / TCP / UDP:** Indicates the protocol stack used in the packet (Ethernet, IP, TCP, or UDP).
- **Source and Destination IP Addresses:** Shows the source and destination IP addresses of the packet.
- **Port Numbers:** For TCP and UDP packets, the source and destination port numbers are displayed.
- **Protocol:** Specifies the protocol used in the packet (e.g., HTTP, DNS).
- **Flags:** For TCP packets, the flags indicate the state of the connection (e.g., SYN, ACK).
- **Payload:** Displays the payload of the packet, if available


