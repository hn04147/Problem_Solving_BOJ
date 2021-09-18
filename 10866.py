import sys

n = int(sys.stdin.readline())
deque =[]
def deque_push_back(x):
    deque.append(x)
def deque_push_front(x):
    global deque
    deque = [x] + deque
def deque_pop_front():
    if not deque:
        print(-1)
    else:
        print(deque.pop(0))
def deque_pop_back():
    if not deque:
        print(-1)
    else:
        print(deque.pop())

def deque_size():
    print(len(deque))
def deque_empty():
    if not deque:
        print(1)
    else:
        print(0)
def deque_front():
    if not deque:
        print(-1)
    else:
        print(deque[0])
def deque_back():
    if not deque:
        print(-1)
    else:
        print(deque[-1])

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque_push_front(command[1])
    elif command[0] == 'pop_front':
        deque_pop_front()
    if command[0] == 'push_back':
        deque_push_back(command[1])
    elif command[0] == 'pop_back':
        deque_pop_back()
    elif command[0] == 'empty':
        deque_empty()
    elif command[0] == 'size':
        deque_size()
    elif command[0] == 'front':
        deque_front()
    elif command[0] == 'back':
        deque_back()