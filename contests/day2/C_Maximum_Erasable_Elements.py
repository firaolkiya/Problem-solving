n = int(input())
array = list(map(int,input().split(" ")))
array.append(1000)
array=[0]+array
total=0
pas=0
for i in range(1,n+2):
    if array[i]-array[i-1]>1:
        pas=i
    else:
        total=max(total,i-pas-1)
print(total)
        
        
    
    
   
