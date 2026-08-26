#!/usr/bin/env bash

if [ "$EUID" -ne 0 ]; then
  echo "❌ Error: Please run this script as root (use sudo)"
  exit 1
fi

echo "=== Deploying Bionic Tools to System Level ==="

# 1. Deploy the core engine globally as 'bread'
cp bionic_filter.py /usr/local/bin/bread
chmod +x /usr/local/bin/bread

# 2. Create a global wrapper binary for 'bcat'
cat << 'EOF' > /usr/local/bin/bcat
#!/usr/bin/env bash
cat "$@" | bread
EOF
chmod +x /usr/local/bin/bcat

echo "✅ System-wide deployment complete!"
echo "The 'bread' and 'bcat' commands are now natively available to all users and all scripts across the entire OS."
