        if(message.content.startswith("-membres")):
            description=""
            for m in Membres:
                descritpion+=m.name
            color=self.random_color()
            embed=self.create_embed("**Liste des membres**", description, color, "")
            await message.channel.send(embed=embed)
