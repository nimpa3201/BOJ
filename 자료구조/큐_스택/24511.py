from collections import deque
n = int(input())
option = list(map(int,input().split()))
initialList = list(map(int,input().split()))
m = int(input())
push = list(map(int,input().split()))
optionList =[]

for i in option:
    if i ==0:
        optionList.append(deque())
    else :
        optionList.append([])

def initial():
    for i in range (len(initialList)):
        optionList[i].append(initialList[i])
initial()

def run(x):
    data = x 
    for i in range(len(optionList)):
        optionList[i].append(data)
        if type(optionList[i]) == deque:
            data =optionList[i].popleft()
        if type(optionList[i]) == list:
            data = optionList[i].pop()
    return data


for i in push:
    print(run(i),end=' ')     
     #  2,4,7





# from collections import deque
# q = deque()
# q2= deque()
# q.append(1)
# q.append(2)
# q.append(3)
# a= []
# a.append(q)
# a.append(q2)
# print(a)
# print(q)
# x= q.popleft()
# print(x)
# print(q)
