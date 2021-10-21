import os

racine="C:/Users/a_A/Documents"                                    #"/tmp/documents/"
fichier ="profiletitles"
fichier1= "candidature"                                            #"universe-formula"


def locate_universe_formula():
    entree1=os.listdir(racine)
    for entree in entree1 :
        if (entree==fichier1) and not(os.path.isdir(os.path.join(racine,entree))):
            return racine+fichier1
        else:
            return None

print(locate_universe_formula())


