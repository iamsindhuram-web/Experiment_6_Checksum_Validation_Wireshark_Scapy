from scapy.all import IP

ip_pkt = IP(
    version=4,
    ihl=5,
    tos=0x80,
    len=1278,
    id=0,
    flags="DF",
    frag=0,
    ttl=59,
    proto=17,
    src="142.251.222.206",
    dst="172.20.121.255"
)

raw_bytes = bytes(ip_pkt)
ip_pkt2 = IP(raw_bytes)

print("Calculated IP Header Checksum:", hex(ip_pkt2.chksum))
