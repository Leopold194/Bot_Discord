import discord
import random
from DonneesBot import *
import asyncio
import youtube_dl
import time
import json

ytdl = youtube_dl.YoutubeDL()


def random_color():
    hexa="0123456789abcdef"
    random_hex="0x"
    for i in range(6):
        random_hex+=random.choice(hexa)
    return discord.Colour(int(random_hex, 16))

def good_desc(ctx, txt):
    if len(ctx.message.content.split(" "))==1:
        description="<@!"+str(ctx.message.author.id)+"> "+txt[1]
        return description
    elif ctx.message.content.split(" ")[1]=="random":
        description="<@!"+str(ctx.message.author.id)+"> "+txt[0]+" <@!"+str(random.choice(ctx.guild.members).id)+">"
        return description
    else:
        user=(ctx.message.mentions[0]).id
        description="<@!"+str(ctx.message.author.id)+"> "+txt[0]+" <@!"+str(user)+">"
        return description

def choisir_mot(type_jeu):
    return random.choice(list_of_words[type_jeu.lower()])

def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque=""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            if lettre=="ㅤ":
                mot_masque += "ㅤ"
            else:
                mot_masque += lettre
        else:
            mot_masque += " ▁ "
    return mot_masque

global compteur
compteur = 0
global score
score = {}

async def play_song(ctx, client, queue, song, nb_musics, channelText, channelVoc, categoryChannel, blindtestrole, Musics_Anime, client1, channelResult, extract_time):
    global compteur
    global score
    compteur += 1
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
        , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))
    
    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            asyncio.run_coroutine_threadsafe(play_song(ctx, client, queue, new_song, nb_musics, channelText, channelVoc, categoryChannel, blindtestrole, Musics_Anime, client1, channelResult, extract_time), client.loop)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), client.loop)
    
    delta=time.time()
    client.play(source, after=next)
    play = True
    while play :
        try:
            respons = await client1.wait_for("message", check=lambda m: m.channel == channelText, timeout=extract_time)
            for reponses_attendues in Musics_Anime[song.url]:
                if reponses_attendues in respons.content.lower():
                    await channelText.send(f"Bravo {respons.author.mention} ! Tu as trouvé, la musique venait de {Musics_Anime[song.url][0].capitalize()} !")
                    if respons.author.name not in score.keys():
                        score[respons.author.name]=1
                    else:
                        score[respons.author.name]+=1
                    client.stop()
                    play=False
        except asyncio.TimeoutError:
            await channelText.send(f"La bonne réponse était : **{Musics_Anime[song.url][0].capitalize()}** ({song.url})")
            client.stop()
            play=False
    if compteur == nb_musics:
        queue = []
        compteur = 0
        if score!={}:
            nb=[]
            for element in score.values():
                if element==score[max(score, key=score.get)]:
                    nb.append(element)
            key_list=[k for (k, val) in score.items() if val==max(nb)]
            if len(nb)==1:
                titre="Le gagnant de ce BlindTest est **"+key_list[0]+"** !"
            else:
                liste_gagnants=" & ".join(key_list)
                titre="Les gagnants de ce BlindTest sont **"+liste_gagnants+"** !"
            embed=discord.Embed(
                title=titre,
                description="Les résultats sont :\n",
                color=random_color())
            embed.set_image(url="https://imgur.com/gUtnwMP.gif")
            embed.set_footer(text="Merci de votre participation !")
            for i in range(len(score.keys())):
                embed.add_field(name=str(list(score.keys())[i])+" :", value="➜ Avec "+str(list(score.values())[i])+" point(s).", inline=False)
            await channelResult.send(embed=embed)
        else:
            embed=discord.Embed(
                description="Aucun point n'ont été marqués dans cette partie !",
                color=random_color())
            await channelResult.send(embed=embed)
        score = {}

        await channelText.send(f"{blindtestrole.mention} Les salons consacrés au BlindTest vont se supprimés dans 30 secondes (excépté le salon ʀᴇꜱᴜʟᴛᴀᴛꜱ-ʙᴛ)")
        await asyncio.sleep(30)
        DeleteSomething(client, channelVoc)
        DeleteSomething(client, channelText)
        DeleteSomething(client, categoryChannel)
        DeleteSomething(client, blindtestrole)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True)}
        await channelResult.edit(overwrites=overwrites)

        return

async def verifMutedRole(guild):
    muted_role=discord.utils.get(guild.roles, name="Muted")
    if muted_role == None:
        await guild.create_role(name="Muted", colour=8487814)
        muted_role=discord.utils.get(guild.roles, name="Muted")
        overwrites = discord.PermissionOverwrite()
        overwrites.send_messages=False
        overwrites.add_reactions=False
        overwrites.speak=False
        for channel in guild.channels:
            await channel.set_permissions(muted_role, overwrite=overwrites)
        for categorie in guild.categories:
            await categorie.set_permissions(muted_role, overwrite=overwrites)
    return muted_role

def DeleteSomething(client, thing):
    asyncio.run_coroutine_threadsafe(thing.delete(), client.loop)

def play_song2(client, queue, song, list_queue):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
      , before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            del list_queue[0]
            play_song2(client, queue, new_song, list_queue)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), client.loop)
    client.play(source, after=next)
        

def sec2hms(ss):
    (hh, ss)=divmod(ss, 3600)
    (mm, ss)=divmod(ss, 60)
    return (hh, mm, ss)

def video_time(time):
    hh, mm, ss = sec2hms(time)
    if len(str(hh)) == 1:
        hh = f"0{hh}"
    if len(str(mm)) == 1:
        mm = f"0{mm}"
    if len(str(ss)) == 1:
        ss = f"0{ss}"    
    if hh != "00":
        return f"[{hh}:{mm}:{ss}]"
    else:
        return f"[{mm}:{ss}]"

def get_prefix(client, message):
    with open("ComplementBot.json", "r") as CompBot:
        data = json.load(CompBot)

    for i in range(len(data["prefix"])):
        if list(data["prefix"][i].keys())[0] == str(message.guild.id):
            prefixe = data["prefix"][i].values()
            break
    
    return prefixe
