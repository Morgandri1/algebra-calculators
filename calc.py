from sys import argv
constant = argv[2]
x = argv[3]
y = argv[4]

if argv[1] == "inv":
    if y == "y":
        eq = float(constant) / float(x)
        print(eq)
    if constant == "k":
        eq = float(y) * float(x)
        print(eq)
    if x == "x":
        eq = float(y) * float(constant)
        print(eq)
if argv[1] == "dir": 
    if y == "y":
        eq = float(constant) * float(x)
        print(eq)
    if constant == "k":
        eq = float(y) / float(x)
        print(eq)
    if x == "x":
        eq = float(y) / float(constant)
        print(eq)
else:
    print("invalid operation, use either inv or dir, use -h for help")