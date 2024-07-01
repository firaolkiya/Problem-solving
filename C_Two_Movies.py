for _ in range(int(input())):
    n  =int(input())
    nums1=  list(map(int,input().split()))
    nums2=  list(map(int,input().split()))
    
    f,s = 0,0
    for i in range(n):
        if f>s:
            if max(nums1[i],nums2[i])>0:
                s+=1
            else:
                f+=max(nums1[i],nums2[i])
        else:
            if max(nums1[i],nums2[i])>0:
                f+=1
            else:
                s+=max(nums1[i],nums2[i])
            
    print(min(f,s))