
def dfs(ans,nums,pivot):
    if len(ans) == 6:
        for i in ans:
            print(i,end =' ')
        print()
        return

    else:
        for i in range(pivot,len(nums)):
            ans.append(nums[i])
            dfs(ans,nums,i+1)
            ans.pop()








while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break
    length = nums.pop(0)
    dfs([],nums,0)
    print()