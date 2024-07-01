
maxWeight=8
weights=[2,3,4,5]
values=[1,2,5,6]
row=len(weights)+1
col=maxWeight+1

board=[[0]*col for _ in range(row)]

for i in range(1,row):
    for w in range(1,col):
        index=w-weights[i-1]
        if index>=0 and index<col:
            board[i][w]=max(board[i-1][w],board[i-1][index]+values[i-1])
        else:
             board[i][w]= board[i-1][w]
        
print(board)