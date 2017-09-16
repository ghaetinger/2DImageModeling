from progress_tracker import progress

###
def __write_vertices__(matrix, obj_file):
    x_cnt = 0
    y_cnt = 0
    cnt = 0

    print "WRITING VERTICES..."
    for i in matrix:

        progress(y_cnt, len(matrix))
        for j in i:
            obj_file.write('v ' + str(x_cnt) + ' ' + str(y_cnt) + ' ' + str(j) + '\n')

            cnt += 1
            x_cnt += 1

        x_cnt = 0
        y_cnt += 1
###

###
def __write_faces__(matrix, obj_file, x_size):

    print "WRITING FACES..."
    for i in range(1, len(matrix) - 1):

        progress(i, len(matrix) - 1)
        for j in range(1, x_size - 1):

            px = j + ((i-1) * x_size)


            obj_file.write('f ' + str(px) + ' ' + str(px + x_size) + ' ' + str(px + 1) + '\n')
            obj_file.write('f ' + str(px + x_size) + ' ' + str(px + x_size + 1) + ' ' + str(px + 1) + '\n')
###

###
def __print_spaces__(file):

    for i in range(0,5):
        file.write('\n')

###

###
def create_obj(matrix, name):


    x_size = len(matrix[0])

    obj = open('src/objects/'+ name + ".obj", 'w+')
    obj.write(name + '.obj' + '\n' + '#Guilherme Gomes Haetinger' + '\n')

    __print_spaces__(obj)

    obj.write('VERTICES COORDINATES:' + '\n')
    __write_vertices__(matrix, obj)

    __print_spaces__(obj)

    obj.write('FACES VERTICES COMBINATIONS:' + '\n')
    __write_faces__(matrix, obj, x_size)




###
