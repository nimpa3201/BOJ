n, k =map(int,input().split())
coins =[int(input()) for _ in range(n)]
coins.sort(reverse = True)

cnt =0
for coin in coins:
    if k >= coin:
        cnt += k//coin
        k -= coin*( k//coin)
    if k ==0:
        print(cnt)
        break