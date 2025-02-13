import os
import subprocess
import sys

INSTALL_DIR = "/home/pi/ChapterDisplay"

def run_command(command):
    """Executes a shell command with error handling."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing: {command}")
        print(e)
        sys.exit(1)

def install_dependencies():
    """Installs required system packages for LEDpi."""
    print("📦 Updating system packages...")
    run_command("sudo apt update && sudo apt upgrade -y")

    print("🔧 Installing dependencies...")
    run_command("sudo apt install -y python3 python3-pip python3-rpi.gpio python3-spidev python3-numpy python3-pil "
                "python3-vlc python3-tk git python3-pynput python3-rpi-ws281x")

def clone_repository():
    """Clones the ChapterDisplay repository or updates it if it exists."""
    if not os.path.exists(INSTALL_DIR):
        print("📂 Cloning ChapterDisplay repository...")
        run_command(f"git clone https://github.com/ThatOneTechnicalGuy/ChapterDisplay.git {INSTALL_DIR}")
    else:
        print("✅ Repository already exists. Pulling latest updates...")
        run_command(f"cd {INSTALL_DIR} && git pull")

def set_executable_permissions():
    """Ensures all Python scripts in the repository are executable."""
    run_command(f"chmod +x {INSTALL_DIR}/*.py")

def main():
    """Main setup process for LEDpi."""
    print("🚀 Setting up LED Pi (NeoPixel LED Control)...")
    install_dependencies()
    clone_repository()
    set_executable_permissions()

    print("\n🎉 Setup complete! To start LED Pi, run:")
    print("📌 Start LED Pi (LED Control):")
    print(f"   cd {INSTALL_DIR} && python3 LED_PI.py")
    print("\n✅ LED Pi setup is complete!")

if __name__ == "__main__":
    main()
