#!/usr/bin/env fish

echo "=== Installing Bionic Terminal Tools for Fish ==="

# Ensure Fish functions directory exists
mkdir -p ~/.config/fish/functions

# 1. Install 'bcat' as a native Fish function
echo 'function bcat --description "Bionic Cat for text files"
    cat $argv | ~/Study/Bionic_Terminal_Tools/bionic_filter.py
end' > ~/.config/fish/functions/bcat.fish

# 2. Install 'bread' as an alias in config
if not grep -q "alias bread=" ~/.config/fish/config.fish
    echo 'alias bread="~/Study/Bionic_Terminal_Tools/bionic_filter.py"' >> ~/.config/fish/config.fish
end

echo "Success! 🚀 Run 'source ~/.config/fish/config.fish' to activate."
