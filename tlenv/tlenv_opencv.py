import os
import argparse
import cv2
from utils import format_duration, save_to_file, message

# add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", type=str)
parser.add_argument("-o", "--output", type=str, default=None)
args = parser.parse_args()


def get_video_duration(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    return duration


def get_durations_in_folder(folder_path):
    durations = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')):
            file_path = os.path.join(folder_path, filename)
            try:
                duration = get_video_duration(file_path)
                durations[filename] = duration
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return durations


folder_path = args.folder  # Update this to the path of your folder
output_path = args.output
durations = get_durations_in_folder(folder_path)
seconds = sum(durations.values())

for filename, duration in durations.items():
    print(f"{filename}: {duration} seconds ({format_duration(duration)})")

print(message(seconds))

if output_path is not None:
    save_to_file(output_path, seconds, durations)
