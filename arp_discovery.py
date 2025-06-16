from scapy.all import ARP, Ether, srp


def arp_scan(subnet):

    print(f"[*] Performing ARP scan on {subnet}.....")

    arp = ARP(pdst=subnet)

    ether = Ether(dst= "ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    devices = []


    for sent,recieved in result:

        devices.append({'ip': recieved.psrc, 'mac': recieved.hwsrc})



    print(f"[+] Found {len(devices)} device(s)")

    return devices
