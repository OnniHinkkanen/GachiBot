# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:09:54 2021

@author: Onni
"""
import os
import discord
import re
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
URL = os.getenv('INV_URL')
client = discord.Client()
quotes=[]
triggers=[]
lyrics=[]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Koodi: ", URL)
    status = discord.Game("18 naked cowboys in the showers at Ram Ranch")
    await client.change_presence(status=discord.Status.online, activity=status)
    
    
    #TODO: emotes properly
    f = open("quotes.dat", "r")
    for x in f:
        quotes.append(x.rstrip("\n"))
    
    f = open("triggers.dat", "r")
    for x in f:
        triggers.append(x.rstrip("\n"))
    
    f = open("lyrics.dat", "r")
    for x in f:
        lyrics.append(x.rstrip("\n"))
        

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    
    found_lyrics=False
    i=-1
    for line in lyrics:
        i = i + 1
        if re.search(line, msg):
            found_lyrics=True
            break
    
    if found_lyrics and i != len(lyrics) - 2:
        await message.channel.send(lyrics[i + 1].rstrip(")(!)?").lstrip("(?i)(") + "!")
        return
    
    found_trigger=False
    
    
    #TODO: maybe no trigger for gachi bot 
    for trigger in triggers:
        if re.search(trigger, msg):
            found_trigger=True
            break
        
    if found_trigger:
        i = random.randint(0, len(quotes) -1)
        await message.channel.send(quotes[i])
        return
    
    

"""
    
    emoji = discord.utils.get(client.emojis, name='DelightfulDog')
    
    
    if ":delightfuldog:" in msg:
        await message.add_reaction(emoji)
    
    
    if found_dog:
        await message.channel.send("what da dog doin? " + str(emoji))
    
        

        
     
    if "dog" in msg:
        await message.channel.send("what da dog doin? :DelightfulDog:")
        
      
"""
client.run(TOKEN)