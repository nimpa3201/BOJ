n = int(input())
li =[]
for i in range(n):
    age,name = input().split()
    age = int(age)
    li.append((age,name,i))

li.sort(key=lambda x : (x[0], x[2]))
for i in range(n):
    print(li[i][0],li[i][1])