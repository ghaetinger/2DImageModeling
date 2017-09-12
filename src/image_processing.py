from PIL import Image

img = Image.open('testing_img.jpg')
im_grey = img.convert('LA') # convert to grayscale

width,height = img.size
out = open("PICTURE_GREY_VALUES.txt", 'w+')

px = [[]]

for i in range(0,width):
    ls = []
    for j in range(0,height):
        ls.insert(j, img.getpixel((i,j))[0])
        out.write(str(i) + '|' + str(j) + '|' + str(ls[j]) + '\n')
    px.insert(i, ls)


