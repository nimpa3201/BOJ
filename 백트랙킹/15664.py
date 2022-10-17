n,m =map(int,input().split())
arr=list(map(int,input().split()))
ans =[]
arr.sort()
s1 =set()
def npr(num,pivot):
    if num ==m+1:
        anstuple= tuple(ans)
        s1.add(anstuple)
    else:
        for i in range(pivot,len(arr)):
            ans.append(arr[i])       
            npr(num+1,i+1)
            ans.pop()
        
npr(1,0)
s1= list(s1)
s1.sort()
for i in range(len(s1)):
    for j in range(len(s1[0])):
        print(s1[i][j],end =' ')
    print()
