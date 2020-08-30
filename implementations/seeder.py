

"""
Nodes : Seeders with IDs & Files
    -Because we need to separate each seeder and one seeder my have more files too

Vertices : ID's of Seeders
    - Because it makes the list operations easier

Weights : None
    -We're assuming cost of 1 at each edge. Weight doesn't matter because ...
        - we're doing a Traversal Problem
        - our cost is measured by far/near seeders not by weights on edge

Type : Undirected/Bi-Directional
    - Every Seeder (nodes) is available to everyone. So bi-directional or undirected

Representation : Linked List
    - Matrix can help us see the connection in O(1) & We can bear the O(V-sqaure) for traversal
    - But extending a Matrix is the main issue... Seeders will be increasing again & again...
    - Also, by using hashing, we can access the element in O(1) even in List Representation

Traversal : Breadth First
    - DFS (I think) will work but that's like forcing DFS to behave like BFS
    - So, I think going with a DFS is fine but makes things complicated un-necessarily
    - BFS, however, is in nature more like going layer by layer instead of digging down till end
"""


'''
Following is a simple graph implemetation.
'''
class Seeder:
    def __init__(self,filename=None,id=None):
        self.filename = filename
        self.id = id


class Graph:
    def __init__(self,vertices={}):
        self.vertices = vertices
    
    def add_vertex(self,data):
        flag = self.vertices.get(data)
        if(flag is None):
            self.vertices.update({data:[]})

        
    def add_edge(self,source,destination):
        flag = True
        s_value = self.vertices.get(source.id)
        d_value = self.vertices.get(destination.id)
        
        for element in s_value:
            print(":",element.id)
            if element.id == destination.id:
                print(element.id,destination.id)
                flag = False
        for element in d_value:
            if element.id == source.id:
                print(".",element.id)
                flag = False
        if(flag):
            s_value.append(destination)
            d_value.append(source)
        self.vertices.update({source.id:s_value})
        self.vertices.update({destination.id:d_value})


obj = Graph()
n1 = Seeder('haha',1)
n2 = Seeder('hehe',2)
n3 = Seeder('hoho',3)

obj.add_vertex(n1.id)
obj.add_vertex(n2.id)
obj.add_vertex(n3.id)
obj.add_edge(n1,n2)
obj.add_edge(n1,n2)
obj.add_edge(n2,n1)
obj.add_edge(n3,n2)


"""
We've a queue for BFS Traversal and a graph like implemented above...

We'll input the file from the user. Then, we'll do a BFS traversal.
We'll keep count of how many nodes (seeders) have this file.

Something like : (for the search, DFS/BFS both are okay. But for cost I think BFS is better)

    visited_array = [all vertices/nodes]
    count = 0
    input = "Enter File :  "
    Start from vertex v
    queue.push(v)
    while(queue is not empty):
        Explore all edges of v
            if (visited[index_of_v] == false):
                insert in the queue
                if edge.filename == input:
                    count ++
        extract the v 
        Pick the next element (first inserted)
        v = this new element

Now we have count of seeders. We'll ask the user how many seeders does he want ?
If he tells, ok. Otherwise, we'll set a default of 5

Now, we want to select the number of seeders that will cost the least
Something like : (here I think BFS is a good choice)

    Just as above, we'll do the same traversal.
    However, we might not need to traverse the whole graph
    We'll traverse for the number of seeders
    If seeders_limit is reached stop and output the layer we're on.
    To keep track of layer, when we extract any vertex, we increment the layer
    At last we can sum all layers (arithmetic sum) or keep track of it as a variable

Why this Works ? 
    Because BFS will go level by level. So, even if we stop in between, we're not losing anything


Time Complexity : 2(V+E)

Option 2 : 

    In a single BFS, we combine the above both steps.
    Means now when we're counting the seeders, we store them in an array
    Also, we keep the track of their costs (so, we keep track of layers as well)

    visited_array = [all vertices/nodes]
    seeders_found = array or hashtable (key as seeder and value as cost)    
    count = 0, layer = 0
    input = "Enter File :  "
    Start from vertex v
    queue.push(v)
    while(queue is not empty):
        Explore all edges of v
            if (visited[index_of_v] == false):
                insert in the queue
                if edge.filename == input:
                    count ++
                    if (edge not in the seeder_found before):
                        seeders_found[edge] = layer
        layer ++ 
        extract the v
        Pick the next element (first inserted)
        v = this new element

Why this works and in a better way ?
    Here, we are cmobining both the things. And taking advantage of the BFS Pattern
    We'll magically get a sorted array of seeders (cost-wise)
    Why sorted ? because once we visit a node/vertex/seeder, we don't visit again
    This ensures that if we've visited someone on layer-1, we'll not visit it one layer-2
    Taking advantage of this sort, we can simply take first "n" seeders for the user
    Also, we can now calculate the cost easily... Sum of those seeders or arithmetic sum
    This saves saves us from another traversal

Time Complexity: (V+E) + (Seeder_Array)

"""


