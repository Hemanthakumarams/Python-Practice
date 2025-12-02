class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.tail = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        #Empty list
        if(self.tail == None):
            self.tail = new_node
            self.tail.next = new_node
            return
        #one or more node
        new_node.next = self.tail.next
        self.tail.next = new_node

    def insert_at_tail(self,data):
        new_node = Node(data)
        #Empty list
        if(self.tail == None):
            self.tail = new_node
            self.tail.next = new_node
            return
        #one or more node present
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

    def delete_at_beginning(self):
        #Empty list
        if(self.tail == None):
            print("Empty list")
            return
        
        #only one node is present
        if(self.tail.next == self.tail):
            self.tail = None
            return
        #two or more node are present
        self.tail.next = self.tail.next.next

    def delete_at_tail(self):
        #Empty list
        if(self.tail == None):
            print("Empty list")
            return
        #only one node
        if(self.tail.next == self.tail):
            self.tail = None
            return
        #2or more nodes
        new_tail = self.tail.next
        while(new_tail.next != self.tail):
            new_tail = new_tail.next
        new_tail.next = self.tail.next
        self.tail = new_tail

    def print_all_nodes(self):
        #Empty list
        if(self.tail == None):
            print("Empty list")
            return
        #one or more nodes
        current_node = self.tail.next
        while(True):
            print(f"{current_node.data}-->")
            if(current_node == self.tail):
                return
            current_node = current_node.next

    def Search_key(self,key):
        #Empty list
        if(self.tail == None):
            print("Empty list")
            return
        #on or more nodes
        curre_node = self.tail.next
        while(True):
            if(curre_node.data == key):
                print("Key is found")
                return
            if(curre_node == self.tail):
                break
            curre_node = curre_node.next
        # if key is not present
        print("Key is not found")


def CircularList_test(clist:CircularList):
    clist.delete_at_beginning()
    clist.insert_at_beginning(10)
    clist.delete_at_beginning()

    clist.insert_at_beginning(10)
    clist.insert_at_beginning(20)
    clist.insert_at_beginning(30)
    clist.insert_at_beginning(40)

    clist.delete_at_beginning()
    clist.delete_at_beginning()

    clist.delete_at_tail()
    clist.delete_at_tail()
    clist.delete_at_tail()

    clist.insert_at_tail(10)
    clist.insert_at_tail(20)
    clist.insert_at_tail(30)
    clist.insert_at_tail(40)

    clist.print_all_nodes()

    clist.Search_key(70)
    clist.Search_key(40)

if __name__ == "__main__":
    clist = CircularList()
    CircularList_test(clist)
