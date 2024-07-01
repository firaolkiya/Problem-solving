

for _ in range(int(input())):
    size = int(input())
    nums = list(map(int, input().split()))

    count=[0,0]
    
    def mergeSort(left,right):
        if left==right:
            return [nums[left]]
        mid = (left+right)//2
        left_array=mergeSort(left,mid)
        right_array = mergeSort(mid+1,right)
        
        ans= []
        l,r,n1,n2=0,0,len(left_array),len(right_array)
        while l<len(left_array) and r<len(right_array):
            if left_array[l]<right_array[r]:
                ans.append(left_array[l])
                l+=1
            else:
                ans.append(right_array[r])
                r+=1
        if l==n1 and r==0:
            ans.extend(right_array)
        elif r==n2 and l==0:
            ans.extend(left_array)
            count[0]+=1
        else:
            count[1]=-1
        return ans
    mergeSort(0,size-1)
    if count[1]==0:
        print(count[0])
    else:
        print(-1)
