# Folder Synchronization

## Steps to run

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python src/main.py -s < sourceFolderPath > -o < outputFolderPath > -i < SyncInterval > -l < logsFilePath >

## Features

1. Checks for changes in the source folder at specified interval
2. Copies/Deletes the files/folders to make output folder replica of source folder
