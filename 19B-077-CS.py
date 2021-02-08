# PROJECT : PAIRING HEAP
# 19B-077-CS  and 19B-117-CS


# making class node
class Node:
    def __init__(self, data):
        self.data=data
        self.child=[]

# making class for min pairing heap
class min_pairingheap:
    #initializing class
    def __init__(self):
        self.root = None
        
    # inserting elements in heap according to priority, min on the root
    def Insert(self,data):
        n=Node(data)
        self.root=self.Meld(self.root,n)
        
    # finding minimum value of heap
    def Find_Min(self):
        r=self.root
        # if the heap is empty an error will occur
        if self.root is None:
            raise ValueError("Heap is empty")
        # if the heap isnt empty the min value will be returned.
        else:
            return self.root.data
        
    # merging two heap by comparing their root nodes 
    # comparing roots of heaps, min will become the root node
    def Meld(self, r1, r2):
        # if rootnode1 is none, rootnode2 will be returned and added as root node
        if r1==None:
            return r2
        # if rootnode2 is none, rootnode1 will be returned and added as root node
        elif r2==None:
            return r1
        #if rootnode1 is lesser, it will returned and become root node.
        elif r1.data > r2.data:
            r2.child.append(r1)
            return r2
        #if rootnode2 is lesser, it will returned and become root node.
        else:
            r1.child.append(r2)
            return r1
        
    # deleting minimum value
    def Delete_Min(self):
        r=self.root
        #if heap is empty error will be occured
        if r is None:
            raise ValueError("Heap is empty")
        # minimum value will be deleted using auxiliary func.
        else:
            self.root=self.merge(self.root.child)
    # auxiliary function for Delete_min
    def merge(self, h):
        if len(h)==0:
            return None
        elif len(h)==h:
            return h[0]
        else:
            return self.Meld(self.Meld(h[0], h[1]), self.merge(h[2:]))

# making class for max pairing heap          
class max_pairingheap:
    def __init__(self):
        self.root = None
        
    # inserting elements in heap according to priority, max on the root
    def Insert(self,data):
        n=Node(data)
        self.root=self.Meld(self.root,n)
    
    # finding max val of heap
    def Find_Max(self):
        r=self.root
        # if heap is empty error will occur
        if r is None:
            raise ValueError("Heap is empty")
        # if the heap isnt empty the max value will be returned.
        else:
            return r.data
    
    # merging two heap by comparing their root nodes 
    # comparing roots of heaps, min will become the root node
    def Meld(self, r1, r2):
        # if rootnode1 is none, rootnode2 will be returned and added as root node
        if r1 is None:
            return r2
        # if rootnode2 is none, rootnode1 will be returned and added as root node
        elif r2 is None:
            return r1
        #if rootnode1 is greater, it will returned and become root node.
        elif r1.data > r2.data:
            r1.child.append(r2)
            return r1
        #if rootnode2 is greater, it will returned and become root node.
        else:
            r2.child.append(r1)
            return r2
        
    # deleting maximum value, i.e, the root
    def Delete_Max(self):
        r=self.root
        # if heap is empty an error wil occur
        if r is None:
            raise ValueError("Heap is empty")
        # maximum value will be deleted
        else:
            self.root=self.merge(self.root.child)
    #auxilary function for delete_max
    def merge(self, h):
        if len(h)==0:
            return None
        elif len(h)==1:
            return h[0]
        else:
            return self.Meld(self.Meld(h[0], h[1]), self.merge(h[10:]))

#drivercode
h1=min_pairingheap()
h2=max_pairingheap()
h1.Insert(2)
h1.Insert(6)
h1.Insert(4)
h2.Insert(7)
h2.Insert(1)
h2.Insert(3)
print("min value in heap: ",h1.Find_Min())
print("max value in heap: ",h2.Find_Max())
h1.Delete_Min()
h2.Delete_Max()


#priority queue using heap for min value.
class PriorityQueue:
    def __init__(self):
        self.queue=[] 
  
    # Inserting an element in the queue without priority
    def Enqueue(self, data): 
        self.queue.append(data) 
  
    # extracting min value according to priority 
    def Dequeue_min(self): 
        q=self.queue
        if q==0:
            raise IndexError("list index out of range")
        min=0
        for i in range(len(q)): 
            if q[i]<q[min]: 
                min=i 
        item=self.queue[min] 
        del self.queue[min] 
        return item 
    
    # extracting max value according to priority
    def Dequeue_max(self): 
        q=self.queue
        if q==0:
            raise IndexError("list index out of range")
        max=0
        for i in range(len(q)): 
            if q[i]>q[max]: 
                max=i 
        item=self.queue[max] 
        del self.queue[max] 
        return item 
    
p=PriorityQueue()
p.Enqueue(2)
p.Enqueue(1)
p.Enqueue(6)
p.Enqueue(4)
print("dequed min value: ",p.Dequeue_min())
print("dequed max value: ",p.Dequeue_max())
    
