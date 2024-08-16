class Queue:
    def __init__(self,num):
        self.num=num
        self.queue=[]

    def lenth(self):
        return len(self.queue)

    def enqueue(self,num1):
        if self.lenth()<self.num:
            self.queue.append(num1)
        
        else: 
            print("queue overflow")

    def showqueue(self):
        print(self.queue)

    def dequeue(self):
        if self.lenth()>0:
            del self.queue[0]
        
        else:
            print("queue underflow")

    def front(self):
        print(self.queue[0])

    def rear(self):
        print(self.queue[self.lenth()-1])

queue1=Queue(3)
queue1.enqueue(1)
queue1.showqueue()
queue1.enqueue(2)
queue1.showqueue()
queue1.enqueue(3)
queue1.showqueue()
queue1.front()
queue1.rear()
queue1.enqueue(1)
queue1.showqueue()
queue1.dequeue()
queue1.showqueue()
queue1.front()
queue1.rear()
queue1.dequeue()
queue1.showqueue()
queue1.dequeue()
queue1.showqueue()
queue1.dequeue()
queue1.showqueue()