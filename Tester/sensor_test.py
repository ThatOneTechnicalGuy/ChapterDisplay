import RPi.GPIO as GPIO
import time

SENSOR_PINS = [5, 6, 13, 19, 26]  # GPIO inputs for sensors

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup sensor inputs
for pin in SENSOR_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Waiting for sensor input... Press a sensor to test.")
try:
    while True:
        for i, pin in enumerate(SENSOR_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                print(f"Sensor {i+1} (GPIO {pin}) is ACTIVE")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Test stopped.")
finally:
    GPIO.cleanup()
