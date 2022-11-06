#pip install selenium : 셀레니움 설치 
#pip install webdriver-manager : 웹 드라이버에 사용하는 크롬 드라이버 파일 다운로드

#https://opentutorials.org/course/4769
#https://opentutorials.org/course/4779
#https://www.edwith.org/search/show?searchQuery=python&MAX=20#course

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.by import By
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get(url='https://opentutorials.org/course/4769')
driver.get(url='https://opentutorials.org/course/4779') 
driver.get(url='https://www.edwith.org/search/show?searchQuery=python&MAX=20#course')

driver.implicitly_wait(time_to_wait=10)

