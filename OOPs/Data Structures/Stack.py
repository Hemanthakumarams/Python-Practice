class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self,data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Pushed node data is {self.top.data}")

    def pop(self) ->int:
        #Empty Stack
        if(self.top == None):
            print("Stack is Empty")
            return -100
        
        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Poped node data is {data}")
        return data
    
    def peek(self) ->int:
        #Empty Stack
        if(self.top == None):
            print("Stack is Empty")
            return -100
        print(f"The top node data is {self.top.data}")
        return self.top.data
    
    def get_count(self)->int:
        print(f"The number of present nodes are {self.count}")
        return self.count
    
    def print_all_nodes(self):
        #Empty Stack
        if(self.top == None):
            print("Stack is Empty")
            return
        
        current_node = self.top
        while(current_node != None):
            print(f"{current_node.data}")
            current_node = current_node.next

if __name__ == "__main__":
    stack = Stack()

    stack.pop()
    stack.print_all_nodes()
    stack.get_count()
    stack.peek()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.print_all_nodes()
    stack.pop()
    stack.pop()

    stack.peek()
    stack.get_count()
