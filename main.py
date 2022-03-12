"""
UniqueFiles will detect files from two directories, if any file is unique in any of the directories;
Move the unique files to a new directory.
"""

# Importing the required modules
import os
import shutil
import sys

# Define the directories
directories = ['dir1', 'dir2', 'dir6']
output = 'unique_files'

# Create the directory if it does not exist
if not os.path.exists(output):
    os.mkdir(output)

# Loop through the directories
count = len(directories)

for directory in directories:
    # Loop through the files in the directory
    for file in os.listdir(directory):
        # Loop through count
        for i in range(count):
            # Check if the file is unique in the directory
            if file not in os.listdir(directories[i]):
                # Move file to the output directory
                try:
                    shutil.move(directory + '/' + file, output)
                    print(f"{file} moved to {output} from {directory}")
                except shutil.Error:
                    print(f"{file} already exists in {output}")
                break
            else:
                print(f"{file} is not unique in {directory}")

# Exit the script
sys.exit()
