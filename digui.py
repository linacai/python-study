def fact(n) :
    return fact_inter(n,1)

def fact_inter(n,num):
    if n==1 :
       return num
    return fact_inter(n-1,n*num)

def move(n,a,b,c) :  #han ni ta
    if n==1:
       print(a,'-->',c)  #only one move a to c
    else :
       move(n-1,a,c,b)  #move n-1 to b
       print(a,'-->',c)  #move the last one in a to c
       move(n-1,b,a,c)   #move b of n-1 to c
#print(move(3,'A','B','C'))

def fabi(max) :
    n,a,b = 0,0,1
    while n<max :
       print(b)
       a , b = b,a+b
       n = n+1
    return 'done'
#fabi(5)

def triangles():
    L=[1]
    while True :
      yield L
      L.append(0)
      L = [L[i-1]+L[i] for i in range(len(L))]
n=0
#for t in triangles() :
#    print(t)
#    n = n+1
#    if n==10 :
#       break

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))

def f(x):
    return x*x

L = list(range(1,10))
r=map(f,L)
print(list(r))

from functools import reduce
def fn(x,y):
    return x*10+y

print(reduce(fn,L))

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y, map(char2num,s))

s='12345'
print(str2int(s))

def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize,L1)))

def prod(L):
    return reduce(lambda x,y:x*y, L)

print('3*5*7*9=%d' % prod([3,5,7,9]))


def str2float(s):
    i=0
    for ch in s :
        if ch=='.' :
           break 
        i=i+1
    before = reduce(fn,map(char2num,s[:i]))
    after = reduce(fn,map(char2num,s[i+1:]))*1.0/10**len(s[i+1:])
    return before+after

print('str2float(\'1234.567\') = %f' % str2float('1234.567'))
