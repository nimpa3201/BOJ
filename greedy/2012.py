n  = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans =0
for i in range(len(arr)):
    ans+= abs(arr[i]-(i+1))
print(ans)