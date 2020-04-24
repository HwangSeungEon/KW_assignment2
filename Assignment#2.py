import qimage2ndarray
import numpy
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

basic_ui = uic.loadUiType("Assignment_widget.ui")[0]
class WindowClass(QMainWindow,basic_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda:self.Imageshow())
        self.pushButton_2.clicked.connect(lambda:self.Imageflip())

    def  Imageshow(self):
        fileName,_= QFileDialog.getOpenFileName(self,"Open File",",")
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self,"Image Viewer","Cannot load %s",fileName)
                return
            qPixmapVar = QPixmap.fromImage(image)
            qPixmapVar = qPixmapVar.scaled(261,261)
            self.label.setPixmap(qPixmapVar)
            self.show()
            
    def Imageflip(self):
        
        self.image = QImage(self.label.pixmap())

        if self.image.isNull():
                QMessageBox.information(self,"Warning!","Please load image first")
                return

        image_array = qimage2ndarray.rgb_view(self.image)
        image_array = numpy.flip(image_array,0)
        self.image = qimage2ndarray.array2qimage(image_array,normalize=False)

        qPixmapVar = QPixmap.fromImage(self.image)
        qPixmapVar = qPixmapVar.scaled(261,261)
        self.label.setPixmap(qPixmapVar)
        self.show()
            
if __name__=="__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
