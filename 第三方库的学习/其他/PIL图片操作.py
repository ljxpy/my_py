from PIL import Image
i = Image.open("buluo (1).jpg")
region = i.crop((140,130,370,300))  #剪切
region.save("000.jpg")      #保存