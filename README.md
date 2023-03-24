# Unofficial Anonfiles Uploader with GUI in Python

This code is a simple Unofficial Anonfiles uploader with Graphical User Interface (GUI) built using PyQt5 library in Python. It allows users to select a file from their local storage, upload it to Anonfiles.com, and display the generated download URL.

## Features
- GUI interface for ease of use.
- Allows selection of any file from local storage to upload.
- Displays the file size in KB or MB.
- Displays upload progress with a progress bar.
- Displays the generated download URL.
- Saves the uploaded file's details, including URL, to a text file.

## Requirements
- Python 3.x installed on your computer.
- PyQt5 module.
- requests module.

## Installation
1. Clone or download the repository.
2. Install PyQt5 and requests modules using pip. `pip install PyQt5 requests`
3. Run the script. `python uploader.py`
4. You should see the application window.

## Usage
1. Click the "Browse" button to select the file you want to upload.
2. Once the file is selected, its file path will be displayed in the "Upload Path" text box and the file size will be displayed in the "File Size" label.
3. Click the "Upload" button to start the upload process.
4. The upload progress will be displayed on the progress bar.
5. Once the upload is complete, the generated download URL will be displayed in the "Upload URL" text box.
6. The uploaded file details, including the URL, will be saved to the "Uploads.txt" file.

## Disclaimer
This is an unofficial uploader and is not affiliated with Anonfiles.com in any way. Use at your own risk.
