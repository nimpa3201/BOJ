k,l = map(int,input().split())
arr =[]
d= dict()
for i in range(l):
    student = input()
    d[student] = i
for j in d:
    arr.append((j,d[j]))
arr.sort(key = lambda x :x[1])

for i in range(k):
    if i < len(arr):
        print(arr[i][0])