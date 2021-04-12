import os
import time
import selenium
import discord
import simple_colors as colore
from bot import *
from sys import platform
from sergio import *
from selenium import webdriver
from discord.ext import commands

global drivers

if platform == "linux":
    locazioneDriver = os.getcwd() + "/programma/driver/geckodriver"
    drivers = webdriver.Firefox(executable_path=locazioneDriver)
    os.system("clear")
elif platform == "win32" or platform == "win64":
    locazioneDriver = os.getcwd() + "/programma/driver/geckodriver.exe"
    drivers = webdriver.Firefox(executable_path=locazioneDriver)

def connessioneAlServer(drivers, username, password):
    #connessione
    drivers.get("https://aternos.org/go/")
    input1 = drivers.find_element_by_xpath('//*[@id="user"]')
    input2 = drivers.find_element_by_xpath('//*[@id="password"]')
    input3 = drivers.find_element_by_xpath('//*[@id="login"]')
    input1.send_keys(username)
    input2.send_keys(password)
    input3.click()
    time.sleep(1.5)
    #controllo credenziali
    if drivers.title == "Servers | Aternos | Free Minecraft Server" or drivers.title == "Server | Aternos | Server Minecraft gratis":
        print()
        print(colore.green("loggato in aternos"))
    elif drivers.title == "Login or Sign up | Aternos | Free Minecraft Server" or drivers.title == "Accedi o registrati | Aternos | Server Minecraft gratis":
        # stampa password sbagliata
        pass
    #entra nel server
    input4 = drivers.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div')
    input4.click()
    time.sleep(4)
    cookieBottone = drivers.find_element_by_xpath('//*[@id="accept-choices"]')
    cookieBottone.click()
    time.sleep(1)
    accendiIlServer()

def riavviaSeInattivo():
    while vuoto == true:
        giocatori = driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[5]/div[2]/div[1]/div[1]/div[2]/div[2]').getText()
        time.sleep(20)
        bottoneRiavvio = drivers.find_element_by_xpath('//*[@id="restart"]')
        popolato = False
        if popolato == False:
            print("attenzione, non c'è nessuno nel server da 5 minuti, lo devo riavviare")
            bottoneRiavvio.click()
        if str(giocatori) != "0/20":
            vuoto = true
        else:
            vuoto = false

def accendiIlServer():
    #avvia
    bottoneAvvio = drivers.find_element_by_xpath('//*[@id="start"]')
    bottoneAvvio.click()
    time.sleep(4)
    try:
        confermaNotifiche = drivers.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[1]')
        confermaNotifiche.click()
    except:
        print(colore.red("quancosa è andato storto, riprova"))
    #controlla se serve confermare
    divConfermaMostrato = False
    while divConfermaMostrato == False:
        divConfermaMostrato = drivers.find_element_by_xpath('//*[@id="confirm"]').is_displayed()
    drivers.find_element_by_xpath('//*[@id="confirm"]').click()
    print()
    print("Confermato")
    print()
    #controlla se è online, se è online continua ad eseguire il codice sotto
    online = False
    while online == False:
        online = drivers.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[3]/div[1]/div/span[1]').is_displayed()
    print("il server è online")
    riavviaSeInattivo()


def esciDaAternos():
    drivers.quit()