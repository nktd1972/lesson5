i = 0
a = []
b = []
while i <= 100:
    a.append(i)
    if a[i] % 7 == 0 and a[i] % 5 != 0:
        b.append(a[i])
    i += 1
print(b)