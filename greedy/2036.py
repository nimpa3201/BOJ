n = int(input())
nums= [ int(input()) for _ in range(n)]
nums.sort()
negative =[]
postive =[]
score =0
for i in nums:
    if i <0 :
        negative.append(i)
        negative.sort(reverse=True)
    else:
        postive.append(i)
        postive.sort()

while len(negative) !=1 :
    if len(negative) ==0:
        break
    n =negative.pop()
    m =negative.pop()
    if n != 1 or m!=1:
        score += n*m
    else :
        score += n
        score +=m
if len(negative)==1:
    score+=negative[0]

while len(postive) !=1 :
    if len(postive) ==0:
        break
    n =postive.pop()
    m =postive.pop()
    if n != 1 or m!=1:
        score += n*m
    else :
        score += n
        score +=m
if len(postive)==1:
    score+=postive[0]
print(score)


