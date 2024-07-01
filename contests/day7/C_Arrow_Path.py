for _ in range(int(input())):
    size=int(input())
    s1=input()
    s2=input()
    string=[s1,s2]
    jump = lambda x:1-x
    def play(row,col):
        if string[row][col]==".":
            return False
        if row>=1 and col>=size-1:
            return True
        for i in range(2):
            temp=string[i][col]
            if temp=="<":
                
    if play(0,0):
        print("YES")
    else:
        print("NO")