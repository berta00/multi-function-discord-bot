import time
import os
import selenium
import discord
import simple_colors
from sys import platform
from selenium import webdriver

#fa la aplicazione di discord

global drivers

def installazioneABC():

    #controlla o installa le dipendenze
    os.system("pip install --upgrade pip")
    os.system("pip install discord")
    os.system("pip install selenium==4.0.0a1")
    os.system("pip install simple_colors==0.1.5")

    nomeBot = input("che nome vuoidare al bot? ")
    print()
    print("credenziali per discord developer portal:")
    inputUsername = input("metti il tuo username discord: ")
    inputPassword = input("metti la tua password discord: ")
    print()

    if platform == "linux":
        locazioneDriver = "../" + os.getcwd() + "/geckodriver"
        drivers = webdriver.Firefox(executable_path=locazioneDriver)
        os.system("clear")
    elif platform == "win32" or platform == "win64":
        locazioneDriver = os.getcwd() + "/geckodriver.exe"
        drivers = webdriver.Firefox(executable_path=locazioneDriver)

    driver.get("https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications")
    time.sleep(1000)


    #ultimo messaggio
    driver.close()
    print("""
    installazione finita!

    per avviare il tuo bot d'ora in poi ti basterà avviare il file .exe che si è creato nel desktop
    """)

installazioneABC()