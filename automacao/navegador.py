import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

COOKIE_FILE = "cookies.pkl"

def abrir_navegador():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://shopee.com.br")

    if os.path.exists(COOKIE_FILE):
        with open(COOKIE_FILE, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                except:
                    pass
        driver.get("https://shopee.com.br")  # Recarrega com cookies aplicados

    return driver

def salvar_cookies(driver):
    with open(COOKIE_FILE, "wb") as file:
        pickle.dump(driver.get_cookies(), file)
