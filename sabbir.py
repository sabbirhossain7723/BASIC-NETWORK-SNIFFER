from scapy.all import *

def packet_callback(packet):
    """Print a summary of each packet captured."""
    print(packet.summary())

def main():
    """Capture and analyze network traffic."""
    # Start sniffing packets
    sniff(prn=packet_callback, filter="tcp", store=0)

if __name__ == "__main__":
    main()

