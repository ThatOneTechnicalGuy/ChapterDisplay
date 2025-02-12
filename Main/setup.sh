#!/bin/bash

echo "🚀 Setting up Chapter Display System..."

# Ensure script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "❌ Please run as root: sudo bash setup.sh"
   exit 1
fi

# Update system packages
echo "📦 Updating system..."
apt update && apt upgrade -y

# Install required packages
echo "🔧 Installing dependencies..."
apt install -y python3 python3-pip vlc git

# Install Python libraries (including breaking system packages if needed)
echo "🐍 Installing Python libraries..."
pip3 install --break-system-packages RPi.GPIO rpi_ws281x adafruit-circuitpython-neopixel

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

echo "🎉 Setup complete! Run the following commands to start:"
echo ""
echo "📌 For Player Pi (Video Playback):"
echo "   cd ~/ChapterDisplay && python3 Player_PI.py"
echo ""
echo "📌 For LED Pi (LED Control):"
echo "   cd ~/ChapterDisplay && python3 LED_PI.py"
echo ""

echo "✅ System is ready to go!"

