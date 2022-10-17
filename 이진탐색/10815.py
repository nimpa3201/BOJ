
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
q = list(map(int,input().split()))

for i in q:
    if i in arr:
        print(1,end=' ')
    else:
        print(0,end=' ')