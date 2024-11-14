import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции/оставить браузер открытым
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере/развернуть на весь экран
driver_chrome.get(base_url)
driver_chrome.maximize_window()

# пауза 1 секунда
time.sleep(1)

# найти поле для логина и установить значение
user_name = driver_chrome.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
print("Ввод логина.")

# пауза 1 секунда
time.sleep(1)

# найти поле для пароля и установить значение
password = driver_chrome.find_element(By.ID, "password")
password.send_keys("secret_sauce")
print("Ввод пароля.")

# пауза 1 секунда
time.sleep(1)

# нажать на кнопку авторизации
driver_chrome.find_element(By.ID, "login-button").click()
print("Нажатие на кнопку Login.")

# пауза 1 секунда
time.sleep(1)

# нажать на кнопку скрытого меню
driver_chrome.find_element(
    By.XPATH, "//div[@class='bm-burger-button']"
).click()
print("Нажатие на кнопку скрытого меню.")

# пауза 1 секунда
time.sleep(1)

# нажать на кнопку Logout
driver_chrome.find_element(
    By.XPATH, "//a[@id='logout_sidebar_link']"
).click()
print("Нажатие на кнопку Logout.")

# проверка совпадения ожидаемого и полученного URL
url = "https://www.saucedemo.com/"
get_url = driver_chrome.current_url
assert url == get_url, "Ошибка: URL должны совпадать!"
print("URL корректен.")

# пауза 2,5 секунды
time.sleep(2.5)

# закрыть окно браузера
driver_chrome.close()
print("Закрытие окна.")