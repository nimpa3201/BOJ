n =int(input())
arr = list(map(int,input().split()))
arr.sort()
tmp = 1
for i in range(len(arr)):
    if tmp <arr[i]:
        break
    else:
        tmp+=arr[i]
print(tmp)
