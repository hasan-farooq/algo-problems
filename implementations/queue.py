

# Circular Queue 

class Queue:

    def __init__(self,capacity = 10):
        self.data = [None] * capacity 
        self.size = 0
        self.capacity = capacity
        self.first = 0
        self.next = 0

    def push(self, data):
        if (self.size < self.capacity):
            if(self.next == self.capacity):
                self.next = 0
            self.data[self.next] = data
            self.size = self.size + 1
            self.next = self.next + 1
    
    def pop(self):
        if (self.size >= 0):
            self.data[self.first] = None
            self.size = self.size - 1
            if(self.first == self.capacity-1):
                self.first = 0
            else:
                self.first = self.first + 1

    def top(self):
        if(self.size >= 0):
            return self.data[self.first]

    def is_empty(self):
        if(self.size <= 0):
            return True

    def is_full(self):
        if(self.size >= self.capacity):
            return True

    def prints(self):
        print(self.data)


def baby_sit(hashtable : dict, queue : Queue):
    times = []
    running_time = 0
    for kid,time in hashtable.items():
        queue.push(kid)
        times.append(time)
    print(times)
    queue.prints()
    print()
    while(not queue.is_empty()):
        temp_kid = queue.top()
        temp_time = hashtable.get(temp_kid)

        if(temp_time > 0):
            running_time = running_time + 2
            queue.pop()
            hashtable[temp_kid] = temp_time - 2
            queue.push(temp_kid)
        else:
            print("Kid : ", temp_kid, "| Time : ",  running_time-2)
            queue.pop()


obj = Queue()
hashtable = {1:20, 2:10, 3:45, 4: 30, 5: 5, 6: 20}
baby_sit(hashtable,obj)

