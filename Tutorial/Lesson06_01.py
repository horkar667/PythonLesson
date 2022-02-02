for i in range(3):
  for j in range(3):
    if i == 1 and j == 1:
      continue
    elif i == 2 and j == 1:
      break
    else:
     print(i, j, sep="-")

arr = [2, 4, 6, 8, 10]
for k in arr:
  print(k)

sum = 0
for k in arr:
  sum += k
print(sum)