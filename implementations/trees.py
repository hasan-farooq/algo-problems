

class Alphabet:
    def __init__(self, data : str = None, next = None):
        self.data = data
        self.next = next

class Node:
    def __init__(self, alphabets : Alphabet = []):
        self.alphabets = alphabets
        self.size = 0
    
    def add_letter(self, letter : str):
        new_letter = Alphabet(data=letter)
        # empty = Alphabet()
        self.alphabets.append(new_letter)
        # self.alphabets.append(empty)
        self.size += 1
        
    def index(self,letter:str):
        """
        Indexing function for dictionary
        """
        i = 0
        for alphabet in self.alphabets:
            # print(alphabet.data)
            # if(alphabet.data != None):
            if(alphabet.data == letter):
                return i
            i += 1
        return -1


class Dictionary:
    def __init__(self):
        self.root = Alphabet()

    def insert(self,word: str):
        """
        Insert a Word in the dictionary. Pass a String
        """
        i = 0
        current = self.root
        index = 0
        while(i < len(word) and index != -1 and current.next is not None):
            index = current.next.index(word[i])
            if(index != -1):                
                # print(current.data,end="|")
                # for alphabet in current.next.alphabets:
                #     if(alphabet.data is not None):
                #         print(alphabet.data,end="")
                # print()
                current = current.next.alphabets[index]
                i += 1
        if(index == -1 or current.next is None):
            while (i < len(word)):
                if(index == -1):
                    temp = Alphabet(word[i])
                    current.next.alphabets.append(temp)
                    index = current.next.index(word[i])
                else:
                    new_node = Node(alphabets=[])
                    new_node.add_letter(word[i])
                    current.next = new_node
                    index = current.next.index(word[i])
                if(index != -1):
                    current = current.next.alphabets[index]
                    i += 1

    def look_up(self, word:str):
        """
        Searches a Word in the dictionary. Pass a String
        """
        i = 0
        current = self.root
        index = 0
        while(i < len(word) and index != -1 and current.next is not None):
            index = current.next.index(word[i])
            if(index != -1):
                current = current.next.alphabets[index]                
                i += 1
            else:
                print("Not Found")
                return
        if (i < len(word)):
            print("Not Found")
        else:
            print("Found...")        
        
    def explore_letter(self,current,previous = None):
        if current.next is None:
            # print("\nExplore : ", previous.data, "|")
            print()
        else:
            previous = current
            for i in range(len(current.next.alphabets)):
                print(current.next.alphabets[i].data,end="")
                self.explore_letter(current.next.alphabets[i],previous)
                # previous = current.next.alphabets[i]

    def explore_letter_r(self,current,index,length):
        if current.next is None:
            if(index < length):
                # print(length,"|",index,"|",current.data)
                pass
            print(length,"|",index,"|",current.data)
            return current
        else:
            # print(length,"|",index,"|",current.data)
            return self.explore_letter_r(self.explore_letter_r(current.next.alphabets[index],index,length),index+1,len(current.next.alphabets))
                


my_dictionary = Dictionary()
file = open("words.txt")
for line in file:
    line = (line).rsplit("\n")
    my_dictionary.insert(line[0])

file.close()

length = len(my_dictionary.root.next.alphabets)
# my_dictionary.explore_letter(my_dictionary.root)
# my_dictionary.look_up("asympto")
my_dictionary.explore_letter_r(my_dictionary.root,0,length)


