# tlenv

Get total length of videos in a folder.

## Prerequisite

- `Python3`
- `ffprobe`, `opencv`, `moviepy` (optional, just pick one)

## Example

```
video1.mp4: 251.876625 seconds (0h 4m 11s)
video2.mp4: 253.544958 seconds (0h 4m 13s)
video3.mp4: 95.84575 seconds (0h 1m 35s)
video4.mp4: 96.721625 seconds (0h 1m 36s)
video5.mp4: 140.89075 seconds (0h 2m 20s)
video6.mp4: 116.035 seconds (0h 1m 56s)
video7.mp4: 69.235833 seconds (0h 1m 9s)
video8.mp4: 225.308417 seconds (0h 3m 45s)
video9.mp4: 229.812917 seconds (0h 3m 49s)
video10.mp4: 291.7915 seconds (0h 4m 51s)

Total duration of all videos: 1771.063375 seconds (0h 29m 31s)
```

## Usages

To show the total length of videos in a folder:

```
python3 tlenv.py --folder <folder_path>
```

To output the total length of videos in a folder to a file:

```
python3 tlenv.py --folder <folder_path> --output <output_file_path>
```
