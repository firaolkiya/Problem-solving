from os import name
import sys
from sys import setrecursionlimit, stdin
import threading
input = sys.stdin.readline

def main():
   pass

if name == 'main':
    setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()
                
    

    
