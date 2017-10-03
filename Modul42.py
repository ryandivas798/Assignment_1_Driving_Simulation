x = []
for y in range(0,10):
    y = int(input())
    a = y % 42
    x.append(a)
print(len(set(x)))
