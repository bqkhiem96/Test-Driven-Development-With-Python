from selenium import webdriver
chromedriver = r'''C:\Users\quockhiem\Documents\IT\Python\TDD\drivers\chromedriver'''
browser = webdriver.Chrome(chromedriver)

browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title

