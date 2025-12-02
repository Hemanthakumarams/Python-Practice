class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self,data):
        new_node = Node(data)

        #insert from the rear
        print(f"Insert value {data} into the queue")

        #case1:If queue is empty
        if(self.rear == None):
            self.front = new_node

        else:
            #case2:Queue has some nodes/elements
            #current rear node 
            self.rear.next = new_node

        self.rear = new_node
        self.count += 1
    
    def dequeue(self)->int:
        #case1:If queue is empty
        if(self.front == None):
            print("Queue is empty")
            return -100
        
        #Queue has some elements
        #Take a copy of the data 
        #Move to the next node
        return_data = self.front.data
        self.front = self.front.next

        #if there was only one element,queue become empty
        #in such case both rear and front become None
        if self.front == None:
            self.rear = None
        self.count -= 1
        print(f"Removing element {return_data} from the queue")
        return return_data
    
    def peek(self)->int:
        #case1:If queue is empty
        if(self.front == None):
            print("Queue is empty")
            return -100
        return self.front.data
    
    def get_count(self):
        return self.count
    
    def print_all_element(self):
        #case1:If queue is empty
        if(self.front == None):
            print("Queue is empty")
            return
        
        current_node = self.front
        print("Element in the queue")
        while  current_node != None:
            print(f"{current_node.data}-->")
            current_node = current_node.next

if __name__ =="__main__":
    my_queue = Queue()

    my_queue.dequeue()
    my_queue.print_all_element()
    my_queue.get_count()

    my_queue.enqueue(10)
    my_queue.print_all_element()
    my_queue.get_count()
    my_queue.dequeue()

    my_queue.enqueue(20)
    my_queue.enqueue(30)
    my_queue.enqueue(40)
    my_queue.enqueue(50)
