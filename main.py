import discord
import random
import asyncio
import time
import json
import operator
import io
import youtube_dl

from discord.ext import commands
from discord.utils import get
from datetime import datetime, timedelta
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, Select, SelectOption
from json.decoder import JSONDecodeError
from PIL import Image, ImageDraw, ImageFont

import keep_alive
import EmbedBot as EB
from DonneesBot import *
from FonctionsBot import *
from QuestionsBot import questions
from MusicsBot import Musics_Anime

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, help_command=None, intents=intents)
musics, musics2={}, {}
music_queue={}
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    # bind to ipv4 since ipv6 addresses cause issues sometimes
    'source_address': '0.0.0.0'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
DiscordComponents(client)

@client.event
async def on_ready() :
    time=datetime.now()
    print("------\nBot Connecté\nNirvaSan\n"+str(client.user.id)+"\nBot lancé le "+str(time.strftime("%d-%m-%Y à %H:%M:%S")+"\n------"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="=help"))

class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]
        self.title = video["title"]
        self.time = video["duration"]
        self.minia = video["thumbnail"]

@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount):
    if int(amount) > 100:
        await ctx.send("Vous ne pouvez pas supprimé plus de 100 messages en une fois !")
        return
    else:
        await ctx.channel.purge(limit=int(amount)+1)

