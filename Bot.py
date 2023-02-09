"""
    DISCORD BOT
"""
import os
import discord
import requests
import json
from dotenv import load_dotenv

# confidential should put in .env


def get_dog():
    # fetch data from dog api
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(response.text)
    return json_data['message']  # return the dog image url


def get_cat():
    # fetch data from cat api
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    json_data = json.loads(response.text)
    return json_data[0]['url']  # return the cat image url


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('!dog'):
            getdog = get_dog()
            await message.channel.send(getdog)

        if message.content.startswith('!cat'):
            getcat = get_cat()
            await message.channel.send(getcat)

        if message.content.startswith(('!hello', '!hi')):
            await message.channel.send(f'Heyy wasuppp! {message.author.mention}')

        if message.content.startswith(('wabyu', 'i love you', 'lablab', 'lab lab', 'labu')):
            await message.channel.send(f'Fuck you! {message.author.mention}')

        if message.content.startswith('!kish'):
            await message.channel.send(f'{message.author.mention} supp brothaa!')

        if message.content == 'ver':
            BotVersion = discord.Embed(
                title="Current Version", description="Beta Version", color=0x00ff00)
            BotVersion.add_field(name="Version Beta:",
                                 value="beta", inline=False)
            BotVersion.add_field(name="Date Released",
                                 value="10/26/2022", inline=False)
            BotVersion.add_field(name="Develop By:", value=message.author.name)
            BotVersion.set_footer(text="I am so fuckin tired")
            await message.channel.send(embed=BotVersion)

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv('TOKEN'))
