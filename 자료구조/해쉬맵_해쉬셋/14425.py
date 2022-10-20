n,m = map(int,input().split())
s= set()
cnt=0
for _ in range(n):
    s.add(input())
li = [input() for _ in range(m)]

for i in li:
    if i in s:
        cnt+=1

print(cnt)