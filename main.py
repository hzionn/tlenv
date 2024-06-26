import os
import argparse
from tlenv import utils, mvpy, opencv

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--method", type=str)
parser.add_argument("-f", "--folder", type=str)
parser.add_argument("-o", "--output", type=str, default=None)
args = parser.parse_args()

METHOD = args.method


def get_durations_in_folder(folder_path: str) -> dict:
    durations = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(utils.media_types):
            file_path = os.path.join(folder_path, filename)
            if METHOD == "mvpy":
                duration = mvpy.get_video_duration(file_path)
            elif METHOD == "opencv":
                duration = opencv.get_video_duration(file_path)
            elif METHOD == "ffprobe":
                print("ffprobe is no longer support")
                break
            else:
                print("available options: mvpy and opencv")
                break
            durations[filename] = duration
    return durations


def main():
    folder_path = args.folder
    output_path = args.output
    durations = get_durations_in_folder(folder_path)
    seconds = sum(durations.values())

    for filename, duration in durations.items():
        print(f"{filename}: {duration} seconds ({utils.format_duration(duration)})")

    print(utils.message(seconds))

    if output_path is not None:
        utils.save_to_file(output_path, seconds, durations)


if __name__ == "__main__":
    main()
