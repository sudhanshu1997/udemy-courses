n=int(input("enter how many no you want to enter:   "))
a=[None]*n
d=0
c={'a':'addition','s':'substraction','m':'multiply','d':'divide'}
#print(len(a)) for calculating length of list


def add(p):

    for i in p:
       global d
       d=i+d
       print(d)

for i in range (0,n,1 ):
 #a.append(int(input ("enter the vlaue:   ")))
 a[i]=int(input ("enter the vlaue:   "))
b=input("enter the operation you want:      ")
if (c[b]=='addition'):
   add(a)
