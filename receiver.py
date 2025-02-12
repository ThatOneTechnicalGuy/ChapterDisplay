import RPi.GPIO as GPIO
import time
from rpi_ws281x import *

# GPIO Pins for receiving signals from Player Pi
INPUT_PINS = [17, 27, 22, 23, 24]

# NeoPixel Setup
LED_PIN = 18  # Single GPIO pin for controlling all LEDs
LED_COUNT = 125  # Total LEDs (5 strips × 25 LEDs each)
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# Define Colors
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
OFF = Color(0, 0, 0)  # LED OFF color

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
    start = index * 25
    end = start + 25
    for i in range(start, end):
        strip.setPixelColor(i, color)
    strip.show()

# Function to turn off all LEDs
def turn_off_leds():
    """Turns all LEDs off."""
    for i in range(LED_COUNT):
        strip.setPixelColor(i, OFF)
    strip.show()

try:
    print("Listening for signals from Player Pi...")
    while True:
        signal_received = False  # Track if any signal is received

        for i, pin in enumerate(INPUT_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                print(f"Signal detected on GPIO {pin} (Station {i+1}) - Turning LEDs GREEN")
                set_led_section(i, GREEN)
                time.sleep(1)  # Keep green briefly
                signal_received = True

        if not signal_received:
            turn_off_leds()  # If no signal, turn LEDs OFF

        time.sleep(0.5)  # Small delay to prevent CPU overuse

except KeyboardInterrupt:
    print("Test interrupted!")

finally:
    turn_off_leds()  # Ensure LEDs turn off before exiting
    GPIO.cleanup()  # Reset GPIO
