class Node:
  def __init__(self, value):
    self.value = value      
    self.next = None    

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)	
    self.size = 1

  def addN(self, value):
    sd = self.head

    while(sd.next != None):
      sd = sd.next
    
    sd.next = Node(value)
    self.size += 1

    if(n == self.size):
      sd.next.next = self.head
  
  def delN(self, cnt):
    sd = self.head
    re = 0
    while(re != (cnt-1)):
      sd = sd.next
      re += 1
    
    yosp.append(sd.next.value) 
    self.size -= 1
    sd.next = sd.next.next

# main 부분
n,k = map(int, (input().split()))
L = LinkedList(1)
yosp = []

for i in range(2, n+1):
  L.addN(i)

cur = 0
move = k-1

cur += move
L.delN(cur)

cur += move
L.delN(cur)

cur += move
L.delN(cur)
while(L.size <= cur):
  cur -= (L.size+1)

cur += move
L.delN(cur)
while(L.size <= cur):
  cur -= L.size

cur += move
L.delN(cur)
while(L.size <= cur):
  cur -= L.size

cur += move
L.delN(cur)
while(L.size <= cur):
  cur -= L.size

cur += move
L.delN(cur)
while(L.size <= cur):
  cur -= L.size

print("<" + ",".join(map(str,(yosp))) + ">" ,end="")
