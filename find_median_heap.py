# https://www.hackerrank.com/challenges/find-the-running-median/problem
import heapq

# max of lowers
min_heap = []
# min of highers
max_heap = []

n_cases = int(input())

for _ in range(n_cases) :
    a = int(input())
    if not max_heap :
        heapq.heappush(max_heap,a)
    else :
        if len(max_heap) > len(min_heap) :
            if max_heap[0] < a :
                b = heapq.heappushpop(max_heap,a)
                heapq.heappush(min_heap,-b)
            else :
                heapq.heappush(min_heap,-a)
        else :
            if -min_heap[0] > a :
                b = -heapq.heappushpop(min_heap,-a)
                heapq.heappush(max_heap,b)
            else :
                heapq.heappush(max_heap,a)

    print(min_heap)
    print(max_heap)
    if len(max_heap) > len(min_heap) :
        print("%.1f" % max_heap[0])
    else :
        print("%.1f" % ((max_heap[0]-min_heap[0])/2))
