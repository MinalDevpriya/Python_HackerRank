# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees
AB=int(input())
BC=int(input())

hypo=((AB**2) + (BC**2))**0.5

M=hypo/2

C=atan(AB/BC)
print((round(degrees(C))), chr(176), sep='')