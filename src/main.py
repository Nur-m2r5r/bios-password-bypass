import argparse
from utils.system_info import SystemInfo
from core.password_generator import BiosPasswordGenerator
from core.uefi_nvram import UefiNvram

def main():
    parser = argparse.ArgumentParser(
        description="BIOS/UEFI Password Bypass Tool",
        epilog="Use responsibly and only on systems you own."
    )
    
    parser.add_argument(
        "-g", "--generate",
        action="store_true",
        help="Generate possible backdoor passwords"
    )
    
    parser.add_argument(
        "-l", "--list-uefi",
        action="store_true",
        help="List UEFI variables (Linux, requires root)"
    )
    
    parser.add_argument(
        "-r", "--reset",
        action="store_true",
        help="Attempt to reset BIOS/UEFI settings (DANGEROUS)"
    )
    
    args = parser.parse_args()
    
    print("[*] Gathering system information...")
    sys_info = SystemInfo.get_smbios_data()
    print(f"    BIOS Vendor: {sys_info['vendor']}")
    print(f"    System Serial: {sys_info['serial']}")
    
    if args.generate:
        print("\n[*] Generating possible backdoor passwords...")
        password = BiosPasswordGenerator.generate(
            sys_info['serial'],
            sys_info['vendor']
        )
        
        if password:
            print(f"    Possible password: {password}")
        else:
            print("    No known algorithm for this vendor")
    
    if args.list_uefi:
        print("\n[*] Listing UEFI variables...")
        try:
            variables = UefiNvram.list_variables()
            print(f"    Found {len(variables)} variables")
            for var in list(variables.keys())[:5]:  # Show first 5 for demo
                print(f"    - {var}")
            if len(variables) > 5:
                print(f"    ... and {len(variables)-5} more")
        except Exception as e:
            print(f"    Error: {str(e)}")
    
    if args.reset:
        print("\n[!] WARNING: This operation is dangerous!")
        print("    It may brick your system or cause data loss.")
        print("    Only proceed if you know what you're doing.")
        confirm = input("    Type 'YES' to confirm: ")
        if confirm == "YES":
            # This would be implemented carefully in a real tool
            print("    Not implemented in this demo version")
        else:
            print("    Operation cancelled")

if __name__ == "__main__":
    main()
