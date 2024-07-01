##declarerouter class
class router:
    def __init__(self,value) -> None:
        self.connected = []
        self.value = value
##take input from list
n  =int(input())
head = router(1)
routerStore={1:head}
connection  = list(map(int,input().split(" ")))
for index in range(n-1):
    route = router(index+2)
    routerStore[connection[index]].connected.append(route)
    routerStore[index+2]=route
