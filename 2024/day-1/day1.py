import numpy as np

def file_to_arrays(file_name):
  with open(file_name, 'r') as data:
    list1 = []
    list2 = []
    for line in data:
      p = [int(num) for num in line.split()]
      list1.append(p[0])
      list2.append(p[1])
  return list1, list2

arr1, arr2 = np.array(file_to_arrays('ids'))
arr1.sort()

arr2.sort()

total_distance = 0
i = 0
for num in arr1:
  distance = np.abs(num - arr2[i])
  total_distance += distance
  i += 1

print(total_distance)

similarity = 0
for num in arr1:
  score = 0
  for num2 in arr2:
    if num == num2:
      score += 1
  similarity += score * num

print(similarity)