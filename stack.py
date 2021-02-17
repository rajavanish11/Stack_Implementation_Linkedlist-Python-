########################## Stack Linked List implementation(LIFO)##################

#####create node class:
class Node:

  def __init__(self,value):
    self.data = value
    self.next = None
    
###################################
##create linklist class:   
class Stack:

  def __init__(self):
    self.top = None

###############################
#### Insert 
  def push(self, value):

    new_node = Node(value)

    new_node.next = self.top

    self.top = new_node
    
###############################
# Delete
  def pop(self):

    if self.top is None:
      return "Stack Empty"
    else:
      data = self.top.data
      self.top = self.top.next
      return data
    

###############################

  def is_empty(self):
    return self.top == None

  

###############################
###peek top or last insert value:
  def peek(self):

    if self.top is None:
      return "Stack Empty"
    else:
      return self.top.data



    

###############################
###Traverse(Print) stack
  def traverse(self):

    temp = self.top

    while temp is not None:
      print(temp.data,end=' ')
      temp = temp.next



      

###############################

  def size(self):

    temp = self.top
    counter = 0

    while temp is not None:
      counter+=1
      temp = temp.next

    return counter



  

#####################################
##reverse stack value:
def reverse_string(text):

  s = Stack()

  for i in text:
    s.push(i)

  res = ""

  while(not s.is_empty()):
    res =  res + s.pop()

  print(res)




  

#############################
#u:-perform Undo operation(To reverse your last action)
#r:-Redo operation

def text_editor(text, pattern):

  u = Stack()
  r = Stack()

  for i in text:
    u.push(i)

  for i in pattern:

    if i == 'u':
      data = u.pop()
      r.push(data)
    else:
      data = r.pop()
      u.push(data)

  res = ""

  while(not u.is_empty()):
    res = u.pop() + res

  print(res)