@client.command()
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, prefix):
    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)

    for i in range(len(data["prefix"])):
        if list(data["prefix"][i].keys())[0] == str(ctx.guild.id):
            data["prefix"][i][str(ctx.guild.id)] = prefix
            break
    
    with open("ComplementBot.json", "w") as CompBot:
        json.dump(data, CompBot)

    await ctx.send(embed=discord.Embed(title=f"Le nouveau préfix est {prefix}"))

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def help(ctx) :
    emojiFromServer = client.get_emoji(874278287143223326)
    emojiFromServer2 = client.get_emoji(874279294296293387)
    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)
    for i in range(len(data["prefix"])):
        if list(data["prefix"][i].keys())[0] == str(ctx.message.guild.id):
            prefixe = data["prefix"][i][str(ctx.guild.id)]
            break
    embed=discord.Embed(
        title="__**Liste des commandes**__",
        description=f"Prefix du bot = `{prefixe}` \n\n:partying_face: **Memes** : \n\n `hug`, `love`, `fight`, `kiss`, `kill`, `cry`, `highfive`, `shoot`, `sleep`, `slap`, `pat`\n\n:gear: **Commandes** : \n\n `pp`, `invite`\n\n:notes: **Musique** : \n\n `play`, `pause`, `resume`, `skip`, `queue`, `leave`\n\n:game_die: **Mini-Jeux** : \n\n `QuizzAnime`, `BlindTest`, `pendu`\n\n:tools: **Modération** (Staff Only) : \n\n `kick`, `kick_except`, `ban`, `unban`, `mute`, `tempmute`, `unmute`, `clear`, `AuGoulag`, `SorsDuGoulag`\n\n:computer: **Serveur** (Staff Only) : \n\n `set_welcome_message`, `del_welcome_message`, `poll`, `prefix`",
        colour=random_color())
    await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.blue, label="Envoyer la liste détaillée", emoji=emojiFromServer2), Button(style=ButtonStyle.URL, label="Serveur d'Assistance", emoji=emojiFromServer, url="https://discord.gg/eJ4W2tQSKM")]])

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def sleep(ctx):
    embed=discord.Embed(
        title="**Ronpichhhhhh**",
        description="<@!"+str(ctx.message.author.id)+">"+" est en train de dodo",
        colour=random_color())
    embed.set_image(url=random.choice(GifSleep))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def love(ctx):
    txt=["envoie de l'amour à", "à l'air de s'aimer"]
    embed=discord.Embed(
        title="**Moooooh trop mimi**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifLove))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def fight(ctx):
    txt=["veut se battre avec", "cherche des gens sur qui taper"]
    embed=discord.Embed(
        title="**Tu cherches la bagarre ?**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifFight))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def hug(ctx):
    txt=["fait un câlin à", "cherche quelqu'un pour faire un câlin"]
    embed=discord.Embed(
        title="**Ah ouai trop cute**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifHug))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def kill(ctx):
    txt=["vient de tuer", "ne sais plus qui tué(e)"]
    embed=discord.Embed(
        title="**Il l'a vraiment tuer !**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifKill))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def cry(ctx):
    txt=["pleure à cause de", "pleure de toutes ses larmes"]
    embed=discord.Embed(
        title="**Mooh, mon p'tit chou !**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifCry))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def highfive(ctx):
    txt=["fais un check à", "cherche désespérément un ami"]
    embed=discord.Embed(
        title="**Tape m'en cinq !**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifHighfive))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def shoot(ctx):
    txt=["vient de tirer sur", "a l'oeil fixé dans son viseur"]
    embed=discord.Embed(
        title="**Et c'est le headshot !**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifShoot))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def slap(ctx):
    txt=["met une claque à", "cherche à qui il va mettre sa claque ?"]
    embed=discord.Embed(
        title="**Allez, la p'tite fessée**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifSlap))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def kiss(ctx):
    txt=["fais un p'tit kiss à", "se demande à qui il peut faire des bisous"]
    embed=discord.Embed(
        title="**Un p'tit bisou ?**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifKiss))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def pat(ctx):
    txt=["offre un peu de réconfort à", "a besoin de papouilles"]
    embed=discord.Embed(
        title="**Olololo, too much cute**",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=random.choice(GifPat))
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def pp(ctx):
    txt=["voici la photo de profil de", "voici votre photo de profil"]
    if len(ctx.message.content.split(" "))==1:
        img=ctx.message.author.avatar_url
    else:
        user=ctx.message.mentions[0]
        img=user.avatar_url
    embed=discord.Embed(
        title=":camera: **P'tit Curieux** :camera:",
        description=good_desc(ctx, txt),
        colour=random_color())
    embed.set_image(url=img)
    await ctx.send(embed=embed)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    user=ctx.message.mentions[0]
    await ctx.channel.purge(limit=1)
    if member.guild_permissions.kick_members:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+"> , je ne peux pas kick cet utilisateur.")
    else:
        if reason==None:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as kick **"+str(member)+"**")
            await user.send("<:pepegun:760984750172799046> Tu as été kick de "+ctx.message.guild.name)
        else:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as kick **"+str(member)+"**, pour la raison suivante : *"+reason+"*")
            await user.send("<:pepegun:760984750172799046> Tu as été kick de "+ctx.message.guild.name+"pour la raison suivante : *"+reason+"*")
        await member.kick(reason=reason)

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    user=ctx.message.mentions[0]
    await ctx.channel.purge(limit=1)
    if member.guild_permissions.ban_members:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+"> , je ne peux pas ban cet utilisateur.")
    else:
        if reason==None:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as ban **"+str(member)+"**")
            try:
                await user.send("<:pepegun:760984750172799046> Tu as été ban de "+ctx.message.guild.name)
            except:
                pass
        else:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as ban **"+str(member)+"**, pour la raison suivante : *"+reason+"*")
            try:
                await user.send("<:pepegun:760984750172799046> Tu as été ban de "+ctx.message.guild.name+"pour la raison suivante : *"+reason+"*")
            except:
                pass
        await member.ban(reason=reason)

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(pass_context=True)
@commands.has_guild_permissions(ban_members=True)
async def kick_except(ctx, role: discord.Role, *, reason=None):
    for member in ctx.guild.members:
        if role in member.roles:
            pass
        else:
            if member.guild_permissions.kick_members:
                pass
            else:
                try:
                    await member.send(f"Yo {str(member)}, tu as été kick de {ctx.message.guild.name} pour cause d'inactivité, car nous avons décidé de faire un tri parmis nos membres, afin de reprendre une vraie activité sur le serveur")
                except discord.Forbidden:
                    pass
                await member.kick(reason=reason)
    await ctx.send("Tout les membres n'ayant pas le grade "+str(role.name)+" ont été expulsés")

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(mute_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = await verifMutedRole(ctx.guild)
    await ctx.channel.purge(limit=1)
    if muted_role in member.roles:
        await ctx.send("<:clown_pepe:760985925274042369> Cet utilisateur est déjà mute !")
    elif member.guild_permissions.mute_members:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+"> , je ne peux pas mute cet utilisateur.")
    else:
        if reason==None:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as mute **"+str(member)+"**")
        else:
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as mute **"+str(member)+"**, pour la raison suivante : *"+reason+"*")
        await member.add_roles(muted_role, reason=reason)
        try:
            await member.edit(mute=True)
        except:
            pass

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(mute_members=True)
async def tempmute(ctx, member: discord.Member, *, timer, reason=None):
    muted_role = await verifMutedRole(ctx.guild) 
    try:
        time=int(timer[:-1])
    except:
        raise commands.MissingRequiredArgument()
    lettersList = ['s','m','h','j']
    nbList = [1,60,3600,86400]
    if timer[-1] not in lettersList:
            await ctx.send("<:meine:760984967840530446> Veuillez renseigner un des paramètres suivants ( s / m / h / j )")
    elif muted_role in member.roles:
        await ctx.send("<:clown_pepe:760985925274042369> Cet utilisateur est déjà mute !")
    elif member.guild_permissions.mute_members:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+"> , je ne peux pas mute cet utilisateur.")
    else:
        for i in range(4):
            if timer[-1] == lettersList[i]:
                await member.add_roles(muted_role, reason=reason)
                try:
                    await member.edit(mute=True)
                except:
                    pass
                await asyncio.sleep(time*nbList[i])
                try:
                    await member.remove_roles(muted_role)
                    await member.edit(mute=False)
                except:
                    pass

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(mute_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role=discord.utils.get(ctx.message.guild.roles, name="Muted")
    await ctx.channel.purge(limit=1)
    if not muted_role in member.roles:
        await ctx.send("<:clown_pepe:760985925274042369> Cet utilisateur n'est pas mute !")
    elif member.guild_permissions.mute_members:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+"> , je ne peux pas unmute cet utilisateur.")
    else:
        await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as unmute **"+str(member)+"**")
        await member.remove_roles(muted_role)
        try:
          await member.edit(mute=False)
        except:
          pass

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, id:int):
    await ctx.channel.purge(limit=1)
    user_unban=False
    member = await client.fetch_user(id)
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = str(member).split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("<:pepegun:760984750172799046> <@!"+str(ctx.message.author.id)+"> tu as unban **"+str(user)+"**")
            await user.send("<:pepegun:760984750172799046> Tu as été unban de "+ctx.message.guild.name)
            user_unban=True
    if user_unban==False:
        await ctx.send("<:clown_pepe:760985925274042369> <@!"+str(ctx.message.author.id)+">, cet utilisateur n'est pas dans la liste des bannis")

@client.command()
async def invite(ctx):
    embed=discord.Embed(
        description="Si vous voulez inviter ce bot sur votre serveur, [cliquez sur ce lien](https://discord.com/api/oauth2/authorize?client_id=783390079770034186&permissions=8&scope=bot)",
        color=random_color())
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_guild_permissions(manage_messages=True)
async def poll(ctx):
    values=[]
    options={}
    message=await ctx.send(embed=EB.embed_channel_sondage, components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=True)]])
    emote=["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    ListEmbed=[EB.embed_title_sondage, EB.embed_description_sondage, EB.embed_timer_sondage, EB.embed_image_sondage, EB.embed_options_sondage]
    global fautpassarreter
    global state
    state=""
    fautpassarreter = True
    for i in range(6):
        if fautpassarreter == True:
            try:
                donnee=await client.wait_for("message", check=lambda m: (m.author == ctx.author or (m.content == "ㅤ" and m.author == client.user)) and m.channel == ctx.channel, timeout=180.0)
                if state=="skip":
                    donnee.content=""
                    state=""
                if i==0 and donnee.content!="ㅤ":
                    try:
                        entree_channel=client.get_channel(int(donnee.content))
                        if entree_channel == None :
                          await ctx.send(embed=EB.embed_erreur_channel) 
                          await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                          return
                    except:
                        await ctx.send(embed=EB.embed_erreur_channel) 
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                elif i==2 and donnee.content!="ㅤ":
                    await message.edit(components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=False)]])
                elif i==3 and donnee.content!="ㅤ" and donnee.content!="":
                    try:
                        int(donnee.content)
                        assert donnee.content >= 1
                        donnee.content=int(donnee.content)*3600
                    except:
                        await ctx.send(embed=EB.embed_erreur_channel) 
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return  
                elif i==4 and donnee.content!="ㅤ" and donnee.content!="":
                    if (donnee.content[0:8]!="https://" or (donnee.content[-4:]!=".gif" and donnee.content[-4:]!=".png" and donnee.content[-4:]!=".jpg" and donnee.content[-5:]!=".jpeg")) and donnee.content!="skip":
                        embed_error_image=discord.Embed(description="Veuillez mettre un lien d'image/gif valable (n'oubliez pas l'extension)")
                        await ctx.send(embed=embed_error_image)
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                    await message.edit(components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=True)]])
                elif i==5 and donnee.content!="ㅤ":
                    try:
                        assert int(donnee.content)>=2 and int(donnee.content)<=10
                    except AssertionError:
                        await ctx.send(embed=EB.embed_erreur_channel) 
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                values.append(donnee)
            except asyncio.TimeoutError:
                await ctx.send(embed=EB.embed_erreur_time)
                return
            if fautpassarreter == True:
                await ctx.channel.purge(limit=1)
                if i!=5:
                    await message.edit(embed=ListEmbed[i])
    if fautpassarreter == True:
        for i in range(int(values[5].content)):

            embed=discord.Embed(
                description="Veuillez donner votre option n°"+str(i+1)+".",
                color=random_color())
            await message.edit(embed=embed)

            try:
                options[emote[i]]=(await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=120.0)).content
                await ctx.channel.purge(limit=1)
            except asyncio.TimeoutError:
                await ctx.send(embed=EB.embed_erreur_time)
                return   

        diff_options=[]
        for i in list(options.values()):
            diff_options.append(i)
        embed_full=discord.Embed(
            title=values[1].content,
            description=values[2].content+"\nㅤ",
            color=random_color())
        for i in range(int(values[5].content)):
            embed_full.add_field(name="ㅤ", value=" "+emote[i]+" "+diff_options[i], inline=False)
        if values[4].content!="":
            embed_full.set_image(url=values[4].content)

        entree_channel=client.get_channel(int(values[0].content))
        await message.edit(embed=EB.embed_fini_sondage, components=[[Button(style=ButtonStyle.blue, label="Sondage intialisé", disabled=True)]])
        poll = await entree_channel.send(embed=embed_full)
        for i in range(int(values[5].content)):
            await poll.add_reaction(emote[i])

        if values[3].content!="":
            await asyncio.sleep(int(values[3].content))

            cache_msg = discord.utils.get(client.cached_messages, id=poll.id)
            reactions = cache_msg.reactions
            present_reactions = []
            counter = {}
            for reaction in reactions:
                if reaction not in present_reactions:
                    present_reactions.append(reaction)
                    nombre = (reaction.count)-1
                    counter[reaction.emoji] = nombre
            
            await poll.clear_reactions()
            nb=[]
            for element in counter.values():
                if element==counter[max(counter, key=counter.get)]:
                    nb.append(element)
            key_list=[k for (k, val) in counter.items() if val==max(nb)]
            if len(nb)==1:
                embed_result=discord.Embed(
                    title="Voici les résultats de votre sondage :",
                    description="*Le choix qui gagne ce sondage est : **"+str(options[key_list[0]])+"** avec **"+str(counter[key_list[0]])+"** vote(s)*\n\nPour rappel, la question était : "+values[1].content,
                    color=random_color())
            else:
                opt=[]
                for i in range(len(key_list)):
                    opt.append(options[key_list[i]])
                respons=" / ".join(opt)
                embed_result=discord.Embed(
                    title="Voici les résultats de votre sondage :",
                    description="*Egalité entre les réponses : **"+respons+"** avec **"+str(max(nb))+"** vote(s)*\n\nPour rappel, la question était : "+values[1].content,
                    color=random_color())
            embed_result.set_footer(text="Merci d'avoir voté")
            await poll.edit(embed=embed_result)

    elif fautpassarreter == False:
        embed_exit=discord.Embed(description=":warning: Commande abandonnée :warning:")
        await message.edit(embed=embed_exit, components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
        return

@client.command(pass_context=True)
@commands.has_guild_permissions(manage_guild=True)
async def set_welcome_message(ctx):
    message= await ctx.send(embed=EB.embed_channel, components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=True)]])
    values=[]
    ListEmbed=[EB.embed_titre, EB.embed_description, EB.embed_color, EB.embed_image, EB.embed_footer, EB.embed_fini]
    global fautpassarreter
    global state
    state=""
    fautpassarreter = True
    for i in range(6):
        if fautpassarreter == True:
            try:
                donnee=await client.wait_for("message", check=lambda m: (m.author == ctx.author or (m.content == "ㅤ" and m.author == client.user)) and m.channel == ctx.channel, timeout=180.0)
                if state=="skip":
                    donnee.content=""
                    state=""
                if i==0 and donnee.content!="ㅤ":
                    try:
                        entree_channel=client.get_channel(int(donnee.content))
                        if entree_channel == None :
                          await ctx.send(embed=EB.embed_erreur_channel) 
                          await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                          return
                    except:
                        await ctx.send(embed=EB.embed_erreur_channel) 
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                    await message.edit(components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=False)]])
                elif i==2:
                    await message.edit(components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=True)]])
                elif i==3 and donnee.content!="ㅤ":
                    try:
                        donnee.content=int(donnee.content)
                        assert donnee.content <= 16777215
                    except:
                        await ctx.send(embed=EB.embed_erreur_channel) 
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                    await message.edit(components=[[Button(style=ButtonStyle.red, label="Annuler la commande"), Button(style=ButtonStyle.blue, label="Skip", disabled=False)]])
                elif i==4 and donnee.content!="" and donnee.content!="ㅤ":
                    if (donnee.content[0:8]!="https://" or (donnee.content[-4:]!=".gif" and donnee.content[-4:]!=".png" and donnee.content[-4:]!=".jpg" and donnee.content[-5:]!=".jpeg")):
                        embed_error_image=discord.Embed(description="Veuillez mettre un lien d'image/gif valable (n'oubliez pas l'extension)")
                        await ctx.send(embed=embed_error_image)
                        await message.edit(components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
                        return
                elif i==5 and donnee.content!="ㅤ":
                    await message.edit(components=[[Button(style=ButtonStyle.blue, label="Message intialisé", disabled=True)]])
                values.append(donnee)
            except asyncio.TimeoutError:
                await ctx.send(embed=EB.embed_erreur_time)
                return
            if fautpassarreter == True:
                await ctx.channel.purge(limit=1)
                await message.edit(embed=ListEmbed[i])
    if fautpassarreter == True:
        embed_complet=[values[1].content, values[2].content, str(values[3].content), values[5].content, str(values[4].content), values[0].content]
        try:
            with open("ComplementBot.json", "r") as CompBot:
                data = json.load(CompBot)
        except:
            data={}

        data["welcome"].append({ctx.guild.id: embed_complet})

        with open("ComplementBot.json", "w") as CompBot:
            json.dump(data, CompBot)

    elif fautpassarreter == False:
        embed_exit=discord.Embed(description=":warning: Commande abandonnée :warning:")
        await message.edit(embed=embed_exit, components=[[Button(style=ButtonStyle.gray, label="Annulé", disabled=True)]])
        return

@client.command()
@commands.has_guild_permissions(manage_guild=True)
async def del_welcome_message(ctx):
    find=False
    embed=discord.Embed(
      title = "Vous êtes sur le point de supprimer la fonctionnalité de message de bienvenue sur votre serveur.",
      description = "Afin de confirmer votre choix, veuillez cliquer sur 'Confirmer', dans le cas contraire, cliquez sur 'Annuler'.",
      color = 12845619)
    message = await ctx.send(embed=embed, components=[[Button(style=ButtonStyle.green, label="Confirmer"), Button(style=ButtonStyle.red, label="Annuler")]])

    res = await client.wait_for("button_click", check=lambda m: m.channel == ctx.channel and m.author == ctx.author)
    if res.component.label == "Annuler":
        await ctx.send("Commande annulée.")
        await message.edit(components=[[Button(style=ButtonStyle.green, label="Confirmer", disabled=True), Button(style=ButtonStyle.red, label="Annuler", disabled=True)]])
    elif res.component.label == "Confirmer":
        with open("ComplementBot.json", "r") as CompBot:
            data = json.load(CompBot)
        for i in range(len(data["welcome"])):
            if list(data["welcome"][i].keys())[0] == str(ctx.guild.id):
                del data["welcome"][i]
                find=True
                break
        if find:
          with open("ComplementBot.json", "w") as CompBot:
              json.dump(data, CompBot)
          await ctx.send("Fonctionnalité supprimée.")
        else:
            await ctx.send("Vous n'aviez pas de message de bienvenue d'initialisé.")
        await message.edit(components=[[Button(style=ButtonStyle.green, label="Confirmer", disabled=True), Button(style=ButtonStyle.red, label="Annuler", disabled=True)]])

@client.command()
async def SondageFilm(ctx, nb_films:int, channel:discord.TextChannel):
    if nb_films>10:
        await ctx.send("Veuillez ne pas dépasser la limite des 10 paramètres, Merci !")
        return

    titles=[]
    desc=[]
    emote=["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    nb=["premier", "deuxième", "deuxième", "troisième", "troisième", "quatrième", "quatrième", "cinquième", "cinquième", "sixième", "sixième", "septième", "septième", "huitième", "huitième", "neuvième", "neuvième", "dizième", "dizième"]
    entree_channel=client.get_channel(channel.id)
    
    message = await ctx.send("Tu es prêt ?! C'est partiiiii")
    await asyncio.sleep(3)

    for i in range(nb_films*2):

        embed_title=discord.Embed(
            title="Titre du Film/Série",
            description=f"\nVeuillez renseigner le titre du {nb[i]} film/série que vous souhaitez proposer",
            color=14942328)
        embed_title.set_footer(text="Merci !")
        embed_title.set_thumbnail(url="https://imgur.com/897BM12.png")
        embed_desc=discord.Embed(
            title="Résumé du Film/Série",
            description=f"\nVeuillez donner le résumé du {nb[i]} film/série que vous voulez proposer",
            color=13238245)
        embed_desc.set_footer(text="Merci !")
        embed_desc.set_thumbnail(url="https://imgur.com/YTWOJYV.png")

        if i == 0:
            await message.edit(text=" ", embed = embed_title)
        
        try:
            donnee = await client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=180.0)
            if i % 2 == 0:
                titles.append(donnee.content.lower())
                await message.edit(embed=embed_desc)
            else:
                desc.append(donnee.content)
                await message.edit(embed=embed_title)
        except asyncio.TimeoutError:
                await ctx.send(embed=embed_erreur_time)
                return

        if i == (nb_films*2)-1:
            await message.delete()

    embed_final=discord.Embed(
        title="**Cinema de FullBurn !**\nㅤ",
        description=f"Nous vous proposons {nb_films} films/séries à l'affiche pour la soirée de lundi, voter pour votre film/série favoris, si il est sélectionné il sera diffusé Lundi 26 Avril à 22H00 en stream dans le salon <#830884830350409759>\nㅤ",
        color=16656146)
    embed_final.set_footer(text="Veuillez sélectionner le chiffre du film de votre choix.", icon_url="https://imgur.com/si32vRT.png")
    embed_final.set_thumbnail(url="https://imgur.com/wepnVXg.png")
    for i in range(nb_films):
        embed_final.add_field(name=emote[i]+" "+titles[i].capitalize(), value=desc[i].capitalize()+"\nㅤ", inline=False)
    await entree_channel.send(embed=embed_final)

@client.command()
async def select(ctx):
    await ctx.send(
        "Hello, World!",
        components=[
            Select(
                placeholder="select something!",
                options=[SelectOption(label="a", value="A"), SelectOption(label="b", value="B")],
                disabled=False,
            )
        ],
    )

    interaction = await client.wait_for("select_option")
    await interaction.respond(content=f"{interaction.component[0].label} selected!")


@client.command(pass_context=True)
async def botservers(ctx):
    bot = 0
    if ctx.author.id == 401448502657417228:
        servers = " / ".join(["**"+i.name+"**" for i in client.guilds])
        embed = discord.Embed(
            title="I'm in " + str(len(client.guilds)) + " servers",
            description=servers,
            color=16224167)
        await ctx.send(embed=embed)
    else:
        raise commands.MissingPermissions("administrator")

@client.command(aliases=["quizzanime", "Quizzanime"])
async def QuizzAnime(ctx, nb_quest:int, time_question="", type_question="normal"):
    if time_question=="easy" or time_question=="normal" or time_question=="hard":
        type_question=time_question
        time_question=60
    elif time_question=="":
        time_question=60
    diff_quest=[]
    question=""
    score={}
    for i in range(nb_quest+1):
        while question in diff_quest:
            question=random.choice(list(questions[str(type_question.lower())].keys()))
        diff_quest.append(question)
    del diff_quest[0]
    for i in range(nb_quest):
        l=["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
        message = await ctx.send(l[-1])
        await asyncio.sleep(1)
        for j in range(4):
            await message.edit(content=l[-j-2])
            await asyncio.sleep(1)
        question=discord.Embed(description=diff_quest[i], color=random_color())
        await message.edit(content=" ", embed=question)
        good=True
        while good==True:
            try:
                answer=await client.wait_for("message", check=lambda m: m.channel == ctx.channel, timeout=int(time_question))
                for reponse_attendu in questions[str(type_question.lower())][diff_quest[i]]:
                    if reponse_attendu in answer.content.lower():
                        await ctx.send(f"ouais, ouais, ouais et c’est gagné {answer.author.mention} ! La bonne réponse était : {questions[str(type_question.lower())][diff_quest[i]][0].capitalize()}")
                        if answer.author.name not in score.keys():
                            score[answer.author.name]=1
                        else:
                            score[answer.author.name]+=1
                        good=False
            except asyncio.TimeoutError:
                embed=discord.Embed(
                    description=f"Eheh, temps écoulé les noobs, le réponse était {questions[str(type_question.lower())][diff_quest[i]][0].capitalize()} !",
                    color=random_color())
                await ctx.send(embed=embed)
                good=False

    if score!={}:
        nb=[]
        for element in score.values():
            if element==score[max(score, key=score.get)]:
                nb.append(element)
        key_list=[k for (k, val) in score.items() if val==max(nb)]
        if len(nb)==1:
            titre="Le gagnant de ce quizz est **"+key_list[0]+"** !"
        else:
            liste_gagnants=" & ".join(key_list)
            titre="Les gagnants de ce quizz sont **"+liste_gagnants+"** !"
        embed=discord.Embed(
            title=titre,
            description="Les résultats sont :\n",
            color=random_color())
        embed.set_image(url="https://imgur.com/gUtnwMP.gif")
        embed.set_footer(text="Merci de votre participation !")
        for i in range(len(score.keys())):
            embed.add_field(name=str(list(score.keys())[i])+" :", value="➜ Avec "+str(list(score.values())[i])+" point(s).", inline=False)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(
            description="Aucun point n'ont été marqués dans cette partie !",
            color=random_color())
        await ctx.send(embed=embed)

@client.command()
async def pendu(ctx, type_jeu:str):
    mot_a_trouver = choisir_mot(type_jeu)
    lettres_trouvees = ["ㅤ"]
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    compteur=0
    lettre_donnees=[]
    good_word=mot_a_trouver.replace("ㅤ", " ")
    while mot_a_trouver!=mot_trouve and nb_chances>0:
        lettre=""
        embed=discord.Embed(
            title="Mot à trouver",
            description=mot_trouve,
            color=random_color())
        embed.set_footer(text="(encore {0} chances)".format(nb_chances))
        if compteur==0:
            message=await ctx.send(embed=embed)
        else:
            embed.add_field(name="ㅤ", value="*Dernière lettre donnée : **"+lettre_donnees[-1]+"***", inline=False)
            await message.edit(embed=embed)
        while (len(lettre)>1 or (not lettre.isalpha() and lettre!=" ")) and lettre!=good_word:
            await asyncio.sleep(1)
            try:
                letter = await client.wait_for("message", check=lambda m: m.channel == ctx.channel, timeout=120.0)
                await ctx.channel.purge(limit=1)
            except asyncio.TimeoutError:
                raise commands.CommandInvokeError
            lettre = letter.content.lower()
        if len(lettre)>1:
            if lettre==good_word:
                mot_trouve=mot_a_trouver
        else:
            if (lettre in lettres_trouvees) or (lettre in lettre_donnees):
                await message.edit(content="\nVous avez déjà choisi la lettre **"+lettre+"** "+letter.author.mention+".")
            elif lettre in mot_a_trouver:
                lettres_trouvees.append(lettre)
                await message.edit(content="\nBien joué "+letter.author.mention+", il y a bien la lettre **"+lettre+"**")
            else:
                nb_chances -= 1
                await message.edit(content="\n... eh non "+letter.author.mention+", la lettre **"+lettre+"** ne se trouve pas dans le mot...")
            lettre_donnees.append(lettre)
            compteur+=1
            mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)

    if mot_a_trouver==mot_trouve:
        embed_win=discord.Embed(
            description=f"\nFélicitations {letter.author.mention} ! Vous avez trouvé le mot **{good_word.capitalize()}**. Tu es donc bien un vrai otaku, vous l'avez fait en **{str(compteur)}** essai(s)",
            color=random_color())
        await message.edit(embed=embed_win, content="")
    else:
        embed_fail=discord.Embed(
            description="\nPENDU !!! Vous avez échoué à votre mission. Le mot était *{0}*, ce sera pour une prochaine fois !".format(good_word.capitalize()),
            color=random_color())
        await message.edit(embed=embed_fail, content="")

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(aliases=["augoulag", "Augoulag"])
@commands.has_permissions(ban_members=True)
async def AuGoulag(ctx, member: discord.Member, *, timer=None):
    addRoles=[]
    i_d=[]
    goulag_role=discord.utils.get(ctx.message.guild.roles, name="Au Goulag")
    lettersList = ['s','m','h','j']
    nbList = [1,60,3600,86400]

    if goulag_role==None:
        await ctx.send("Futur Explication de comment créer le goulag si ce n'est pas fait")
    elif ctx.guild.me.top_role.position<=member.top_role.position:
        await ctx.send(f"<:clown_pepe:760985925274042369> {ctx.message.author.mention} , je ne peux pas envoyer cet utilisateur au goulag, il est trop puissant.")
    elif timer==None:
        for j in member.roles:
            try:
                await member.remove_roles(j)
                i_d.append(j.name)
            except:
                pass
        await member.add_roles(goulag_role)
        try:
            await member.send("<:goulag:854484832356270120> Tu as été envoyé au goulag de la part de Staline (non je rigole c'est "+str(ctx.author)+") ")
        except:
            pass
        try:
            with open("ComplementBot.json", "r") as CompBot:
                data = json.load(CompBot)
        except:
            data={}

        data["goulag"].append({member.id: i_d})

        with open("ComplementBot.json", "w") as CompBot:
            json.dump(data, CompBot)

    elif timer[-1] not in lettersList:
        await ctx.send("<:meine:760984967840530446> Veuillez renseigner un des paramètres suivants ( s / m / h / j )")
    else:
        try:
            time=int(timer[:-1])
        except:
            raise commands.MissingRequiredArgument()
        for i in range(4):
            if timer[-1] == lettersList[i]:
                for j in member.roles:
                    try:
                        await member.remove_roles(j)
                        addRoles.append(j.name)
                    except:
                        pass
                try:
                    with open("ComplementBot.json", "r") as CompBot:
                        data = json.load(CompBot)
                except:
                    data={}

                data["goulag"].append({member.id: addRoles})

                with open("ComplementBot.json", "w") as CompBot:
                    json.dump(data, CompBot)
                
                await member.add_roles(goulag_role)
                try:
                    await member.send("<:goulag:854484832356270120> Tu as été envoyé au goulag de la part de Staline (non je rigole c'est "+str(ctx.author)+") ")
                except:
                    pass
                await asyncio.sleep(time*nbList[i])
                try:
                    await member.remove_roles(goulag_role)
                    await member.add_roles(*addRoles)
                except:
                    pass

@commands.cooldown(1, 10, commands.BucketType.user)
@client.command(aliases=["sorsdugoulag", "Sorsdugoulag"])
@commands.has_permissions(ban_members=True)
async def SorsDuGoulag(ctx, member: discord.Member):
    addRoles=[]
    goulag_role=discord.utils.get(ctx.message.guild.roles, name="Au Goulag")
    try:
        with open("ComplementBot.json", "r") as CompBot:
            data = json.load(CompBot)
    except:
        return

    for i in range(len(data["goulag"])):
        if list(data["goulag"][i].keys())[0] == str(member.id):
            RolesList=list(data["goulag"][i].values())[0]
            data["goulag"].remove(data["goulag"][i])
            break

    with open("ComplementBot.json", "w") as CompBot:
            json.dump(data, CompBot)

    for i in RolesList:
        addRoles.append(discord.utils.get(ctx.message.guild.roles, name=i))
    await member.remove_roles(goulag_role)
    await member.add_roles(*addRoles)

    try:
        await member.send("<:shinobulaught:804795193614139473> Tu es enfin sorti du goulag, bon retour dans notre monde (Ton sauveur est "+str(ctx.author)+") ")
    except:
        pass

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def play(ctx, url):
    if not discord.utils.get(ctx.message.guild.roles, name="BlindTest"):
        client = ctx.guild.voice_client
        try:
            channel = ctx.author.voice.channel
        except AttributeError:
            embed_fail=discord.Embed(description="Veuillez vous connecter à un salon vocal pour lancer de la musique.")
            await ctx.send(embed=embed_fail)
            return

        if client and client.channel:
            if client.channel != channel:
                await ctx.send(f"Un utilisateur est actuellement en train d'écouter de la musique dans le channel {client.channel.mention}")
                return
            try:
              video = Video(url)
            except youtube_dl.utils.DownloadError:
              await ctx.send("Le lien n'est pas valable (droits d'auteur)")
              return
            await ctx.message.add_reaction("✅")
            musics[ctx.guild].append(video)
            music_queue[ctx.guild].append("**➜ "+video_time(video.time)+"** - "+video.title+"\n")
        else:
            client = await channel.connect()
            musics[ctx.guild] = []
            try:
              video = Video(url)
            except youtube_dl.utils.DownloadError:
              await ctx.send("Le lien n'est pas valable (droits d'auteur)")
              await client.disconnect()
              return
            music_queue[ctx.guild]= ["**➜ "+video_time(video.time)+"** - "+video.title+"\n"]
            await ctx.message.add_reaction("✅")
            play_song2(client, musics[ctx.guild], video, music_queue[ctx.guild])
    else:
        await ctx.send(f"{ctx.author.mention} Un BlindTest est en cours sur ce serveur !")

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def skip(ctx):
    if not discord.utils.get(ctx.message.guild.roles, name="BlindTest"):
        client = ctx.guild.voice_client
        try:
            channel = ctx.author.voice.channel
            if client.channel == channel:
                del music_queue[ctx.guild][0]
                client.stop()
            else:
                raise AttributeError
        except AttributeError:
            embed_fail=discord.Embed(description="Veuillez vous connecter au salon vocal pour passer une musique.")
            await ctx.send(embed=embed_fail)
            return
    else:
        await ctx.send(f"{ctx.author.mention} Un BlindTest est en cours sur ce serveur et vous ne pouvez pas le passer !")

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    try:
        channel = ctx.author.voice.channel
        if client.channel == channel:
            if not client.is_paused():
                client.pause()
        else:
            raise AttributeError
    except AttributeError:
        embed_fail=discord.Embed(description="Veuillez vous connecter au salon vocal pour mettre en pause une musique.")
        await ctx.send(embed=embed_fail)
        return

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    try:
        channel = ctx.author.voice.channel
        if client.channel == channel:
            if client.is_paused():
                client.resume()
        else:
            raise AttributeError
    except AttributeError:
        embed_fail=discord.Embed(description="Veuillez vous connecter au salon vocal pour remettre en route une musique.")
        await ctx.send(embed=embed_fail)
        return

@commands.cooldown(1, 2, commands.BucketType.user)
@client.command()
async def leave(ctx):
    if not discord.utils.get(ctx.message.guild.roles, name="BlindTest"):
        client = ctx.guild.voice_client
        try:
            channel = ctx.author.voice.channel
            if client.channel == channel:
                musics[ctx.guild]= []
                await client.disconnect()
                return
            else:
                raise AttributeError
        except AttributeError:
            embed_fail=discord.Embed(description="Veuillez vous connecter au salon vocal pour stopper la musique.")
            await ctx.send(embed=embed_fail)
            return
    else:
        await ctx.send(f"{ctx.author.mention} Un BlindTest est en cours sur ce serveur et vous ne pouvez pas le faire quitter !")

@commands.cooldown(1, 3, commands.BucketType.user)
@client.command()
async def queue(ctx):
    if not discord.utils.get(ctx.message.guild.roles, name="BlindTest"):
        client = ctx.guild.voice_client
        if client:
            queue = "\n".join([i for i in music_queue[ctx.guild]])
            embed = discord.Embed(
                description="Début de votre playlist.\n\n"+queue,
                color=16656146)
            await ctx.send(embed=embed)
        else:
            embed_fail=discord.Embed(description="Aucune musique n'a été lancée avec ce bot.")
            await ctx.send(embed=embed_fail)
    else:
        await ctx.send(f"{ctx.author.mention} Vous ne pouvez pas acceder à la liste des musiques du BlindTest.")

@client.command(aliases=["blindtest", "Blindtest"])
@commands.has_permissions(manage_messages=True, manage_roles=True, manage_channels=True)
async def BlindTest(ctx, nb_musics:int, extract_time=30):
    if not discord.utils.get(ctx.message.guild.roles, name="BlindTest"):
        player = 0
        start = False
        players = []
        musics2[ctx.guild] = []
        diff_music=[]
        musics=""
        for i in range(nb_musics+1):
            while musics in diff_music:
                musics = random.choice(list(Musics_Anime.keys()))
            diff_music.append(musics)
        del diff_music[0]
        client1 = ctx.guild.voice_client
        rules = await ctx.send(embed=EB.embed(ctx, client, player), components=[[Button(style=ButtonStyle.blue, label="Rejoindre le BlindTest"), Button(style=ButtonStyle.green, label="Lancer la partie"), Button(style=ButtonStyle.red, label="Annuler !")]])
        
        blindtestrole = await ctx.guild.create_role(name="BlindTest", color=14485512)
        overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
                blindtestrole: discord.PermissionOverwrite(read_messages=True, speak=False)
            }
        categoryChannel = await ctx.guild.create_category("BlindTest", position=0, overwrites=overwrites)
        channelResult = discord.utils.get(ctx.message.guild.channels, name="ʀᴇꜱᴜʟᴛᴀᴛꜱ-ʙᴛ")
        channelText = await ctx.guild.create_text_channel("ʙʟɪɴᴅ-ᴛᴇꜱᴛ", category=categoryChannel)
        channelVoc = await ctx.guild.create_voice_channel("ʙʟɪɴᴅ-ᴛᴇꜱᴛ", category=categoryChannel)
        if not channelResult:
            channelResult = await ctx.guild.create_text_channel("ʀᴇꜱᴜʟᴛᴀᴛꜱ-ʙᴛ", category=categoryChannel)
        else:
            await channelResult.edit(category=categoryChannel, sync_permissions=True)
        
        while start == False:
            try:
                res = await client.wait_for("button_click", check=lambda m: m.channel == ctx.channel and m.message == rules)
                if res.component.label == "Lancer la partie":
                    if res.author == ctx.author:
                        await channelText.send(f"{blindtestrole.mention}, la partie démarre dans quelques secondes ! C'est ici qu'il faut écrire les réponses !")
                        try:
                            client1 = await channelVoc.connect()
                        except:
                            pass
                        for url in diff_music:
                            video = Video(url)
                            musics2[ctx.guild].append(video)

                        await play_song(ctx, client1, musics2[ctx.guild], video, nb_musics, channelText, channelVoc, categoryChannel, blindtestrole, Musics_Anime, client, channelResult, extract_time)
                        start = True
                    else:
                        pass
                elif res.component.label == "Rejoindre le BlindTest":
                    member = res.guild.get_member(res.user.id)
                    if member not in players:
                        players.append(member)
                        await member.add_roles(blindtestrole)
                        player+=1
                        await rules.edit(embed=EB.embed(ctx, client, player))
                elif res.component.label == "Annuler !":
                    DeleteSomething(client, channelVoc)
                    DeleteSomething(client, channelText)
                    DeleteSomething(client, categoryChannel)
                    DeleteSomething(client, blindtestrole)
                    overwrites = {
                      ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),
                      ctx.guild.me: discord.PermissionOverwrite(read_messages=True)}
                    await channelResult.edit(overwrites=overwrites)
            except:
                pass
    else:
        await ctx.send(f"{ctx.author.mention} Un BlindTest est déjà en cours sur ce serveur !")
            
