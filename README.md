# 🛡️ OSINT Intelligence Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![OSINT](https://img.shields.io/badge/OSINT-Toolkit-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

A modular Python-based **Open Source Intelligence (OSINT)** toolkit that gathers publicly available information about a domain from multiple sources.

> **For educational purposes and authorized security assessments only.**

---

# 📌 Features

✅ WHOIS Lookup

✅ DNS Records Lookup

✅ IP Address Information

✅ SSL Certificate Analysis

✅ HTTP Headers Inspection

✅ Technology Detection

✅ robots.txt Analysis

✅ Reverse DNS Lookup

✅ GeoIP Lookup

✅ Subdomain Enumeration

✅ Email Security Checks
- SPF
- DKIM
- DMARC

✅ Port Scanning

---

# 📂 Project Structure

```
OSINT-INTELLIGENCE-TOOLKIT/
│
├── app.py
├── requirements.txt
├── README.md
│
└── modules/
    ├── whois_lookup.py
    ├── dns_lookup.py
    ├── ip_lookup.py
    ├── ssl_lookup.py
    ├── headers_lookup.py
    ├── technology_lookup.py
    ├── robots_lookup.py
    ├── reverse_dns_lookup.py
    ├── geoip_lookup.py
    ├── subdomain_lookup.py
    ├── email_security.py
    └── port_scan.py
```

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/kishoreshenrayanperumal-byte/OSINT-INTELLIGENCE-TOOLKIT.git
```

Move into the project directory

```bash
cd OSINT-INTELLIGENCE-TOOLKIT
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run the toolkit

```bash
python app.py
```

Example

```
Enter a domain:

example.com
```

---

# 💻 Example Output

```
==============================
        OSINT REPORT
==============================

Target Domain:
example.com

WHOIS Information
-------------------------
Registrar:
IANA

Creation Date:
1995-08-13

Expiration Date:
2026-08-12

-------------------------

DNS Records
A Record:
93.184.216.34

MX Records:
mail.example.com

-------------------------

IP Information

IP:
93.184.216.34

Country:
United States

Organization:
Example Organization

-------------------------

SSL Certificate

Issuer:
Let's Encrypt

Valid Until:
2026-02-10

-------------------------

HTTP Headers

Server:
nginx

Content-Type:
text/html

-------------------------

Technology Detection

Nginx
Bootstrap
jQuery

-------------------------

robots.txt

Found:
https://example.com/robots.txt

-------------------------

Email Security

SPF:
Configured

DKIM:
Configured

DMARC:
Configured

-------------------------

Port Scan

80/tcp  Open

443/tcp Open

==============================
```

---

# 📦 Requirements

- Python 3.10+
- requests
- python-whois
- dnspython
- builtwith
- python-nmap
- ipwhois
- pyOpenSSL
- socket

Install them using

```bash
pip install -r requirements.txt
```

---

# 🛠 Technologies Used

- Python
- Requests
- DNSPython
- Socket
- OpenSSL
- WHOIS
- Nmap
- BuiltWith

---

# 🎯 Future Improvements

- Web Interface (Flask)
- PDF Report Generation
- HTML Report Generation
- Shodan Integration
- VirusTotal Integration
- URL Reputation Checker
- Threat Intelligence APIs
- JSON Export
- CSV Export

---

# ⚠️ Disclaimer

This project is intended **only for educational purposes** and authorized security assessments.

Do **not** use this tool against systems you do not own or have explicit permission to test.

The developer is not responsible for any misuse of this project.

---


GitHub:
https://github.com/kishoreshenrayanperumal-byte
