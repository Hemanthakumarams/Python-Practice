class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        
        #list is empty
        if self.head == None:
            self.head = new_node
            return
        
        #list has a nodes
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return
    
    def insert_at_end(self,data):
        new_node = Node(data)

        #list is empty
        if self.head == None:
            self.head = new_node
            return
        
        # list has only one node
        if self.head.next == None:
            new_node.prev = self.head
            self.head.next = new_node
            return
        
        #list has 2 or more nodes
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next

        new_node.prev = last_node
        last_node.next = new_node

    def insert_at_position(self,data,target_position):
        if target_position <= 0:
            print("Invalid Position")
            return
        if self.head == None and target_position != 1:
            print("Invalid Position")
            return
        if target_position == 1:
            self.insert_at_beginning(data)
            return
        if self.head.next == None and target_position > 2:
            print("Invalid Position")
            return
        current_node = self.head
        current_position = 1
        while (current_node != None and current_position < target_position-1):
            current_node = current_node.next
            current_position += 1
        if current_node == None:
            print("Invalid Position")
            return
        new_node = Node(data)
        #These are needed for insert at between 2 nodes
        if current_node.next != None:
            new_node.next = current_node.next
            current_node.prev = new_node
        #These are needed for insert both at between and end of 2 nodes
        current_node.next = new_node
        new_node.prev = current_node

    def print_all_nodes(self):
        #Case1:Empty List
        if (self.head == None):
            print("List is Empty")
            return
        
        #Case:List is not empty
        current_node = self.head
        while(current_node != None):
            print(f"<--{current_node.data}-->",end=" ")
            current_node = current_node.next

    def Search(self,key):
        #Case1:Empty list
        if self.head == None:
            print("Key is not found.Because List is empty")
            return
        
        #Case2:List has one or more nodes
        current_node = self.head
        while(current_node != None):
            if current_node.data == key:
                print("Key is found")
            current_node = current_node.next
            return
        #if we reach here,key is not found
        print("Key is not found")

    def delete_at_beginning(self):
        #List is empty
        if self.head == None:
            print("List is empty")
            return
        
        #List has only one element
        if self.head.next == None:
            self.head=None
            return
        #List have 2 or more nodes
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        #List is empty
        if self.head == None:
            print("List is empty")
            return
        #List has only one element
        if self.head.next == None:
            self.head=None
            return
        
        #List have 2 or more nodes
        last_node = self.head
        while(last_node.next.next != None):
            last_node = last_node.next
        last_node.next = None
    
    def delete_at_position(self,target_position):
        #1.List is empty
        if self.head == None:
            print("List is empty")
            return
        #2.Invalid position
        if target_position <= 0:
            print(f"Position {target_position} is invalid")
            return
        #3.Only one node
        if self.head.next == None:
            self.head=None
            return
        #4.List hava multiple nodes
        current_position = 1
        to_be_delete = self.head
        while(current_position < target_position and to_be_delete is not None ):
            current_position += 1
            to_be_delete = to_be_delete.next
        if (to_be_delete == None):
            print(f"Target position {target_position} is invalid, we have lesser no.of nodes")
            return
        #4.1 to_be_delete node is at last node
        if(to_be_delete.next == None):
            to_be_delete.prev.next = None
            return
        #4.2 to_be_delete is at between the 2 nodes
        to_be_delete.next.prev = to_be_delete.prev
        to_be_delete.prev.next = to_be_delete.next

#Driver code to test the above class
def insert_at_beginning_test(dlist:DoublyLinkedList):
    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)

def insert_at_end_test(dlist:DoublyLinkedList):
    dlist.insert_at_end(40)
    dlist.insert_at_end(50)
    dlist.insert_at_end(60)

def insert_at_position_test(dlist:DoublyLinkedList):
    dlist.insert_at_position(10,-2)
    dlist.insert_at_position(10,0)
    dlist.insert_at_position(10,5)
    dlist.insert_at_position(10,1)
    dlist.insert_at_position(20,2)
    dlist.insert_at_position(30,10)
    dlist.insert_at_position(30,3)
    dlist.insert_at_position(40,2)

def print_all_nodes_test(dlist:DoublyLinkedList):
    dlist.print_all_nodes()
    dlist.insert_at_beginning(10)
    dlist.print_all_nodes()

    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.print_all_nodes()

def Search_test(dlist:DoublyLinkedList):
    dlist.Search(10)
    dlist.insert_at_beginning(10)
    dlist.Search(10)

def delete_at_beginning_test(dlist:DoublyLinkedList):
    dlist.delete_at_beginning()

    dlist.insert_at_beginning(10)
    dlist.delete_at_beginning()

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.delete_at_beginning()
    dlist.delete_at_beginning()

def delete_at_end_test(dlist:DoublyLinkedList):
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.delete_at_end()

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.delete_at_end()
    dlist.delete_at_end()

def delete_at_position_test(dlist:DoublyLinkedList):
    dlist.delete_at_position(2) #empty list

    dlist.insert_at_beginning(10)
    dlist.delete_at_position(-1)  #invalid target position

    dlist.delete_at_position(1)   #only one node present

    dlist.insert_at_beginning(10)
    dlist.insert_at_beginning(20)
    dlist.insert_at_beginning(30)
    dlist.insert_at_beginning(40)
    dlist.insert_at_beginning(50)

    dlist.delete_at_position(8)   #invalid target position
    dlist.delete_at_position(3)
    dlist.delete_at_position(2)

#This is the main block to invoke the driver method
if __name__ == "__main__":
    dlist = DoublyLinkedList()
    # insert_at_beginning_test(dlist)
    # insert_at_end_test(dlist)
    # insert_at_position_test(dlist)
    # print_all_nodes_test(dlist)
    Search_test(dlist)
    # delete_at_beginning_test(dlist)
    # delete_at_end_test(dlist)
    # delete_at_position_test(dlist)