@client.event
async def on_button_click(res):
    if res.component.label == "Annuler la commande":
        global fautpassarreter 
        fautpassarreter = False
        await res.channel.send("ㅤ")
        await res.channel.purge(limit=1)
    elif res.component.label == "Skip":
        global state
        state = "skip"
        await res.channel.send("ㅤ")
    elif res.component.label == "Envoyer la liste détaillée":
        await res.user.send(embed=EB.embed_presentation)
        await res.user.send(embed=EB.embed_moderation)
        await res.user.send(embed=EB.embed_serveur)
        await res.user.send(embed=EB.embed_minijeux)
        await res.user.send(embed=EB.embed_musique)
        await res.user.send(embed=EB.embed_commandes)
        await res.user.send(embed=EB.embed_meme)

@client.event
async def on_guild_join(guild):
    channel=client.get_channel(867078841377095690)
    await channel.send(f"**{client.user.name}** à rejoint un nouveau serveur \n\nNom : {guild.name}\nID : {guild.id}\nMembres : {guild.member_count}\nFondateur : {guild.owner}ㅤ/ㅤ{guild.owner_id}")
    await verifMutedRole(guild)

    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)
    data["prefix"].append({str(guild.id): "="})
    with open("ComplementBot.json", "w") as CompBot:
        json.dump(data, CompBot)

