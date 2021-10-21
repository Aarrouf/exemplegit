def tripletpythagor(l):
    l.sort()
    lg=len(l)
    tp=[]
    for i in range(lg-2):
        for j in range(i+1,lg):
            for k in range(j+1,lg-1):
                if l[i]*l[i] + l[j]*l[j] == l[k]*l[k] :
                    tp.append((l[i],l[j],l[k]))
    return tp

print(tripletpythagor([0, 3, 6, 1, 2, 4, 5]))






