import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

# GPIO Pin Assignments
INPUT_PINS = [17, 27, 22, 23, 24]  # Receiving signals from Player Pi

# NeoPixel LED Setup (Single Pin for All LEDs)
LED_PIN = 18  # GPIO 18 controls all LEDs
LED_COUNT = 125  # 5 stations × 25 LEDs each
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# Define Colors
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
OFF = Color(0, 0, 0)

# Setup NeoPixel LED strip
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup inputs from Player Pi
for pin in INPUT_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Function to set LED sections
def set_led_section(index, color):
    """Sets only the corresponding LED section."""
    start = index * 25  # Each station has 25 LEDs
    end = start + 25
    for i in range(start, end):
        strip.setPixelColor(i, color)
    strip.show()

# Function to turn all LEDs red initially
def set_all_leds(color):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()

set_all_leds(RED)  # Start with all LEDs red

# Function to turn off all LEDs
def turn_off_leds():
    """Turns all LEDs off."""
    for i in range(LED_COUNT):
        strip.setPixelColor(i, OFF)
    strip.show()

def listen_for_signals():
    """Listens for signals from Player Pi and updates LEDs accordingly."""
    while True:
        signal_received = False  # Track if any signal is received

        for i, pin in enumerate(INPUT_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                print(f"Signal detected on GPIO {pin} (Station {i+1}) - Turning LEDs GREEN")
                set_led_section(i, GREEN)
                time.sleep(5)  # Keep LEDs green for 5 seconds
                set_led_section(i, RED)  # Turn back to red
                signal_received = True

        if not signal_received:
            turn_off_leds()  # If no signal, turn LEDs OFF

        time.sleep(0.5)  # Small delay

if __name__ == "__main__":
    try:
        listen_for_signals()
    except KeyboardInterrupt:
        print("Shutting down.")
        turn_off_leds()  # Ensure LEDs turn off before exiting
        GPIO.cleanup()
