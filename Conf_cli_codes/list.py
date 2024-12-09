result = []
for x in range(10):
    if x % 2 == 1 or x == 4:
        continue
    if x % 2 == 0:
        result.append(x * 2)
    else:
        result.append(x * 3)

print(result)
