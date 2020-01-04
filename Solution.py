import os 
import sys 


class Solution:
    
    def __init__(self):
        self.maxLen = 0
        pass 

    
    def driver(self, a:str, b:str, aIndex:int, bIndex:int)->int:
        
        currMax = 0
        ##at the end of a string 
        if aIndex >= len(a) or bIndex >= len(b):
            return 0
        
        ##if the are equal then keep checking while they are equal
        ##by incremeneting both their indexes
        temp1 = aIndex 
        temp2 = bIndex
        if a[temp1] == b[temp2]:
            while a[temp1] == b[temp2]:
                currMax += 1
                temp1 += 1
                temp2 += 1
                if temp1 >= len(a) or temp2 >= len(b):
                    break
            
            if currMax >= self.maxLen:
                self.maxLen = currMax

            ##once they are no longer equal,
            ##continue with the recursion at the current indexes
            self.driver(a, b, aIndex + 1, bIndex)
            self.driver(a, b, aIndex, bIndex+1)
        
        ##else if they are not equal
        self.driver(a, b, aIndex + 1, bIndex)
        self.driver(a, b, aIndex, bIndex + 1)

        return self.maxLen
    
    def min(self, a, b):
        if a <= b:
            return a 
        
        else:
            return b
        
