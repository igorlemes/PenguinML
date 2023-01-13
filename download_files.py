import os
import subprocess
import sys

# Download a list of files from a text file
# Usage: download_files.py <file_list.txt>

# Check if the file list exists
if not os.path.isfile(sys.argv[2]):
    print("File list does not exist")
    sys.exit(1)

# Download the files to dataset/images and unzip them
with open(sys.argv[2]) as file_list:
    for line in file_list:
        subprocess.run(["wget", line.strip(), "-P", "dataset/images"])
        subprocess.run(["unzip", "-q", "dataset/images/*.zip", "-d", "dataset/images"])

# End of script
