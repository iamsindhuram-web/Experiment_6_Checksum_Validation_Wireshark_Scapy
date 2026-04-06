from scapy.all import IP, TCP

ip_pkt = IP(
    version=4,
    ihl=5,
    tos=0x00,
    len=40,
    id=0x3475,
    flags="DF",
    frag=0,
    ttl=63,
    proto=6,
    src="104.18.39.21",
    dst="172.20.121.255"
)

tcp_pkt = TCP(
    sport=12345,
    dport=80,
    seq=1,
    ack=0,
    flags="S",
    window=64240
)

pkt = ip_pkt / tcp_pkt

raw_bytes = bytes(pkt)
pkt2 = IP(raw_bytes)

print("IPv4 Header Checksum:", hex(pkt2.chksum))
print("TCP Checksum:", hex(pkt2[TCP].chksum))
