# BIOS/UEFI Password Bypass Tool By Nur-m2r5r

![Security](https://img.shields.io/badge/Security-Firmware-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-GPLv3-red)


A security research tool for BIOS/UEFI password recovery and analysis. **Use responsibly and only on systems you own.**

## ⚠️ Important Disclaimer

This tool is provided for:
- Legitimate password recovery on systems you own
- Ethical security research
- Educational purposes

**Unauthorized access to computer systems is illegal in most jurisdictions.** The developers assume no liability for misuse of this software.

## Features

- 🛠️ BIOS backdoor password generation for major vendors
- 🔍 UEFI variable inspection (Linux)
- 📊 System firmware information gathering
- 🖥️ Cross-platform support (Windows/Linux)
- 🔒 Safety checks to prevent system damage

## Supported Vendors
```
| Vendor | Status | Notes |
|--------|--------|-------|
| Phoenix | ✅ Working | Basic algorithm support |
| Insyde | ✅ Working | Similar to Phoenix |
| AMI | ✅ Working | Partial support |
| Award | ⚠️ Limited | Basic support |
| Lenovo | 🚧 Experimental | Work in progress |
| Dell | 🚧 Experimental | Work in progress |
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Administrative privileges (for some features)

### Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/bios-password-bypass.git
cd bios-password-bypass

# Install dependencies
pip install -r requirements.txt
````
Usage
```bash
python src/main.py
```
Displays system BIOS/UEFI information without performing any modifications.

Password Generation
```bash
python src/main.py --generate
```
UEFI Variable Inspection (Linux)
```
sudo python src/main.py --list-uefi
```
Generate passwords for a Phoenix BIOS:
```

python src/main.py --generate --vendor Phoenix
```
List first 10 UEFI variables:
```
sudo python src/main.py --list-uefi | head -n 10
```
Code By Nur-m2r5r
