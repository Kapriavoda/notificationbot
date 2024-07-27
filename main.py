# This example requires the 'message_content' intent.

import discord
from discord.ext import commands, tasks
import scrape

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

subs = []

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    periodic_task.start()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


is_online = False
@tasks.loop(seconds=300)  # Change the seconds parameter to set the interval
async def periodic_task():
    global is_online
    str = ""
    for k in subs:
        str += f"<@{k}>"

    if scrape.check_online("michaelaverage") and not is_online:
        is_online = True
        await client.get_channel(1266738624284856343).send(f"michaelaverage je online!!! {str} https://kick.com/michaelaverage")
    elif not scrape.check_online("michaelaverage") and is_online:
        is_online = False
        await client.get_channel(1266738624284856343).send(f"michaelaverage uz nie je online zzzZZZ {str}")


client.run('TOKEN')
