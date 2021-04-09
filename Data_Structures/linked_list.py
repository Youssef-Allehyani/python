class Node:
    data = None
    next_Node = None
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return f"Node data: {self.data}" 





class Linked_list:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None       


    def size(self):
        current = self.head
        count = 0 

        while current :  #current != none
            count +=1
            current = current.next_Node
        return count 
    def add(self, data):
        new_node = Node(data)   
        new_node.next_Node = self.head
        self.head = new_node

    def search(self,key):  
          current = self.head
          Node.next_Node
          while current:
            if current.data == key:
              return current 
            else:
              current =  current.next_Node
          return None
    def insert (self,data,index):
        if  index == 0 :
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1 :
                current = current.next_Node
                position -= 1

            prev_node = current
            next_node = current.next_Node

            prev_node.next_Node = new 
            new.next_Node = next_node
    def remove(self,key):
        current = self.head 
        previons = None
        found = False
        while current and not found:
            if current.data == key and current is self.head :
                self.head = current.next_Node
                found = True
            elif current.data == key :
                previons.next_Node = current.next_Node
                found = True
            else:
                previons = current
                current = current.next_Node     
        return current   
    def node_at_index(self,index):       
        if index ==  0 :
            return self.head
        else:
            current = self.head
            position = 0

            while position < index :
                current = current.next_Node  
                position +=1
        return current     

    def __repr__(self):
        Nodes = []
        current = self.head 

        while current:
            if current is self.head :
                Nodes.append(f"[Head: {current.data}]")
            elif current.next_Node is None :
                Nodes.append(f"[Tail: {current.data}]")
            else:       
              Nodes.append(f"[{current.data}]")

            current = current.next_Node
            
        return ('->').join(Nodes)      






# N1 =Node(10)
# N2 = Node(20)
# N1.next_Node = N2
# l1 = Linked_list()
# l1.head = N1
# l1.add(3)
# l1.add(80)
# l1.add(90)

# # print(l1.head)
# print(l1)
# l1.insert(76,3)
# print(l1)
# l1.remove(3)
# print(l1)
# l1.insert(3,2)
# print(l1.head)
