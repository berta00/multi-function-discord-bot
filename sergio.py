import os
import time
import discord
import selenium
import simple_colors
from platform import system
from selenium import webdriver


#sistem operativo
sistemaOperativo = str(system())


# selenium

if sistemaOperativo == "Linux":
    locazioneDriver = os.getcwd() + "/geckodriver"
    driver = webdriver.Firefox(executable_path=locazioneDriver)
elif sistemaOperativo == "Windows":
    locazioneDriver = os.getcwd() + "/geckodriver.exe"
    driver = webdriver.Firefox(executable_path=locazioneDriver)

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
    if driver.title == "Servers | Aternos | Free Minecraft Server" or driver.title == "Server | Aternos | Server Minecraft gratis":
        print()
        print(simple_colors.green("loggato correttamente"))
    elif driver.title == "Login or Sign up | Aternos | Free Minecraft Server" or driver.title == "Accedi o registrati | Aternos | Server Minecraft gratis":
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
    time.sleep(4)
    cookieBottone = driver.find_element_by_xpath('//*[@id="accept-choices"]')
    cookieBottone.click()
    time.sleep(1)

def riavviaSeInattivo():
    time.sleep(100)
    bottoneRiavvio = driver.find_element_by_xpath('//*[@id="restart"]')
    popolato = False
    if popolato == False:
        print("attenzione, non c'è nessuno nel server da 5 minuti, lo devo riavviare")
        bottoneRiavvio.click()

def accendiIlServer():
    #avvia
    bottoneAvvio = driver.find_element_by_xpath('//*[@id="start"]')
    bottoneAvvio.click()
    time.sleep(4)
    confermaNotifiche = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[1]')
    confermaNotifiche.click()
    #controlla se serve confermare
    divConfermaMostrato = False
    while divConfermaMostrato == False:
        divConfermaMostrato = driver.find_element_by_xpath('//*[@id="confirm"]').is_displayed()
    driver.find_element_by_xpath('//*[@id="confirm"]').click()
    print()
    print("Confermato")
    print()
    #controlla se è online, se è online continua ad eseguire il codice sotto
    online = False
    while online == False:
        online = driver.find_element_by_xpath('//*[@id="stop"]').is_displayed()
    print("il sevrer è online")
    riavviaSeInattivo()


def esciDaAternos():
    driver.quit()




# discord
