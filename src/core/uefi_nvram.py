import os
import subprocess
from typing import Dict, Optional

class UefiNvram:
    """Handles UEFI NVRAM operations (Linux only)"""
    
    @staticmethod
    def _check_privileges() -> bool:
        """Check if we have root privileges"""
        return os.geteuid() == 0
    
    @staticmethod
    def list_variables() -> Dict[str, str]:
        """List UEFI variables"""
        if not UefiNvram._check_privileges():
            raise PermissionError("Root privileges required")
            
        variables = {}
        try:
            output = subprocess.check_output(["efivar", "-l"], text=True)
            for line in output.splitlines():
                if line.strip():
                    variables[line.strip()] = ""
        except FileNotFoundError:
            # Try alternative method
            try:
                output = subprocess.check_output(["ls", "/sys/firmware/efi/efivars"], text=True)
                for var in output.splitlines():
                    if var.strip():
                        variables[var.strip()] = ""
            except Exception as e:
                raise RuntimeError(f"Failed to list UEFI variables: {str(e)}")
        
        return variables
    
    @staticmethod
    def delete_variable(var_name: str) -> bool:
        """Delete a UEFI variable (CAUTION: Can brick system if misused)"""
        if not UefiNvram._check_privileges():
            raise PermissionError("Root privileges required")
            
        try:
            if os.path.exists(f"/sys/firmware/efi/efivars/{var_name}"):
                os.remove(f"/sys/firmware/efi/efivars/{var_name}")
                return True
            else:
                # Try using efivar command
                subprocess.run(["efivar", "-d", "-n", var_name], check=True)
                return True
        except Exception as e:
            print(f"Warning: Failed to delete variable {var_name}: {str(e)}")
            return False
