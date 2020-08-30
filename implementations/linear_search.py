

names = ['hasan', 'ahmed', 'ali', 'aisha', 'haseeb', 'haamad']

key = input("Enter your key : ")
flag = False
i = 0


for index in names:
    if index == key:
        names[i] = index.capitalize()
        flag = True
        print("Key Found....")
    i = i + 1

'''
Alternative for loop (c++ way)

for i in range(names.__len__()):
    if names[i] == key:
        flag = True
        print("Key Found...")
'''

if flag == False:
    print("Key Not Found....")


#print (names)

#---------------------------------------------------


names_t = ("hasan","ahmed", 'aisha','ali')
i = 0

for index in names_t:
    if index == key:
        #names_t[i] = index.capitalize()
        flag = True
        print("Key Found....")
    #i = i + 1

if flag == False:
    print("Key Not Found....")


#---------------------------------------------------


names_d = {1:"hasan",2:"ahmed", 3:'aisha',4:'ali'}
i = 0

for keys,name in names_d.items():
    if name == key:
        names_d[keys] = name.capitalize()
        flag = True
        print("Key Found....")
    i = i + 1

if flag == False:
    print("Key Not Found....")


# print(names)
# print(names_t)
# print(names_d)



def linear_search(arr,start, end,key):
    if start == end:
        return 0
    elif arr[start] == key:
        print('Found...')
        return
    else:
        linear_search(arr,start+1,end,key)
        # print('Not Found')

linear_search(names,0,len(names)-1,'asan')


