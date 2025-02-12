import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

# GPIO Pin Assignments
LED_PIN = 18  # Only one GPIO pin needed
LED_COUNT = 125  # Total LEDs (5 strips × 25 LEDs each)
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# Define Colors
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)

# Setup NeoPixel LED strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# GPIO Pins for input signals from Player Pi
INPUT_PINS = [17, 27, 22, 23, 24]  # Receiving signals from Player Pi

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup inputs from Player Pi
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set all LEDs to red initially
def set_all_leds(color):
    """Sets all LEDs to the given color."""
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()

set_all_leds(RED)  # Start with all LEDs red

def set_led_section(index, color):
    """Sets only the specific section of LEDs to the given color."""
    start = index * 25  # Each station has 25 LEDs
    end = start + 25
    for i in range(start, end):
        strip.setPixelColor(i, color)
    strip.show()

def listen_for_signals():
    """Listens for signals from Pi 1 and updates LEDs accordingly."""
    while True:
        for i, pin in enumerate(INPUT_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                print(f"LED section {i + 1} turning GREEN for 5 seconds.")

                # Set only the corresponding section to green
                set_led_section(i, GREEN)
                time.sleep(5)

                # Revert to red
                set_led_section(i, RED)

if __name__ == "__main__":
    try:
        listen_for_signals()
    except KeyboardInterrupt:
        print("Shutting down.")
        GPIO.cleanup()
