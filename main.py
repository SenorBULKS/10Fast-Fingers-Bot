import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def code(browser):
    browser.get('https://10fastfingers.com/typing-test/english')
    form = browser.find_element_by_class_name('form-control')
    time.sleep(3)
    while True:
        words = browser.find_element_by_class_name('highlight').text
        form.send_keys(words)
        form.send_keys(Keys.SPACE)
    


def main():
    browser = webdriver.Chrome(r"location of driver.exe [C:\Users\user\something\something\chromedriver.exe]")
    code(browser)
main()
