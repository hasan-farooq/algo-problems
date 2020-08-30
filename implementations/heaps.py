
from copy import deepcopy


class Heap:
    def __init__(self, data: list = [0], size=0):
        self.data = data
        self.size = size

    def heap_up(self, value):
        self.data.append(value)
        self.size = self.size + 1
        parent = self.size//2
        inserted = self.size
        while(parent > 0):
            if(value > self.data[parent]):
                temp = deepcopy(self.data[parent])
                self.data[parent] = deepcopy(self.data[inserted])
                self.data[inserted] = deepcopy(temp)
                inserted = parent
                parent = parent//2
            else:
                return (inserted)
        return inserted

    def heap_down(self):
        if(self.size == 1):
            self.size -= 1
            removed = self.data[1]
            self.data.pop()
            return removed

        elif(self.size > 0):
            self.size -= 1
            size = self.size
            removed = self.data[1]
            self.data[1] = self.data[size+1]
            self.data.pop()
            parent = 1
            left = 2 * parent
            right = left + 1
            largest = self.data[parent]
            while(parent <= size):
                if(right <= size):
                    if(self.data[parent] > self.data[left] and self.data[parent] > self.data[right]):
                        return removed
                    elif(self.data[parent] > self.data[right] and self.data[parent] <= self.data[left]):
                        # largest = self.data[left]
                        temp = deepcopy(self.data[parent])
                        self.data[parent] = deepcopy(self.data[left])
                        self.data[left] = deepcopy(temp)
                        parent = left
                        left = 2 * parent
                        right = left + 1
                    elif(self.data[parent] > self.data[left] and self.data[parent] <= self.data[right]):
                        # largest = self.data[right]
                        temp = deepcopy(self.data[parent])
                        self.data[parent] = deepcopy(self.data[right])
                        self.data[right] = deepcopy(temp)
                        parent = right
                        left = 2 * parent
                        right = left + 1
                    else:
                        if(self.data[left] > self.data[right]):
                            temp = deepcopy(self.data[parent])
                            self.data[parent] = deepcopy(self.data[left])
                            self.data[left] = deepcopy(temp)
                            parent = left
                            left = 2 * parent
                            right = left + 1
                        else:
                            temp = deepcopy(self.data[parent])
                            self.data[parent] = deepcopy(self.data[right])
                            self.data[right] = deepcopy(temp)
                            parent = right
                            left = 2 * parent
                            right = left + 1

                elif(left <= size):
                    if(self.data[parent] < self.data[left]):
                        temp = deepcopy(self.data[parent])
                        self.data[parent] = deepcopy(self.data[left])
                        self.data[left] = deepcopy(temp)
                        parent = left
                        left = 2 * parent
                        right = left + 1
                    else:
                        return removed
                else:
                    return removed 

    def delete(self):
        min = self.heap_down()
        return min

    def insert(self, value):
        self.heap_up(value)

    def is_empty(self):
        if(self.size <= 1):
            return True
        else:
            return False

    def update_priority(self):
        removed = self.heap_down()
        removed -= 1
        self.heap_up(removed)

    def maximum(self):
        return self.data[1]


"""
This heap is not suited for keys (we've to manage one more hashtable or list etc)
So, the question can not be implemented with this.
Here's the pseudocode, however, for the question

here the queue is Priority Queue with Heaps

It is nearly same as the Queues one but we are doing it w.r.t Priority

while(not queue.is_empty()):
        temp_kid = queue.maximum()
        temp_time = hashtable.get(temp_kid)

        if(temp_time > 0):
            running_time = running_time + 2
            queue.update_priority()
            hashtable[temp_kid] = temp_time - 2
            queue.insert(temp_kid)
        else:
            print("Kid : ", temp_kid, "| Time : ",  running_time-2)
            queue.delete()

"""


obj = Heap()

obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(12)
obj.insert(42)
print(obj.maximum())
obj.insert(32)
obj.delete()
obj.update_priority()
print(obj.data)

