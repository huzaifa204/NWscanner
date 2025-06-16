from local_info import get_local_ip
from arp_discovery import arp_scan
from port_scanner import scan_ports
from ai_tagging import tag_device
import threading
import socket
import json
import subprocess

def run_scanner():
    local_ip = get_local_ip()
    ip_parts = local_ip.split(".")
    subnet = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"   
    print(f"[*] Scanning SUbnet: {subnet}")
    

    devices = arp_scan(subnet)
    results = []
    threads = []

    def scan_and_tag(device):
        ip = device['ip']
        mac = device['mac']
        try:
            hostname = socket.gethostbyadr(ip)[0]
        except:
            hostname = subprocess.getoutput(f"nmblookup -A {ip} | grep '<00>' | awk '{{print $1}}'")
            if not hostname or "name_query" in hostname:
                hostname = "unknown"
        open_ports = scan_ports(ip)
        tags = tag_device(ip,open_ports,mac,hostname)
        
        

        results.append({
            "ip": ip,
            "mac": mac,
            "hostname": hostname,
            "open_ports": open_ports,
            "tags": tags
            })

    for device in devices:
        t = threading.Thread(target=scan_and_tag, args=(device,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[*] Scan Results: ")
    print(json.dumps(results, indent = 2))



if __name__ == "__main__":
    run_scanner()
