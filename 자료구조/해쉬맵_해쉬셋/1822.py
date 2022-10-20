n,m = map(int,input().split())
A= set(map(int,input().split()))
B= set(map(int,input().split()))
ans =list(A-B)
ans.sort()
print(len(A-B))
for i in ans:
    print(i,end=' ')
