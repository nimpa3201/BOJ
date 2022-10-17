from collections import deque
n = int(input())
cards = [i for i in range(1,n+1)]
cards = deque(cards)
while len(cards) !=1:
    print(cards.popleft(),end =" ")
    cards.append(cards.popleft())
for i in cards:
    print(i)