import os
import subprocess
import sys
import argparse
# Download a list of files from a text file
# Usage: download_files.py <file_list.txt>
# Args
#   file_list.txt: A text file containing a list of files to download


def main():
    args = argparse.ArgumentParser()
    args.add_argument("--file", type=str, help="File list to download")
    args = args.parse_args()


    # Check if the file list exists
    if not os.path.isfile(args.file):
        print("File list does not exist")
        sys.exit(1)

    # Download the files to dataset/images and un-tgz them
    with open(args.file) as file_list:
        for line in file_list:
            subprocess.run(["wget", line.strip(), "-P", "dataset/images"])
            subprocess.run(["tar", "-xzf", "dataset/images/{}".format(line.strip().split('/')[-1]), "-C", "dataset/images"])

    # End of script

if __name__ == "__main__":
    main()