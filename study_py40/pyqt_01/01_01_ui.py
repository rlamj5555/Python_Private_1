import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("C:\\Private_Python_github\\study_py40\\pyqt_01\\pyqtui.ui")[0] # ui 파일 경로

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        self.btn_3.appendText.clicked.connect(self.appendText1Function)
        self.btn_4.appendText.clicked.connect(self.appendText2Function)

 
    def button1Function(self) :
        print("btn_1 Clicked")


    def button2Function(self) :
        print("btn_2 Clicked")

    def appendText1Function(self) :
        print(self.textbrow_Test.toPlainText())

    def appendText2Function(self) :
        print(self.textbrow_Test.toPlainText())


if __name__ == "__main__" :
  
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()