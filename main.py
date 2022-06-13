import discord
from discord.ext import commands
import random
from random import randint
import asyncio

intents = discord.Intents.all()
intents.members = True

token = "OTc5NzA0MjExODQ1NTc0NzA3.GBWdL9.AOSp-xLZOZrPVXUva8nEAGmympNL5edkDgjIkI"
command_prefix = "!", "！"
bot = commands.Bot(command_prefix = command_prefix, intents = intents)
bot.remove_command("help")

@bot.event
async def on_ready():
  await bot.change_presence(status = discord.Status.dnd, activity = discord.Game(name = f"駐守伺服器:{len(bot.guilds)-2}\n!help"))
  print("Bot is online!")

@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(964706875557957685)
    Hi = await guild.text_channels[0].create_invite(dgs = True, max_age = 0, max_uses=0)
    await channel.send(Hi)

@bot.event
async def on_guild_remove(guild):
  Hi = await guild.text_channels[0].create_invite(dgs = True, max_age = 0, max_uses=0)
  channel = bot.get_channel(964707169255694336)
  await channel.send(Hi)

@bot.event
async def on_member_join(member):
  if member.guild.id == "982183316264452116":
    channel = bot.get_channel(982183316264452119)
    await channel.send(f"__歡迎訊息__\n{member.mention}, 歡迎加入{member.guild.name}!\n請到<#982185579326373918>查閱規則及按下☑️,謝謝合作。")

@bot.event
async def on_member_remove(member):
  if member.guild.id == "982183316264452116":
    channel = bot.get_channel(982184324415766598)
    await channel.send("__離開訊息__\n{member}已離開{member.guild.name}(;´༎ຶД༎ຶ`)\n希望你玩得開心,再見")

@bot.command()
async def help(ctx, msg = None):
  if msg == "mod":
    embed = discord.Embed(
      color = randint(0, 0xffffff),
      title = "管理員指令",
      description = "!clear[數值]_刪除訊息"
    )
    await ctx.reply(embed = embed, delete_after = 60)
    await asyncio.sleep(60)
    await ctx.message.delete()
  elif msg == "fun":
    embed = discord.Embed(
      color = randint(0, 0xffffff),
      title = "有趣指令",
      description = "!lucky_查看當天幸運指數"
    )
    await ctx.reply(embed = embed, delete_after = 60)
    await asyncio.sleep(60)
    await ctx.message.delete()
  else:
    embed = discord.Embed(
      color = randint(0, 0xffffff),
      title = "指令分類",
      description = "!help[分類ID]\n\n管理員指令_ID:mod\n有趣指令_ID:fun"
    )
    await ctx.reply(embed = embed, delete_after = 60)
    await asyncio.sleep(60)
    await ctx.message.delete()
    
@bot.command()
async def ping(ctx):
  embed = discord.Embed(
    color = randint(0, 0xffffff),
    description = f"狗勾延遲:\n{round(bot.latency*1000)}ms"
  )
  await ctx.reply(embed = embed, delete_after = 15)
  await asyncio.sleep(15)
  await ctx.message.delete()

@bot.command()
async def lucky(ctx):
  lucky = random.randint(0, 100)
  dgs = -1
  if lucky == 0:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"你真的想知道幸運指數嗎?emmmmm...抱歉,你的幸運指數只有很少qwq\n```diff\n-幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)
  elif lucky > dgs and lucky < 11:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"你今天的幸運指數不太好\n```diff\n-幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)
  elif lucky > 10 and lucky < 51:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"你沒過50所以不太好( ；´Д｀)\n```diff\n-幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)
  elif lucky > 50 and lucky < 81:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"很好的分數!\n```diff\n+幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)
  elif lucky > 80 and lucky < 100:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"你一定很喜歡的(除非你是抖M)\n```diff\n+幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)    
  elif lucky == 100:
    embed=discord.Embed(color=randint(0, 0xffffff), description=f"最高的幸運指數\n```diff\n+幸運指數:{lucky}%```")
    await ctx.reply(embed=embed)
  else:
    pass

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, num:int = None):
  if num == None:
    embed = discord.Embed(
      color = randint(0, 0xffffff),
      description = f"{ctx.author.mention}\n請打上數值!"
    )
    await ctx.reply(embed = embed)
  else:
    await ctx.channel.purge(limit=num+1)
    embed=discord.Embed(
      color=randint(0, 0xffffff),
      description=f"管理員[{ctx.author.mention}]已删除{num}條訊息。")
    await asyncio.sleep(0.1)
    await ctx.send(embed=embed, delete_after=10)

@clear.error
async def clear_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    embed = discord.Embed(
      color=randint(0, 0xffffff),      
      description="抱歉，你沒有理管訊息的權限。")
    await ctx.reply(embed = embed, delete_after = 10)
    await asyncio.sleep(10)
    await ctx.message.delete()

bot.run(token)
