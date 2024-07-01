n , k =  map(int,input().split())

city =list(map(int,input().split()))
tower = list(map(int,input().split()))

def bina(radius):
    c,t =0,0
    while c<n and t<k:
        if abs(tower[t]-city[c])<=radius:
            c+=1
        else:
            t+=1
    return c==n

left,right,best = 0,max(abs(city[0]-tower[-1]),abs(city[-1]-tower[0])),0
while left<=right:
    mid = (left+right)//2
    if bina(mid):
        best=mid
        right=mid-1
    else:
        left=mid+1
print(best)
    
    

    
    
    

# near = [float('-inf')]*n
# target = 0

# for i in range(k):
#     while target<n and (i==k-1 or abs(city[target]-tower[i])<abs(city[target]-tower[i+1])):
#         near[target]= abs(city[target]-tower[i])
#         target+=1
# print(max(near))
        