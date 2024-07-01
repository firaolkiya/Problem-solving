for _ in range(int(input())):
    n = int(input())
    
    ans=["-1"]
    run = []
    runSum = [0]
    def back(num):
        if runSum[0]==n:
            x="".join(run)
            if int(x)<int(ans[0]) or ans[0]=="-1":
                ans[0]= x
            return
        for i in range(num,10):
            run.append(str(i))
            runSum[0]+=i
            back(i+1)
            run.pop()
            runSum[0]-=i
    back(1)
    print("".join(ans[0]))
        
    
    
    
    