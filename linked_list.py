class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node
  
  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)
      
  def Print(self):
    if self.head is None:
      print("Linked List is empty")
      return
    
    itr = self.head
    llstr =""
    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next      
    print(llstr)
    
  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
      
  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count +=1
      itr = itr.next
      
    return count
  
    
if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_values(['Peter','John','Luke','Mathew','Mark'])
  ll.Print()
  print("length of the linked List: ",ll.get_length() )

  

  