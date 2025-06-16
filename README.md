# NWscanner

A lightweight network scanner built on Kali Linux that:
- Scans the local network using ARP
- Scans common ports on active devices
- Tags devices with AI-based risk labels

## Features
- ARP scan of `/24` subnet
- Port scan of common ports
- Rule-based AI tagging engine
- JSON output for easy parsing

## Usage
```bash
pip install -r requirements.txt
sudo python3 scanner.py
