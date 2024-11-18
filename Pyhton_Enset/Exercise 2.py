Employes = ['Alami', 'Bassou', 'Amraoui', 'Baghdadi', 'Mohammadi', 'Alaoui']
# Corresponding salaries
Salaires = [15345.93, 7850.75, 12780.00, 4500.25, 17575.53, 3750.29]
# Corresponding services
Services = ['Commercial', 'Comptabilité', 'Approvisionnement',
            'Commercial', 'Approvisionnement', 'Comptabilité']


def ListesToDict(E_s, S_y, S_s):
    Diction = {}
    for i in range(len(E_s)):
        Diction["Emp"+str(i+1)] = {"Nom" : E_s[i], "Salaire" : S_y[i] , "Service" : S_s[i]}
    return Diction

Dic = ListesToDict(Employes,Salaires,Services)

def SynDictonary(Dic):
    Vvalues = list(Dic.values())
    dicto = {"Commercial" :[], "Comptabilité" : [], "Approvisionnement" : []}
    for itme in Vvalues:
        if itme["Service"] in dicto.keys():
            dicto[itme["Service"]].append(itme["Salaire"])
    return {oneitem : [min(dicto[oneitem]), sum(dicto[oneitem])/2, sum(dicto[oneitem])] for oneitem in dicto}


liste = SynDictonary(Dic)

print(liste)