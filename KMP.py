def name():
    x = input().split('-')
    y = []
    for z in x:
        y.append(z[0])
    print(''.join(y).upper())
name()
