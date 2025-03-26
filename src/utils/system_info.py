import subprocess
import re
import platform

class SystemInfo:
    """Gathers system information needed for password generation"""
    
    @staticmethod
    def get_bios_vendor() -> str:
        """Get BIOS vendor information"""
        try:
            if platform.system() == "Windows":
                command = "wmic bios get manufacturer /value"
                result = subprocess.check_output(command, shell=True, text=True)
                return result.split("=")[1].strip()
            elif platform.system() == "Linux":
                with open('/sys/class/dmi/id/bios_vendor', 'r') as f:
                    return f.read().strip()
        except Exception:
            return "Unknown"
    
    @staticmethod
    def get_system_serial() -> str:
        """Get system serial number"""
        try:
            if platform.system() == "Windows":
                command = "wmic bios get serialnumber /value"
                result = subprocess.check_output(command, shell=True, text=True)
                return result.split("=")[1].strip()
            elif platform.system() == "Linux":
                with open('/sys/class/dmi/id/product_serial', 'r') as f:
                    return f.read().strip()
        except Exception:
            return "Unknown"
    
    @staticmethod
    def get_smbios_data() -> dict:
        """Get SMBIOS data (more comprehensive)"""
        # This would be expanded to get detailed SMBIOS/DMI information
        return {
            "vendor": SystemInfo.get_bios_vendor(),
            "serial": SystemInfo.get_system_serial(),
            "version": "1.0"  # Placeholder
        }
