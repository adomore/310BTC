from PIL import Image

data = ['584', 'L3', '7', '9F', '20']

im_path = r'challenge.png'
im = Image.open(im_path)
width, height = im.size
# 宽高
print(im.size, width, height)
# 格式，以及格式的详细描述
print(im.format, im.format_description)

# im.show()


