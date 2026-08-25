#!/usr/bin/env python3
import sys
import math
import re
import argparse

# ANSI escape codes for terminal bolding
BOLD = '\033[1m'
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
    parser.add_argument('--version', action='version', version='Bionic Terminal v1.0 (GOAT Edition)')
    # If the user passes --help, argparse automatically intercepts and prints the manual
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
