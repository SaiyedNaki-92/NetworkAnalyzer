from scapy.all import sniff

packet_count = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "OTHER": 0
}

def process_packet(packet):
    try:
        if packet.haslayer("TCP"):
            packet_count["TCP"] += 1
        elif packet.haslayer("UDP"):
            packet_count["UDP"] += 1
        elif packet.haslayer("ICMP"):
            packet_count["ICMP"] += 1
        else:
            packet_count["OTHER"] += 1
    except:
        pass

def start_capture():
    sniff(prn=process_packet, store=False)