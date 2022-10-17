n = int(input())
arr = [ i for i in range(1,n+1)]
ans =[]
visited =[0 for _ in range(n+1)] 
def permutation(num):
    if num == n+1:
        for i in ans:
            print(i,end =' ')
        print()
        return
    else:
        for  i in range(n):
            if visited[i] ==1 :
                continue
            ans.append(arr[i])
            visited[i] = 1
            permutation(num+1)
            ans.pop()
            visited[i] =0
permutation(1)
