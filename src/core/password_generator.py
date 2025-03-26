import hashlib
from typing import Optional

class BiosPasswordGenerator:
    """Generates BIOS backdoor passwords based on known algorithms"""
    
    @staticmethod
    def _phoenix_hash(serial: str) -> str:
        """Phoenix BIOS hash algorithm"""
        # Implementation of known Phoenix hash algorithm
        # (Simplified example - real implementation would be more complex)
        hash_str = hashlib.md5(serial.encode()).hexdigest().upper()
        return hash_str[:8]
    
    @staticmethod
    def _ami_hash(serial: str) -> str:
        """AMI BIOS hash algorithm"""
        # AMI-specific algorithm would go here
        return "AMI" + serial[-5:]
    
    @staticmethod
    def generate(serial: str, vendor: str) -> Optional[str]:
        """Generate a backdoor password based on serial and vendor"""
        vendor = vendor.lower().strip()
        
        if not serial:
            return None
            
        if 'phoenix' in vendor or 'insyde' in vendor:
            return BiosPasswordGenerator._phoenix_hash(serial)
        elif 'ami' in vendor:
            return BiosPasswordGenerator._ami_hash(serial)
        elif 'award' in vendor:
            # Award BIOS algorithm would go here
            return "AWARD_" + serial[-4:]
        
        return None
