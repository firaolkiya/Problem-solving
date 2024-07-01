s = input()
s=s.lower()
num = []
cons=["a","o","y","e","i","u"]
for let in s:
    if let not in cons:
        num.append(".")
        num.append(let)
print("".join(num))