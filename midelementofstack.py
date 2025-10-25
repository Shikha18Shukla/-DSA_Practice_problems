from collections import deque

def delete_middle(stack):
    items = []
    while stack:
        items.append(stack.pop())
    middle_index = len(items) // 2
    items.pop(middle_index)
    for i in range(len(items) - 1, -1, -1):
        stack.append(items[i])

if __name__ == "__main__":
    stack = deque([10, 20, 30, 40, 50])
    delete_middle(stack)
    while stack:
        print(stack.pop(), end=" ")
