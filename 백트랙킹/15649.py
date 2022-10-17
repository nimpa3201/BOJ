n,m =map(int,input().split())
li=[]
def ncm(num):
    if num == m+1:
        for i in li:
            print(i,end=' ')
        print()

        return 
    else:
        for i in range(1,n+1):
            if i not in li:
                li.append(i)
                ncm(num+1)
                li.pop()
        return

ncm(1)