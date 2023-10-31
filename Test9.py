dict={}
n=int(input())
for i in range(n):
    a=int(input())
    if a in dict:
        print(dict[a])
    else:
        dict[a]=f(a)
        print(dict[a])