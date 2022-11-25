import os

import discord
from dotenv import load_dotenv

from euribor_library import Euribor

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


class DiscordLibrary(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!euribor12"):
            print("Got message: '"+str(message.content) + "'. Responding...")
            await message.reply(Euribor().reply_to_12_months(), mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

client = DiscordLibrary(intents=intents)
client.run(TOKEN)
