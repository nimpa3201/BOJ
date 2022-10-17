n = int(input()) 
arr = [input() for _ in range(n)]
cnt = n
for s in arr:
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            if s[i] in s[i+1:]:
                cnt-=1
                break
print(cnt)
                
        