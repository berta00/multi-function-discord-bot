import time
import os
import selenium
import discord
import simple_colors
from sys import platform
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

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
        locazioneDriver = os.getcwd() + "programma\\geckodriver"
        drivers = webdriver.Firefox(executable_path=locazioneDriver)
        os.system("clear")
    elif platform == "win32" or platform == "win64":
        locazioneInstallazione = os.getcwd()
        locazioneDriverS = locazioneInstallazione.split("\\")
        locazioneDriverS.remove("installazione")
        locazioneDriverS.append("programma")
        locazioneDriverS.append("geckodriver.exe")
        a = len(locazioneDriverS)
        a = a - 1
        i = 0
        driverL = ""
        c = ""
        while i < a:
            c = str(locazioneDriverS[i])
            driverL = driverL + c + "\\"
            i = i + 1
        driverL = driverL + "geckodriver.exe"
        driver = webdriver.Firefox(executable_path=driverL)

    driver.get("https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications")
    
    #login
    input1 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input')
    input2 = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
    inputInvio = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')

    input1.send_keys(inputUsername)
    input2.send_keys(inputPassword)
    inputInvio.click()

    time.sleep(1000)
    #ultimo messaggio
    driver.close()
    print("""
installazione finita!

per avviare il tuo bot d'ora in poi ti basterà avviare il file .exe che si è creato nel desktop
    """)

installazioneABC()