class MinStack:

    def __init__(self):
      
        self.minstk=[]
        self.norstk=[]

    def push(self, val: int) -> None:
        self.norstk.append(val)
        if len(self.minstk)==0 or val<= self.minstk[-1]:
            self.minstk.append(val)
        
    def pop(self) -> None:
        if self.norstk[-1] == self.minstk[-1]:
            self.minstk.pop()
        self.norstk.pop()
        
    def top(self) -> int:
        return self.norstk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
        
