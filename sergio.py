import time
import os
import selenium
from selenium import webdriver                                                                                                     # password: abeteswag17

a = ""      # appena aggiungi la parte di login
b = ""      # nella interfaccia poi toglierle

# selenium

#webdriver
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
    #controlla se è online, se è online continua ad eseguire il codice sotto
    online = False
    while online == False:
        online = driver.get_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[4]/div[1]/div/span[2]/span').is_displayed()
    print("il sevrer è online")
    #controlla c'è gentre dentro al server, se c'è gente continua ad eseguire il codice sotto
    popolato = False
    while popolato == False:
        popolato = driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[4]/div[1]/div/span[1]').is_displayed()
        print("attenzione, non c'è nessuno nel server")
    


def esciDaAternos():
    driver.quit()

    #oiteyfeotgdfohguiuidfghifdu
    #sssssssssss
    #dddddddddddddd