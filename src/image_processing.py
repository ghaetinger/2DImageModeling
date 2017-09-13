from PIL import Image

###
def create_obj(matrix):


    item_sz = len(matrix[0])
    obj = open("picture_mod.obj", 'w+')
    obj.write('#picture_mod.obj' + '\n' + '#Guilherme Gomes Haetinger' + '\n')
    x_cnt = 0
    y_cnt = 0
    cnt = 0
    for i in matrix:
        for j in i:
            obj.write('v ' + str(x_cnt) + ' ' + str(y_cnt) + ' ' + str(j) +'\n')
            cnt += 1
            x_cnt += 1
        x_cnt = 0
        y_cnt += 1


    create_background(item_sz, len(matrix), obj, cnt, matrix)


    print item_sz
    for i in range(1, len(matrix) - 1):
        for j in range(1, item_sz - 1):

            px = j + ((i-1) * item_sz)

            #print('f ' + str(j) + ' ' + str(j + item_sz) + ' ' + str(j + 1))
            #print('f ' + str(j + item_sz) + ' ' + str(j + item_sz + 1) + ' ' + str(j + 1))

            obj.write('f ' + str(px) + ' ' + str(px + item_sz) + ' ' + str(px + 1) + '\n')
            obj.write('f ' + str(px + item_sz) + ' ' + str(px + item_sz + 1) + ' ' + str(px + 1) + '\n')


###

###
def create_background(x, y, file, end, mtx):

    size = len(mtx)
    it_size = len(mtx[0])
    print mtx[size - 1]

    coord00 = (0, 0, mtx[0][0])
    coord01 = (it_size, 0, mtx[0][it_size-1])
    coord02 = (0, 0, 0)
    coord03 = (size, 0, 0)
    coord10 = (0, size, mtx[size-1][0])
    coord11 = (it_size, size, mtx[size-1][it_size-1])
    coord12 = (0, size, 0)
    coord13 = (it_size, size, 0)

    file.write('v ' + '0'+ ' '  + '0'+ ' '  + '0' + '\n')
    file.write('v ' + str(x)+ ' '  + '0'+ ' '  + '0' + '\n')
    file.write('v ' + '0'+ ' '  + str(y)+ ' '  + '0' + '\n')
    file.write('v ' + str(x)+ ' '  + str(y)+ ' '  + '0' + '\n')

    file.write('v ' + str(coord00[0]) + ' ' + str(coord00[1]) + ' ' + str(coord00[2]) + '\n')
    file.write('v ' + str(coord01[0]) + ' ' + str(coord01[1]) + ' ' + str(coord01[2]) + '\n')
    file.write('v ' + str(coord02[0]) + ' ' + str(coord02[1]) + ' ' + str(coord02[2]) + '\n')
    file.write('v ' + str(coord03[0]) + ' ' + str(coord03[1]) + ' ' + str(coord03[2]) + '\n')
    file.write('v ' + str(coord10[0]) + ' ' + str(coord10[1]) + ' ' + str(coord10[2]) + '\n')
    file.write('v ' + str(coord11[0]) + ' ' + str(coord11[1]) + ' ' + str(coord11[2]) + '\n')
    file.write('v ' + str(coord12[0]) + ' ' + str(coord12[1]) + ' ' + str(coord12[2]) + '\n')
    file.write('v ' + str(coord13[0]) + ' ' + str(coord13[1]) + ' ' + str(coord13[2]) + '\n')

    file.write('f ' + str(end + 3) + ' ' + str(end + 2) + ' ' +str(end + 1) + '\n')
    file.write('f ' + str(end + 3) + ' ' +str(end + 4) + ' ' +str(end + 2) + '\n')

    file.write('f ' + str(end + 8) + ' '  + str(end + 5) + ' ' + str(end + 7) + '\n')
    file.write('f ' + str(end + 8) + ' '  + str(end + 6) + ' ' + str(end + 5) + '\n')
    file.write('f ' + str(end + 11) + ' '  + str(end + 9) + ' ' + str(end + 7) + '\n')
    file.write('f ' + str(end + 9) + ' '  + str(end + 5) + ' ' + str(end + 7) + '\n')
    file.write('f ' + str(end + 11) + ' '  + str(end + 10) + ' ' + str(end + 9) + '\n')
    file.write('f ' + str(end + 11) + ' '  + str(end + 12) + ' ' + str(end + 10) + '\n')
    file.write('f ' + str(end + 12) + ' '  + str(end + 6) + ' ' + str(end + 10) + '\n')
    file.write('f ' + str(end + 12) + ' '  + str(end + 8) + ' ' + str(end + 6) + '\n')

###


img_nm = raw_input("Type the name of the file: ")

img = Image.open(img_nm + ".jpg")
im_grey = img.convert('LA') # convert to grayscale

width,height = img.size
out = open("PICTURE_GREY_VALUES.txt", 'w+')

px = []
j = 0
for i in range(0,height):
    ls = []
    for j in range(0,width):
        ls.insert(j, float(img.getpixel((j,i))[0])/2.5)
        #out.write(str(j) + '|' + str(i) + '|' + str(ls[j]) + '\n')
    px.insert(i, ls)
    print str(ls) + '\n'


out.write(str(px[len(px)-2]))
create_obj(px)