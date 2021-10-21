def U(n):
    if n<0:
        return print('Le n doit être positif !')
    elif n<=1:
        return 1
    else:
        return (U(n-1)+U(n-2))

def fib_int(a,b):
    c=max(a,b)
    d=min(a,b)
    l=[]
    i=0
    while(d<=U(i)) and (U(i)<=c):
        l.append((U(i))
        i=i+1
    return l

print(fib_int(2,10))