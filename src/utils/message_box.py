"""Utility class for creating adaptive message boxes"""
from colorama import Fore, Style
from typing import List, Optional, Tuple

class MessageBox:
    def __init__(self, min_width: int = 31, max_width: int = 71):
        """Initialize MessageBox with minimum and maximum widths
        
        Args:
            min_width: Minimum internal width (default: 31)
            max_width: Maximum internal width (default: 71)
        """
        self.min_width = min_width
        self.max_width = max_width
    
    def _calculate_width(self, title: str, content: List[str]) -> int:
        """Calculate required width based on content
        
        Args:
            title: Box title
            content: List of content lines
        
        Returns:
            Required width that fits all content
        """
        # Get max length from title and content
        lengths = [len(title)] + [len(line) for line in content]
        required_width = max(lengths) + 4  # Add padding
        
        # Ensure width is odd for perfect centering
        if required_width % 2 == 0:
            required_width += 1
        
        # Clamp between min and max width
        return max(min(required_width, self.max_width), self.min_width)
    
    def _format_line(self, content: str, width: int, align: str = 'left') -> str:
        """Format a line with proper alignment and padding
        
        Args:
            content: Line content
            width: Box width
            align: Alignment ('left', 'center', or 'right')
        
        Returns:
            Formatted line
        """
        if align == 'center':
            return f"║ {content:^{width}} ║"
        elif align == 'right':
            return f"║ {content:>{width}} ║"
        else:  # left align
            return f"║ {content:<{width}} ║"
    
    def show(self, title: str, content: List[str], color: str = Fore.YELLOW,
             title_align: str = 'center', content_align: str = 'left') -> None:
        """Display a message box with adaptive width
        
        Args:
            title: Box title
            content: List of content lines
            color: Color for the box (default: yellow)
            title_align: Title alignment (default: center)
            content_align: Content alignment (default: left)
        """
        # Calculate appropriate width
        width = self._calculate_width(title, content)
        
        # Create box borders
        top_border = "╔" + "═" * (width + 2) + "╗"
        mid_border = "╠" + "═" * (width + 2) + "╣"
        bottom_border = "╚" + "═" * (width + 2) + "╝"
        
        # Print box
        print(f"\n{color}{top_border}")
        print(self._format_line(title, width, title_align))
        print(mid_border)
        
        for line in content:
            print(self._format_line(line, width, content_align))
        
        print(f"{bottom_border}{Style.RESET_ALL}")
    
    def prompt(self, title: str, content: List[str], 
               prompt_text: str = "Continue?", 
               options: Tuple[str, str] = ("y", "N")) -> bool:
        """Display a message box and prompt for confirmation
        
        Args:
            title: Box title
            content: List of content lines
            prompt_text: Text to show in prompt (default: "Continue?")
            options: Tuple of (yes, no) options (default: ("y", "N"))
        
        Returns:
            True if user confirmed, False otherwise
        """
        self.show(title, content)
        response = input(f"\n{Fore.YELLOW}{prompt_text} ({options[0]}/{options[1]}): {Style.RESET_ALL}").lower()
        return response == options[0].lower()
