#Converts Video FIles to .MP4(H.264)
import os
import subprocess

def convert_to_mp4(input_file, output_file):
    """
    Converts any video file to an MP4 (H.264) format optimized for Raspberry Pi.
    """
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,         # Input file
        "-c:v", "libx264",        # Use H.264 codec
        "-preset", "fast",        # Fast encoding with good quality
        "-crf", "23",             # Controls quality (lower = better quality, but larger file size)
        "-c:a", "aac",            # Audio codec (AAC is lightweight)
        "-b:a", "128k",           # Set audio bitrate to 128 kbps
        "-movflags", "+faststart", # Optimizes MP4 for streaming/playback
        output_file
    ]

    print(f"Converting {input_file} to {output_file}...")
    subprocess.run(ffmpeg_cmd, check=True)
    print(f"Conversion complete: {output_file}")

# Convert all videos in a folder
def batch_convert(directory):
    for file in os.listdir(directory):
        if file.lower().endswith((".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpg", ".webm")):
            input_path = os.path.join(directory, file)
            output_path = os.path.join(directory, os.path.splitext(file)[0] + ".mp4")
            convert_to_mp4(input_path, output_path)

if __name__ == "__main__":
    folder = input("Enter the folder containing videos: ")
    batch_convert(folder)
