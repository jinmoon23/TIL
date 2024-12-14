'''
Queue
'''
#
# N = 10
# q = [0] * N
# front = -1
# rear = -1
#
# rear += 1
# q[rear] = 1
# rear += 1
# q[rear] = 2
# rear += 1
# q[rear] = 3
#
# front += 1
# print(q[front])
# front += 1
# print(q[front])
# front += 1
# print(q[front])

Q_SIZE = 4
cQ = [] *4
front = rear = 0
#enqueue(1,2,3)
rear = (rear+1)%Q_SIZE
cQ[rear] = 1
rear = (rear+1)%Q_SIZE
cQ[rear] = 2
rear = (rear+1)%Q_SIZE
cQ[rear] = 2

#dequeue
front = (front+1)%Q_SIZE
print(cQ[front])
front = (front+1)%Q_SIZE
print(cQ[front])
front = (front+1)%Q_SIZE
print(cQ[front])


