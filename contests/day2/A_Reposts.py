class Node:
    def __init__(self,name) -> None:
        self.name = name
        self.repost = []
n = int(input())
nodeStore = {}
head=None
for i in range(n):
    name,string,repost = input().split(" ")
    newNonde = Node(name)
    nodeStore[repost]=newNonde
    if not head:
        head=newNonde
    nodeStore[name].append(newNonde)
while head:
    print(head.name,head.repost)
    head=head.repost