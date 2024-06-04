import os
import subprocess
import argparse

# add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", type=str)
parser.add_argument("-o", "--output", type=str, default=None)
args = parser.parse_args()

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the absolute path to ffprobe
assert "ffprobe" in os.listdir(), "must have ffprobe in the same directory"
ffprobe_path = os.path.join(current_dir, "ffprobe")  # For Windows use 'ffprobe.exe'


def get_video_duration(filename: str):
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


def format_duration(seconds: int) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}h {minutes}m {seconds}s"


def total_duration(seconds: int) -> str:
    return f"\nTotal duration of all videos: {seconds} seconds ({format_duration(seconds)})"


def save_to_file(output_path: str, seconds: int, durations: dict):
    with open(output_path, "w") as f:
        for filename, duration in durations.items():
            f.write(
                f"{filename}: {duration} seconds ({format_duration(duration)})\n"
            )
        f.write(total_duration(seconds))


def main():
    folder_path = args.folder
    output_path = args.output

    durations = get_durations_in_folder(folder_path)
    seconds = sum(durations.values())

    for filename, duration in durations.items():
        print(f"{filename}: {duration} seconds ({format_duration(duration)})")

    print(total_duration(seconds))

    # Save to a file (optional)
    if output_path is not None:
        save_to_file(output_path, seconds, durations)


if __name__ == "__main__":
    main()
