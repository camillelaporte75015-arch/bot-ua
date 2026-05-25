import discord
from discord.ext import commands
import random
import asyncio

# ============ CONFIG ============
PREFIX = "-"
OWNER_ID = 1507830698743038122

# ============ GIFs ANIME (safe) ============
GIF_LIST = [
    "https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd459eaf877.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd459f14394.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd459f6d267.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd459fc75eb.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a02bca8.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a084d62.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a0ddb2f.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a1423d8.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a19b1cb.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a1f3e10.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a258610.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a2b141b.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a3168ea.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a36f3fd.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a3c845d.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a42b35a.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a484425.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a4dcad1.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a5415e3.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a598901.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a5f1ec8.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a656046.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a6af1aa.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a712990.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a769d40.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a7c1a1c.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a825a91.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a87d47b.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a938976.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a9903a5.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45a9e8c1f.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45aa4d0de.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45aaa711e.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ab0b8ee.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ab635cf.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45abbc4c0.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ac20f25.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ac786a5.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45acd0644.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ad346c7.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ad8c3fd.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ade45d4.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ae47e32.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45ae9f066.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45af02a47.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45af5b435.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45afb3c6c.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45b017ac6.gif",
"https://s2.pictoa.com/media/galleries/296/760/2967605ffd459cac8ec/38322265ffd45b070efd.gif",
"https://www.cougarillo.com/wp-content/uploads/2023/12/porno-hentai.gif",
"https://www.cougarillo.com/wp-content/uploads/2023/12/levrette-gif-hentai.gif",
"https://www.cougarillo.com/wp-content/uploads/2023/12/gif-hentai-gros-seins.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai145.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai125.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai143.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai129.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai119.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai127.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai122.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai120.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai141.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai139.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai140.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai114.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai123.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai115.gif",
"https://www.cougarillo.com/wp-content/uploads/2024/04/gif-hentai142.gif",
"https://img2.gelbooru.com//images/40/5f/405f442f0a5b6631821708238aed7d9a.gif",
"https://img2.gelbooru.com//images/32/44/324418be5fba84ca057ce3601b944292.gif",
"https://img2.gelbooru.com//images/70/09/7009626c5baad944ab31565e9509109a.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-41.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-40.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-39.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-38.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-37.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-36.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-35.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-34.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-32.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-30.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-29.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-28.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-27.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-25.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-24.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-23.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-22.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-21.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-20.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-19.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-18.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-17.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-16.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-15.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-14.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-13.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-12.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-11.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-10.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-9.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-7.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-6.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-5.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-4.gif",
"https://commentseduire.net/wp-content/uploads/2017/06/hentai-gif-1.gif",
 "https://wetgif.com/wp-content/uploads/hentai-1.gif",
 "https://m1.hentaiera.com/002/wrmde0u65c/1.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/2.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/3.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/4.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/5.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/6.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/7.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/8.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/9.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/12.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/13.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/15.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/17.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/18.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/19.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/20.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/21.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/22.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/23.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/24.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/25.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/26.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/28.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/30.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/31.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/32.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/33.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/34.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/35.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/36.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/37.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/38.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/39.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/40.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/41.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/42.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/43.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/44.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/45.gif",
    "https://m1.hentaiera.com/002/wrmde0u65c/46.gif",
    "https://m4.hentaiera.com/013/zbl8pwx6im/1.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/1.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/3.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/4.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/7.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/8.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/9.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/10.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/11.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/14.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/16.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/19.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/21.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/22.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/27.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/29.gif",
    "https://m2.hentaiera.com/009/wzchv6ndpy/30.gif"]

# ============ BOT SETUP ============
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

used_gifs = []


@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user}")
    print(f"Préfixe : {PREFIX}")


# ============ COMMANDE -ua ============
@bot.command(name="ua")
async def ua(ctx):
    global used_gifs

    # Supprime le message de commande
    try:
        await ctx.message.delete()
    except:
        pass

    # Si tous les GIFs ont été utilisés, on réinitialise
    if len(used_gifs) >= len(GIF_LIST):
        used_gifs = []
        notif = await ctx.send("🔄 Liste réinitialisée, on recommence !")
        await asyncio.sleep(5)
        await notif.delete()

    # Choisir un GIF pas encore utilisé
    remaining = [g for g in GIF_LIST if g not in used_gifs]
    chosen = random.choice(remaining)
    used_gifs.append(chosen)

    embed = discord.Embed(color=discord.Color.purple())
    embed.set_image(url=chosen)
    embed.set_footer(text=f"GIF {len(used_gifs)}/{len(GIF_LIST)} • Suppression dans 5s")

    msg = await ctx.send(embed=embed)

    # Suppression automatique après 5 secondes
    await asyncio.sleep(5)
    await msg.delete()


# ============ COMMANDE -play (owner only) ============
@bot.command(name="play")
async def play(ctx, *, activity: str = None):
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ Tu n'as pas la permission d'utiliser cette commande.")
        return

    if activity is None:
        await bot.change_presence(activity=None)
        await ctx.send("✅ Activité supprimée.")
        return

    game = discord.Game(name=activity)
    await bot.change_presence(activity=game)
    await ctx.send(f"✅ Le bot joue maintenant à **{activity}**.")


# ============ LANCEMENT ============
TOKEN = "METS_TON_TOKEN_ICI"
bot.run(TOKEN)
