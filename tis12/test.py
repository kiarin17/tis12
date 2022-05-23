from selenium import webdriver
from selenium.webdriver.common.by import By


# Получаем в переменную browser указатель на браузер
browser=webdriver.Chrome()


# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://ok.ru/')


# заполняем поле логин, привязываемся к элементу через его имя
login=browser.find_element(by=By.ID, value='login')
login.send_keys('8800553535')


# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.ID, value='password')
password.send_keys('172003')


#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
button=browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
#Нажимаем на кнопку входа
button.click()

