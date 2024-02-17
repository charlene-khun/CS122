def topKFrequent(nums, k):
  # Enter your code below. Remove keyword 'pass'
  list = {}
  for i in nums:
    list[i] = list.get(i, 0) + 1
  sorted_nums = sorted(list.keys(), key=list.get, reverse = True)
  result = sorted_nums[:k]
  return result

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([2, 2, 3, 2, 1, 5, 1, 2, 4, 2, 3, 5, 1, 5, 1], 3))