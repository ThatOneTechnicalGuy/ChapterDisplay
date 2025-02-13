import RPi.GPIO as GPIO
import vlc
import time
import tkinter as tk

# GPIO Pin Assignments
SENSOR_PINS = [5, 6, 13, 19, 26]  # Pressure sensors GPIO inputs
SIGNAL_PINS = [17, 27, 22, 23, 24]  # GPIO outputs to LED Pi (one per station)

# Video Paths
VIDEOS = [
    "/home/pi/videos/video1.mp4",
    "/home/pi/videos/video2.mp4",
    "/home/pi/videos/video3.mp4",
    "/home/pi/videos/video4.mp4",
    "/home/pi/videos/video5.mp4"
]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup sensor inputs
for pin in SENSOR_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Setup signal outputs
for pin in SIGNAL_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Default to LOW

# VLC Setup - Preload videos
instance = vlc.Instance("--no-xlib")  # Prevent VLC from taking over the display
players = [instance.media_player_new() for _ in range(len(VIDEOS))]

for i, player in enumerate(players):
    media = instance.media_new(VIDEOS[i])
    player.set_media(media)
    player.set_fullscreen(True)

# Tkinter Black Screen Setup
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.update()

def send_signal(index):
    """Send a HIGH signal to LED Pi to indicate video completion."""
    GPIO.output(SIGNAL_PINS[index], GPIO.HIGH)
    time.sleep(1)  # Hold signal for 1 second
    GPIO.output(SIGNAL_PINS[index], GPIO.LOW)  # Reset to LOW

def play_video(index):
    """Plays the preloaded video for its full duration."""
    print(f"Playing video {index + 1}...")

    # Hide black screen
    root.withdraw()

    # Play the video
    players[index].play()
    time.sleep(1)  # Allow VLC to start

    # Get video duration and ensure it plays fully
    duration = players[index].get_length() / 1000  # Convert to seconds
    while duration <= 0:  # If VLC hasn't loaded duration, keep checking
        time.sleep(0.5)
        duration = players[index].get_length() / 1000

    time.sleep(duration)  # Wait for video to finish

    # Stop video playback
    players[index].stop()

    # Notify LED Pi that video has ended
    send_signal(index)

    # Show black screen again
    root.deiconify()
    root.update()

def monitor_sensors():
    """Continuously monitors pressure sensors for activation."""
    while True:
        for i, pin in enumerate(SENSOR_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                play_video(i)
        time.sleep(0.1)  # Small delay to reduce CPU usage

if __name__ == "__main__":
    try:
        root.update()  # Ensure black screen is active
        monitor_sensors()
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        print("Cleaning up resources...")
        GPIO.cleanup()
        root.destroy()
