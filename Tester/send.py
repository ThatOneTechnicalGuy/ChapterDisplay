import RPi.GPIO as GPIO
import time

# GPIO Pins for sending signals (must match LED Pi's input pins)
SIGNAL_PINS = [17, 27, 22, 23, 24]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set all signal pins as outputs
for pin in SIGNAL_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Ensure all start LOW

try:
    print("Testing signal transmission...")
    
    for i, pin in enumerate(SIGNAL_PINS):
        print(f"Sending HIGH signal to GPIO {pin} (Station {i+1})")
        GPIO.output(pin, GPIO.HIGH)  # Send signal
        time.sleep(2)  # Hold signal for 2 seconds
        GPIO.output(pin, GPIO.LOW)  # Turn off signal
        print(f"Signal to GPIO {pin} turned OFF")
        time.sleep(1)  # Small delay before testing next

    print("Test complete! All signals sent.")
    
except KeyboardInterrupt:
    print("Test interrupted!")

finally:
    GPIO.cleanup()  # Reset GPIO on exit
