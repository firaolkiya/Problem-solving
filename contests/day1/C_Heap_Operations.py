from heapq import *
import sys
input = sys.stdin.readline

heap = []
ans=[]
for _ in range(int(input())):
    operation=input()
    if operation[0]=="r":
        if heap:
            heappop(heap)
        else:
            ans.append(("insert 1"))
        ans.append("removeMin")
    elif operation[0]=="i":
        ins,num = operation.split()
        ans.append("insert "+num)
        heappush(heap,int(num))
    else:
        ins,num = operation.split()
        while heap and heap[0]<int(num):
            ans.append("removeMin")
            heappop(heap)
        if not heap or heap[0]!=int(num):
            heappush(heap,int(num))
            ans.append("insert "+num)
        ans.append(operation)
        
print(len(ans))
for ele in ans:
    print(ele)
