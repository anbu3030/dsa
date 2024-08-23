class Stack:

    def __init__(self,num):
        self.num=num
        self.stack=[]

    def printing(self):
        print(self.stack)

    def lenth(self):
        return len(self.stack)

    def push(self,put):
        if self.lenth()<self.num:
            self.stack.append(put)

        else:
            print("stack overflow")

    def pop(self):
        if self.lenth()>0:
            return self.stack.pop()
        else:
            print("stack is empty")
    def top(self):
        print(self.stack[-1])

class Queue:

    def __init__(self,num):
        self.num=num
        self.queue=Stack(num)
        self.tempstack=Stack(num)

    def enqueue(self,put):
        while self.queue.lenth()>0:
            q=self.queue.pop()
            self.tempstack.push(q)
        self.queue.push(put)
        while self.tempstack.lenth()>0:
            t=self.tempstack.pop()
            self.queue.push(t)

    def dequeue(self):
        self.queue.pop()

    def printing(self):
        self.queue.printing()

queue1=Queue(10)
queue1.enqueue(10)
queue1.printing()
queue1.enqueue(9)
queue1.printing()
queue1.enqueue(8)
queue1.printing()
queue1.enqueue(7)
queue1.printing()
queue1.enqueue(6)
queue1.printing()
queue1.enqueue(5)
queue1.printing()
queue1.enqueue(4)
queue1.printing()
queue1.dequeue()
queue1.printing()