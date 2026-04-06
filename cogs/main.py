import json
import discord
from discord.ext import commands

with open("settings.json", mode = "r", encoding="utf-8") as jfile:
    data = json.load(jfile) 

keywords = data["keywords"]

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if data["bot_name"].lower() in message.content.lower():
            await message.channel.send("Manager!!!")

        if any(keyword in message.content.lower() for keyword in keywords):
            embed = discord.Embed(
                title="都市零协会汉化组 | Localize Limbus Company",
                description="Keep your Determination.",
                url = "https://www.zeroasso.top/",
                color=discord.Color.red())
            await message.channel.send(embed=embed)
            
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))