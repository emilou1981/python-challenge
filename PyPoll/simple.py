d = [10,12,13,44,55]

for i in range(1,len(d)):
  print(f'index {i}')
  previous = d[i-1]
  current = d[i]
  difference = current - previous
  print(f'current {current}, previous {previous}')
  print(f'difference {difference}')
