# tlenv

get total length of videos in a folder.

## Prerequisite

- `Python3`
- `ffprobe`

## Example

```
3-小專案.mp4: 251.876625 seconds (0h 4m 11s)
7-任務三.mp4: 253.544958 seconds (0h 4m 13s)
4-創作坊.mp4: 95.84575 seconds (0h 1m 35s)
2-展示遊戲.mp4: 96.721625 seconds (0h 1m 36s)
9-小挑戰.mp4: 140.89075 seconds (0h 2m 20s)
10-回家挑戰與回顧.mp4: 116.035 seconds (0h 1m 56s)
1-開場白.mp4: 69.235833 seconds (0h 1m 9s)
5-任務一.mp4: 225.308417 seconds (0h 3m 45s)
6-任務二.mp4: 229.812917 seconds (0h 3m 49s)
8-任務四.mp4: 291.7915 seconds (0h 4m 51s)

Total duration of all videos: 1771.063375 seconds (0h 29m 31s)
```

## Usages

to show the total length of videos in a folder:

```
python3 tlenv.py --folder <folder>
```

to output the total length of videos in a folder to a file:

```
python3 tlenv.py --folder <folder> --output <output_file_path>
```
