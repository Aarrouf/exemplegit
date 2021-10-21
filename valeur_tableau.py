def is_on_position(table,valeur):
    if table==[]:
        return False
    else:
        if (valeur in table) and (table.index(valeur)%2==0) :
            return True
        else :
            return False





print (is_on_position([0,1,2,3,4,5,6],2))