import numpy as np
import matplotlib.pyplot as plt
file=open('input.txt', 'r')
A=list(file.read().split())
X=[]
Y=[]
y=0
x=0
i=0
while i<=len(A):
    s=A[i]
    x=len(s)
    X.append(x)
    for i+1<=len(A):
        S=A[i+1]
        if x==len(S):
            y+=1
        Y.append(y) 
  
     
