n =int(input())
li=[]
for _ in range(n):
    li.append(int(input()))
li.sort()
ans =0
first = li[0]+li[1]
result =first
for i in li[2:]:
    ans = i +first
    first = ans
    result += ans
print(result)