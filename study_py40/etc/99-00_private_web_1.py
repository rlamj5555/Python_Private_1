from lib2to3.pgen2 import driver

titles=driver.find_elements(By.css_selector, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a> font')
urls=driver.find_elements(By.css_selector, '#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > a')

for i in range(len(titles)):
    print(titles[i].text)
    print(urls[i].get_attribute('href'))