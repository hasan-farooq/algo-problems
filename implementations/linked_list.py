

class Node:

    def __init__(self, key = None, data=None, next=None, prev=None):
        self.data = data
        self.key = key
        self.next = next
        self.prev = prev


class Doubly_Cirucular_Linked_List:

    def __init__(self):
        self.head = Node(key = None)
        self.tail = Node(key = None)
        self.size = 0

    def insert_at_end(self, key, data):
        new_node = Node(key = key, prev=None, next=None, data=data)

        if(self.size == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.tail.next = self.head
        self.head.prev = self.tail
        self.size = self.size + 1
        return

    def print_forwards(self):
        print("Size : ", self.size)
        if self.head != None:
            current = self.head  # current points to head
            while (current != self.tail):
                print("Key : " ,current.key, " | Data : ", current.data)
                current = current.next
            print("Key : " ,current.key, " | Data : ", current.data)

        return

    def print_backwards(self):
        print("Size : ", self.size)
        if self.head != None:
            current = self.tail  # current points to head
            while (current != self.head):
                print("Key : " ,current.key, " | Data : ", current.data)
                current = current.prev
            print("Key : " ,current.key, " | Data : ", current.data)
        return

def help_meet(meetings : Doubly_Cirucular_Linked_List):
    record = {}
    current = meetings.head
    last_met = 1
    can_skip = True
    print("\n            Day Starts....\n")
    for turn in range(1,meetings.size+1):           #turn is the last time meeting
        if current.key not in record:
            record.update({current.key : last_met})
            print('Turn ', last_met, ' : ', current.data)
            last_met = last_met + 1
        elif current.key != (max(record, key = record.get)):
            record.update({current.key : last_met})
            print('Turn ', last_met, ' : ', current.data)
            last_met = last_met + 1
            # print(record.get(current.key))
            # print(max(record, key = record.get))   #gets minimum value from dict
        else:
            if(can_skip):
                print('haha...skipped')
                can_skip = False
            else:
                record.update({current.key : last_met})
                print('Turn ', last_met, ' : ', current.data)
                last_met = last_met + 1
                can_skip = True
            
            # turn = turn - 5
        current = current.next

    print('\nTotal People Met : ', last_met-1, "\n")


mylist = Doubly_Cirucular_Linked_List()
mylist.insert_at_end(key = 1, data = "Hasan")
mylist.insert_at_end(key = 2, data = "Ali")
mylist.insert_at_end(key = 3, data = "Ahmed")
mylist.insert_at_end(key = 4, data = "Aisha")
mylist.insert_at_end(key = 5, data = "Hamaad")
mylist.insert_at_end(key = 6, data = "Noob")
mylist.insert_at_end(key = 5, data = "Hamaad")
mylist.insert_at_end(key = 5, data = "Hamaad")
mylist.insert_at_end(key = 5, data = "Hamaad")
mylist.insert_at_end(key = 6, data = "Noob")
mylist.insert_at_end(key = 4, data = "Aisha")
mylist.insert_at_end(key = 6, data = "Noob")

# mylist.print_forwards()
help_meet(mylist)






