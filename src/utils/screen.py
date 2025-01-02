import os
import platform

class Screen:
    @staticmethod
    def clear():
        """Clear terminal screen in a cross-platform way"""
        if platform.system().lower() == "windows":
            os.system('cls')
        else:
            os.system('clear')
