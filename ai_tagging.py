def tag_device(ip, open_ports, mac_address, hostname):
    tags = []

    # Risky service check
    if 23 in open_ports or 21 in open_ports:
        tags.append("🔴 Risk: Insecure services (Telnet/FTP)")

    if 445 in open_ports:
        tags.append("🟡 SMB detected")

    if 31337 in open_ports:
        tags.append("🔴 Suspicious: Backdoor port 31337")

    if "unknown" in hostname.lower():
        tags.append("❓ Hostname unknown")

    # Vendor logic (dummy check for now)
    if mac_address.startswith(("00:1A:2B", "00:11:22")):
        tags.append("🟢 Known Vendor")
    else:
        tags.append("🟡 Unknown Vendor")

    if not open_ports:
        tags.append("🟢 No open ports")

    if not tags:
        tags.append("🟢 Safe")

    return tags

