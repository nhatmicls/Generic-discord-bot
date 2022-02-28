from distutils.command.config import config
import os
import random
import discord
from typing import *

from discord.ext import commands

from get_data import ReadDatabase
from process_data import *


class ConfigBot:
    token = ""
    discord_guild = ""
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix="cat>", intents=intents)
    database = ReadDatabase()


def update_config(token: str, discord_guild: str, json_directory: str):
    ConfigBot.token = token
    ConfigBot.discord_guild = discord_guild
    ConfigBot.database.update_json_directory(json_directory)


@ConfigBot.bot.command(name="getDrive")
async def get_drive_link(ctx):
    link_drive = ConfigBot.database.get_drive()
    _recv = multi_data_to_messeage(link_drive)
    await ctx.channel.send(_recv)


@ConfigBot.bot.event
async def on_message(ctx):
    if ctx.content == "cat>":
        random_respond = ConfigBot.database.get_random_messeage()
        _recv = random_return(random_respond)
        await ctx.channel.send(_recv)
    await ConfigBot.bot.process_commands(ctx)


@ConfigBot.bot.event
async def on_ready():
    global server
    print(f"{ConfigBot.bot.user.name} has connected to Discord!")
    server = ConfigBot.bot.get_guild(int(ConfigBot.discord_guild))


def _exec():
    ConfigBot.bot.run(ConfigBot.token)
