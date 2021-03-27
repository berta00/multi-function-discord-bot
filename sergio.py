import os
import time
import selenium
import discord
import simple_colors
from bot import *
from sys import platform
from sergio import *
from selenium import webdriver
from discord.ext import commands


#sistem operativo qualiò

global drivers

if platform == "linux":
    locazioneDriver = os.getcwd() + "/geckodriver"
    drivers = webdriver.Firefox(executable_path=locazioneDriver)
elif platform == "windows":
    locazioneDriver = os.getcwd() + "/geckodriver.exe"
    drivers = webdriver.Firefox(executable_path=locazioneDriver)

os.system("clear")

def connessioneAlServer(drivers, username, password):
    #connessione
    drivers.get("https://aternos.org/go/")
    input1 = drivers.find_element_by_xpath('//*[@id="user"]')
    input2 = drivers.find_element_by_xpath('//*[@id="password"]')
    input3 = drivers.find_element_by_xpath('//*[@id="login"]')
    input1.send_keys(username)
    input2.send_keys(password)
    input3.click()
    time.sleep(1)
    #controllo credenziali
    if drivers.title == "Servers | Aternos | Free Minecraft Server" or drivers.title == "Server | Aternos | Server Minecraft gratis":
        print()
        print(simple_colors.green("loggato correttamente"))
    elif drivers.title == "Login or Sign up | Aternos | Free Minecraft Server" or drivers.title == "Accedi o registrati | Aternos | Server Minecraft gratis":
        os.system("clear")
        print(simple_colors.red("hai sbagliato credenziali, rimettile:"))
        print()
        serverOn(ctx)
        esciDaAternos()
    else:
        print()
        print("qualcosa è andato storto!")
        esciDaAternos()
    #entra nel server
    input4 = drivers.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div')
    input4.click()
    time.sleep(4)
    cookieBottone = drivers.find_element_by_xpath('//*[@id="accept-choices"]')
    cookieBottone.click()
    time.sleep(1)

def riavviaSeInattivo():
    time.sleep(100)
    bottoneRiavvio = drivers.find_element_by_xpath('//*[@id="restart"]')
    popolato = False
    if popolato == False:
        print("attenzione, non c'è nessuno nel server da 5 minuti, lo devo riavviare")
        bottoneRiavvio.click()

def accendiIlServer():
    #avvia
    bottoneAvvio = drivers.find_element_by_xpath('//*[@id="start"]')
    bottoneAvvio.click()
    time.sleep(4)
    confermaNotifiche = drivers.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[1]')
    confermaNotifiche.click()
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
        online = drivers.find_element_by_xpath('//*[@id="stop"]').is_displayed()
    print("il sevrer è online")
    riavviaSeInattivo()


def esciDaAternos():
    drivers.quit()