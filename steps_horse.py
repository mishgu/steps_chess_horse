def steps_horse(x,y):
    x = abs(x)
    y = abs(y)
    if x == 2 and y == 2:
        return 4
    if x >= y:
        x,y = y,x
    # algorithm
    if y % 4 == 0:
        if x % 2 == 0:
            return int(y/2)
        else:
            return int(y/2)+1
    elif y % 4 == 3:
        if x % 2 == 0:
            return int(y/2)+2 # test 14 bad
        else:
            return int(y/2)+1
    elif y % 4 == 2:
        if x % 2 == 0 :
            return int(y/2)+1
        else:
            return int(y/2)
    else:
        if x % 2 == 0:
            return int(y/2)+1
        else:
            return int(y/2)+2