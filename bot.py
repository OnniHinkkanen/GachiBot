# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:09:54 2021

@author: Onni
"""
import os
import discord
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
URL = os.getenv('INV_URL')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("Koodi: ", URL)
    status = discord.Game("with the virgins' dogs")
    await client.change_presence(status=discord.Status.online, activity=status)

"""
buffer = ""
"""

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    
    
    """    
    global buffer
    buffer = buffer + msg
    
    if  "nigger" in buffer:
        await message.channel.send("YO! You did not have the N word pass!!")
        buffer = ""
        return
    """
    

    
    SEXExp = "(?i)(\A[s]+[e€3£]+[x]+[!?]*$)|(\A[s]+[e3€£]+[x]+[!?]*\s)|((?<!no)[\s][s]+[e3€£]+[x]+[!?]*(?!\S))"
    SEXbot = "(?i)[s]+[e3€£]+[x]\sbot"
    found_sex_bot=re.search(SEXbot, msg)   
    
    if found_sex_bot:
        msg = msg.replace("sex bot", " ")


    found_sex = re.search(SEXExp, msg)
    
    #if found_sex_bot and not found_sex:
    #   return
    
    DOGExp = "(?i)(\A[d]+[o]+[g]+[!?]*$)|(\A[d]+[o]+[g]+[!?]*\s)|((?<!no)[\s][d]+[o]+[g]+[!?]*(?!\S))"
    DOGbot = "(?i)[d]+[o]+[g]\sbot"
    found_dog_bot = re.search(DOGbot, msg)
    
    if found_dog_bot:
        msg = msg.replace("dog bot", " ")
    
    
    found_dog = re.search(DOGExp, msg)
    
    emoji = discord.utils.get(client.emojis, name='DelightfulDog')
    
    
    if ":delightfuldog:" in msg:
        await message.add_reaction(emoji)
    
    
    if found_dog:
        await message.channel.send("what da dog doin? " + str(emoji))
    
    if found_sex:
        await message.channel.send("NO SEX!")
        

        
    """    
    if "dog" in msg:
        await message.channel.send("what da dog doin? :DelightfulDog:")
        
        """

client.run(TOKEN)