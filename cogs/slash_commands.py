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
        Choice(name="15-floor", value="15 Floor"),
        Choice(name="ego-gift", value="Ego gift"),
        Choice(name="package", value="Package:\nhttps://limbuscompany.wiki.gg/wiki/List_of_Floor_Themes"),
        Choice(name="video", value="Video"),
        Choice(name="translator", value="Limbus Company Translator")
    ])
    async def mirror_dungeon(self, interaction: discord.Interaction, type: str):
        try:
            if type == "15 Floor":
                await interaction.response.send_message("15 Floor:\n【【边狱巴士】镜牢15层攻略-李箱单通全流程讲解，满制约公式化打法，助力萌新第一次通关15牢】\nhttps://www.bilibili.com/video/BV1ubcSz6E8V")
            elif type == "Ego gift":
                await interaction.response.send_message("Ego Gift:\nhttps://limbuscompany.wiki.gg/wiki/List_of_E.G.O_Gifts")
            elif type == "Package":
                await interaction.response.send_message("Package:\nhttps://limbuscompany.wiki.gg/wiki/List_of_Floor_Themes")
            elif type == "Video":
                await interaction.response.send_message("Video:\nhttps://www.bilibili.com/video/BV1CY411f7yh")
            elif type == "Limbus Company Translator":
                await interaction.response.send_message("Limbus Company Translator:\nhttps://www.zeroasso.top/")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Slash_Commands(bot))