import discord
from FonctionsBot import *
from datetime import datetime, timedelta
import time
import json

#Set Welcome Message
embed_erreur_time=discord.Embed(
    title="Erreur :warning:",
    description="Le temps est écoulé, veuillez respecter le délai de 180 secondes",
    colour=15539236)

embed_channel=discord.Embed(
    title="**Étape 1/6**",
    description="ㅤ\nBienvenue à toi dans la création de message personnalisé de Bienvenue\n\nPour commencer, envoie moi l'ID du salon de Bienvenue\n*(Activez le mode développeur dans vos paramètres discord, dans la __catégorie avancés__ sur PC, et dans la __catégorie apparence__ sur téléphone, puis clique droit sur le channel, et 'copier l'identifiant')*",
    colour=3200456)
embed_channel.set_footer(text="De nombreuses informations, paramètres, exemples, etc se trouverons sur les screens des étapes suivantes, n'hésitez pas à cliquer dessus.")

embed_erreur_channel=discord.Embed(
	title="Erreur :warning:",
	description="Information incorrecte, veuillez donner une réponse valable",
	colour=15539236)

embed_titre=discord.Embed(
    title="**Étape 2/6**",
    description="ㅤ\nMaintenant, il me faut le titre\n*Ce qui est en haut de ton embed*",
    colour=3200456)
embed_titre.set_image(url="https://imgur.com/aQqzVFR.png")

embed_description=discord.Embed(
	title="**Étape 3/6**",
	description="ㅤ\nEnsuite il faut le corps, la description de ton message\n*Différents paramètres sont disponible pour améliorer votre description, les différents exemples sont sur le screen ci-dessous*",
	colour=3200456)
embed_description.set_image(url="https://imgur.com/7Il6wp6.png")

embed_color=discord.Embed(
	title="**Étape 4/6**",
	description="ㅤ\nVeuillez incrire le code décimal de la couleur choisis pour votre message, vous pourrez trouver ce code sur [ce site](https://fr.spycolor.com/#)",
	colour=3200456)
embed_color.set_image(url="https://imgur.com/47JxDwh.png")

embed_image=discord.Embed(
	title="**Étape 5/6**",
	description="ㅤ\nVeuillez mettre le lien [imgur](https://imgur.com/), d'une image, ou d'un gif que vous souhaitez incorporer à votre message (sans oublier de rajouter l'exetnsion .gif ou .png)",
	colour=3200456)
embed_image.set_image(url="https://imgur.com/wR4aMaY.png")

embed_footer=discord.Embed(
	title="**Étape 6/6**",
	description="ㅤ\nVeuillez renseigner le contenu du footer, *petit texte sous l'image*, les paramètres sont également disponible dans cette section",
	colour=3200456)
embed_footer.set_image(url="https://imgur.com/LC4gDS7.png")

embed_fini=discord.Embed(
	title="**Embed crée** :white_check_mark:",
	description="Votre message de Bienvenue a bien été crée dans le salon séléctionné !",
	colour=6729778)



#Sondage
embed_channel_sondage=discord.Embed(
	title="**Étape 1/6**",
    description="ㅤ\nBienvenue à toi dans la création de Sondage\n\nPour commencer, envoie moi l'ID du salon de Sondage\n*(Activez le mode développeur dans vos paramètres discord, dans la __catégorie avancés__ sur PC, et dans la __catégorie apparence__ sur téléphone, puis clique droit sur le channel, et 'copier l'identifiant')*",
	color=3200456)

embed_title_sondage=discord.Embed(
	title="**Étape 2/6**",
	description="ㅤ\nQuel question souhaitez vous pour votre sondage ?",
	color=3200456)

embed_description_sondage=discord.Embed(
	title="**Étape 3/6**",
	description="ㅤ\nVeuillez donner la description de votre sondage.",
	color=3200456)

embed_timer_sondage=discord.Embed(
	title="**Étape 4/6**",
	description="ㅤ\nSi vous souhaitez mettre un timer pour votre sondage, qui supprimera les réactions, et enverra les résultats au bout du temps donné. ( Min : 1 Heure )",
	color=3200456)

embed_options_sondage=discord.Embed(
	title="**Étape 6/6**",
	description="ㅤ\nCombien souhaitez-vous d'options pour votre sondage ? ( Min : 2, Max : 10 )",
	color=3200456)

