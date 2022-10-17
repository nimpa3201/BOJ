n = input()
n =sorted(n,reverse = True)
sum =0
if '0' not in n:
    print(-1)
    exit()

for i in n:
    i = int(i)
    sum+=i

if sum %3 ==0:
    print(''.join(n))
else:
    print(-1)