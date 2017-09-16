from PIL import Image
import math as m
from progress_tracker import progress

###
def __change_contrast__(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)
    return img.point(contrast)
###

###
def generate_diagram():

    img_nm = raw_input("Type the name of the file(ONLY '.JPG' FILES): ")

    img = Image.open("src/images/" + img_nm + ".jpg")
    final_img = img.convert('LA')
    __change_contrast__(final_img, 1000)

    width,height = final_img.size

    px = []

    print "CREATING DIAGRAM"
    for i in range(0,height-1):

        progress(i, height-1)
        ls = []

        for j in range(0,width-1):

            k = width - 1 - j

            color = final_img.getpixel((k,i))[0]

            if color < 0:
                buf = -(m.log(-color + 1, 2))
            elif color == 0:
                buf = 0
            else:
                buf = 8**(m.log(color, 10))

            ls.insert(j, float(buf))
        px.insert(i, ls)

    return px

###