embed_image_sondage=discord.Embed(
	title="**Étape 5/6**",
	description="ㅤ\nSi vous souhaitez mettre une image ou un gif, veuillez renseigner [un lien imgur](https://imgur.com/) (sans oublier de rajouter l'extension .gif ou .png)",
	color=3200456)

embed_fini_sondage=discord.Embed(
	title="**Embed crée** :white_check_mark:",
	description="Votre Sondage a bien été crée dans le salon séléctionné !",
	colour=6729778)

#Erreur
def embed_SondageFilm(ctx, client, prefixe):
    time=datetime.now()
    embed_SondageFilm=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description="**Description:** la commande "+ctx.command.qualified_name+", Permet d'initialiser un sondage entre différents films/séries.\n\n• Il faut renseigner un nombre de films/séries à proposer pour le sondage (10 Max), en l'indiquant juste après la commande.\n\n• Il faut également mentionner le salon dans lequel vous souhaitez que le sondage s'envoie.\nㅤ",
        color=random_color(),
        timestamp=time)
    embed_SondageFilm.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_SondageFilm.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} 5 <#835660396794216458>", inline=False)
    embed_SondageFilm.set_image(url="https://imgur.com/qbAIrif.gif")
    return embed_SondageFilm

def embed_AuGoulag(ctx, client, prefixe):
    time=datetime.now()
    embed_AuGoulag=discord.Embed(
        title="Commande: "+ctx.command.qualified_name, 
        description="**Description:** "+ctx.command.qualified_name+" envoie un utilisateur au plus profond du Goulag.\n\n• Avec la possibilité d'un temps determiné. Quatre options sont disponible ( s / m / h / j ).\n\n• Si vous ne renseignez aucun paramètres, le membre restera dans le goulag, jusqu'à ce que vous le sortiez avec la commande =SorsDuGoulag\nㅤ", 
        colour=random_color(), 
        timestamp=time)
    embed_AuGoulag.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_AuGoulag.add_field(name="**Paramètres**", value="s : secondes / m : minutes / h : heures / j : jours", inline=False)
    embed_AuGoulag.add_field(name="**Exemples**", value=f"{prefixe}{ctx.command.qualified_name} <@!783390079770034186> 30m\n{prefixe}{ctx.command.qualified_name} <@!783390079770034186> ", inline=False)
    embed_AuGoulag.set_image(url="https://imgur.com/qhwQ2iY.gif")
    return embed_AuGoulag

def embed_SorsDuGoulag(ctx, client, prefixe):
    time=datetime.now()
    embed_SorsDuGoulag=discord.Embed(
        title=f"Commande: {ctx.command.qualified_name}",
        description=f"**Description:** la commande {ctx.command.qualified_name}, comme son nom l'indique, permet de sortir quelqu'un du goulag, il suffit pour cela, de le ping après la commande",
        colour=random_color(),
        timestamp=time)
    embed_SorsDuGoulag.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_SorsDuGoulag.add_field(name="**Exemple**", value=f"{prefixe}{ctx.command.qualified_name} <@!783390079770034186>")
    embed_SorsDuGoulag.set_image(url="https://imgur.com/eUtcpWJ.gif")
    return embed_SorsDuGoulag

def embed_QuizzAnime(ctx, client, prefixe):
    time=datetime.now()
    embed_QuizzAnime=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description="**Description:** la commande "+ctx.command.qualified_name+", lance un quizz sur les animés/mangas.\n\n• Il faut renseigner un nombre de questions voulu pour le quizz, en l'indiquant juste après la commande. **[Obligatoire]**\n\n• Il y également la possibilité de changer le temps de réponse entre chaque question, qui est automatiquement à 60 secondes, pour cela, veuillez renseigner un temps en seconde après le nombre de questions. **[Optionnel]**\n\n• Et enfin, il y a la possibilité de choisir le niveau entre trois degrés de difficulté : easy / normal / hard. Le niveau par défaut est : Normal. **[Optionnel]**\nㅤ",
        color=random_color(),
        timestamp=time)
    embed_QuizzAnime.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_QuizzAnime.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} 20 120 easy\n{prefixe}{ctx.command.qualified_name} 32", inline=False)
    embed_QuizzAnime.set_image(url="https://imgur.com/pciAbhn.gif")
    return embed_QuizzAnime

