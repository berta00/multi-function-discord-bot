#
import time
import os
#controlla o installa le dipendenze
os.system("pip install selenium==4.0.0a1")
os.system("pip install simple_colors")

from sergio import *
print("""
          █████ ████████ ███████ ██████  ███    ██  ██████  ███████     ██████   ██████ ████████                                                     
         ██   ██   ██    ██      ██   ██ ████   ██ ██    ██ ██          ██   ██ ██    ██   ██                                                        
         ███████   ██    █████   ██████  ██ ██  ██ ██    ██ ███████     ██████  ██    ██   ██                                                        
         ██   ██   ██    ██      ██   ██ ██  ██ ██ ██    ██      ██     ██   ██ ██    ██   ██                                                        
         ██   ██   ██    ███████ ██   ██ ██   ████  ██████  ███████     ██████   ██████    ██  

 ██████  ██████  ███    ██ ████████ ██████   ██████  ██      ██       █████       █████ ████████ ███████ ██████  ███    ██  ██████  ███████ 
██      ██    ██ ████   ██    ██    ██   ██ ██    ██ ██      ██      ██   ██     ██   ██   ██    ██      ██   ██ ████   ██ ██    ██ ██      
██      ██    ██ ██ ██  ██    ██    ██████  ██    ██ ██      ██      ███████     ███████   ██    █████   ██████  ██ ██  ██ ██    ██ ███████ 
██      ██    ██ ██  ██ ██    ██    ██   ██ ██    ██ ██      ██      ██   ██     ██   ██   ██    ██      ██   ██ ██  ██ ██ ██    ██      ██ 
 ██████  ██████  ██   ████    ██    ██   ██  ██████  ███████ ███████ ██   ██     ██   ██   ██    ███████ ██   ██ ██   ████  ██████  ███████ 
                                                                                                                                            
                                                                                                                                            """)
nomeServer = input("Inserisci l'id del server: ")             # implementala nella interfaccia
passwordServer = input("inserisci la password: ")         # implementala nella interfaccia
print ("")


connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia
accendiIlServer()                                         # implementala nella interfaccia
# esciDaAternos()                                         # implementala nella interfaccia



