import argparse
import tlenv

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--method", type=str)
parser.add_argument("-f", "--folder", type=str)
parser.add_argument("-o", "--output", type=str, default=None)
args = parser.parse_args()

METHOD = args.method
if METHOD == "ffprobe":
    tlenv.ffprobe
    pass
elif METHOD == "mvpy":
    pass
else:
    pass
