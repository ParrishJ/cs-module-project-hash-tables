import math
import unittest

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
            currStr += f'{str(curr.value)} -> '
            curr = curr.next
        return currStr

    def find(self, key):
        #returns node with value
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            else:
                curr = curr.next
        return None


    def delete(self, key):
        
        curr = self.head

        #special case if we need to delete the head
        if curr.key == key:
            self.head = curr.next
            curr.next = None
            return curr


        # General case ( we are not removing from head )
        prev = None

        while curr != None:
            if curr.key == key:
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
        existing_node = self.find(node.key)
        if existing_node != None:
            existing_node.value = node.value
        else:
            self.insert_at_head(node)


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0 

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return float(self.size / self.get_num_slots())

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):

        hash = 5381
        
        for char in key:
            unicode_point = ord(char)

            hash = ((hash << 5) + hash) + unicode_point
        
        return hash & 0xffffffff

    
    """ Another implemenation of this algo """
    """ def djb2(self, key):
        
        hash = 5381

        for char in key:
            unicode_point = ord(char)

            hash = (hash * 33) + unicode_point

        return hash """
    


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!check to see if load factor is greater than 0.7, resize to double if so 
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        new_hash_index = self.hash_index(key)

        """ if self.storage[new_hash_index] == None:
            self.size += 1

        self.storage[new_hash_index] = value """

        # With collision resolution
        # If no linked list implemented, implement linked list, attach with reference (insert reference into hashed index), add node to head 
        # If linked list implemented, insert_at_head_or_overwrite

        if self.storage[new_hash_index] == None:
            new_list = LinkedList()
            new_list.insert_at_head(HashTableEntry(key, value))
            self.storage[new_hash_index] = new_list
            self.size += 1 
        else:
            """ if self.storage[new_hash_index].find(key) != None:
                self.size += 1 """
            if self.storage[new_hash_index].find(key) == None:
                self.size += 1
            self.storage[new_hash_index].insert_at_head_or_overwrite(HashTableEntry(key, value))
            
            



    def delete(self, key):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!check to see if load factor is less than 0.2, resize to half if so 
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        new_hash_index = self.hash_index(key)

        if self.storage[new_hash_index] != None:
            self.storage[new_hash_index].delete(key)
            self.size -= 1

        if self.storage[new_hash_index] == None:
            print("No Key Found")

        # self.storage[self.hash_index(key)] = None

        # return self.storage[self.hash_index(key)]
        

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        new_hash_index = self.hash_index(key)
        node = self.storage[new_hash_index].find(key)

        return node.value
        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # first make new list, set to new_storage
        # then run logic copying everything from curr storage to new storage
        # then reassign self.storage at end. 

        """ temp_storage = self.storage

        self.storage = [None] * new_capacity
        self.capacity = new_capacity

        for item in temp_storage:
            self.put("???", "???") """
        
        temp_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity 
        


        for ll in temp_storage:
            if ll != None:
                curr = ll.head
                while curr != None:
                    self.put(curr.key, curr.value)
                    curr = curr.next


        


    def __str__(self):
            return f"Storage: {self.storage}"

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")




ht = HashTable(8)


ht.put("key-0", "val-0")
ht.put("key-1", "val-1")
ht.put("key-2", "val-2")
ht.put("key-3", "val-3")
ht.put("key-4", "val-4")
ht.put("key-5", "val-5")
ht.put("key-6", "val-6")
ht.put("key-7", "val-7")
ht.put("key-8", "val-8")
ht.put("key-9", "val-9")
ht.put("key-10", "val-10")
ht.put("key-10", "val-!!!!!")
print(ht.size)
print(ht)




