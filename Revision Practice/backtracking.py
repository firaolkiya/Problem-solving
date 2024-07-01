##given board of chess nxn size and n queun. in how many ways can you put 
#queuens as they not atack each other
n=4

count=[0]
dig1 =[0]*(n*2)
dig2 = [0]*(2*n)
column = [0]*n
def backtrack(row):
    if row==n:
        count[0]+=1
        return
    for col in range(n):
        if column[col]==dig1[col+row]==dig2[row+n-col]==0:
            column[col]=dig1[col+row]=dig2[row+n-col]=1
            backtrack(row+1)
            column[col]=dig1[col+row]=dig2[row+n-col]=0
            
backtrack(0)   
print(count)