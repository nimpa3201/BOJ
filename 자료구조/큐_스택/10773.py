n = int(input())
li =[]
for _ in range(n):
    a = int(input())
    if a ==0:
        li.pop()
    else :
        li.append(a)
print(sum(li))