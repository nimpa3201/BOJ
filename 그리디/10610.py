from itertools import permutations
li =[]
s = input()
flag = True
for i in permutations(s,len(s)):
    if i[0] =='0':
        i = i[1:]
    num =''.join(i)
    li.append(num)

for i in li:
    i =int(i)
    if i %30 ==0:
        print(i)
        flag =False
        break
if flag:
    print(-1)


