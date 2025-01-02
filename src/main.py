#!/usr/bin/env python3

from src.interface.menu import Menu
from src.utils.system_check import SystemCheck
from src.utils.installer import Installer

def main():
    """Main function of SVTool"""
    # Check system requirements
    system = SystemCheck()
    if not system.check_requirements():
        installer = Installer()
        installer.install_requirements()
    
    # Start main menu
    menu = Menu()
    menu.start()

if __name__ == "__main__":
    main()
