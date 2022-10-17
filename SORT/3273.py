n = int(input())
a= set(map(int,input().split()))
target = int(input())
count=0
for x in a:
    if target-x in a:
        count+=1
print(count//2)