from pythonping import ping
from scapy.all import ARP, Ether, srp

def get_MAC_from_IP(ip):
    ping(ip, count=1)
    arp = ARP(pdst="{}/32".format(ip))
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc