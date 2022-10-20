n,c = map(int,input().split())
arr = list(map(int,input().split()))
nums = dict()
ans = []
for i in arr:
    if i not in nums:
        nums[i]=(1,0)
    else:
        nums[i] = (nums[i][0]+1,nums[i][1])
for i in nums:
     ans.append((i,nums[i][0],nums[i][1]))
ans.sort(key = lambda x : (-x[1],x[2]))
for i,j,k in ans:
    for x in range(j):
        print(i,end=' ')