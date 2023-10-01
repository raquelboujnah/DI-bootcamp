#exercise-1
from queue import PriorityQueue
def task_queue():
    queue = PriorityQueue()
    queue.put((2, 'Clean room'))
    queue.put((1, 'Do homework'))
    first_task = queue.get()
    print(first_task)
    queue.put(first_task)
    

task_queue()
    


# #exercise-2
# from collections import deque

# def is_palindrome(word):
#     word_queue = deque()
#     word = word.replace(" ", "").lower()
#     for x in word:
#         word_queue.append(x)
#     if word_queue.popleft() == word_queue.pop():
#         return True
#     else:
#         return False
    
# print(is_palindrome("helleh"))

#exercise-3

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node: Node):
        last_node = self.find_last_node()
        last_node.next = node

    def find_last_node(self):
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        return last_node 

def merge_sorted_linked_lists(linkdelist1, linkdelist2):
    dummy = Node(0)
    linkedlist3 = LinkedList()
    linkedlist3.head = dummy
    node3 = dummy
    
    node1 = linkdelist1.head
    node2 = linkdelist2.head
    while node1 is not None and node2 is not None:
        if node1 is None:
            node3.next = node2
        elif node2 is None:
            node3.next = node1
        else:
            if node1.value <= node2.value:
                node3.next = node1 
                node1 = node1.next
            elif node1.value > node2.value:
                node3.next = node2
                node2 = node2.next

            node3 = node3.next
            

        
        
linkdelist1 = LinkedList()
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
linkdelist1.head = node1
linkdelist1.append(node2)
linkdelist1.append(node3)
linkdelist2 = LinkedList()
node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
linkdelist2.head = node1
linkdelist2.append(node2)
linkdelist2.append(node3)
linkdelist3 = merge_sorted_linked_lists(linkdelist1, linkdelist2)

