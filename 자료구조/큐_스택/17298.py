from collections import deque
import sys
n = int(input())
arr = deque(map(int, sys.stdin.readline().split()))
ans = []
while arr:
    flag = True
    x = arr.popleft()
    for i in arr:
        if i>x:
            ans.append(i)
            flag = False
            break
    if flag:
        ans.append(-1)
        flag= False
print(*ans)