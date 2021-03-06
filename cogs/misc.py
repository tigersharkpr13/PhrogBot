import discord
from discord.ext import commands


class misc(commands.Cog):
    """Misc commands for fun and some utilities"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def phrog(self, ctx):
        """Sends a picture of a phrog"""
        await ctx.message.delete(delay=1)
        url = 'https://cdn.discordapp.com/attachments/722691331339583551/722691369713270834/image0.png'
        await ctx.send(embed=discord.Embed(title="*P H R O G*", colour=0xFFAE00).set_image(url=url))

    @commands.command()
    async def cheems(self, ctx):
        """Sends a picture of cheems"""
        await ctx.message.delete(delay=1)
        url = 'https://i.imgur.com/HJfTbaY.png'
        await ctx.send(embed=discord.Embed(title="*C H E E M S*", colour=0xFFAE00).set_image(url=url))

    @commands.command()
    async def marv(self, ctx):
        """Sends a picture of a beloved pet"""
        await ctx.message.delete(delay=1)
        url = "https://i.imgur.com/wlJHI79.jpg"
        await ctx.send(
            embed=discord.Embed(title="*M A R V*", colour=0xFFAE00).set_image(url=url))

    @commands.command()
    async def phrogbomb(self, ctx):
        """A bunch of phrogs"""
        await ctx.message.delete(delay=1)
        url = 'https://i.imgur.com/MmoyMap.jpg'
        await ctx.send(embed=discord.Embed(title="*Le phrogge bombah*", colour=0xFFAE00).set_image(url=url))

    @commands.command(aliases=['me'])
    async def author(self, ctx: commands.Context):
        """Returns a greeting from the bot to the author, alias: 'me'"""
        await ctx.message.delete()
        await ctx.send(f'Hey {ctx.author}')

    @commands.command(aliases=['itn'])
    async def idtoname(self, ctx: commands.Context, userid: int):
        """Returns the name of the user using their id, alias: 'itn'"""
        await ctx.message.delete()
        user_nick = await self.bot.fetch_user(userid)
        await ctx.send(f'{userid} --> {user_nick}')

    @commands.command()
    async def clear(self, ctx, amount: int = 1):
        """Deletes messages from Inari
        e.g: $clear 10 (Will clear 10 messages belonging to Inari)"""
        await ctx.message.delete()
        msglist = []
        async for x in ctx.channel.history(limit=100):
            if x.author.id == self.bot.user.id:
                msglist.append(x)
        i = 0
        for msg in msglist:
            await msg.delete()
            i += 1
            if i >= amount:
                break
        msglist.clear()


def setup(bot):
    bot.add_cog(misc(bot))
