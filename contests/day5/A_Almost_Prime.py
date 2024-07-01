

def isPrime(n):
    div=2
    while div*div<=n:
        if n%div==0:
            return False
        div+=1
    return True

def countPrimeDiv(n):
    div=2
    count=0
    while div<n:
        if n%div==0 and isPrime(div):
            count+=1
        div+=1
    return count
    
n= int(input())
count=0
for i in range(1,n+1):
    if countPrimeDiv(i)==2:
        count+=1
    
print(count)
