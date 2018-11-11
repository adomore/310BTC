from PIL import Image

data = ['584', 'L3', '7', '9F', '20']

file = open('challenge_alpha.jpg', mode='rb')
while file.readable():
    print(file.readline())
im = Image.open('challenge_alpha.jpg.png')
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

# im.show()


