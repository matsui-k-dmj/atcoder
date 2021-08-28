from collections import deque

# Queue
queue = deque()
queue.append(0)
queue.append(1)

print(queue.popleft())


# Stack
stack = deque()
stack.append(0)
stack.append(1)

print(stack.pop())
