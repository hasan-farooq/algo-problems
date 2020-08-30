

class Stack:
    
    def __init__(self):
        self.data = []
        self.keys = {}
        self.size = 0

    def push(self, data):
        self.data.append(data)
        # self.data[self.size] = data
        if data in self.keys:
            count = self.keys.get(data)
            self.keys.update({data : count + 1})
        else:
            self.keys.update({data : 1})

        self.size = self.size + 1

    def pop(self):
        if(self.size > 0):
            data = self.data[self.size-1]
            count = self.keys.get(data)
            if count > 1:                       #one time occurence only
                self.keys.update({data : count - 1})
            else:
                del self.keys[data]

            self.data.pop()
            self.size = self.size - 1
        
    def pop_lf(self):
        if (self.size > 0):
            minimum = min(self.keys, key = self.keys.get)   #min key
            count = self.keys.get(minimum)
            if (self.keys.get(minimum) <= 1):
                del self.keys[minimum]
            else:
                self.keys.update({data : count - 1})
            self.data.remove(minimum)
            self.size = self.size - 1
            
    def pop_min(self):
        if(self.size > 0):
            minimum = float("inf")        #positive infinity
            for key in self.keys:
                if (key < minimum):
                    minimum = key
        
        count = self.keys.get(minimum)        
        self.data.remove(minimum)
        
        if (self.keys.get(minimum) <= 1):
            del self.keys[minimum]
        else:
            self.keys.update({minimum : count - 1})
        
        self.size = self.size - 1




    def prints(self):
        print(self.keys)
        print(self.data)



obj = Stack()
obj.pop()
obj.push(5)
obj.push(5)
obj.push(2)
obj.push(4)
obj.push(5)
obj.push(4)
obj.push(4)
obj.prints()
obj.pop()
obj.prints()
obj.pop_lf()
obj.prints()
obj.push(4)
obj.prints()
obj.pop_min()
obj.prints()


