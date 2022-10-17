li = [int(input()) for i in range(10)]
ans =0
for x in li :
    ans +=x
    if ans >=100 :
        if ans == 100:
            print(ans)
        elif ans-100 >100-ans+x:
            print(ans-x)
        elif  ans-100 <= 100-ans+x :
            print(ans)
        break 
if sum(li) <100:
    print(sum(li))