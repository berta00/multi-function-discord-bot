import time
import os
#controlla o installa le dipendenze
os.system("pip install selenium")
os.system("pip install simple_colors")

from sergio import *
print("buongiorno")
print ("hai scleto")
print ("Questo bot ha diverse funzionalità:")
nomeServer = input("inserisci lo username: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia
nocheat=input("questa funzione controlla che non vengano usati cheat ")
connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia
accendiIlServer()                                         # implementala nella interfaccia
# esciDaAternos()                                         # implementala nella interfaccia


