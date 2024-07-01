from collections import defaultdict, deque
n =int(input())
word = input()
unique= set(word)
entered = set()

counter=defaultdict(int)

size=n
right,left=0,0

while right<n:
    entered.add(word[right])
    counter[word[right]]+=1
    while len(entered)==len(unique) and left<=right:
        size=min(size,right-left+1)
        temp=word[left]
        if counter[temp]==1:
            entered.remove(temp)
        counter[word[left]]-=1
        left+=1
    right+=1   
print(size)