import discord
import random
import asyncio
from GifHug import *

class Bot(discord.Client):

    def __init__(self):
	       super().__init__()

    def random_color(self):
        hexa="0123456789abcdef"
        random_hex="0x"
        for i in range(6):
            random_hex+=random.choice(hexa)
        return discord.Colour(int(random_hex, 16))

    def create_embed(self, title, description, color, img):
        embed=discord.Embed()
        embed.title=title
        embed.description=description
        embed.colour=color
        if(img!=""):
            embed.set_image(url=img)
        return embed

    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        Membres=message.guild.members

        if(message.author==self.user):
            return

        if(message.content.startswith("-help")):
            color=self.random_color()
            description="Prefix du bot = `-` \n\n:partying_face: **Memes** : \n\n `-hug`, `-love`, `-fight`, `-kill`, `-cry`, `-highfive`, `-shoot`, `-sleep`, `-slap`, `etc` \n\n:underage: **NSFW** : \n\n `-fuck`, `-suck`, `etc`"
            embed=self.create_embed("**Liste des commandes**", description, color, "")
            await message.channel.send(embed=embed)

        if(message.content.startswith("-sleep")):
            color=self.random_color()
            description="<@!"+str(message.author.id)+">"+" est en train de dodo "
            img=random.choice(GifSleep)
            embed=self.create_embed("**Ronpichhhhhh**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-fight")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" se bat contre "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" se bat contre "+name
            color=self.random_color()
            description="<@!"+str(message.author.id)+">"+" se bat contre "+name
            img=random.choice(GifFight)
            embed=self.create_embed("**Que le plus fort gagne !**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-love")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" envoie de l'amour à "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" envoie de l'amour à "+name
            color=self.random_color()
            img=random.choice(GifLove)
            embed=self.create_embed("**Moooooh trop mimi**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-hug")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" fait un câlin à "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" fait un câlin à "+name
            color=self.random_color()
            img=random.choice(GifHug)
            embed=self.create_embed("**Ah ouai trop cute**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-kill")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" vient de tuer "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" vient de tuer "+name
            color=self.random_color()
            img=random.choice(GifKill)
            embed=self.create_embed("**Oh non, il est mort**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-cry")):
            command=message.content.split(" ")
            if(len(command)==2):
                name=command[1]
                description="<@!"+str(message.author.id)+">"+" pleure à cause de "+name
            if(len(command)==1):
                description="<@!"+str(message.author.id)+">"+" est en train de pleurer"
            color=self.random_color()
            img=random.choice(GifCry)
            embed=self.create_embed("**Oh mais non**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-highfive")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" Hey "+str(name)+", tope-là !"
            else:
                description="<@!"+str(message.author.id)+">"+" Hey "+name+", tope-là !"
            color=self.random_color()
            img=random.choice(GifHighfive)
            embed=self.create_embed("**Tape m'en cinq !**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-shoot")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" vient de tirer sur "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" vient de tirer sur "+name
            color=self.random_color()
            img=random.choice(GifShoot)
            embed=self.create_embed("**Aïe, je crois que ça fait mal**", description, color, img)
            await message.channel.send(embed=embed)

        if(message.content.startswith("-slap")):
            name=message.content.split(" ")[1]
            if name=="random":
                name=random.choice(Membres)
                description="<@!"+str(message.author.id)+">"+" met une claque à "+str(name)
            else:
                description="<@!"+str(message.author.id)+">"+" met une claque à "+name
            color=self.random_color()
            img=random.choice(GifSlap)
            embed=self.create_embed("**Allez, la p'tite fessée**", description, color, img)
            await message.channel.send(embed=embed)

if __name__ == "__main__":
    bot=Bot()
    bot.run("NzQwMTcxNzExNzQzMjYyNzgx.XylInw.xizvwRBGOOntHT-0ATj4Yff2b8I")
