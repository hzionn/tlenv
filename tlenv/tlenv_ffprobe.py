import os
import subprocess
import argparse
from utils import format_duration, save_to_file, message

# add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", type=str)
parser.add_argument("-o", "--output", type=str, default=None)
args = parser.parse_args()

# Define the absolute path to ffprobe
assert "ffprobe" in os.listdir(), "must have ffprobe in the same directory"
ffprobe_path = os.path.join(os.getcwd(), "ffprobe")  # For Windows use 'ffprobe.exe'


def get_video_duration(filename: str) -> float:
    result = subprocess.run(
        [
            ffprobe_path,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            filename,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return float(result.stdout)


def get_durations_in_folder(folder_path: str) -> dict:
    durations = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv")):
            file_path = os.path.join(folder_path, filename)
            try:
                duration = get_video_duration(file_path)
                durations[filename] = duration
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return durations


def main():
    folder_path = args.folder
    output_path = args.output
    durations = get_durations_in_folder(folder_path)
    seconds = sum(durations.values())

    for filename, duration in durations.items():
        print(f"{filename}: {duration} seconds ({format_duration(duration)})")

    print(message(seconds))

    # Save to a file (optional)
    if output_path is not None:
        save_to_file(output_path, seconds, durations)


if __name__ == "__main__":
    main()
