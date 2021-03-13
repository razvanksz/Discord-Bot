import discord
from discord.ext import commands
from discord import utils
import asyncio
import json

class Settings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name='settings', aliases=["suggestsettings", "suggestsetting"])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def settings(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Setari', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}settings <sub-commanda>**', value=f'Sub-Comenzi valide: *toggle*, *output*, *prefix*, *togglepm*')
            await ctx.send(embed=embed)
            return


    @settings.command(name="toggle")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def toggle(self, ctx):
            if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] == "ON":
                self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] = "OFF"
                with open('settings.json', 'w') as f:
                    json.dump(self.bot.config, f, indent=2)
                    await ctx.send(f'Sugestiile au fost inchise!')
                    return

            if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] == "OFF":
                self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLED"] = "ON"
                with open('settings.json', 'w') as f:
                    json.dump(self.bot.config, f, indent=2)
                    await ctx.send(f'Sugestiile au fost deschise!')
                    return

    @settings.command(name="togglepm")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def togglepm(self, ctx):

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "ON":
            self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] = "OFF"
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)
                await ctx.send(f'Sugestile vor fii facute in PMs!')
                return

        if self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] == "OFF":
            self.bot.config["GUILDS"][str(ctx.guild.id)]["TOGGLEPM"] = "ON"
            with open('settings.json', 'w') as f:
                json.dump(self.bot.config, f, indent=2)
                await ctx.send(f'Sugestile vor fi facute in canalul unde s-a executat comanda!')
                return


    @settings.command(name="output")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def output(self, ctx, output: str = None):

        if output == None:
            embed = discord.Embed(title=":tools: Setari", color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}settings output <id-canal>**', value=f'Canalul specificat este invalid!Incearca din nou! [**Cum sa gasesti ID Canal!**](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-server-ID-)')
            await ctx.send(embed=embed)
            return

        try:
            channel = discord.utils.get(ctx.guild.text_channels, id=int(output))
            await channel.send(f'Sugestile vor aparea aici!')
        except:
            embed = discord.Embed(title=f':tools: Setari', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}settings output <id-canald>**', value=f'Canalul specificat este invalid!Incearca din nou! [**Cum sa gasesti ID Canal!**](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-server-ID-)')
            await ctx.send(embed=embed)
            return

        self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"] = output
        with open('settings.json', 'w') as f:
            json.dump(self.bot.config, f, indent=2)
            channel = discord.utils.get(ctx.guild.text_channels, id=int(self.bot.config["GUILDS"][str(ctx.guild.id)]["OUTPUT"]))
            await ctx.send(f'Propunerile vor aparea de acum in canalaul: {channel.mention}')
            return


    @settings.command(name="prefix")
    @commands.guild_only()
    async def prefix(self, ctx, newprefix: str = None):

        if newprefix == None:
            embed = discord.Embed(title=f':tools: Settings', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}settings prefix <prefix noux>**', value=f'Te rugam sa introduci un prefix! ex: **!**')
            await ctx.send(embed=embed)
            return


        self.bot.config["GUILDS"][str(ctx.guild.id)]["PREFIX"] = newprefix
        with open('settings.json', 'w') as f:
            json.dump(self.bot.config, f, indent=2)
            await ctx.send(f'Prefixul pentru **{ctx.guild.name}** ''a fost schimbat in: **{}**'.format(newprefix))
            return

def setup(bot):
    bot.add_cog(Settings(bot))