def embed_Pendu(ctx, client, prefixe):
    time=datetime.now()
    embed_Pendu=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description="**Description:** la commande "+ctx.command.qualified_name+", permet de lancer un jeu du pendu, plusieurs modes sont disponibles.Il y a aussi un choix de difficultés à renseigner après le mode : Easy, Normal, Hard (pas encore fait)",
        color=random_color(),
        timestamp=time)
    embed_Pendu.add_field(name="➜ Mangas", value="Un pendu regroupant des noms de Mangas.", inline=False)
    embed_Pendu.add_field(name="➜ Persos", value="Un pendu regroupant les noms des protagonistes et antagonistes de Mangas.", inline=False)
    embed_Pendu.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} mangas", inline=False)
    embed_Pendu.set_image(url="https://imgur.com/4k6L6Tg.gif")
    embed_Pendu.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    return embed_Pendu

def embed_Tempmute(ctx, client, prefixe):
    time=datetime.now()
    embed_Tempmute=discord.Embed(
        title="Commande: "+ctx.command.qualified_name, 
        description="**Description:** "+ctx.command.qualified_name+" un utilisateur avec une raison optionnelle. Quatre options sont disponible ( s / m / h / j ) [Optionnel]", 
        colour=random_color(), 
        timestamp=time)
    embed_Tempmute.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_Tempmute.add_field(name="**Paramètres**", value="s : secondes / m : minutes / h : heures / j : jours", inline=False)
    embed_Tempmute.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} @utilisateur 30m [raison]", inline=False)
    embed_Tempmute.add_field(name="**Exemple**", value=f"{prefixe}{ctx.command.qualified_name} <@!783390079770034186> 30m Raison potentielle", inline=False)
    embed_Tempmute.set_image(url="https://imgur.com/Z2XrjBC.gif")
    return embed_Tempmute

def embed_Clear(ctx, client, prefixe):
    time=datetime.now()
    embed_Clear=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description="**Description:** la commande "+ctx.command.qualified_name+", supprime un nombre de message indiqué. La limite est de 100 messages.",
        colour=random_color(),
        timestamp=time)
    embed_Clear.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_Clear.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} 10", inline=False)
    embed_Clear.set_image(url="https://imgur.com/Er6eFKD.gif")
    return embed_Clear

def embed_Kickexcept(ctx, client, prefixe):
    time=datetime.now()
    embed_Kickexcept=discord.Embed(
      title="Commande: "+ctx.command.qualified_name,
      description="**Description:** La commande ="+ctx.command.qualified_name+" permet de kick tous les membres d'un serveur, sauf ceux qui possèdent le rôle que vous mentionnez à la suite de la commande. Vous avez également la possibilité de mettre une raison, qui sera envoyé en message privé aux membres kick.",
      colour=random_color(),
      timestamp=time)
    embed_Kickexcept.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_Kickexcept.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} @rôle [raison]")
    embed_Kickexcept.set_image(url="https://imgur.com/1AZ3d8M.gif")
    return embed_Kickexcept

def embed_Play(ctx, client, prefixe):
    time=datetime.now()
    embed_Play=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description=f"**Description:** La commande = {ctx.command.qualified_name} permet de lancer une musique en renseignant un lien [Youtube](https://www.youtube.com/). Pour cela, il faut être au préalable dans un salon vocal. Les commandes pause, resume, skip, queue, et leave sont également là pour améliorer votre expérience d'écoute.",
        colour=random_color(),
        timestamp=time)
    embed_Play.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_Play.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} https://www.youtube.com/watch?v=4TsqlT0rfJI")
    embed_Play.set_image(url="https://imgur.com/doBlCHt.gif")
    return embed_Play

def embed_Blindtest(ctx, client, prefixe):
    time=datetime.now()
    embed_Blindtest=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description=f"**Description:** La commande ={ctx.command.qualified_name} lance un BlindTest où l'objectif est de trouver de quel animé vient cet opening/OST. Après la commande, vous devez renseigner le nombre de musiques que vous souhaitez, et optionnellemment, le temps en seconde de l'extrait musical, qui est de 30 secondes par défaut. Une fois la commande lancée, trois salons vont être crées, pour y avoir accès, il faudra rejoindre le BlindTest en cliquant sur le bouton. Les règles et explication du jeu vous serons donné lorsque vous lancerez la commande.",
        colour=random_color(),
        timestamp=time)
    embed_Blindtest.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_Blindtest.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} 10 45", inline=False)
    embed_Blindtest.set_image(url="https://imgur.com/aTcvPUK.gif")
    return embed_Blindtest

