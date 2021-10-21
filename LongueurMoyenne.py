def Longueur_moyen(ch):
    l=list(ch)
    n=0
    p=[" ","'","!",".","?",";",","]
    for i in l :
        if i in p:
            n+=1
    return len(l)-n/len(l)

