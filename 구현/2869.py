a,b,v = map(int,input().split())
n =0
cnt =0
while True:
    n+=a
    cnt+=1
    if n >= v:
        print(cnt)
        break
    n-=b