def embed_ErrorCMD(ctx, client, prefixe):
    time=datetime.now()
    if ctx.command.qualified_name == "unban":
      comp = " ID_de_l'utilisateur"
      comp1 = " 783390079770034186"
    else:
      comp = " @utilisateur"
      comp1 = " <@!783390079770034186>"
    embed_ErrorCMD=discord.Embed(
        title="Commande: "+ctx.command.qualified_name,
        description="**Description:** "+ctx.command.qualified_name+" un utilisateur avec une raison optionnelle. [Optionnel]",
        colour=random_color(),
        timestamp=time)
    embed_ErrorCMD.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    embed_ErrorCMD.add_field(name="**Utilisation**", value=f"{prefixe}{ctx.command.qualified_name} {comp} [raison]", inline=False)
    embed_ErrorCMD.add_field(name="**Exemple**", value=f"{prefixe}{ctx.command.qualified_name} {comp1} Raison potentielle", inline=False)
    embed_ErrorCMD.set_image(url="https://imgur.com/Z2XrjBC.gif")
    return embed_ErrorCMD

#Autre
def embed_test(ctx):
	embed_test=discord.Embed(
	    title="**Ceci est le titre de votre Embed**",
	    description="*Cette partie est la description*\nVous pouvez y mettre le texte de votre message de Bienvenue.\nPlusieurs paramètres sont disponible comme {member} qui permet d'afficher la mention du membre qui rejoint cela donne : "+ctx.author.mention+".\nVous pouvez aussi mettre {member.count} qui vous donnera le nombre de membres sur votre serveur, ceci donne : "+str(ctx.guild.member_count)+".\nOu encore l'option {member.created_at} qui va vous permettre d'afficher la date de création du compte de l'utilisateur sous cette forme : "+ctx.author.created_at.strftime("%d %B %Y")+".\n\nPour mettre du texte en gras, il faut l'entourer de 2 astérisques, comme cela = **Texte en Gras**, pour l'italique il n'en faut qu'un = *Texte en Italique*, enfin pour souligner, il faut l'entourer de 2 underscores, comme cela = __Texte Souligné__.",
	    colour=15539236)
	embed_test.set_footer(text="Ici vous trouvez le 'footer', un petit texte en fin d'embed, vous ne pouvez pas mettre de texte en gras, italique, souligné, .... Mais vous pouvez tout de même ajouter les différentes options comme {member}, etc")
	embed_test.set_image(url="https://imgur.com/05TBnpG.gif")
	return embed_test

def embed(ctx, client, player):
    time=datetime.now()
    embed=discord.Embed(
        title="Un p'tit BlindTest ... mmmh, quelle bonne idée !",
        description=f"ㅤ\n*Holà, voici les règles de ce jeu :*\n\n• Tout d'abord, si vous voulez rejoindre la partie, veuillez cliquer sur le bouton ci-dessous.\n• Ensuite, vous pourrez rejoindre le salon vocal consacré au BlindTest.\n• L'administrateur de la partie pourra la démarrer quand il le souhaite. Le bot rejoindra alors le salon vocal, et la musique sera jouée.\n• Vous devrez trouver de quel animé provient la musique que jouera le bot.\n• Envoyez la réponse dans le salon textuel prévu à cet effet.\n• À la fin de la partie, un décompte des points sera effectué et envoyé dans le salon **« ʀᴇꜱᴜʟᴛᴀᴛꜱ »** qui ne se supprimera pas, contrairement aux deux autres\n\n\nNombre de joueurs : {player}\nㅤ",
        color=random_color(),
        timestamp=time)
    embed.set_thumbnail(url="https://imgur.com/LSi5QjO.png")
    embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
    return embed


#Help Detaillé
embed_presentation=discord.Embed(
    title = "__Liste des commandes détaillées__",
    description = "\nVoici une liste des commandes de <@783390079770034186>, avec plus d'explication.",
    color = 7841509)

embed_moderation=discord.Embed(
    title = ":tools: Modération (Staff seulement) :",
    description = "ㅤ",
    color = 7841509)
