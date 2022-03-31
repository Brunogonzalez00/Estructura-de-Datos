class Stack:
    def __init__(self):  #El constructor
        self.items = []
 
    def isEmpty(self):
        return self.items == []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        return self.items.pop()
 
    def top(self):
        return self.items[len(self.items)-1]
 
    def size(self):
        return len(self.items)
        
s = Stack()
print (s.isEmpty())
for letra in range(5):
    a=input("ingrese letras: ")
    if (a == str and a not in "aeiou"):
        s.push(a)
for i in len(s):
    s.pop()
s.size()