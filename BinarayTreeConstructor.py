class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# [1, 2, 3]

# def dummy(list, start, end):
#     if start == end:
#         return None
    
#     if start < len(list) and end >= 0:
#         mid = (start + end) // 2
        
#     else:
#         return None

#     left_node = dummy(list, start, mid - 1)
#     right_node = dummy(list, mid + 1, end)
#     root = list[mid]
#     root.left = left_node
#     root.right = right_node
#     return root

# [1,2,3,4]
# [1,2,3,4,5]

def tree(lis, start, end):
    if start <= end:
        len = end - start
        if len % 2 == 0:
            mid = (start + end + 1) // 2
        else:
            mid = (start + end) // 2
    else:
        return None
    
    leftChild = tree(lis, start, mid-1)
    rightChild = tree(lis, mid+1, end)
    root = Node(lis[mid])
    root.left = leftChild
    root.right = rightChild

    return root



def print_root(root):
    arr = [root] # this is an array which holds all the nodes to be printed
    while len(arr) > 0:
        size = len(arr)
        while size > 0:
            # remove the head element
            curr = arr.pop(0)
            # print the current
            if curr:
                print(curr.val, " - ", end="")
            else:
                print(curr, " - ", end="")
            # add the left child to the array if exist
            if curr:
                arr.append(curr.left)
            # add the right child to the array if exist
                arr.append(curr.right)
            size = size - 1
        print()
        # once size becomes zero, that means this level has been printed.
        # Print a newline character here and goes to the next iteration



lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


head = tree(lis, 0, len(lis)-1)


print_root(head)
