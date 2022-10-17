s= input()
stack =[]
cnt =0
for i in s:
    if i =='(':
        stack.append('(')
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else :
            cnt+=1
if stack :
    cnt+=len(stack)
print(cnt)

