import discord
from discord.ext import commands
from discord import utils
import asyncio
import json

class Suggest(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="suggest")
    @commands.guild_only()
    async def suggest(self, ctx):
        """Test"""


        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] == "OFF":
            await ctx.send("Sugestiile nu sunt deschide!")
            return

        author = ctx.author
        time = discord.Embed(title=f'Timp', description=f'Ai ramas fara timp,te rugam incearca din nou!', footer=f'Sugestie facuta de: {author.name} • TheGuy#3784', color=0xFF4C4C)
        briefembed = discord.Embed(title=f'Sugestie', description=f'Te rugam sa scrii o explicatie pe scurt a sugestiei tale!', footer=f'Sugestie facuta de: {author.name} • TheGuy#3784', color=0xffffff)
        explainembed = discord.Embed(title=f'Sugestie', description=f'Te rugam sa scrii o explicatie detaliata a sugestiei tale!', footer=f'Sugestie facuta de: {author.name} • TheGuy#3784', color=0xffffff)
        channelnotexist = discord.Embed(title=f'Sugestie', description=f'Canalul specificat nu exista.', footer=f'Sugestie facuta de: {author.name} • TheGuy#3784', color=0xffffff)
        await ctx.message.delete()

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "ON":

            def check(m):
                return True if m.channel.id == ctx.channel.id and m.author.id == author.id else False

            msg = await ctx.send(f'Te rugam sa raspunzi la urmatoarele intrebari, {author.mention}!')

            await ctx.send(embed=briefembed)
            try:
                brief = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                timemsg = await ctx.send(embed=time)
                await asyncio.sleep(30)
                await timemsg.delete()
                await msg.delete()
                return

            await msg.delete()
            await ctx.send(embed=explainembed)
            try:
                explain = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                timemsg = await ctx.send(embed=time)
                await asyncio.sleep(30)
                await timemsg.delete()
                return

            embed = discord.Embed(title=f'ID Sugestie: {self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"]}', colour=0xffffff)
            embed.add_field(name=f'Explicatie pe scurt: ', value=f'{brief.content}')
            embed.add_field(name=f'Explicatie detaliata: ', value=f'{explain.content}')
            embed.set_footer(text=f'Sugestie facuta de: {author.name} • TheGuy#3784')

            try:
                channel = discord.utils.get(ctx.guild.text_channels, id=int(self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"]))
                msg = await channel.send(embed=embed)
            except:
                await ctx.send(embed=discord.Embed(title=f'Sugestie', description=f'Trimiterea sugestiei a esuat.Limita de 2000 de caractere atinsa.', color=0xff4c4c))
                return
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

            id = self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"]
            newid = int(id) + 1
            self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"] = str(newid)
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "OFF":

            def check(m):
                return True if m.channel.id == author.dm_channel.id and m.author.id == author.id else False


            msg = await ctx.send(f'{author.mention} Verifica in PM''s')

            await author.send(embed=briefembed)
            try:
                brief = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                timemsg = await author.send(embed=time)
                await asyncio.sleep(30)
                await timemsg.delete()
                await msg.delete()
                return

            await msg.delete()
            await author.send(embed=explainembed)
            try:
                explain = await self.bot.wait_for('message', check=check, timeout=300)
            except asyncio.TimeoutError:
                timemsg = await author.send(embed=time)
                await asyncio.sleep(30)
                await timemsg.delete()
                return

            embed = discord.Embed(title=f'ID Sugestie: {self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"]}', colour=0xffffff)
            embed.add_field(name=f'Explicatie pe scurt: ', value=f'{brief.content}')
            embed.add_field(name=f'Explicatie detaliata: ', value=f'{explain.content}')
            embed.set_footer(text=f'Sugestie facuta de: {author.name} • TheGuy#3784')

            try:
                channel = discord.utils.get(ctx.guild.text_channels, id=int(self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"]))
                msg = await channel.send(embed=embed)
            except:
                await author.send(embed=discord.Embed(title=f'Sugestie', description=f'Trimiterea sugestiei a esuat.Limita de 2000 de caractere atinsa.', color=0xff4c4c))
                return

            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

            id = self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"]
            newid = int(id) + 1
            self.bot.config["GUILDS"][str(ctx.guild.id)]["ID"] = str(newid)
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)

def setup(bot):
    bot.add_cog(Suggest(bot))