x, y , z = input().split()

intX = int(x)
intY = int(y)
intZ = int(z)

if (intX == intY == intZ):
    total = 10000 + (intX * 1000)
    print(total)

elif (intX == intY) and (intY != intZ):
    total = 1000 + (intX * 100)
    print(total)

elif (intX == intZ) and (intX != intY):
    total = 1000 + (intX * 100)
    print(total)

elif (intY == intZ) and (intY != intX):
    total = 1000 + (intY * 100)
    print(total)
else:
    if intX > intY and intX > intZ:
        total = intX * 100
        print(total)
    elif intY > intX and intY > intZ:
        total = intY * 100
        print(total)
    else:
        total = intZ * 100
        print(total)