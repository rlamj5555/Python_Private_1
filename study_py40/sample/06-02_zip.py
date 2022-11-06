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
            
            break
        except:
            pass

# ctrl+c : 터미널 종료 / 한 번으로 종료 안될 시, 반복해서 키 입력