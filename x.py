import math
def quadratic(a, b, c):
    d=b*b - 4*a*c
    for num in (a,b,c):
        if not isinstance(num, (int,float)):
           raise TypeError('wrong input args!')
    if a==0:
       return (-1.0)*c/b
    elif d<0:
       print("no results!")
       return
    elif d==0 :
       return (-1.0)*b/2*a
    else :
       x1 = ((-1)*b + math.sqrt(d))/(2*a)
       x2 = ((-1)*b - math.sqrt(d))/(2*a)
       return x1,x2
print("x=%.2f" % quadratic(1,2,1))
print("x1=%.2f  x2=%.2f" % quadratic(2,3,1))
print("x1=%.2f  x2=%.2f" % quadratic(1,3,-4))
