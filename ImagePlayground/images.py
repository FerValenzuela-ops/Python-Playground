from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')

img.thumbnail((400,400))
img.save("thumbnail.jpg")
print(img.size)
# we can apply filter like smooth or blur to a image
# filter_img = img.filter(ImageFilter.SMOOTH)
# filter_img = img.convert('L')  # this makes the image tun to grey
# crooked = filter_img.rotate(120)  # we can rotate in 90 degrees with this
# resize = filter_img.resize((300, 300))
# box = (100,100,400,400)
# crop = filter_img.crop(box)
# crop.save("crop.png", 'png')
# resize.save("resize.png", 'png')
# # this will save the pic above whith the name: grey.png and also the second paramter allows to save it like a .png file
# crooked.save("grey.png", 'png')
# #filter_img.show()  # this allow us to instanly show the imaga above us

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))
