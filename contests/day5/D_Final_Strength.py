
from collections import Counter, defaultdict


for _ in range(int(input())):
    n = int(input())
    nums=list(map(int,input().split()))
    
    def merge(nums1,nums2):
        left=0
        right=0
        ans=[]
        count_l=defaultdict(int)
        count_r=defaultdict(int)
        while right<len(nums2) and left<len(nums1):
            if nums[nums1[left]]<nums[nums2[right]]:
                count_l[nums[nums1[left]]]+=1
                nums[nums1[left]]+=right-count_r[nums[nums1[left]]]
                ans.append(nums1[left])
                left+=1
            else:
                count_r[nums[nums2[right]]]+=1
                nums[nums2[right]]+=left-count_l[nums[nums2[right]]]
                ans.append(nums2[right])
                right+=1
            
        for i in range(left,len(nums1)):
            ans.append(nums1[i])
            nums[nums1[i]]+=right-count_r[nums[nums1[i]]]
        for i in range(right,len(nums2)):
            ans.append(nums2[i])
            nums[nums2[i]]+=left-count_l[nums[nums2[i]]]
        ans = sorted(ans,key=lambda x:nums[x])
        return ans
        
        
    def play(left,right):
        if left==right:
            return [left]
        mid= (right+left)//2
        left_arr=play(left,mid)
        right_arr=play(mid+1,right)
        return merge(left_arr,right_arr)
   
    play(0,2**n-1)
    print(*nums)
        
        
        
    