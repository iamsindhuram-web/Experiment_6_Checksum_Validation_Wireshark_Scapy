from scapy.all import IP, UDP

ip_pkt = IP(
    version=4,
    ihl=5,
    tos=0x80,
    len=306,
    id=0,
    flags="DF",
    frag=0,
    ttl=59,
    proto=17,
    src="142.251.222.206",
    dst="172.20.121.255"
)

udp_pkt = UDP(
    sport=12345,
    dport=443
)

pkt = ip_pkt / udp_pkt

raw_bytes = bytes(pkt)
pkt2 = IP(raw_bytes)

print("IPv4 Header Checksum:", hex(pkt2.chksum))
print("UDP Checksum:", hex(pkt2[UDP].chksum))
