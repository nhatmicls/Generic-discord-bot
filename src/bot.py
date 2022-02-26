# bot.py
import os
import random
import discord
from dotenv import load_dotenv

from xml.dom import minidom

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")

server = []

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="cat>", intents=intents)


def updateemoji():
    global server
    print(f"{bot.user.name} is updating emoji to xml file!")

    # for emoji in bot.emojis:
    #     print("Name:", emoji.name + ",", "ID:", emoji.id)

    # channel = discord.utils.get(server.channels, name="welcome")
    # channel_id = channel.id


@bot.event
async def on_ready():
    global server
    print(f"{bot.user.name} has connected to Discord!")
    server = bot.get_guild(int(DISCORD_GUILD))
    updateemoji()


@bot.command()
async def ping(ctx):
    print(server.id)
    await ctx.channel.send("Pong!")


@bot.command(name="DM")
async def DMrandom(ctx):
    pass


@bot.command(name="Welcome")
async def welcome(ctx):
    icon = str(server.icon_url)
    channel = os.getenv("WELCOME_ID")
    channel = bot.get_channel(int(channel))
    embebHello = discord.Embed(
        title="Server info", description="", color=discord.Color.blue()
    )
    embebHello.add_field(name="Server name", value=server.name, inline=True)
    embebHello.add_field(name="Server member", value=server.member_count, inline=True)
    embebHello.set_thumbnail(url=icon)
    msg = await channel.send(embed=embebHello)

    # Reaction zone
    emojis = ":02Stab:820157290392846337"
    await msg.add_reaction(emojis)
    # reaction = await bot.wait_for_reaction()
    # await ctx.channel.send(msg,":pepesimp:")


@bot.command(name="getDrive")
async def get_drive_link(ctx):
    link_drive = "https://drive.google.com/drive/u/0/folders/0AKWNoIiS6q1BUk9PVA"
    await ctx.channel.send(link_drive)


@bot.command(name="bug")
async def bug_handle(ctx):
    response = "chịu thôi chứ sao @@"
    await ctx.channel.send(response)


@bot.event
async def on_message(message):

    response_list = [
        "thế kỷ 21 rồi ai cũng làm wjbu",
        "chạn vương muôn năm",
        "làm gì thì làm, đừng làm thinh là được",
        "tao sắp ra trường rồi",
        "bug vler",
        "làm luận văn chán quá!",
        "tao muốn lấy chị giàu",
    ]

    if message.content == "cat>":
        response = random.choice(response_list)
        await message.channel.send(response)
    await bot.process_commands(message)


@bot.event
async def on_reaction_add(reaction, user):
    messageid = reaction.message.id
    channel = reaction.message.channel
    # print("ID: ",messageid)
    # if(messageid==820542000075374592)
    #     await bot.se


@bot.event
async def on_member_join(member):
    icon = str(server.icon_url)
    channel = os.getenv("WELCOME_ID")
    channel = bot.get_channel(int(channel))
    embebHello = discord.Embed(
        title="Server info", description="", color=discord.Color.blue()
    )
    embebHello.add_field(name="Server name", value=server.name, inline=True)
    embebHello.add_field(name="Server member", value=server.member_count, inline=True)
    embebHello.set_thumbnail(url=icon)
    msg = await channel.send(embed=embebHello)

    # DM channel

    # Reaction zone
    emojis = ":02Stab:820157290392846337"
    await msg.add_reaction(emojis)


bot.run(TOKEN)
