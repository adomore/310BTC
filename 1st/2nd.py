from PIL import Image
img = Image.open("challenge_alpha.jpg")
img_array = img.load()

for i in range(2800):
    print(img_array[i, 311])


data = ['584', 'L3', '7', '9F', '20']

file = open('challenge_alpha.jpg', mode='rb')
while file.readable():
    print(file.readline())
# im = Image.open('challenge_alpha.jpg.png')
# width, height = im.size
# 宽高
# print(im.size, width, height)
# 格式，以及格式的详细描述
# print(im.format, im.format_description)

# im.show()


