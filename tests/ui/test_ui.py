import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome()

    #відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #знаходимо поле в яке будемо вводити неправильне імя користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #вводимо неправильне імя користувача або поштову адресу
    login_elem.send_keys("khorunzha.natalia@gmail.com")

    #знаходимо поле в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #водимо неправильний пароль
    pass_elem.send_keys("wrong password")

    #знаходимо кнопку sing in
    btn_elem = driver.find_element(By.NAME, "commit")

    #емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    assert driver.title == "Sign in GitHub - GitHub"

    time.sleep(3)

    #закриваємо браузер
    driver.close()
