import heapq

scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]

print(heapq.nlargest(3, scores))  # [91, 87, 82]
print(heapq.nsmallest(5, scores))  # [15, 33, 33, 49, 51]

_, *elements_in_the_middle, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(elements_in_the_middle)  # [2, 3, 4, 5, 6, 7