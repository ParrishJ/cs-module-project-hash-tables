class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

    def find(self, value):
        #returns node with value
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            else:
                curr = curr.next
        return None


    def delete(self, value):
        
        
        curr = self.head

        #special case if we need to delete the head
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr


        # General case ( we are not removing from head )
        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return None
            else:
                prev = curr 
                curr = prev.next

        return None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def insert_at_head_or_overwrite(self, node):
        existing_node = self.find(node.value)
        if existing_node != None:
            existing_node.value = node.value
        else:
            self.insert_at_head(node)

a = Node(1)
b = Node(2)
c = Node(3)

ll = LinkedList()

ll.insert_at_head(a)
ll.insert_at_head(b)
ll.insert_at_head(c)
print(ll.head)