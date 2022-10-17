n = int(input())
player = list(map(int,input().split()))
player.sort()
li = []
score=0
sum=0
out=0
for x in player:
    if x >=0:
        li.append(x)
    else:
        score+=x

for i in li:
    sum += len(li)*i

out = sum+score
print(out)