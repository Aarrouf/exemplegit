def reverse_int(n):
        p=abs(n)
        s=str(p)
        l=list(s)
        lr=[i for i in reversed(l)]
        f="".join(lr)
        r=int(f)
        if n>0:
            return r
        else:
            return -r

print(reverse_int(-6523))
