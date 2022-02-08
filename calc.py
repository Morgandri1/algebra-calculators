import math
from sys import argv

r = float(argv[2])
d = r*2

pi = math.pi

if argv[1] == "a":
    eq = pi*r**2
    print(eq)
if argv[1] == "c":
    eq = 2*pi*r
    print(eq)

