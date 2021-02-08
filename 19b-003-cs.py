# Creating a node

class Node:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        llink=None
        rlink=None

   #


class PiorityQueue:

    def __init__(self):
        # Initializting Empty queue
        self.queue = []

    def Insert(self, key, priority):
        n = Node(key, priority)# for adding a value
        l = len(self.queue)
# Checking if the queue is empty
        if len(self.queue) == 0:
            self.queue.append(n)

        else:
            i = 1
            if self.queue[0].priority > priority:
                self.queue.insert(0, n)

            else:
                while(i < l and self.queue[i].priority <= priority):
                    i+=1

            self.queue.insert(i, n)
# Changes the piority of the element
    def Update(self, key, newPriority):
        for i in self.queue:
            if i.key == key:
                print("Changed priority of " + "(" + str(i.key) + "," + str(i.priority) + ") to " + str(newPriority))
                i.priority = newPriority
                return
        
        print("Node not found")
     # deletes a value           
    def Delete(self,key):
        for i in range(len(self.queue)):
            if(self.queue[i].key == key):
                del self.queue[i]
                print("Deleted node")
                return
        # if value is not in the queue
        print("Node not found")
# for showing the queue
    def Print(self):
        for i in self.queue:
            print("[" + str(i.key) + "," + str(i.priority) + "]" + "->", end="")
        
        print("\n")
# Give the element having minimum piority
    def Min(self):
        min = self.queue[0]
        for i in range(len(self.queue)):
            if self.queue[i].priority < min.priority:
                min = self.queue[i]

        print("Minimum node ny priority: ")
        print(min.key,",",min.priority)
# return the size of the qeue
    def size(self):
        return len(self.queue)
# Rlink is right most node
#Llink is the left most node
    def RLink_LLink(self):
        if len(self.queue) == 0:
            return None, None
        
        else:
            return self.queue[0], self.queue[-1]


    

# merges two queues
    def union(self,Q1,Q2):
        n1 = Q1.size() # node of Queue 1
        n2 = Q2.size() # node of Queue 2

        n3 = n1+n2 # adding two nodes
        res=0 # resultant output

        res = PiorityQueue()
    # checking which queue is smaller
        if n1 > n2:
            res.queue = Q1.queue + Q2.queue

        else:
            res.queue = Q2.queue + Q1.queue

        return  res.Print() #final output
        


# Driver Code
if __name__ == "__main__":
    # creating 2 queues
    q1 = PiorityQueue()
    q2 = PiorityQueue()

    print("----------------------------------Queue 1-------------------------------------------------------")
    q1.Insert(0,1)
    q1.Insert(0,2)
    q1.Insert(1,1)
    q1.Update(1,0)
    q1.Min()
    q1.Print()
    print("----------------------------------Queue 2-------------------------------------------------------")

    q2.Insert(5,1)
    q2.Insert(4,2)
    q2.Insert(7,3)
    q2.Insert(5,4)
    q2.Delete(8)


    q2.Print()
    print("The Union is")
    q1.union(q1,q2)

    