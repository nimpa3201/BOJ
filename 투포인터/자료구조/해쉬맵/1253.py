n = int(input())
arr = list(map(int,input().split()))
s = set()
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        s.add(arr[i]+arr[j])
    for elem in arr:
        if elem in s:
            count+=1
    print(count)