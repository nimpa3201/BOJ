n,m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
ans =set()
def ncm(s):
    if s == m+1:
        for i in ans:
            print(i,end=' ')
        print()
        return
    else :
        for num in nums:
            if num not in ans:
                ans.add(num)
                ncm(s+1)
                ans.pop()
ncm(1)

