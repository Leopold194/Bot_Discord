import discord


'''@client.command(name='canvas')
async def canvas(ctx, text=None):

    IMAGE_WIDTH = 1100
    IMAGE_HEIGHT = 650

    # create empty image 600x300 
    image = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT)) # RGB, RGBA (with alpha), L (grayscale), 1 (black & white)

    # or load existing image
    #image = Image.open('/home/furas/images/lenna.png')

    # create object for drawing
    draw = ImageDraw.Draw(image)

    # draw red rectangle with green outline from point (50,50) to point (550,250) #(600-50, 300-50)
    draw.rectangle([20, 20, IMAGE_WIDTH-680, IMAGE_HEIGHT-20], fill=(122,17,0), outline=(0,255,0))

    # draw text in center
    text = f'Hello {ctx.author.name}'

    #font = ImageFont.truetype('Arial.ttf', 30)

    text_width, text_height = draw.textsize(text, font=None)
    x = (IMAGE_WIDTH - text_width)//2
    y = (IMAGE_HEIGHT - text_height)//2

    draw.text( (x, y), text, fill=(0,0,255), font=None)

    # create buffer
    buffer = io.BytesIO()

    # save PNG in buffer
    image.save(buffer, format='PNG')    

    # move to beginning of buffer so `send()` it will read from beginning
    buffer.seek(0) 

    # send image
    await ctx.send(file=discord.File(buffer, 'myimage.png'))'''