@client.event
async def on_guild_remove(guild):
    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)

    for i in range(len(data["prefix"])):
        if list(data["prefix"][i].keys())[0] == str(guild.id):
            del data["prefix"][i]
            break
    
    with open("ComplementBot.json", "w") as CompBot:
        json.dump(data, CompBot)

@client.event
async def on_member_join(member):
    
    nb_bot = sum([1 for member in member.guild.members if member.bot == True])
    try:
        with open("ComplementBot.json", "r") as CompBot:
            data = json.load(CompBot)
    except FileNotFoundError:
        return
    
    for i in range(len(data["welcome"])):
        if list(data["welcome"][i].keys())[0] == str(member.guild.id):
            values = list(data["welcome"][i].values())[0]
            break

    for element in values:
        if '{member}' in element:
            values[values.index(element)]=element.replace('{member}', member.mention)
    for element in values:
        if '{member.count}' in element:
            values[values.index(element)]=element.replace('{member.count}', str(member.guild.member_count-nb_bot))
    for element in values:
        if '{member.created_at}' in element:
            values[values.index(element)]=element.replace('{member.created_at}', member.created_at.strftime("%d %B %Y"))

    embed=discord.Embed(
        title=values[0],
        description=values[1],
        colour=int(values[2]))
    if values[3]!="":
        embed.set_footer(text=values[3])
    if values[4]!="":
        embed.set_image(url=values[4])
    entree_channel=client.get_channel(int(values[5]))
    await entree_channel.send(embed=embed)

