"""
Global settings for SVTool
"""
from src.modules.samba_dc.menu import SambaDCMenu

# Main menu options
MENU_OPTIONS = [
    {
        'name': 'Samba AD DC',
        'module': SambaDCMenu()
    }
]

# Color settings
COLORS = {
    'primary': '\033[92m',    # Light green
    'secondary': '\033[32m',  # Green
    'error': '\033[91m',      # Red
    'warning': '\033[93m',    # Yellow
    'reset': '\033[0m'        # Reset
}
