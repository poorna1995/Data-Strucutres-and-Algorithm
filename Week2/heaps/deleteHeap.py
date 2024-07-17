class DeleteElement:
    def __init__ (self):
        self.heap=[]

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,index):
        parent_index= (index-1)//2
        if index>0 and self.heap[index]<self.heap[parent_index]:
            self.heap[index],self.heap[parent_index] =self.heap[parent_index] ,self.heap[index]
            self.heapify_up(parent_index)

    def delete(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root= self.heap[0] # store the index o value to the root 
        self.heap[0]=self.heap.pop()
        self.bubbling_down(0)
        return root

    def bubbling_down(self,index):
        smallest=index
        left=(2*index)+1
        right=(2*index)+2
        if index>0 and left <len(self.heap) and self.heap[left_child]<self.heap[smallest]:
            smallest=left_child
        if index>0 and right <len(self.heap) and self.heap[right_child]<self.heap[smallest]:
            smallest=right_child
        
        if smallest!=index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.bubbling_down(smallest)
    
    def display(self):
        print(self.heap)


delete_element= DeleteElement()

delete_element.insert(10)
delete_element.insert(1)
delete_element.insert(2)
delete_element.insert(6)
delete_element.insert(7)
delete_element.insert(9)

delete_element.display()
print(delete_element.delete())
delete_element.display()






    