import subprocess
import sys
import os

class Installer:
    def __init__(self):
        self.requirements_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'requirements.txt'
        )
    
    def install_requirements(self):
        """Install required dependencies"""
        try:
            subprocess.check_call([
                sys.executable, 
                '-m', 
                'pip', 
                'install', 
                '-r', 
                self.requirements_file
            ])
            return True
        except subprocess.CalledProcessError:
            return False
