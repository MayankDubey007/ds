_front(self):
        if self.findSize()==1:  #new
            self.head = None    #new
        elif self.head!=None:
            self.head=self.head.next
            self.head.previous=None
        return self
    
    def remove_from_back(self):
        if self.tail!=None:
            self.tail=self.tail.previous
            self.tail.next=None
        return self