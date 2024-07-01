from heapq import heappop, heappush, heapreplace

m,n=map(int,input().split())
max_ = ["0"]*m
ans=["-1"]*2

temp=n
ind=0
while temp>0 and ind<m:
    if temp>9:
        max_[ind]="9"
        temp-=9
    else:
        max_[ind]=str(temp)
        temp=0
    ind+=1
if temp==0 and n>0:
    ans[1]="".join(max_)
elif n==0 and m==1:
    ans[1]="0"
    ans[0]="0"
min_=["0"]*m
mtemp=n
ind=m-1
while mtemp>1 and ind>=0:
    if mtemp>10:
        min_[ind]="9"
        mtemp-=9
    else:
        min_[ind]=str(mtemp-1)
        mtemp=1
    ind-=1

min_[0]=str(int(min_[0])+mtemp)
if  0<int(min_[0])<10:
    ans[0]="".join(min_)

print(*ans)







# m,n=map(int,input().split())
# average=n//m
# modul=n%m
# min_heap=[]
# for i in range(m):
#     if modul>0:
#         heappush(min_heap,average+1)
#         modul-=1
#     else:
#         heappush(min_heap,average)
# store=[]
# small=heappop(min_heap)

# while min_heap:
#     if min_heap[0]>=9:
#         store.append(small)
#         break
#     if not store and small==1:
#         store.append(1)
#         small=heappop(min_heap)
#     elif small==0:
#         store.append(0)
#         small=heappop(min_heap)
#     heapreplace(min_heap,min_heap[0]+1)   
#     small-=1
# if min_heap:
#     store.extend(sorted(min_heap))
# print(store,min_heap)