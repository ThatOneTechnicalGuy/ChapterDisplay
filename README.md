# ChapterDisplay
Chapter Display ECAT 2025

📌 Chapter Display - Raspberry Pi Interactive Video & LED System

An interactive display system using Raspberry Pi, sensor-triggered video playback, and synchronized LED signaling.

🛠️ Features

✔ Sensor-activated video playback – Different stations trigger different videos.


✔ LED signaling system – LEDs change colors based on video status.

✔ Multiple Raspberry Pis – One for video playback (Player Pi), one for LED control (LED Pi).

✔ Compatible with various video formats (MP4, AVI, MKV, WebM, etc.).

✔ Supports up to 5 stations – Each station can have its own sensor, video, and LED output.


🛠️ Hardware Requirements

Component	Quantity	Purpose

Raspberry Pi 4 (or 3B+)	2	Player Pi & LED Pi

MicroSD Card (32GB+)	2	OS and scripts

Pressure Sensors	5	To trigger videos

NeoPixel LED Strips (25 LEDs each)	5	For station indicators

HDMI Display	1	Video output

Power Supply (5V 3A)	2	For Raspberry Pi

Jumper Wires	Multiple	Wiring connections

Display Device(Screen)





SETUP_LEDPI:
This is for the Pi that will manipulate the LED's:Note this disables audio use on the device
run this command in terminal: 

cd ~ && curl -O https://raw.githubusercontent.com/ThatOneTechnicalGuy/ChapterDisplay/main/setup_led.sh && chmod +x setup_led.sh && sudo bash setup_led.sh

SETUP_PLAYER:
This is for the Pi that will play video and audio

run this command in terminal:

cd ~ && curl -O https://raw.githubusercontent.com/ThatOneTechnicalGuy/ChapterDisplay/main/setup_player.sh && chmod +x setup_player.sh && sudo bash setup_player.sh




