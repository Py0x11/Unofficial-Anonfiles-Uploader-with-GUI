from PyQt5.QtWidgets import QMainWindow , QApplication , QLabel, QPushButton, QTextEdit , QProgressBar
from PyQt5 import uic , QtCore , QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import os
from time import sleep
import requests
class app(QMainWindow):
    def __init__(self):
        super(app,self).__init__()
        uic.loadUi("Main.ui", self)
        qpixmap = QPixmap('logo.png')
        
        self.Logo_lab.setPixmap(qpixmap)
        self.Upload_btn = self.findChild(QPushButton,"Upload_btn")
        self.Browse = self.findChild(QPushButton,"Browse_btn")
        self.up_path = self.findChild(QTextEdit,"Upload_path_txt")
        self.up_url = self.findChild(QTextEdit,"Upload_URL")
        self.Upload_progress = self.findChild(QProgressBar,"Upload_progress")
        self.File_Size = self.findChild(QLabel,"File_Size")

        self.Upload_progress.hide()
        self.Browse.clicked.connect(self.getfiles)
        self.Upload_btn.clicked.connect(self.Upload)
        self.show()
        
    def update_progress(self,progressbar, progress=0):
        self.Upload_progress.show()
        self.Upload_progress.setValue(progress)
        progressbar.setValue(progress)
        QApplication.processEvents()

    def getfiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.*')
        self.up_path.setText(fileName,)
        self.File = fileName
        self.size = os.path.getsize(self.File)
        if self.size <= 1000:
            self.File_Size.setText(f"{self.size*1000} KB")   
        elif self.size >= 1000000:
            self.File_Size.setText(f"{self.size/1000000} KB")     


    def Upload(self):
        self.update_progress(self.Upload_progress,progress=10)
        files = {
            'file': (self.File, open(self.File, 'rb')),
            }
        url = 'https://api.anonfiles.com/upload'
        self.update_progress(self.Upload_progress,progress=40)
        response = requests.post(url, files=files)
        self.update_progress(self.Upload_progress,progress=60)
        data = response.json()
        self.update_progress(self.Upload_progress,progress=80)
        self.fileurl = data['data']['file']['url']['full']
        self.up_url.setText(self.fileurl)
        self.update_progress(self.Upload_progress,progress=100)
        sleep(4)
        self.Upload_progress.hide()
        self.dat = open("Uploads.txt","a")
        self.dat.write(f"\n{'------------------------'*2}\nFile : {self.File} \nSize : {self.size} Bytes\nURL : {self.fileurl}\n{'------------------------'*2}\n")
        self.dat.close()

main = QApplication(sys.argv)
UIWindow = app()
main.exec_()
        