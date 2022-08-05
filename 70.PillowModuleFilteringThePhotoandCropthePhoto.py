from PIL import Image,ImageFilter

image=Image.open("Bird.jpg")

#image.show()

image.save("bird2.jpg")

image.rotate(180).save("bird3.jpg")

image.rotate(90).save("bird4.jpg")

image.convert(mode="L").save("bird5.jpg")

change=(300,400)   #why happened 300,200 ????? ok I understood

image.thumbnail(change)

image.save("bird6.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("bird7.jpg")

crop_area=(63,18,679,688)

image2=Image.open("Ataturk.jpg")

image2.crop(crop_area).save("Ataturk1.jpg")
















