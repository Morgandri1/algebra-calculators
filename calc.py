from sys import argv
import math

p = argv[5]
a = argv[2]
b = argv[3]
c = argv[4]

if argv[1] == "ar":
    c = float(c)
    a = float(a)
    b = float(b)

    eq = a*b*(math.radians(c)/2)
    print(eq)
if argv[1] == "pr":
    if b == "b":
        eq = float(p) - float(a) - float(c)
        print(eq)
    if c == "c":
        eq = float(p) - float(a) - float(b)
        print(eq)
    if a == "a":
        eq = float(p) - float(b) - float(c)
        print(eq)
    if p == "p":
        eq = float(a)+float(b)+float(c)
        print(eq)
