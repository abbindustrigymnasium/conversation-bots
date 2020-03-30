import random
import math
from random import randint
from discord.ext.commands import Bot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

BOT_PREFIX = ">"
TOKEN = "secret"
client = Bot(command_prefix = BOT_PREFIX)

Ray = ChatBot(
            "Ray",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            database_uri='sqlite:///database.sqlite3',
            logic_apapter=[
            "chatterbot.logic.TimeLogicAdapter",
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.BestMatch"]
)

@client.command(name = "chat",
                description = "chats with the dumb bot",
                pass_context = True)
async def chat(context, *, arg):
    if context.author == client.user:
            return

    Ray_input = Ray.get_response(str(arg))
    await context.send(Ray_input)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')

client.run(TOKEN)