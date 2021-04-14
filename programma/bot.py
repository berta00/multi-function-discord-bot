import time
import os
import selenium
import discord
import simple_colors
from sys import platform
from selenium import webdriver
from aternosBot import *
from discord.ext import commands
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get


token = input("Metti il token del bot: ")

global client

client = commands.Bot(command_prefix = 'ciro: ')

@client.event
async def on_ready():
    print(simple_colors.green('loggato in discord'))
    print()

@client.command()
async def serverOn(ctx):
    await ctx.send("Oke, metti lo username:")
    username = await client.wait_for('message')
    print("username messo")
    await ctx.send("Oke, metti il password:")
    password = await client.wait_for('message')
    print("password messa")

    await connessioneAlServer(drivers, username.content, password.content)

@client.command()
async def serverOff(ctx):
    await ctx.send("Okey capo")
    await esciDaAternos()

@client.command()
async def ruba(ctx):
    await ctx.send("vado a rubare orologi ok")
    #mi dissocio

@client.command()
async def nutella(ctx):
    await ctx.send("la sto riproducendo, a mi me piace nutella celato cu panna")
    voicechannel = discord.utils.get(ctx.guild.channels, name='queue')
    vc = await voicechannel.connect()
    vc.play(discord.FFmpegPCMAudio("countdown.mp3"), after=lambda e: print('done', e))

client.run(token)
