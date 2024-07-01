for _ in range(int(input())):
    x,y,z,k = map(int,input().split())
    side=[x,y,z]
    side.sort()
    
    s = int(pow(k,1/3))
    x1,y1,z1=s,s,s
        
    
    # volume=1
    
    # while volume<k:
        
    #     x1+=1
    #     volume=x1*y1*z1
    #     if volume==k:
    #         break
    #     if y1<side[1]:
    #         y1+=1
    #     volume=x1*y1*z1
    #     if volume==k:
    #         break
    #     if z1<side[2]:
    #         z1+=1
    #     volume=x1*y1*z1
    #     if volume==k:
    #         break
    # x=side[0]-x1
    # y=side[1]-y1
    # z=side[2]-z1
    
    # if volume!=k:
    #     print(0)
    # else:
    #     print((x+1)*(y+1)*(z+1))