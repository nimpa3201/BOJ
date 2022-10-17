n,m =map(int,input().split())
nums = list(map(int,input().split()))
ans =[]
nums.sort()
def ncm (num):
    if len(ans) ==m:
        for i in ans:
            print(i,end=' ')
        print()
        return
    else:
        for i in range(num,len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
                ncm(i+1)
                ans.pop()
ncm(0)