from typing import List

def nextGreaterElement(arr: List[int],n) -> List[int]:
    greater=[]
    stack=[]
    for i in reversed(arr):
        if len(greater)==0:
            stack.append(-1)
            greater.append(i)
        else:
            while len(greater)!=0 and greater[-1]<=i:
                greater.pop()
            if len(greater)!=0 and greater[0]>i:
                stack.insert(0,greater[-1])
                greater.append(i)
            else:
                stack.insert(0,-1)
                greater.append(i)
