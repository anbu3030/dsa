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
            self.stack.pop()
        else:
            print("stack is empty")
    def top(self):
        print(self.stack[-1])

stack1=Stack(10)
stack1.printing()
stack1.push(10)
stack1.printing()
stack1.push(100)
stack1.printing()
stack1.top()
stack1.push(1000)
stack1.printing()
stack1.top()
stack1.pop()
stack1.printing()
stack1.push(10000)
stack1.printing()
stack1.pop()
stack1.printing()