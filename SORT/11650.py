n = int(input())
arr =[]
for _ in range(n):
    x1,x2 = map(int,input().split())
    arr.append((x1,x2))
arr.sort(key = lambda x : (x[0],x[1]))

for i in arr:
    print(i[0],i[1])