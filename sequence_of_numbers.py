a=[]
n, s =int(input()), 0
for i in range(1, n+1):
    a.append([i]*i)
for i in a:
    for j in i:
        s+=1
        if s <= n:
            print(j, end=' ')
        else:
            break