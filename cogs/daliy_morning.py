import json
import random
from discord.ext import tasks, commands
import datetime
import discord

with open("settings.json", mode = "r", encoding="utf-8") as jfile:
    data = json.load(jfile)

channel_id = data["channel_id"]
lucky_number = random.randint(1, 100)

class Daily_Morning(commands.Cog):

    tz_hk = datetime.timezone(datetime.timedelta(hours=8))
    tz = datetime.timezone(datetime.timedelta(hours=1))
    everyday_time = datetime.time(hour=7, minute=0, tzinfo=tz)
    everyday_time_hk = datetime.time(hour=7, minute=0, tzinfo=tz_hk)

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()
        self.everyday_hk.start()

    @tasks.loop(time=everyday_time)
    async def everyday(self):
        channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(
            title="【 Don Quixote Adventure 】",
            description="Good morning! It's a new day! Is time to start a new adventure!",
            color=discord.Color.blue(),
            timestamp = datetime.datetime.now(self.tz)
        )
        await channel.send(embed=embed)

    @tasks.loop(time=everyday_time_hk)
    async def everyday_hk(self):
        channel = self.bot.get_channel(channel_id)
        embed_hk = discord.Embed(
            title="【 Don Quixote Adventure 】",
            description="Good morning! It's a new day in h.k! Is time to start a new adventure! " + f"(Today's lucky number for today is {lucky_number}.)",
            color=discord.Color.blue(),
            timestamp = datetime.datetime.now(self.tz_hk)
        )
        await channel.send(embed=embed_hk)

async def setup(bot: commands.Bot):
    await bot.add_cog(Daily_Morning(bot))