import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice

class Slash_Commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="translator", description="Download Limbus Company translator.")
    async def translator(self, interaction: discord.Interaction):
        await interaction.response.send_message("Limbus Company translator:\nhttps://www.zeroasso.top/")

    @app_commands.command(name="mirror-dungeon", description="Ego gift,package,15 floor, video about mirror dungeon etc.")
    @app_commands.describe(type="Choose the type of mirror dungeon content you want to see.")
    @app_commands.choices(type=[
        Choice(name="15 Floor", value="15_floor"),
        Choice(name="Ego Gift", value="ego_gift"),
        Choice(name="Package", value="package"),
        Choice(name="Video", value="video"),
        Choice(name="Translator", value="translator")
    ])
    async def mirror_dungeon(self, interaction: discord.Interaction, type: Choice[str]):
        if type == "15_floor":
            await interaction.response.send_message("15 Floor:\n【【边狱巴士】镜牢15层攻略-李箱单通全流程讲解，满制约公式化打法，助力萌新第一次通关15牢】\nhttps://www.bilibili.com/video/BV1ubcSz6E8V")
        elif type == "ego_gift":
            await interaction.response.send_message("Ego Gift:\nhttps://limbuscompany.wiki.gg/wiki/List_of_E.G.O_Gifts")
        elif type == "package":
            await interaction.response.send_message("Package:\nhttps://limbuscompany.wiki.gg/wiki/List_of_Floor_Themes")
        elif type == "video":
            await interaction.response.send_message("Video:\n【零基础萌新镜牢毕业只用一期视频？这些知识老玩家也不可能全部知道】\nhttps://www.bilibili.com/video/BV1cQXmBBEtC")
        elif type == "translator":
            await interaction.response.send_message("Limbus Company translator:\nhttps://www.zeroasso.top/")

async def setup(bot: commands.Bot):
    await bot.add_cog(Slash_Commands(bot))