from scapy.all import IP, ICMP, raw

ip_pkt = IP(
    version=4,
    ihl=5,
    tos=0x88,
    len=60,
    id=0x9FF3,
    flags=0,
    frag=0,
    ttl=54,
    proto=1,
    src="1.1.1.1",
    dst="10.242.7.206"
)

icmp_pkt = ICMP()

pkt = ip_pkt / icmp_pkt

pkt_bytes = raw(pkt)
pkt2 = IP(pkt_bytes)

print("Calculated IPv4 checksum:", hex(pkt2.chksum))
pkt2.show()
