from scapy.all import IP, TCP, raw

ip_pkt = IP(
    version=4,
    ihl=5,
    tos=0x00,
    len=64,
    id=0xE60C,
    flags="DF",
    frag=0,
    ttl=63,
    proto=6,
    src="27.123.43.205",
    dst="172.20.121.255"
)

tcp_pkt = TCP(
    sport=443,
    dport=65402,
    seq=1,
    ack=1
)

pkt = ip_pkt / tcp_pkt

pkt_bytes = raw(pkt)
pkt2 = IP(pkt_bytes)

print("Calculated IP checksum:", hex(pkt2.chksum))
