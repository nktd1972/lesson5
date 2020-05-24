import random

i = 0
a = []
while i <= 10:
    a.append(random.randint(1, 100))
    i += 1
max_a = a[0]
print(a)
i = 1
while i <= len(a) - 1:
    if max_a < a[i]:
        max_a = a[i]
    i += 1
print(max_a)
