#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]; then
  echo "❌ Error: Please run this script as root (use sudo)"
  exit 1
fi

echo "=== Removing Bionic Tools from System ==="
rm -f /usr/local/bin/bread
rm -f /usr/local/bin/bcat

echo "✅ System-wide removal complete!"
