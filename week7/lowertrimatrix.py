n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
  for j in range(n):
    end = '' if j == n-1 else ' '
    if(i<j):
      print(0, end=end)
    else:
      print(a[i][j], end=end)
  end = '' if i == n-1 else '\n'
  print('',end=end)
    
