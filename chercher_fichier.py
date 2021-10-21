import os
fichier = "test.txt"
rep="C:/Users/a_A/Documents"
def search(fichier,rep):
    entrees=os.listdir(rep)
    for entree in entrees :
        if entree==fichier and  not(os.path.isdir(os.path.join(rep,fichier))):
            return rep
    for entree in entrees:
        rep2=os.path.join(rep,entree)
        if os.path.isdir(rep2):
            chemin=search(fichier,rep2)
            if chemin!="":
                return chemin
            else:
                return ""

print(search("test.txt","C:/Users/a_A/Documents"))



