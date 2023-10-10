"""

list - > Binaray Search Tree

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

[5, 3, 8, 1, 4, 6, 9, n, 2, n, n, n, 7, n, 10]

                    [5]                     1
                 /      \                   
              [3]        [8]                2
            /   \        /   \
         [1]    [4]     [6]   [9]           3
         / \    / \     / \    / \ 
       [n] [2] [n][n] [n][7] [n] [10]       4

height = 

       
Conduct a binaray search order on parameter list and append in order
       
"""

def biTreeConstructor(lis, ordered):
    # if lis empty return
    if len(lis) == 0:
        return ordered
    # if only one num in lis
    if len(lis) == 1:
        return ordered.append(lis[0])
    
    # append middle value
    mid = len(lis) // 2
    if len(lis) % 2 == 0:
        mid -= 1
        
    ordered.append(lis[mid])

    # do same to the left
    if len(lis[:mid]) > 0:
        return biTreeConstructor(lis[:mid], ordered)

    # do same to the right
    if len(lis[mid+1:]) > 0:
        return biTreeConstructor(lis[mid+1:], ordered)
    
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = []

ans = biTreeConstructor(lis, ans)

print(ans)