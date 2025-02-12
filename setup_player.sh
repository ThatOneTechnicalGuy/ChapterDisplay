#!/bin/bash

echo "🚀 Setting up Player Pi (Video Playback) System..."

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ Please run as root: sudo bash setup_player.sh"
   exit 1
fi

# Update system packages
echo "📦 Updating system..."
apt update && apt upgrade -y

# Install required system packages (NO LED LIBRARIES)
echo "🔧 Installing dependencies..."
apt install -y python3 python3-pip python3-rpi.gpio python3-spidev python3-numpy python3-pil \
               python3-vlc python3-tk git python3-pynput

# Clone Chapter Display repo (if not already cloned)
INSTALL_DIR="/home/pi/ChapterDisplay"

if [ ! -d "$INSTALL_DIR" ]; then
    echo "📂 Cloning Chapter Display repository..."
    git clone https://github.com/ThatOneTechnicalGuy/ChapterDisplay.git "$INSTALL_DIR"
else
    echo "✅ Repository already exists. Pulling latest updates..."
    cd "$INSTALL_DIR"
    git pull
fi

# Ensure scripts are executable
chmod +x "$INSTALL_DIR"/*.py

echo "🎉 Setup complete! Run the following command to start Player Pi:"
echo ""
echo "📌 Start Player Pi (Video Playback):"
echo "   cd ~/ChapterDisplay && python3 PlayerPI2.py"
echo ""

echo "✅ Player Pi setup is complete!"
