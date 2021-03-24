#
import time
import os
#controlla o installa le dipendenze
os.system("pip install discord")
os.system("pip install selenium==4.0.0a1")
os.system("pip install simple_colors")

from sergio import *
print("""
 █████  ████████ ███████ ██████  ███    ██  ██████  ███████ 
██   ██    ██    ██      ██   ██ ████   ██ ██    ██ ██      
███████    ██    █████   ██████  ██ ██  ██ ██    ██ ███████ 
██   ██    ██    ██      ██   ██ ██  ██ ██ ██    ██      ██ 
██   ██    ██    ███████ ██   ██ ██   ████  ██████  ███████ 
                                                            
                                                            
██████   ██████  ████████                                   
██   ██ ██    ██    ██                                      
██████  ██    ██    ██                                      
██   ██ ██    ██    ██                                      
██████   ██████     ██                                      
  """)
#nomeServer = input("Inserisci l'id del server: ")             # implementala nella interfaccia
#passwordServer = input("inserisci la password: ")         # implementala nella interfaccia
print ("")


#connessioneAlServer(driver, nomeServer, passwordServer)   # implementala nella interfaccia
#accendiIlServer()                                         # implementala nella interfaccia
# esciDaAternos()                                         # implementala nella interfaccia







client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODI0MzAxMTc1NTYyMTc0NDg0.YFtYSw.JXGW0kPQO86sopCoO8PeTUEgSbU')