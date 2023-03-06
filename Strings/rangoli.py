#https://www.hackerrank.com/challen
# ges/alphabet-rangoli/problem?isFullScreen=true
def print_rangoli(size):
    # your code goes here
    slist = []
    sup, sdown = '', ''
    for asc in range(96 + size, 96, -1):
        slist.append(chr(asc))
        row = '-'.join(slist + (sorted(slist)[1:])).center(((size - 1) * 3) + size, '-') + '\n'
        sup = sup + row
        sdown = row + sdown

    sup = ''.join(list(sup)[:-1])
    sdown = ''.join(list(sdown)[((size - 1) * 3) + size:])
    print(sup + sdown)

