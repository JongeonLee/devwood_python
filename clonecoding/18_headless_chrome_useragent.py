from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36')
# user-agent를 따로 설정해두지 않았을 시 user-agent가 다르게 설정되어 접근이 차다될 수 있음
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

id = browser.find_element_by_id('detected_value')
print(id.text)
browser.quit()