class MinHeap:
    def __init__(self):
        self.heap=[]
  
    def insert_value(self,value):
       self.heap.append(value) # thsi adds a new value at the end the list
       self.heapify_up(len(self.heap)-1) #index=0 # this function called to ensure the heap proprty is maneintes . the agrument is the index of the newly added element , which is the last index of the list
        
    def heapify_up(self, index):  # this method restore the heap property
         parent_index=(index-1)//2
         if index >0 and self.heap[index]<self.heap[parent_index]: # will checl tje ondex value is less than the parent value , if it is swap the value
           self.heap[index],self.heap[parent_index] = self.heap[parent_index],self.heap[index]
           self.heapify_up(parent_index)


    def display(self):
        print(self.heap)
    

min_heap=MinHeap()
min_heap.insert_value(10)
min_heap.insert_value(0)
min_heap.insert_value(20)
min_heap.insert_value(12)
min_heap.insert_value(3)
min_heap.insert_value(2)
min_heap.insert_value(8)
min_heap.insert_value(1)
min_heap.display()







class MaxHeap:
    def __init__ (self):
        self.heap =[]

    def insert(self,value):
        self.heap.append(value)
        self.bubbling_up(len(self.heap)-1)
    
    def bubbling_up(self,index):
        parent_index=(index-1)//2
        if index>0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index],self.heap[parent_index]=self.heap[parent_index],self.heap[index]
            self.bubbling_up(parent_index)

        

max_heap=MaxHeap()
max_heap.insert(10)
max_heap.insert(200)
max_heap.insert(00)
max_heap.insert(1)
max_heap.insert(5)
print(max_heap.heap)





