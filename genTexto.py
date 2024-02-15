from PIL import Image, ImageDraw, ImageFont

width = 300
height = 150
image = Image.new('RGB', (width, height), color=(255, 255, 255))

draw = ImageDraw.Draw(image)

text = "HELLO WORLD"
text_position = (20, 60)

font = ImageFont.truetype("arial.ttf", 24)

draw.text(text_position, text, fill=(0, 0, 0), font=font)

image.save("imagem.png")

