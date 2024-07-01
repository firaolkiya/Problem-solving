import sys

input = sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    s = input().strip()
    ans=float('inf')
    if(len(s)<=2):
        print(int(s))
    else:
        tara = ["*","+"]
        for symbol in tara:
            sy = symbol
            for i in range(1,n):
                cal = [s[0]]
                cal.append(sy)
                for j in range(1,n):
                    if j==i and s[i-1]!="0":
                        cal.pop()
                        sy=cal.pop()
                        cal.append(s[i-1:i+1])
                    else:
                        cal.append(s[j])
                    cal.append(sy)
                    sy = "*" if sy=="+" else "*"
                cal.pop()       
                ans=min(ans,eval("".join(cal)))
        
            print(ans)
                    
                    
                    
                
