import heapq

before = [10,0,5,2,6,1]
heapq.heapify(before)
after = []
while len(before):
  after.append(heapq.heappop(before))

print(after)