@client.event
async def on_command_error(ctx, error):

    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)
    for i in range(len(data["prefix"])):
        if list(data["prefix"][i].keys())[0] == str(ctx.message.guild.id):
            prefixe = data["prefix"][i][str(ctx.guild.id)]
            break

    if isinstance(error, commands.MissingPermissions):
        await ctx.send("<:pepesmile:828677897288024154> Vous n'avez pas les permissions pour effectuer cette commande !")
    
    elif isinstance(error, commands.CommandNotFound):
        pass

    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("<:pepesmile:828677897288024154> Je n'arrive pas à trouver cette utilisateur, soit vous l'avez mal mentionné, soit il ne se trouve pas sur ce serveur.")

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"<:nop:829138349511016478> Oh **{ctx.author.name}**, tout doux le loup, peux-tu patienter encore *{error.retry_after:.2f}s*. Merci :thumbsup:")

    else:
        Embed_Errors  = {
            "SondageFilm":EB.embed_SondageFilm(ctx, client, prefixe),
            "AuGoulag":EB.embed_AuGoulag(ctx, client, prefixe),
            "SorsDuGoulag":EB.embed_SorsDuGoulag(ctx, client, prefixe),
            "QuizzAnime":EB.embed_QuizzAnime(ctx, client, prefixe),
            "pendu":EB.embed_Pendu(ctx, client, prefixe),
            "tempmute":EB.embed_Tempmute(ctx, client, prefixe),
            "clear":EB.embed_Clear(ctx, client, prefixe),
            "kick_except":EB.embed_Kickexcept(ctx, client, prefixe),
            "play":EB.embed_Play(ctx, client, prefixe),
            "BlindTest":EB.embed_Blindtest(ctx, client, prefixe)}
        try:
            await ctx.send(embed=Embed_Errors[ctx.command.qualified_name])
        except KeyError:
            await ctx.send(embed=EB.embed_ErrorCMD(ctx, client, prefixe))

keep_alive.keep_alive()

client.run("TOKEN")
