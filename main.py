import os
os.system("pip install selenium")
os.system("pip install simple_colors")

import selenium
import simple_colors
from selenium import webdriver

a = ""      # appena aggiungi la parte di login
b = ""      # nella interfaccia poi toglierle

# selenium

driver = webdriver.Firefox(executable_path="/home/alienozzo/Scrivania/Coding/broswer_driver/geckodriver")
os.system("clear")

def connessioneAlServer(driver, username, password):
    driver.get("https://aternos.org/go/")
    input1 = driver.find_element_by_xpath('//*[@id="user"]')
    input2 = driver.find_element_by_xpath('//*[@id="password"]')
    input1.send_keys(username)
    input2.send_keys(password)

def esciDaAternos():
    driver.quit()



# interfaccia  (va sotto perchè sopra ci sono tutte le funzioni che senno non legge)


nomeServer = input("inserisci lo username: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia

connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia

esciDaAternos()                                           # implementala nella interfacciaì
a