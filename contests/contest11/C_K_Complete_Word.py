from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    
queue = deque([0,n-1])
while queue:
    pos = queue.popleft()
    
   
        
            
            
            
            