embed_moderation.add_field(name = "➜ Kick", value = "Cette commande permet d'expulser un utilisateur avec une raison optionnelle, qu'il recevra en Message Privé. Il faut le mentionner après la commande. Lorsqu'un membre est expulser, à la différence du bannissement, il peut revenir.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Kick_except", value = "Cette commande permet d'expulser tous les membres d'un serveur, sauf ceux qui possèdent le rôle que vous mentionnez à la suite de la commande. Vous avez également la possibilité de mettre une raison, qui sera envoyé en Message Privé aux membres exclus.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Ban", value = "Cette commande permet de bannir un utilisateur avec une raison optionnelle, qu'il recevra en Message Privé. Il faut le mentionner après la commande. Quand un utilisateur est banni, il ne peut pas revenir, pour lui offrir la possibilité de revenir, il faut utiliser la commande unban.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Unban", value = "Cette commande permet de débannir un utilisateur avec une raison optionnelle, qu'il recevra en Message Privé. Pour le unban, il faut renseigner l'identifiant de l'utilisateur que vous souhaitez débannir, vous pouvez voir comment l'obtenir [ici](https://support.discord.com/hc/fr/articles/206346498-O%C3%B9-trouver-l-ID-de-mon-compte-utilisateur-serveur-message-).\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Mute", value = "Cette commande permet d'empecher un membre de parler dans différents salons textuels/vocaux avec une raison optionnelle. Il faut le mentionner après la commande. Un mute n'a pas de limite de temps, il faut donc utiliser la commande unmute pour retirer la sanction à l'utilisateur.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Tempmute", value = "Cette commande permet d'empecher un membre de parler dans différents salons textuels/vocaux avec une raison optionnelle. Pour cette commande, il faut également le mentionner. Quatre options sont disponible ( s / m / h / j ), ce qui correspond à 'secondes', 'minutes', 'heures', 'jours'.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Unmute", value = "Cette commande permet de rendre la possibilité de parler à un membre, on peut également renseigner une raison optionnelle. Cela fonctionne toujours avec une mention.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ Clear", value = "Cette commande permet de supprimer un nombre de message indiqué après l'appel de la commande. Le nombre de message qui doivent être supprimés ne doit pas dépasser 100.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ AuGoulag", value = "Cette commande envoie un utilisateur au plus profond du Goulag. Avec la possibilité d'un temps determiné. Quatre options sont disponible ( s / m / h / j ), les mêmes que pour la commande tempmute. Si vous ne renseignez aucun paramètres, le membre restera dans le goulag, jusqu'à ce que vous le sortiez avec la commande =SorsDuGoulag. Une fois au Goulag, il ne verra plus qu'un seul salon textuel.\nㅤ", inline=False)
embed_moderation.add_field(name = "➜ SorsDuGoulag", value = "Cette commande, comme son nom l'indique, permet de sortir quelqu'un du goulag, il suffit pour cela, de le ping après la commande. Et il pourra à nouveau voir le monde de ses propres yeux.\nㅤ", inline=False)

embed_serveur=discord.Embed(
    title = ":computer: Serveur (Staff seulement) :",
    description = "ㅤ",
    color = 7841509)
embed_serveur.add_field(name = "➜ set_welcome_message", value = "Cette commande permet d'initialiser une message de bienvenue. Il s'enverra dans le salon choisi (au cours de la commande) à chaque fois qu'un membre rejoindra votre serveur.\nㅤ", inline=False)
embed_serveur.add_field(name = "➜ del_welcome_message", value = "Cette commande permet de supprimé la fonctionnalité de message de bienvenue, si vous souhaitez par exemple le changer.\nㅤ", inline=False)
embed_serveur.add_field(name = "➜ Poll", value = "Cette commande permet d'initialiser un sondage simple entre plusieurs options. Vous pouvez créer un sondage sans limite de temps, ou alors un sondage avec timer, qui enverra les résultats au cours de celui-ci.\nㅤ", inline=False)
embed_serveur.add_field(name = "➜ Prefix", value = "Cette commande permet de changer le préfix du bot <@783390079770034186> sur votre serveur.\nㅤ", inline=False)

embed_minijeux=discord.Embed(
    title = ":game_die: Mini-Jeux :",
    description = "ㅤ",
    color = 7841509)
