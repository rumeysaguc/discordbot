import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def siberguvenliknedir(ctx):
    await ctx.send("Siber güvenlik; bilgisayarları, sunucuları, mobil cihazları, elektronik sistemleri, ağları ve verileri kötü amaçlı saldırılardan koruma uygulamasıdır. Bilgi teknolojisi güvenliği veya elektronik bilgi güvenliği olarak da bilinir. ")


@bot.command()
async def linuxnedir(ctx):
    await ctx.send("Linux, açık kaynaklı bir işletim sistemidir")

@bot.command()
async def beyazsapkalıhackernedir(ctx):
    await ctx.send("eyaz Şapkalı Hacker, bilişim suçları işleyen kötü niyetli kişilerin kullanmış oldukları teknik ve yöntemleri iyi bir şekilde öğrenmiş, siber korsanların eylemleri sırasında kullandıkları araçları ve yazılımları tanıyan, aynı bilgi ve beceriye sahip, iyi niyetli siber güvenlik güvenlik uzmanlarıdır. ")
  
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("GİZLİ TOKEN BURAYA")
