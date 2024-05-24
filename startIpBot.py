import discord
import requests
import os

TOKEN = os.environ['BOT_TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def getIp():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request for getting ip. Sorry'

    data = response.json()

    return data['ip']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if 'ip please' in message.content.lower():
        await message.channel.send(getIp())


client.run(TOKEN)
