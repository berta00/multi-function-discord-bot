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
    #connessione
    driver.get("https://aternos.org/go/")
    input1 = driver.find_element_by_xpath('//*[@id="user"]')
    input2 = driver.find_element_by_xpath('//*[@id="password"]')
    input3 = driver.find_element_by_xpath('//*[@id="login"]')
    input1.send_keys(username)
    input2.send_keys(password)
    input3.click()
    time.sleep(1)
    #controllo credenziali
    if driver.title == "Servers | Aternos | Free Minecraft Server":
        print()
        print(simple_colors.green("loggato correttamente"))
    elif driver.title == "Login or Sign up | Aternos | Free Minecraft Server":
        os.system("clear")
        print(simple_colors.red("hai sbagliato credenziali, rimettile:"))
        print()
        nomeServer = input("inserisci lo username: ")
        passwordServer = input("inserisci la password: ")
        connessioneAlServer(driver, nomeServer, passwordServer)

        esciDaAternos()
    else:
        print()
        print("qualcosa è andato storto!")
        esciDaAternos()
    #entra nel server
    input4 = driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div')
    input4.click()
    time.sleep(1.5)
    cookieBottone = driver.find_element_by_xpath('//*[@id="accept-choices"]')
    cookieBottone.click()
    time.sleep(1)

def accendiIlServer():
    #avvia
    bottoneAvvio = driver.find_element_by_xpath('//*[@id="start"]')
    bottoneAvvio.click()
    time.sleep(1)
    confermaNotifiche = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[1]')
    confermaNotifiche.click()
    #controlla se serve confermare
    divConfermaMostrato = False
    while divConfermaMostrato == False:
        divConfermaMostrato = driver.find_element_by_xpath('//*[@id="confirm"]').is_displayed()
    driver.find_element_by_xpath('//*[@id="confirm"]').click()
    print()
    print("Confermato")


def esciDaAternos():
    driver.quit()



# interfaccia  (va sotto perchè sopra ci sono tutte le funzioni che senno non legge)

nomeServer = input("inserisci lo username: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia

connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia
accendiIlServer()                                         # implementala nella interfaccia

# esciDaAternos()                                         # implementala nella interfaccia