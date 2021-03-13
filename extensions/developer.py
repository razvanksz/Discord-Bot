import discord
from discord.ext import commands
from discord import utils
import asyncio
import json


class Developers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot




    @commands.group()
    @commands.is_owner()
    async def extension(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Extensii', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}extension <sub-comanda>**', value=f'Sub-Comenzi valide: *reload*, *load*, *load*')
            await ctx.send(embed=embed)
            return


    @extension.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, extension: str = None):
        """Load a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensii', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}extension load <extensie>**', value=f'Te rugam sa introduci o extensie valabila! ex: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.load_extension(f'extension.' + extension)
        except Exception as e:
            await ctx.send(f'**`Eroare:`** Nu am putut incarca extensia {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send(f'**`Succes`** Am incarcat extensia: *{extension}*')

    @extension.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, extension: str = None):
        """Unload a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensii', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}extension unload <extensie>**', value=f'Te rugam sa introduci o extensie valabila! ex: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.unload_extension(f'extension.' + extension)
        except Exception as e:
            await ctx.send(f'**`Eroare:`** Nu am putut dezactiva {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send(f'**`Succes:`** Extensie dezactivata: *{extension}*')

    @extension.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, extension: str = None):
        """Reload a extension!"""

        if extension == None:
            embed = discord.Embed(title=f':tools: Extensii', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}extension reload <extensie>**', value=f'Te rugam sa introduci o extensie valida: **suggest**')
            await ctx.send(embed=embed)
            return

        try:
            self.bot.unload_extension(f'extension.' + extension)
            self.bot.load_extension(f'extension.' + extension)
        except Exception as e:
            await ctx.send(f'**`Eoare:`** Nu am putut reincarca extensia {extension}')
            await ctx.send(f'=========================================')
            await ctx.send(f'```{e}```')
        else:
            await ctx.send(f'**`Succes`** Extensia reincarcata: *{extension}*')

    @commands.group(name="bot")
    @commands.is_owner()
    async def bots(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title=f':tools: Unelte Bot', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}bot <sub-comanda>**', value=f'Sub-Comenzi valide: *stop*')
            await ctx.send(embed=embed)
            return


    @bots.command(name='stop', alias="restart")
    @commands.is_owner()
    async def stop(self, ctx):
        """Stops/Restarts the bot."""

        await ctx.send(f'Oprire bot!')
        await self.bot.logout()


    @bots.command(name="prefix")
    async def prefix(self, ctx, newprefix: str = None):

        if newprefix == None:
            embed = discord.Embed(title=f':tools: Setari', color=0xffffff)
            embed.add_field(name=f'Sintaxa invalida! **{ctx.prefix}bot prefix <prefixnou>**', value=f'Te rugam sa introduci un prefix valid! ex: **!**')
            await ctx.send(embed=embed)
            return



        self.bot.config["GLOBAL"]["PREFIX"] = newprefix
        with open('settings.json', 'w') as f:
            json.dump(selg.bot.config, f, indent=2)
            await ctx.send('Prefixul global a fost schimbat in: **{}**'.format(newprefix))
            return

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        if isinstance(error, discord.ext.commands.NoPrivateMessage):
            await ctx.send(f':no_entry: Aceasta comanda se poate folosi doar pe un server!')
            return
        if isinstance(error, discord.ext.commands.NotOwner):
            await ctx.send(f':no_entry: Nu ai permisiune de a folosi aceasta comanda!')
            return
        if isinstance(error, discord.ext.commands.MissingPermissions):
            await ctx.send(f':no_entry: YNu ai permisiunea de a folosi aceasta comanda!')
            return
        if isinstance(error, discord.ext.commands.BotMissingPermissions):
            await ctx.send(":no_entry: Botul nu are permisiunea.Te rugam sa contactezi Ownerul serverului pentru a rezolva eroarea!")
            await ctx.guild.owner.send(f':no_entry: Botul nu are permisiunea sa execute aceasta comanda!: {ctx.prefix}{ctx.name}, te rugam sa te asiguri ca botul are urmatoarea permisiune: `Administrator` sau urmatoarele permisiuni: `Manage messages`, `Add reactions`, `Read messages`, `Send messages`, `Read message history`, `Embed links` si `Attach file`')
            return

        await ctx.send(f'**`Eoare:`** Eroare la executarea comenzii! **{ctx.prefix}{ctx.command.qualified_name}**')
        await ctx.send(f'=========================================')
        await ctx.send(f'```{error}```')


def setup(bot):
    bot.add_cog(Developers(bot))