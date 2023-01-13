# Download a list of files from a text file
# Usage: download_files.sh <file_list.txt>

# Check if the file list exists
if [ ! -f $1 ]; then
    echo "File list does not exist"
    exit 1
fi

# Download the files to dataset/images and unzip them
while read line; do
    wget $line -P dataset/images && unzip dataset/images/*.zip -d dataset/images
done < $1

# End of script