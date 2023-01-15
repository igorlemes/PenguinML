# Move all images in the dataset/images/"Some camera"/image.JPG to dataset/image.JPG

import os
import subprocess
import sys

# Move all images in the dataset/images/"Some camera"/image.JPG to dataset/image.JPG
# Usage: mv_files.py

def main():
    # Check if the dataset/images folder exists
    if not os.path.isdir("dataset/images"):
        print("Dataset folder does not exist")
        sys.exit(1)
    
    # Move all images from dataset/images/line.strip().split('/')[-1] folders inside the dataset folder
    subprocess.run(["mv", "dataset/images/*/*.JPG", "dataset/"])

    # End of script

if __name__ == "__main__":
    main()