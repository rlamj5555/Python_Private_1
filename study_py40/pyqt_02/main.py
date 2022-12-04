import sys # 파이썬 인터프리터 제어 모듈
import os # OS 제어 모듈
from PyQt5.QtWidgets import *
from PyQt5 import uic


form_class = uic.loadUiType("C:\\Private_Python_github\\study_py40\\pyqt_02\\wus.ui")[0]
# 역슬래쉬 앞에 역슬래쉬 추가 필요 : 진주님 감사해용 :)

#화면 출력 클래스 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 9


        #버튼-기능 연결
        self.btn_1.clicked.connect(self.button1Function) # edit_1에서 입력된 버전의 Windows Update 삭제 버튼
        self.btn_2.clicked.connect(self.button2Function) # wuauserv 서비스 중지 버튼
        self.btn_3.clicked.connect(self.button3Function) # wuauserv 서비스 시작 버튼
        self.btn_4.clicked.connect(self.button4Function) # edit_2에서 입력된 서비스 중지 버튼
        self.btn_5.clicked.connect(self.button5Function) # edit_2에서 입력된 서비스 시작 버튼



    #btn_1 - edit_1 함수
    def button1Function(self) :
        print("패치 파일 번호 %r이 삭제됩니다." %self.edit_1.toPlainText()) 
        os.system("wusa \/uninstall\/KB:%r\/norestart" %self.edit_1.toPlainText())
        # wusa /uninstall /KB:4023057 /norestart : KB4023057
    
    #btn_2 함수
    def button2Function(self) :
        print("wuauserv 서비스가 중지됩니다.")
        os.system("net stop wuauserv")

    #btn_3 함수
    def button3Function(self) :
        print("wuauserv 서비스가 시작됩니다.")
        os.system("net start wuauserv")

    #btn_4 - edit_2 함수
    def button4Function(self) :
        print("%r가 중지됩니다." %self.edit_2.toPlainText()) 
        os.system("net stop %r" %self.edit_2.toPlainText())

    #btn_5 - edit_2 함수
    def button5Function(self) :
        print("%r가 시작됩니다." %self.edit_2.toPlainText()) 
       # os.system("net user administrator \/active:yes") 
        os.system("net start %r" %self.edit_2.toPlainText())
    


if __name__ == "__main__" :
    app = QApplication(sys.argv) # 명령의 인자값을 전달 받음
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()



# 메모

# 관리자 권한 코드 추가 예정 
# >> os.system("net user administrator \/active:yes")


# UI 고도화 : 폰트 스타일 및 사이즈 조정
# >> 버튼 선택 시, 안내창 노출 

# 예외처리 : 잘못된 버전 및 서비스명 입력 시
# >> 안내창 노출
# >> 실행 x