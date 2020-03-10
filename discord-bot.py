import discord
import main

TOKEN = 'Njc4OTM0MTg3MzMxNTUxMjMz.XkqA3Q.BGhaFTctIbT6uxos_2uOJKnuPz8'

norman = discord.Client()

# @norman.command(name="chat",
#                 pass_context=True)
# async def chat(ctx, *args):
#     input = " ".join(args)
#     bot_output = main.messageArrive(input)
#     await norman.send((bot_output, ctx.message.author.mention))

@norman.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == norman.user:
        return
    elif message.content:
        await norman.send("Hello")


@norman.event
async def on_ready():
    print('Logged in as')
    print(norman.user.name)
    print(norman.user.id)
    print('------')

norman.run(TOKEN)