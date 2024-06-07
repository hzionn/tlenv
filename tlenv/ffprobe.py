import os
import platform
import subprocess


def get_video_duration(filename: str) -> float:
    ffprobe = "ffprobe.exe" if platform.system() == "Windows" else "ffprobe"
    ffprobe_path = os.path.join(os.getcwd(), ffprobe)
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
