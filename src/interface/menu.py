"""Main menu interface module"""
import pyfiglet
from colorama import Fore, Style, init
from src.config.settings import MENU_OPTIONS
from src.utils.screen import Screen
from src.utils.message_box import MessageBox

class Menu:
    def __init__(self):
        init()  # Initialize colorama
        self.screen = Screen()
        self.msg_box = MessageBox()
    
    def show_banner(self):
        """Display the main banner"""
        self.screen.clear()
        banner = pyfiglet.figlet_format("SVTool", font="slant")
        print(Fore.GREEN + banner + Style.RESET_ALL)
        print(f"{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║ {'SERVER MANAGEMENT HUB':^61} ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    def show_menu(self):
        """Display the main menu options"""
        print(f"\n{Fore.LIGHTGREEN_EX}╔═══════════════════════════════════╗")
        for i, option in enumerate(MENU_OPTIONS, 1):
            print(f"║ [{i}] {option['name']:<29} ║")
        print(f"║ [0] {'Exit':<29} ║")
        print(f"╚═══════════════════════════════════╝{Style.RESET_ALL}")
    
    def handle_input(self):
        """Process user input"""
        try:
            choice = int(input(f"\n{Fore.YELLOW}Choose an option: {Style.RESET_ALL}"))
            
            if choice == 0:
                self.msg_box.show(
                    "GOODBYE",
                    ["Thank you for using SVTool!"],
                    color=Fore.GREEN
                )
                return False
            elif 1 <= choice <= len(MENU_OPTIONS):
                MENU_OPTIONS[choice-1]['module'].start()
            else:
                self.msg_box.show(
                    "ERROR",
                    ["Invalid option selected."],
                    color=Fore.RED
                )
                input("\nPress Enter to continue...")
            
            return True
        except ValueError:
            self.msg_box.show(
                "ERROR",
                ["Please enter a valid number!"],
                color=Fore.RED
            )
            input("\nPress Enter to continue...")
            return True
    
    def start(self):
        """Start the main menu loop"""
        running = True
        while running:
            self.show_banner()
            self.show_menu()
            running = self.handle_input()
