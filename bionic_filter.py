#!/usr/bin/env python3
import sys
import math
import re
import argparse
import os

def get_dynamic_color():
    """
    Reads the dynamic color from end-4 dots (kitty-theme.conf) 
    and returns a precise ANSI TrueColor code to match the wallpaper.
    """
    theme_path = os.path.expanduser("~/.local/state/quickshell/user/generated/terminal/kitty-theme.conf")
    
    try:
        with open(theme_path, 'r') as f:
            for line in f:
                # We extract color4 (or color6) which Material-You uses as a primary accent
                if line.startswith("color4"):
                    hex_color = line.split()[1].strip().lstrip('#')
                    # Convert hex to RGB integers
                    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
                    # Return the exact ANSI TrueColor escape sequence for Bold + RGB
                    return f'\033[1;38;2;{r};{g};{b}m'
    except Exception:
        pass # Silently fallback if the user changes setups
        
    # Default fallback: Standard white bold
    return '\033[1m'

# Dynamically set the BOLD color at runtime
BOLD = get_dynamic_color()
RESET = '\033[0m'

def bionic_word(word):
    if len(word) < 2:
        return word
    mid = math.ceil(len(word) / 2)
    return f"{BOLD}{word[:mid]}{RESET}{word[mid:]}"

def process_line(line):
    tokens = re.split(r'(\W+)', line)
    return "".join([bionic_word(t) if t.isalnum() else t for t in tokens])

def main():
    parser = argparse.ArgumentParser(description="Bionic Terminal Text Filter")
    parser.add_argument('--version', action='version', version='Bionic Terminal v1.1 (Dynamic Color Edition)')
    args = parser.parse_args()

    try:
        for line in sys.stdin:
            sys.stdout.write(process_line(line))
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit(0)
    except IOError:
        sys.exit(0)

if __name__ == "__main__":
    main()
