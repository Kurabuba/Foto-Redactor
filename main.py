from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QTextEdit, QListWidget, QLineEdit, QInputDialog, QFileDialog)
from PIL import Image
from PIL import ImageFilter
import os
from PyQt5.QtGui import QPixmap





app = QApplication([])
main_win = QWidget()
main_win.resize(500, 300)
main_win.setWindowTitle("Easy Editor")

list1 = QListWidget()
pap_button = QPushButton('Папка')
turn_left = QPushButton('Лево')
turn_right = QPushButton('Право')
mirrow = QPushButton('Зеркало')
sharpness = QPushButton('Резкость')
grey = QPushButton('Ч/Б')
label = QLabel('Картина')

ans_layout = QHBoxLayout()
ans_layout1 = QVBoxLayout()
ans_layout2 = QVBoxLayout()

ans_layout1.addWidget(pap_button)
ans_layout1.addWidget(list1)

ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)

button_layout = QHBoxLayout()
button_layout.addWidget(turn_left)
button_layout.addWidget(turn_right)
button_layout.addWidget(mirrow)
button_layout.addWidget(sharpness)
button_layout.addWidget(grey)

ans_layout2.addWidget(label)
ans_layout2.addLayout(button_layout)

workdir = ''
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    res = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                res.append(filename)
    return res

def showFilenameList():
    chooseWorkdir()
    filenemes = os.listdir(workdir)
    extensions = ["png", "jpeg", 'jpg']
    result = filter(filenemes, extensions)
    list1.clear()
    list1.addItems(result)



class ImageProcessor():
    def __init__(self):
        self.image = None
        self.direc = None
        self.namefile = None
        self.save_dir = 'Save'

    def zagruz_image(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image.putz = os.path.join(dir, filename)
        self.image = Image.open(image.putz)

def showPaint():
    label.hide()
    image_putz = os.path.join(self.dir, self.filename)
    piximage = QPixmap(image_putz)
    w = label.width()
    h = label.height()
    piximage = piximage.scaled(w, h, Qt.KeepAspectRatio)
    label.setPixmap(piximage)
    label.show()

def saveImage():
    putz = os.path.join(self.save_dir, self.filename)
    if not (os.path.exists(path)) or os.path.isdir(path):
        os.mkdir(path)
    image_putz = os.path.join(path, self.filename)
    self.image.save(image_putz)

def do_black_white(self):
    self.image = self.image.convert('L')
    self.saveImage()

image1 = ImageProcessor()


pap_button.clicked.connect(showFilenameList)
list1.itemClicked.connect(showPaint)

main_win.setLayout(ans_layout)
main_win.show()
app.exec_()
