n =int(input())
arr =[]
cnt =1
for _ in range(n):
    s,e = map(int,input().split())
    arr.append((s,e))
arr.sort(key = lambda x : x[1])
end = arr[0][1]
for s,e in arr[1:]:
    if s >= end:
        end =e
    else:
        cnt+=1
print(cnt)
print(arr)