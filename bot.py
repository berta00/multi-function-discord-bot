import time
import os
import selenium
import discord
import simple_colors
from sys import platform
from sergio import *
from selenium import webdriver
from discord.ext import commands


token = input("Metti il token del bot: ")

os.system("clear")

global username
global password

client = commands.Bot(command_prefix = 'ciro: ')

@client.event
async def on_ready():
    print(simple_colors.green('loggato'))
    print()

@client.command()
async def serverOn(ctx):
    await ctx.send("Oke, metti lo username:")
    username = await client.wait_for("message")
    print("username messo")
    await ctx.send("Oke, metti il password:")
    password = await client.wait_for("message")
    print("password messa")
    await connessioneAlServer(drivers, username, password)

async def serverOff(ctx):
    await ctx.send("Okey capo")
    await esciDaAternos()

client.run(token)