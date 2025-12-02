#class which represents the node in the singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#class impliments all the operation for singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None


        #This method add the node at the beginning
        #This needs to handle the two scenarios/cases
        #1)When list is empty
        #2)List has some elements
    def insert_at_beginning(self,data):
        # create new node
        new_node = Node(data)

        #case-1 :If the list is empty ,make the new node as head
        if self.head == None:
            self.head = new_node
            return
        #case-2: If the list is not empty,make the new node as head and point to the old head
        new_node.next = self.head
        self.head = new_node
        return
    

    def insert_at_end(self,data):
        new_node = Node(data)

        #list is empty
        if self.head == None:
            self.head = new_node
            return
        
        #list has one element
        if self.head.next == None:
            self.head.next = new_node
            return
        
        #list has 2 or more elements
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node
        return
    
    def print_list(self):
        #list is empty
        if self.head == None:
            print("List is Empty")
            return
        
        current_node = self.head
        while current_node != None:
            print(str(current_node.data)+ "-->")
            current_node = current_node.next


    def search_list(self,key):
        #list is empty
        if self.head == None:
            print("List is Empty")
            return
        
        current_node = self.head
        while current_node != None:
            if current_node.data == key:
                print("Given Key is present at a list")
                return
            current_node = current_node.next
        print("Given Key is not present at list")

    def delete_at_beginning(self):
        #list is empty
        if self.head == None:
            return
        
        #list has only one element
        if self.head.next == None:
            self.head = None
            return
        
        #list has 2 or more nodes
        self.head = self.head.next

    def delete_at_end(self):
        #list is empty
        if self.head == None:
            return
        
        #list has only one element
        if self.head.next == None:
            self.head = None
            return
        
        #list has 2 or more nodes
        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None


    def insert_at_position(self, data, insert_position):
        # Position is invalid 
        if (insert_position <= 0):
            print("Invalid position")
            return
        
        # Insert at the first position
        if (insert_position == 1):
            self.insert_at_beginning(data)
            return

        # Insert at positions 2 or greater 
        current_node = self.head
        current_position = 1

        while current_position < insert_position-1 and current_node is not None:
            current_position = current_position + 1
            current_node = current_node.next
        
        if (current_node == None):
            print("Invalid position, there are lesser number of nodes")
            return
        
        new_node = Node(data)
        new_node.next = current_node.next #1
        current_node.next = new_node #2
        

    def delete_at_position(self, delete_position):
        # Position is invalid 
        if (delete_position <= 0):
            print("Invalid position")
            return
        
        # Insert at the first position
        if (delete_position == 1):
            self.delete_at_beginning()
            return

        # Insert at positions 2 or greater 
        current_node = self.head
        current_position = 1

        while current_position < delete_position-1 and current_node is not None:
            current_position = current_position + 1
            current_node = current_node.next
        
        if (current_node == None):
            print("Invalid position, there are lesser number of nodes")
            return
        
        current_node.next = current_node.next.next


#Driver code to test the above class

def insert_at_begenning_driver_code(list:SinglyLinkedList):
    print("Head node data is :", list.head)

    list.insert_at_begenning(10) 
    list.insert_at_begenning(20)
    list.insert_at_begenning(30)

    print("List created successfully")
    print("Head node data is :", list.head.data)
    print("Head node data is :", list.head.next.data)
    print("Head node data is :",list.head.next.next.data)

def insert_at_end_driver_code(list: SinglyLinkedList):
    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)
    list.insert_at_end(40)


def print_search_driver_code(list:SinglyLinkedList):
    list.print_list()
    list.insert_at_begenning(10)
    list.print_list()

    list.insert_at_begenning(20)
    list.insert_at_begenning(30)
    list.print_list()

    list.search_list(50)
    list.search_list(20)


def delete_operation_start_end(list:SinglyLinkedList):
    list.delete_at_begenning()
    list.delete_at_end()

    list.insert_at_begenning(10)
    list.delete_at_begenning()

    list.insert_at_begenning(20)
    list.delete_at_end()

    list.insert_at_begenning(10)
    list.insert_at_begenning(20)
    list.insert_at_begenning(30)
    list.delete_at_end()
    list.delete_at_end()
    list.delete_at_end()


def insert_delete_at_given_position(list: SinglyLinkedList):
    list.insert_at_position(10, -1)
    list.delete_at_position(-1)

    list.insert_at_position(10, 1)
    list.delete_at_position(1)

    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)

    list.insert_at_position(15, 2)
    list.insert_at_position(40, 4)
    list.insert_at_position(100, 10)





#This is the main block to invoke the driver method
if __name__ == "__main__":
    #create a new singly linked list
    list = SinglyLinkedList()


    # insert_at_begenning_driver_code(list)
    
    # print_search_driver_code(list)

    # delete_operation_start_end(list)

    # insert_delete_at_given_position(list)

    insert_at_end_driver_code(list)
