# Folder Synchronization

## Steps to run
1. git clone https://github.com/ravi105362/Project.git
2. cd Project 
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python src/main.py -s < fullSourceFolderPath > -o < fullOutputFolderPath > -i < syncInterval > -l < logsFilePath >
 
 EG:- python src/main.py -s /Users/nirjharijankar/ravi/projects/test-folder/Project/sourceFolder -o /Users/nirjharijankar/ravi/projects/test-folder/Project/outputFolder -i 5 -l /Users/nirjharijankar/ravi/projects/test-folder/logs
 
## Features

1. Checks for changes in the source folder at specified interval
2. Copies/Deletes the files/folders to make output folder replica of source folder
