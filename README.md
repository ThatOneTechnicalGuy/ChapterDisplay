ChapterDisplay

Chapter Display ECAT 2025

📌 Raspberry Pi Interactive Video & LED System
An interactive display system using Raspberry Pi, sensor-triggered video playback, and synchronized LED signaling.
🛠️ Features

✔ Sensor-activated video playback – Different stations trigger different videos.
✔ LED signaling system – LEDs change colors based on video status.
✔ Multi-Raspberry Pi setup – One for video playback (Player Pi), one for LED control (LED Pi).
✔ Supports multiple video formats – MP4, AVI, MKV, WebM, and more.
✔ Expandable up to 5 stations – Each station has its own sensor, video, and LED output.
🔩 Hardware Requirements
Component	Quantity	Purpose
Raspberry Pi 4 (or 3B+)	2	Player Pi & LED Pi
MicroSD Card (32GB+)	2	OS and scripts
Pressure Sensors	5	To trigger videos
NeoPixel LED Strips (25 LEDs each)	5	For station indicators
HDMI Display	1	Video output
Power Supply (5V 3A)	2	Power for Raspberry Pis
Jumper Wires	Multiple	Wiring connections
Large Breadboard	1	Circuit prototyping and sensor connections
Display Device (Screen)	1	Output video playback
📥 Installation & Setup
1️⃣ Setup LEDPi (Controls LEDs)

⚠ Note: This setup disables audio on the device.
Method 1: Using Shell Script

Run the following command in the terminal:

cd ~ && curl -O https://raw.githubusercontent.com/ThatOneTechnicalGuy/ChapterDisplay/main/setup_led.sh && chmod +x setup_led.sh && sudo bash setup_led.sh

Method 2: Using Python Installer

    Download install_ledpi.py from the install scripts.
    Run the installer:

    python3 install_ledpi.py(use full file path)

2️⃣ Setup PlayerPi (Plays Video & Audio)
Method 1: Using Shell Script

Run the following command in the terminal:

cd ~ && curl -O https://raw.githubusercontent.com/ThatOneTechnicalGuy/ChapterDisplay/main/setup_player.sh && chmod +x setup_player.sh && sudo bash setup_player.sh

Method 2: Using Python Installer

    Download install_playerpi.py from the install scripts.
    Run the installer:

    python3 install_playerpi.py(use full file path)

✅ Final Notes

    Player Pi handles video and audio playback while LED Pi controls the lighting system.
    Make sure all hardware is correctly connected before running the setup.
