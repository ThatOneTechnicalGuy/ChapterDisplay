import RPi.GPIO as GPIO
import vlc
import time
import tkinter as tk
import threading
import keyboard  # Import keyboard module for key press detection

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
    player.play()
    time.sleep(1)  # Allow VLC to start
    player.pause()  # Pause for instant playback

# Tkinter Black Screen Setup
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.update()

# Kill switch flag
running = True

def send_signal(index):
    """Send a HIGH signal to LED Pi to indicate video completion."""
    GPIO.output(SIGNAL_PINS[index], GPIO.HIGH)
    time.sleep(1)  # Hold signal for 1 second
    GPIO.output(SIGNAL_PINS[index], GPIO.LOW)  # Reset to LOW

def play_video(index):
    """Plays the preloaded video instantly and returns to a black screen."""
    print(f"Playing video {index + 1}...")

    # Hide black screen
    root.withdraw()
    players[index].play()

    # Get video duration
    time.sleep(0.5)
    duration = players[index].get_length() / 1000  # Convert to seconds

    time.sleep(duration)  # Wait for video to finish

    # Reset video for instant playback next time
    players[index].set_time(0)
    players[index].pause()

    # Notify LED Pi that video has ended
    send_signal(index)

    # Show black screen again
    root.deiconify()
    root.update()

def monitor_sensors():
    """Continuously monitors pressure sensors for activation."""
    global running
    while running:
        for i, pin in enumerate(SENSOR_PINS):
            if GPIO.input(pin) == GPIO.HIGH:
                play_video(i)
        time.sleep(0.1)  # Small delay to reduce CPU usage

def listen_for_kill_switch():
    """Detects keyboard input for a kill switch."""
    global running
    while running:
        if keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
            print("🔴 Kill switch activated! Exiting...")
            running = False
            break
        time.sleep(0.1)  # Prevents high CPU usage

if __name__ == "__main__":
    try:
        # Start keyboard listening in a separate thread
        kill_thread = threading.Thread(target=listen_for_kill_switch, daemon=True)
        kill_thread.start()

        # Run sensor monitoring
        monitor_sensors()
    except KeyboardInterrupt:
        print("Shutting down.")
    finally:
        print("🛑 Cleaning up resources...")
        GPIO.cleanup()
        root.destroy()
