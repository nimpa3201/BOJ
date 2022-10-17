n,x = map(int,input().split())
arr = list(map(int,input().split()))
pr = [0 for _ in range(n+1)]
pr[1]=arr[0]
ans =0
cnt=0
li =[]
for i in range(2,n+1):
    pr[i] = pr[i-1]+arr[i-1]

def get_sum(s,e):
    return pr[e]-pr[s]

for i in range(n+1-x):
    tmp = get_sum(i,i+x)
    li.append(tmp)
ans = max(li)
for i in li:
    if i ==ans:
        cnt+=1
if ans == 0 :
    print("SAD")
else:
    print(ans)
    print(cnt)