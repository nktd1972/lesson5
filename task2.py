import random

i = 0
a = []
b = []
while i <= 9:
    a.append(random.randint(1, 10))
    b.append(random.randint(1, 10))
    i += 1
print(a)
print(b)
c = []
i = 0
j = 0
while i <= 9:
    j = 0
    while j <= 9:
        if a[i] == b[j]:
            flag = True
            if len(c) > 1:
                k = 0
                while k <= len(c) - 1:
                    if c[k] == a[i]:
                        flag = False
                        break
                    k += 1
            else:
                flag = True
            if flag:
                c.append(a[i])
            break
        j += 1
    i += 1
print(c)
