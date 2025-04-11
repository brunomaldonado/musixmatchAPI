import time
import threading

def print_dots(dot_delay, duration):
  start_time = time.time()
  while time.time() - start_time < duration:
    print(".", end='', flush=True)
    time.sleep(dot_delay)

def starting_threads():
  dot_delay = 0.125
  duration = 6
  dot_thread = threading.Thread(target=print_dots, args=(dot_delay, duration))
  dot_thread.start()
  dot_thread.join()
  print(" Done!\n")

class TwoWayNode:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

  def size(self):
    if self.head is None:
      return 0
    current = self.head
    count = 0
    while current:
      current = current.next
      count += 1
    return count
  
  def enqueue(self, data):
    new_node = TwoWayNode(data)

    if self.head is None:
      self.head = new_node
      self.tail = self.head
    else: #else, if node already exists, then...
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
    
    self.count += 1

  def dequeue(self):
    # print("\nFirst In, First Out (FIFO)")
    current = self.head

    if self.count == 1:
      self.count -= 1
      self.head = None
      self.tail = None
    elif self.count > 1:
      self.head = self.head.next
      self.head.prev = None
      self.count -= 1
    
    # print(f"Data to remove is: {current.data}")
    # print(f"  🎧 {current.data}")
    return current.data
  
  def list_data(self):
    current = self.head
    elements = []
    while current is not None:
      elements.append(current.data)
      current = current.next
    return elements

  def __str__(self):
    if self.head is None:
      # raise IndexError("Empty!!!")
      print("List Empty!!!")
      return
    elements = []
    current = self.head
    while current is not None:
      if isinstance(current.data, (int, float)):
        elements.append(str(current.data))
      else:
        elements.append(f"'{str(current.data)}'")
      current = current.next
    if current == self.head:
      self.head

    return "[" + ", ".join(elements) + "]"

def main():
  Q = Queue()
  Q.enqueue(10)
  Q.enqueue(20)
  Q.enqueue(30)
  print(f"{Q}\nSize: {Q.size()}")
  print()
  Q.dequeue()
  starting_threads()
  time.sleep(0.125)
  print(f"{Q}\nSize: {Q.size()}")
  Q.dequeue()
  starting_threads()
  time.sleep(0.125)
  print(f"{Q}\nSize: {Q.size()}")
  Q.enqueue(50)
  Q.enqueue(60)
  Q.enqueue(70)
  time.sleep(0.125)
  print(f"{Q}\nSize: {Q.size()}")


if __name__ == '__main__':
  main()
  
