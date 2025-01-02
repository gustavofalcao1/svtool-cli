"""Samba AD DC module menu interface"""
from colorama import Fore, Style
from src.utils.screen import Screen
from src.utils.message_box import MessageBox
from .controller import SambaDCController

class SambaDCMenu:
    def __init__(self):
        self.controller = SambaDCController()
        self.screen = Screen()
        self.msg_box = MessageBox()
    
    def show_banner(self):
        """Display the Samba AD DC module banner"""
        print(f"\n{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║ {'SAMBA AD DC - MANAGEMENT':^61} ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    def show_menu(self):
        """Display the module menu options"""
        print(f"\n{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════╗")
        print(f"║ [1] {'Check Requirements':<29} ║")
        print(f"║ [2] {'Prepare System':<29} ║")
        print(f"║ [3] {'Install Samba':<29} ║")
        print(f"║ [4] {'Configure Domain':<29} ║")
        print(f"║ [9] {'Advanced Options':<29} ║")
        print(f"║ [0] {'Back':<29} ║")
        print(f"╚═══════════════════════════════════╝{Style.RESET_ALL}")

    def show_advanced_menu(self):
        """Display advanced options menu"""
        print(f"\n{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════╗")
        print(f"║ {'ADVANCED OPTIONS':^33} ║")
        print(f"╠═══════════════════════════════════╣")
        print(f"║ [1] {'Purge Samba':<29} ║")
        print(f"║ [0] {'Back':<29} ║")
        print(f"╚═══════════════════════════════════╝{Style.RESET_ALL}")
    
    def handle_advanced_menu(self):
        """Handle advanced menu options"""
        while True:
            self.screen.clear()
            self.show_banner()
            self.show_advanced_menu()
            
            try:
                choice = int(input(f"\n{Fore.YELLOW}Choose an option: {Style.RESET_ALL}"))
                
                if choice == 0:
                    break
                elif choice == 1:
                    if self.msg_box.prompt(
                        "WARNING - PURGE SAMBA",
                        [
                            "This will completely remove Samba and all its configurations:",
                            "• Remove all Samba packages",
                            "• Delete configuration files",
                            "• Remove domain controller setup",
                            "• Clear system configurations"
                        ],
                        "Are you sure you want to continue?",
                        ("y", "N")
                    ):
                        success, message = self.controller.purge_samba()
                        self.msg_box.show(
                            "PURGE RESULT",
                            [message],
                            color=Fore.GREEN if success else Fore.RED
                        )
                    else:
                        self.msg_box.show(
                            "OPERATION CANCELLED",
                            ["Purge operation cancelled by user."],
                            color=Fore.YELLOW
                        )
                else:
                    self.msg_box.show(
                        "INVALID OPTION",
                        ["Please select a valid option."],
                        color=Fore.RED
                    )
                
                input("\nPress Enter to continue...")
                
            except ValueError:
                self.msg_box.show(
                    "INPUT ERROR",
                    ["Please enter a valid number!"],
                    color=Fore.RED
                )
                input("\nPress Enter to continue...")
    
    def prepare_system(self):
        """Handle system preparation with confirmation"""
        # First check requirements
        success, message = self.controller.check_system_requirements()
        if not success:
            self.msg_box.show(
                "SYSTEM CHECK FAILED",
                [message],
                color=Fore.RED
            )
            return
        
        # Ask for confirmation
        if not self.msg_box.prompt(
            "WARNING - READ CAREFULLY",
            [
                "This operation will prepare your system:",
                "• Complete system update",
                "• Install all dependencies",
                "• Configure timezone",
                "• Configure DNS"
            ],
            "Do you want to continue?",
            ("y", "N")
        ):
            self.msg_box.show(
                "OPERATION CANCELLED",
                ["Operation cancelled by user."],
                color=Fore.YELLOW
            )
            return
        
        # Execute preparation
        success, message = self.controller.prepare_system()
        self.msg_box.show(
            "OPERATION RESULT",
            [message],
            color=Fore.GREEN if success else Fore.RED
        )
    
    def start(self):
        """Start the module menu loop"""
        while True:
            self.screen.clear()
            self.show_banner()
            self.show_menu()
            
            try:
                choice = int(input(f"\n{Fore.YELLOW}Choose an option: {Style.RESET_ALL}"))
                
                if choice == 0:
                    break
                elif choice == 1:
                    success, message = self.controller.check_system_requirements()
                    self.msg_box.show(
                        "SYSTEM CHECK RESULT",
                        [message],
                        color=Fore.GREEN if success else Fore.RED
                    )
                elif choice == 2:
                    self.prepare_system()
                elif choice == 9:
                    self.handle_advanced_menu()
                else:
                    self.msg_box.show(
                        "NOT IMPLEMENTED",
                        ["This option is not implemented yet."],
                        color=Fore.RED
                    )
                
                input("\nPress Enter to continue...")
                
            except ValueError:
                self.msg_box.show(
                    "INPUT ERROR",
                    ["Please enter a valid number!"],
                    color=Fore.RED
                )
                input("\nPress Enter to continue...")
