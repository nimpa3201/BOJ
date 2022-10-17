import sys
INF = sys.maxsize

n =int(input())
m =int(input())
dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    dist[i][i] =0
for _ in range(m):
    a,b,w = map(int,input().split())
    dist[a][b] =min(dist[a][b],w)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] ==INF:
            print(0,end=' ')
        else:
            print(dist[i][j],end=' ')
    print()