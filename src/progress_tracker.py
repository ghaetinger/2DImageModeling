from random import randint
import sys
###
def progress(now, end):

    if now >= end-1:
        print '\n'
        return

    percentage = float(now / (end / 100))
    if percentage >= 100.0:
        percentage = 100.0

    progress = round(percentage)


    loading_str = ''

    loading_str += '[ '
    for i in range(0,int(progress/10)):
        loading_str += '|'
    loading_str += ' ]'

    loading_str += str(percentage)

    sys.stdout.write('\r'+ loading_str)


###
