import discord
from discord.ext import commands
from discord import utils
import asyncio
import time
import json
import os

extensions = ["settings", "developer", "suggest", "general"]

def get_prefix(bot, message):
    """Get the prefixes."""
    gprefix = client.config["GLOBAL"]["PREFIX"]
    if message.guild is None:
        extras = gprefix
        return commands.when_mentioned_or(*extras)(bot, message)
    prefix = client.config["GUILDS"][str(message.guild.id)]["PREFIX"]
    extras = [prefix, gprefix]
    return commands.when_mentioned_or(*extras)(bot, message)


client = commands.Bot(command_prefix=get_prefix)

with open('settings.json', 'r') as f:
    client.config = json.load(f)


async def add_guild():
    if not "GUILDS" in client.config:
            client.config["GUILDS"] = {}
    for guild in client.guilds:
        gid = str(guild.id)
        if gid not in client.config["GUILDS"]:
            client.config["GUILDS"][gid] = {
            "TOGGLED": "ON",
            "TOGGLEPM": "OFF",
            "OUTPUT": None,
            "ID": "1",
            "PREFIX": "!"
            }
            print(f"Server adaugat in config ({guild.name})")
            with open('settings.json', 'w') as f:
                json.dump(client.config, f, indent=2)



@client.event
async def on_guild_join(guild):
    await add_guild()
    embed = discord.Embed(title=f':tools: Suggestion Bot', color=0xffffff)
    embed.add_field(name=f'Multumim pentru ca ai adaugat Suggestion Bot in {guild.owner.name}!', value=f'Pentru a configura botul foloseste **!settings** intr-un canal de text. Pentru a vedea ce face o anumita comanda foloseste: **!help**, \nFii sigur ca botul are urmatoare permisiune: `Administrator` sau urmatoarele permisiuni: `Manage messages`, `Add reactions`, `Read messages`, `Send messages`, `Read message history`, `Embed links` si `Attach file`')
    embed.add_field(name=f'Linkuri', value=f'[Instagram](https://www.instagram.com/razvanksz/)  | [Suport] (TheGuy#3784)' )
    await guild.owner.send(embed=embed)


@client.event
async def on_ready():
    print('-------------------------------------------------------------')
    print('Bot pregatit!')
    print('Foloseste !help pentru ajutor')
    print('Support TheGuy#3784')
    print('-------------------------------------------------------------')
    await client.change_presence(activity=discord.Activity(name='Suggestion Bot | !help', type=0))
    await add_guild()


if __name__ =='__main__':
    for extension in extensions:
        try:
            client.load_extension("extensions." + extension)
        except Exception as e:
            print("")
            print("TRACEBACK")
            print("--------------------------------")
            print(e)
            print("--------------------------------")
            print('Failed to load extension {}'.format(extension))
            print("")

try:
    client.run(client.config["GLOBAL"]["TOKEN"], bot=True, reconnect=True)
except:
    print("---------------------------------------------------------------------")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("INVALID TOKEN, PLEASE EDIT THE TOKEN FIELD IN SETTINGS.JSON")
    print("---------------------------------------------------------------------")
    time.sleep(10)
