
for _ in range(int(input())):
    n,k = map(int,input().split(" "))
    s=input()
    wo=input()
    
    count_word=0
    count_s=0
    for i in range(len(wo)):
        count_word+=ord(wo[i])
        count_s+=ord(s[i])
       
    if count_s==count_word:
        print("YES")
    else:
        for i in range(k,n):
            count_s+=ord(s[i])
            count_s-=ord(s[i-k])
            if count_s==count_word:
                print("YES")
                break
        else:
            print("NO")
