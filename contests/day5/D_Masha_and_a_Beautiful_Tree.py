def mergeSort(arr):
    if len(arr)==1:
        return [arr,0]
    mid=len(arr)//2
    temp1=mergeSort(arr[:mid])
    temp2=mergeSort(arr[mid:])
    left=temp1[0]
    right=temp2[0]
    count=temp1[1]+temp2[1]
    if left==[[],-1] or right==[[],-1]:
        return [[],-1]
    ans=[]
    if left[-1]<right[0]:
        ans=left.extend(right)
    elif right[-1]<left[0]:
        count+=1
        ans=right.extend(left)
    else:
        return [[],-1]
    return [ans,count]

for i in range(int(input())):
    leng=int(input())
    nums=list(map(int,input().split()))
    print(mergeSort(nums)[1])
    