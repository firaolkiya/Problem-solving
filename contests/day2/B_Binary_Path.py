import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def change(char):
        if char!="z":
            return "a"
        else:
            return chr(ord(char)+1)
    s= input()
    list1=list(s)
    for i in range(1,len(s)-1):
        if list1[i]==list1[i-1] and list1[i]==list1[i+1]:
            list1[i]=[change(list1[i])]
        elif list1[i]==list1[i-1]:
            if change[list1[i-1]]!=
        
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
