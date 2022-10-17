import sys
input = sys.stdin.readline
d = dict()
tree_num=0
while True:
    tree = input().rstrip()

    if not tree :
        break
    tree_num+=1
    if tree not in d:
        d[tree]=1
    else :
        d[tree]+=1
a = list(d.keys())
a.sort()
for i in a:
    per =(d[i]/tree_num)*100
    print("%s %.4f" %(i,per))