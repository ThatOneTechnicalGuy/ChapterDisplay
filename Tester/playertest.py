import RPi.GPIO as GPIO
import vlc
import time
import tkinter as tk

# GPIO Pin Assignments (Not used for testing, but kept for later use)
SENSOR_PINS = [5, 6, 13, 19, 26]  # Pressure sensors GPIO inputs
SIGNAL_PINS = [17, 27, 22, 23, 24]  # GPIO outputs to LED Pi (one per station)

# Path to single test video
VIDEO_PATH = "/home/pi/videos/video1.mp4"

# Setup GPIO (Not needed for video-only test, but leaving it)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup signal outputs
for pin in SIGNAL_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Default to LOW

# VLC Setup
instance = vlc.Instance("--no-xlib")  # Prevent VLC from taking over display
player = instance.media_player_new()
media = instance.media_new(VIDEO_PATH)
player.set_media(media)
player.set_fullscreen(True)

# Tkinter Black Screen Setup
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.update()

def play_video():
    """Plays a single video and ensures it runs to completion."""
    print("Playing video...")

    # Hide black screen
    root.withdraw()

    # Start video playback
    player.play()
    time.sleep(1)  # Allow VLC to start

    # Ensure VLC has loaded the video duration
    duration = player.get_length() / 1000  # Convert to seconds
    while duration <= 0:
        print("Waiting for VLC to load duration...")
        time.sleep(0.5)
        duration = player.get_length() / 1000

    print(f"Video duration: {duration} seconds")

    # Wait for the video to finish playing
    while player.get_state() != vlc.State.Ended:
        time.sleep(0.5)

    print("Video finished.")

    # Stop playback to reset VLC state
    player.stop()

    # Show black screen again
    root.deiconify()
    root.update()

# Run the test
play_video()

# Cleanup (not strictly necessary since no GPIO used in this test)
GPIO.cleanup()
