n,m =map(int,input().split())
arr= list(input().rstrip().split())
arr.sort()
ans =[]
tmp = set(['a', 'e', 'i', 'o', 'u']) 
cnt1=0
cnt2=0

def dfs(num,pivot):
    global cnt1,cnt2,ans
   
    if num ==n+1:
        if cnt1>=1 and cnt2>=2:
            for i in ans:
                print(i,end='')
            print()
        return
    else:
        for i in range(pivot,m):
            if arr[i] in tmp:
                cnt1+=1
            else:
                cnt2+=1
            ans.append(arr[i])
            dfs(num+1,i+1)          
            if ans.pop() in tmp:
                cnt1-=1
            else:
                cnt2-=1

            
dfs(1,0)

# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw