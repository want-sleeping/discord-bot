import discord
from discord.ext import commands 
import os
import asyncio
import json

with open("settings.json", mode = "r", encoding="utf-8") as jfile:
    data = json.load(jfile)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    print(f"機器人擁有者 ID: {bot.owner_id}")
    print(f"目前登入身份 --> {bot.user}")
    print("Slash command names:", [cmd.name for cmd in bot.tree.walk_commands()])
    print("I'm ready for new adventures!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    print(f"收到內容: '{message.content}' | 來自: {message.author}")
    await bot.process_commands(message)


@bot.command()
@commands.is_owner()
async def update(ctx):
    await ctx.send("收到指令，開始同步...")
    print(">>> 開始執行同步...")
    try:
        synced = await bot.tree.sync()
        await ctx.send("同步成功！")
        print(f"同步成功！已更新 {len(synced)} 個指令。")
    except Exception as e:
        print(f"同步出錯: {e}")
        await ctx.send(f"同步失敗: {e}")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(data["token"])

if __name__ == "__main__":
    asyncio.run(main())