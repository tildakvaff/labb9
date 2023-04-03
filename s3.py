from queue import LinkedQ
from sys import stdin
#DENNA GER KORREKTA UTSKRIFTER MED KATTISKODEN
class Syntaxfel(Exception):
    pass

atomlagring = LinkedQ()

def readformel(q):
    readmol(q) 

def readmol(q):
    readgroup(q)
    if q.peek() != "&":
        readmol(q)

def readgroup(q):
    #Fall 1
    if q.peek().isnumeric() == True:
        raise Syntaxfel(f'Felaktig gruppstart vid radslutet {restutskrivare(q)}')   #Gruppen kan aldrig börja med en siffra
    #Fall 2
    if q.peek() == "(":
        q.dequeue()                                                                 #Om vi får ( innebär det att det är en molekyl          
        while q.peek() != ")":                                                          #läser in tills vi når slutparantesen                                                                
            if q.peek() == "&":                                                         #Om kön blir tom innan slutparantes är något fel
                raise Syntaxfel(f'Saknad högerparentes vid radslutet {restutskrivare(q)}')
            readgroup(q)                                                                               
        q.dequeue()                               
        if q.peek().isnumeric() != True:                                            #Om tecknet inte är en siffra är det felaktigt
            raise Syntaxfel(f'Saknad siffra vid radslutet {restutskrivare(q)}')
        else:
            readnum(q)

    #Fall 3
    elif q.peek() == ")":
        raise Syntaxfel(f'Felaktig gruppstart vid radslutet {restutskrivare(q)}')   #Gruppen kan aldrig börja med en )

    #Fall 4
    if q.peek().isalpha() == True: #Om gruppen börjar med en bokstav är det en atom   
        if q.peek().islower() == True:     #Endast en atom om den börjar med stor bokstav, om liten är det felaktigt
            raise Syntaxfel(f'Saknad stor bokstav vid radslutet {restutskrivare(q)}')
        if q.peek().isupper() == True:     #Om bokstaven är stor är det en korrekt gruppstart
            readatom(q)
        try:
            int(q.peek())
            readnum(q)
        except (ValueError, TypeError): None

def readnum(q):
    #Om siffran är en 1a
    if q.peek() == "1":
        q.dequeue()
        if q.peek().isnumeric() == False:               #Om tecknet efter 1an INTE ÄR en siffra är det syntaxfel
            raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
        if q.peek().isnumeric() == True:                #Om tecknet efter 1an ÄR en siffra är det ok
            kolla_sifferföljden(q)                      
            return
    #Om siffran är en 0a        
    if q.peek() == "0":         #En 0a som första siffra i följden är alltid felaktigt
        q.dequeue()                                 
        raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
    #Om siffran är större än 1
    else: 
        kolla_sifferföljden(q)
        return
        
def kolla_sifferföljden(q):
    if q.peek().isnumeric() == True:
        q.dequeue()
        kolla_sifferföljden(q)
    else:
        return
    
def readatom(q):
    atomlagring = LinkedQ()
    atomlagring.enqueue(q.dequeue())        #lagrar den första stora bokstaven
    if q.peek().isalpha() == True:          #kollar om nästa tecken är en bokstav          
        if q.peek().islower():
            atomlagring.enqueue(q.dequeue())
    atomcheck(atomlagring,q)
    return

def atomcheck(atomlagring,q):
    #print("ATOMCHECK")
    atomlista= ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y",
            "Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir",
            "Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]
    atomstr = ""
    while atomlagring.size() != 0:
        atomstr += atomlagring.dequeue()
    if atomstr in atomlista:
        return #atomlagring
    #Nu vet vi att atomen vi testa är korrekt. Nu tömmer vi därför atomlagringen och returnerar den
    else:
        raise Syntaxfel(f'Okänd atom vid radslutet {restutskrivare(q)}')

def restutskrivare(q):
    radslut = ""
    while not q.peek() =="&":
        radslut += str(q.dequeue())
    return radslut
########################################################################################################################################################################
def dela_upp_molekyl(molekyl):
        q = LinkedQ()
        for varje_tecken in molekyl:
                q.enqueue(varje_tecken)
        q.enqueue("&")
        return kollamolekyl(q)
        
def kollamolekyl(q):
    try:
        readformel(q)
        return("Formeln är syntaktiskt korrekt")
    except Syntaxfel as fel:
        return(str(fel))






# #FÖR ATT LÄSA FRÅN TEXTFIL
# def main():
#     with open("test1.txt", "r") as molekylfil:
#         molekyllista = molekylfil.read().splitlines()

#     for varje_rad in molekyllista:

#         if varje_rad.strip() =="#":
#             break

#         resultat = dela_upp_molekyl(varje_rad)
#         print(resultat)


#lista1 = ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332", "#" ]
lista2 = ["C(Xx4)5", "C(OH4)C", "C(OH4C", "H2O)Fe", "H0", "H1C", "H02C", "Nacl", "a", "(Cl)2)3", ")", "2", "#"  ]




#FÖR ATT LÄSA FRÅN STDIN - KATTIS-KOMPATIBEL
def main(): 
    for varje_rad in lista2: #in stdin
        if varje_rad.strip() == "#":
            break            
        else:
            varje_rad = varje_rad.strip()
            resultat = dela_upp_molekyl(varje_rad)
            print(resultat)
        

    

if __name__ == "__main__":
    main()

