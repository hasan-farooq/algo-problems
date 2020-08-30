

import os
from tqdm import tqdm
from time import sleep
from prettytable import PrettyTable


class Record:
    def __init__(self, address = None, data = None, returned = None):
        self.address = address
        self.data = data
        self.type = type(data)
        self.returned = returned
    
    def prints(self):
        table = PrettyTable(["Attributes","Values"])
        table.align = 'c'
        table.add_row(["Address", self.address])
        table.add_row(["Data", self.data])
        table.add_row(["Data Type", self.type])
        table.add_row(["Returned", self.returned])
        print(table)

class Stack:

    def __init__(self):
        self.data = []
        self.size = 0

    def push(self, data : Record):
        self.data.append(data)
        self.data[self.size].prints()
        self.size += 1
        

    def pop(self):
        if (self.size > 0):
            # print(self.data[self.size-1].prints())
            temp = self.data[self.size-1]
            self.data[self.size-1] = None
            self.size -= 1
            
            return temp

    def is_empty(self):
        if(self.size > 0):
            return False
        else:
            return True

def simulate_recursion(memory : Stack, calls : int, base_case : int = None):
    
    result = None
    for call in range(1,calls+1):
        sleep(3)
        record = Record(address="00F" + str(call),data=call,returned= None)
        print("______________________________________")
        # print("Pushing into Stack...")
        memory.push(record)
        print("Next Call Sent... ")
        print("______________________________________")
    
    sleep(3)
    clear = lambda: os.system('clear')
    clear()
    # print(chr(27) + "[2J")
    print("\nReturning....")
    sleep(3)
    # print(chr(27) + "[2J")
        
    while(not memory.is_empty()):
        sleep(4)
        temp = memory.pop()
     
        if (temp.data == base_case):
            print("Base Case Reached.....")
            temp.returned = "Base Case"
            temp.prints()
            print()
            return

        print("______________________________________")
        # print("Popping from Stack...")
        if(result == None):
            result = 1
            temp.returned = temp.data
            result *= temp.data
        else:
            prev = result
            result *= temp.data
            temp.returned = str(prev) + "x" + str(temp.data) + "=" + str(result)
        
        temp.prints()
        print("Return Value Sent... ")
        print("______________________________________")
    


memory = Stack()
simulate_recursion(memory, 5, 1)


