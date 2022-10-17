word = input()
li = []
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        s1 = word[:i]
        s2 =word[i:j]
        s3 = word[j:]
        s1 =s1[::-1]
        s2 =s2[::-1]
        s3 =s3[::-1]
        ans = s1+s2+s3
        li.append(ans)
li.sort()
print(li[0])