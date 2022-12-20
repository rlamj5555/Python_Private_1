import sys # 파이썬 인터프리터 제어 모듈
import os # OS 제어 모듈
#import win32com.shell.shell as shell
from PyQt5.QtWidgets import *
from PyQt5 import uic



form_class = uic.loadUiType("C:\\Private_Python_github\\study_py40\\pyqt_02\\wus.ui")[0]


#화면 출력 클래스 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 8


        #버튼-기능 연결
        self.btn_1.clicked.connect(self.button1Function) # edit_1에서 입력된 버전의 Windows Update 삭제 버튼
        self.btn_2.clicked.connect(self.button2Function) # wuauserv 서비스 중지 버튼
        self.btn_3.clicked.connect(self.button3Function) # wuauserv 서비스 시작 버튼
        self.btn_4.clicked.connect(self.button4Function) # edit_2에서 입력된 서비스 중지 버튼
        self.btn_5.clicked.connect(self.button5Function) # edit_2에서 입력된 서비스 시작 버튼



    

    #btn_1 - edit_1 함수
    def button1Function(self) :
        print("패치 파일을 삭제합니다.") 
        a=("%r")%self.edit_1.toPlainText()
        b=a.replace('\'','')
        c= "wusa /uninstall /KB:"
        d=" /norestart"
        
        result_0=os.system(c+b+d)
        # wusa /uninstall /KB:4023057 /norestart : KB4023057

        print(result_0)
        if result_0==0:
            buttonReply = QMessageBox.result(self,'삭제 완료', '패치 파일을 성공적으로 삭제했습니다.')
            if buttonReply==QMessageBox.Ok:
               print('Ok clicked.')
            self.close()
        else:
            buttonReply=QMessageBox.warning(self,'삭제 실패', '패치 파일을 삭제하지 못했습니다.')    
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')



#1214 추가    
    
    
    #btn_2 함수
    def button2Function(self) :
        print("wuauserv 서비스가 중지됩니다.")
       # os.system("net stop wuauserv")
        #result_2=os.system('')
        result_2=os.system("net stop wuauserv")
        print(result_2)
        if result_2==2:
            buttonReply=QMessageBox.warning(self,'동작 실패', '서비스가 실행 중이 아닙니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')
            #self.close()
        elif result_2==0:
            buttonReply=QMessageBox.warning(self,'동작 성공', '서비스를 성공적으로 중지했습니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')
        else:
            buttonReply=QMessageBox.warning(self,'오류', '오류가 발생했습니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')



    #btn_3 함수
    def button3Function(self) :
        print("wuauserv 서비스가 시작됩니다.")
       # os.system("net start wuauserv")
        result_3=os.system("net start wuauserv")
        print(result_3)
        if result_3==0:
            buttonReply = QMessageBox.warning(self,'동작 성공', '서비스를 성공적으로 시작했습니다.')
            if buttonReply==QMessageBox.Ok:
               print('Ok clicked.')

        elif result_3==2:
            buttonReply=QMessageBox.warning(self,'동작 실패', '서비스가 이미 실행 중입니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')

        else:
            buttonReply=QMessageBox.warning(self,'오류', '오류가 발생했습니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')




    #btn_4 - edit_2 함수
    def button4Function(self) :
        print("서비스가 중지됩니다.")
        a=("%r")%self.edit_2.toPlainText()
        b=a.replace('\'','')
        c= "net stop "
        result_4=os.system(c+b)

        
        print(result_4)
        if result_4==0:
            buttonReply = QMessageBox.warning(self,'동작 성공', '서비스를 성공적으로 중지했습니다.')
            if buttonReply==QMessageBox.Ok:
               print('Ok clicked.')

        elif result_4==2:
            buttonReply=QMessageBox.warning(self,'동작 실패', '서비스가 실행 중이 아닙니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')

        else:
            buttonReply=QMessageBox.warning(self,'오류', '오류가 발생했습니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')
    

    #btn_5 - edit_2 함수
    def button5Function(self) :
        print("서비스가 시작됩니다.")
        a=("%r")%self.edit_2.toPlainText()
        b=a.replace('\'','')
        c= "net start "
        result_5=os.system(c+b)

        print(result_5)
        if result_5==0:
            buttonReply = QMessageBox.warning(self,'동작 성공', '서비스를 성공적으로 시작했습니다.')
            if buttonReply==QMessageBox.Ok:
               print('Ok clicked.')

        elif result_5==2:
            buttonReply=QMessageBox.warning(self,'동작 실패', '서비스가 이미 실행 중입니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')

        else:
            buttonReply=QMessageBox.warning(self,'오류', '오류가 발생했습니다.')
            if buttonReply==QMessageBox.Ok:
                print('Ok clicked.')
    

    


if __name__ == "__main__" :
    app = QApplication(sys.argv) # 명령의 인자값을 전달 받음
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
