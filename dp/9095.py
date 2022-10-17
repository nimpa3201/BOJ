t =int(input())


def fun(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return fun(n-1)+fun(n-2)+fun(n-3)
for _ in range(t):
    num =int(input())
    print(fun(num))