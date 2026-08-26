#!/usr/bin/env python3
import sys
import math
import re
import argparse

# Standard ANSI Bold
BOLD = '\033[1m'
RESET = '\033[0m'

def bionic_word(word):
    if len(word) < 2:
        return word
    mid = math.ceil(len(word) / 2)
    first_half = word[:mid]
    second_half = word[mid:]
    
    # Kitty Text Sizing Protocol (OSC 66)
    # n=6:d=5 gives a 1.2x scale multiplier (slightly larger text)
    # We wrap the first half in the OSC 66 protocol and embed the ANSI Bold inside it
    kitty_scaled_first = f"\033]66;n=6:d=5;{BOLD}{first_half}{RESET}\a"
    
    return f"{kitty_scaled_first}{second_half}"

def process_line(line):
    tokens = re.split(r'(\W+)', line)
    return "".join([bionic_word(t) if t.isalnum() else t for t in tokens])

def main():
    parser = argparse.ArgumentParser(description="Bionic Terminal Text Filter")
    parser.add_argument('--version', action='version', version='Bionic Terminal v2.0 (Kitty Sizing Protocol Edition)')
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
