#압축할 샘플 파일(sample.txt) 생성 및 압축(암호 설정)

import itertools
# itertools : 반복문 사용의 편의 제공 모듈
# https://docs.python.org/ko/3.7/library/itertools.html


passwd_string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 교재 내 코드에 숫자 '6'이 빠져있어, 작성 시 체크 필요

for len in range(1,4): 
    #1~3까지 반복, 이중 for문

    to_attempt =itertools.product(passwd_string, repeat=len)
    # passwd_string 문자열을 길이(len)로 정렬하여 반환

    for attempt in to_attempt:
    #정렬해 반환된 문자의 수만큼 반복 : 복습 필요

        passwd=''.join(attempt)
        # 리스트로 반환된 값을 문자열로 변환 : 복습 필요
        # .join(리스트) : 리스트의 값을 문자열로 변환

        print(passwd)

