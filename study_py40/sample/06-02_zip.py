import itertools
# itertools : 반복문 제공의 편의 제공 모듈
# https://docs.python.org/ko/3.7/library/itertools.html

import zipfile
# zipfile : 압축파일 관련 모듈
# https://docs.python.org/ko/3.7/library/zipfile.html


passwd_string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile=zipfile.ZipFile('C:\Private_Python_github\study_py40\sample\sample.zip')
# 교재 내 'r' : raw data 뜻함, 그러나 'r' 입력 시 출력이 되지 않아 해당 부분 확인 필요

# OSError: [Errno 22] Invalid argument: 'C:\\Private_Python_github\\study_py40\x06-01\\sample.zip'
# >> 원인 : 경로 내, 특수문자 삽입 시 해당 오류 발생
# >> 해결 : 경로 내, 특수문자 삭제 및 경로 수정


for len in range(1,6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd=''.join(attempt)
        print(passwd)
        try:
            zFile.extractall(pwd=passwd.encode())
            print("비밀번호는 {passwd} 입니다.")
            # 교재 내 'f' 삭제 필요 : 'f' 문자열 의미(질문)
            # 3.6부터 f string 표현 방법 생김
            # https://github.com/OhJiMin/minjiminju/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EA%B3%BC%2040%EA%B0%9C%EC%9D%98%20%EC%9E%91%ED%92%88%EB%93%A4/5.%20%EC%BB%B4%ED%93%A8%ED%84%B0%EC%9D%98%20%EC%A0%95%EB%B3%B4%20%ED%99%95%EC%9D%B8/main5-1%2C2%2C3.py
            # print(f"CPU 속도 : {cpu_current_ghz}GHz") 
            # # python3.6 이상부터 f-string 표현 방법
            # print("CPU 속도 :",cpu_current_ghz,"GHz")
            
            break
        except:
            pass

# ctrl+c : 터미널 종료 / 한 번으로 종료 안될 시, 반복해서 키 입력