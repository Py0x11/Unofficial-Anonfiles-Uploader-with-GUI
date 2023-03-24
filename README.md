# Unofficial Anonfiles Uploader with GUI in Python
<p align="center">
  <a href="https://anonfiles.com/">
    <img src="https://i.ibb.co/kJY81TL/Anon-Files.png" alt="logo" width="190" border="0">
  </a>
</p>
<br> 
This code is a simple Unofficial Anonfiles uploader with Graphical User Interface (GUI) built using PyQt5 library in Python. It allows users to select a file from their local storage, upload it to Anonfiles.com, and display the generated download URL.

### Built With

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Features
- GUI interface for ease of use.
- Allows selection of any file from local storage to upload.
- Upto 20 GB filesize limit and unlimited bandwidth
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
2. Install PyQt5 and requests modules using pip. `python -m pip install -r requirements.txt`
3. Run the script. `python Main.py`
4. You should see the application window.

## Usage
1. Click the "Browse" button to select the file you want to upload.
2. Once the file is selected, its file path will be displayed in the "Upload Path" text box and the file size will be displayed in the "File Size" Section.
3. Click the "Upload" button to start the upload process.
4. The upload progress will be displayed on the progress bar.
5. Once the upload is complete, the generated download URL will be displayed in the "Upload URL" text box.
6. The uploaded file details, including the URL, will be saved to the "Uploads.txt" file.

## For People Who Just Want to Try the Uploader


## Disclaimer
This is an unofficial uploader and is not affiliated with Anonfiles.com in any way. Use at your own risk.
