import time
import os
os.system("pip install selenium")
os.system("pip install simple_colors")

import selenium                                                                                                                    # CREDENZIALI TEST:
import simple_colors                                                                                                               # username: ServerAbete
from selenium import webdriver                                                                                                     # password: abeteswag17

a = ""      # appena aggiungi la parte di login
b = ""      # nella interfaccia poi toglierle

# selenium

locazioneDriver = os.getcwd() + "/geckodriver"
driver = webdriver.Firefox(executable_path=str(locazioneDriver))
os.system("clear")

def connessioneAlServer(driver, username, password):
    driver.get("https://aternos.org/go/")
    input1 = driver.find_element_by_xpath('//*[@id="user"]')
    input2 = driver.find_element_by_xpath('//*[@id="password"]')
    input3 = driver.find_element_by_xpath('//*[@id="login"]')
    input1.send_keys(username)
    input2.send_keys(password)
    input3.click()
    if driver.title == "Servers | Aternos | Free Minecraft Server":
        print("loggato correttamente")
    elif driver.title == "Login or Sign up | Aternos | Free Minecraft Server":
        nomeServer = input("inserisci lo username: ")
        passwordServer = input("inserisci la password: ")
        connessioneAlServer(driver, nomeServer, passwordServer)
    else:
        print()
        print("qualcosa è andato storto!")
        esciDaAternos()
    input4 = find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]')

def esciDaAternos():
    driver.quit()



# interfaccia  (va sotto perchè sopra ci sono tutte le funzioni che senno non legge)

nomeServer = input("inserisci lo username: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia

connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia

# esciDaAternos()                                         # implementala nella interfaccia