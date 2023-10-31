objects = [1, 2, 1, 2, 3, 4, 5, 4, 4, 4, 4]
ans = 0
a = 0
for i in range(len(objects)):
    for j in range(i + 1, len(objects)):
        if objects[j] is objects[i]:
            a += 1
    if a == 0:
        ans += 1
    a = 0
print(ans)