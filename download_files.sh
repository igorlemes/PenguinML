# Download a list of files from a text file
# Usage: download_files.sh <file_list.txt>

# Check if the file list exists
if [ ! -f $1 ]; then
    echo "File list does not exist"
    exit 1
fi

# Download the files
while read line; do
    wget $line
done < $1

# End of script