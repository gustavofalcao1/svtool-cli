import platform
import shutil
import os

class SystemCheck:
    def __init__(self):
        self.system = platform.system().lower()
        self.required_commands = ['python3', 'pip3']
    
    def check_requirements(self):
        """Check if all system requirements are met"""
        for cmd in self.required_commands:
            if not shutil.which(cmd):
                return False
        return True
    
    def get_system_info(self):
        """Return system information"""
        return {
            'system': self.system,
            'python_version': platform.python_version(),
            'architecture': platform.machine(),
            'processor': platform.processor()
        }