embed_minijeux.add_field(name = "➜ QuizzAnime", value = "La commande QuizzAnime, lance un quizz sur les animés/mangas. Il faut renseigner un nombre de questions voulu pour le quizz, en l'indiquant juste après la commande **[Obligatoire]**. Il y également la possibilité de changer le temps de réponse entre chaque question, qui est automatiquement à 60 secondes, pour cela, veuillez renseigner un temps en seconde après le nombre de questions **[Optionnel]**. Et enfin, il y a la possibilité de choisir le niveau entre trois degrés de difficulté : easy / normal / hard. Le niveau par défaut est : Normal **[Optionnel]**.\nㅤ", inline=False)
embed_minijeux.add_field(name = "➜ Pendu", value = "la commande pendu, permet de lancer un jeu du pendu, plusieurs modes sont disponibles (Mangas/Perso). Un choix de difficultés est disponible, et est à renseigner après après le mode de jeu : Easy, Normal, Hard (pas encore fait). Le mode Mangas envoie un pendu regroupant des noms de Mangas, quand à lui, le mode Persos crée un pendu regroupant les noms des protagonistes et antagonistes de Mangas.\nㅤ", inline=False)
embed_minijeux.add_field(name = "➜ BlindTest (lançable uniquement par le Staff)", value = "La commande BlindTest lance un BlindTest où l'objectif est de trouver de quel animé vient cet opening/OST. Après la commande, vous devez renseigner le nombre de musiques que vous souhaitez, et optionnellemment, le temps en seconde de l'extrait musical, qui est de 30 secondes par défaut. Une fois la commande lancée, trois salons vont être crées, pour y avoir accès, il faudra rejoindre le BlindTest en cliquant sur le bouton. Les règles et explication du jeu vous serons donné lorsque vous lancerez la commande.\nㅤ", inline=False)

embed_musique=discord.Embed(
    title = ":notes: Musique :",
    description = "ㅤ",
    color = 7841509)
embed_musique.add_field(name = "➜ Play", value = "Cette commande permet de lancer une musique en renseignant un lien [Youtube](https://www.youtube.com/). Pour cela, il faut être au préalable dans un salon vocal. Les commandes pause, resume, skip, queue, et leave sont également là pour améliorer votre expérience d'écoute.\nㅤ", inline=False)
embed_musique.add_field(name = "➜ Pause", value = "Cette commande permet de mettre la musique en pause. Pour cela il faut être dans le salon vocal où se trouve le bot qui diffuse la musique.\nㅤ", inline=False)
embed_musique.add_field(name = "➜ Resume", value = "Cette commande permet d'annuler le pause et de relancer la musique, il faut également se trouver dans le salon vocal où la musique est jouée.\nㅤ", inline=False)
embed_musique.add_field(name = "➜ Skip", value = "Cette commande permet de passer la musique en cours, et de passer à la suivante. Il est requis de se trouver dans le salon vocal de la musique.\nㅤ", inline=False)
embed_musique.add_field(name = "➜ Queue", value = "Cette commande permet d'obenir la liste des musiques qui se jouent par le bot. Pour cette commande, il n'est pas obligatoire de se trouver dans le salon où le bot joue la musique.\nㅤ", inline=False)
embed_musique.add_field(name = "➜ Leave", value = "Cette commande permet de faire quitter le bot du salon vocal, il faut également être dans le salon vocal pour utiliser cette commande.\nㅤ", inline=False)

embed_commandes=discord.Embed(
    title = ":gear: Commandes :",
    description = "ㅤ",
    color = 7841509)
embed_commandes.add_field(name = "➜ Pp", value = "Cette commande permet d'integrer votre photo de profil, ou celle d'un autre utilisateur si vous le mentionnez. Afin de la voir en plus grand, ou de la copier.\nㅤ", inline=False)
embed_commandes.add_field(name = "➜ Invite", value = "Cette commande vous envoie le lien d'invitation du bot <@783390079770034186>. Si vous souhaitez qu'il rejoigne votre serveur.\nㅤ", inline=False)

embed_meme=discord.Embed(
    title = ":partying_face: Memes :",
    description = "ㅤ",
    color = 7841509)
embed_meme.add_field(name = "➜ Les différents mêmes", value = "Ces commandes vous permette d'envoyer des gifs avec un petit texte, soit tout seul, soit en mentionnant un autre utilisateur.\nㅤ", inline=False)
embed_meme.add_field(name = "➜ Signification ", value = "• hug : câlin\n• love : amour\n• fight : combat\n• kiss : bisous\n• kill : meurtre\n• cry : pleurer\n• highfive : check\n• shoot : tirer\n• sleep : dormir\n• slap : claque\n• pat : tapoter\nㅤ", inline=False)