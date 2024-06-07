media_types = (".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv")

def format_duration(seconds: int) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours}h {minutes}m {seconds}s"


def message(seconds: int) -> str:
    return f"\nTotal duration of all videos: {seconds} seconds ({format_duration(seconds)})"


def save_to_file(output_path: str, seconds: int, durations: dict):
    with open(output_path, "w") as f:
        for filename, duration in durations.items():
            f.write(
                f"{filename}: {duration} seconds ({format_duration(duration)})\n"
            )
        f.write(message(seconds))
