T = int(input())


def cal(li):
    ouput=0
    for i in range(0,len(li)):
        maxim=0
        for j in range(i+1,len(li)):
            ans = li[j]-li[i]
            if ans > maxim:
                maxim = ans
        ouput+=maxim
    return ouput




for _ in range(T):
    n = int(input())
    li = list(map(int,input().split()))
    print(cal(li))