#https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types&filters%5Bsubdomains%5D%5B%5D=py-sets
def average(array):
    # your code goes here
    set_a=set(array)
    return sum(set_a)/len(set_a)

