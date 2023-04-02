from nylinkedqlabb9 import LinkedQ
from sys import stdin



class Syntaxfel(Exception):
    pass




atomlagring = LinkedQ()

def readformel(q):
    "<formel>::= <mol> \n"
    print("1a") 
    readmol(q) 
#__________________________________________________________________________________________


def readmol(q):
    "<mol>   ::= <group> | <group><mol>"
    print("2a")
    tecken1 = q.peek()
    if tecken1 == ")" or tecken1.isnumeric() == True:
        print("3a")
        raise Syntaxfel(f'Felaktig gruppstart vid radslutet {restutskrivare(q)}')
    
    if tecken1.islower() == True:
        print("4a")

        raise Syntaxfel(f'Saknad stor bokstav vid radslutet {restutskrivare(q)}')
    
    if q.peek() == "(":
        print("5a")
        readgroup(q)

    else:
        print("6a")
        readgroup(q)
        if q.peek() != "&":
            print("7a")
            readmol(q)
        if q.peek() == "&":
            print("8a")
            return
#__________________________________________________________________________________________


    #denna läser gruppen --> EN grupp börjar alltid med stor bokstav eller en parantes, Se rad 3 i syntax
def readgroup(q):
    "<group> ::= <atom> |<atom><num> | (<mol>) <num>"

    print("9a")
    
    if q.peek() == "(":
        print("10a") #Om man tagit sig hit innebär det att första tecknet är en startparantes och vi ANROPAR DÄRFÖR readmolekyl
        q.dequeue()
        readmol(q)
    else:
        print("11a")#Om man tagit sig hit innebär det att första tecknet är en stor bokstav och vi ANROPAR DÄRFÖR readatom
        readatom(q) # vi vill läsa den bokstaven för att se om det är en atom som finns i periodiska systemet
        if q.peek() == "&":
            ("12a")
            return
        if q.peek().isnumeric() == True:
            print("13a")
            readnum(q)
            return
#__________________________________________________________________________________________


def readatom(q):
    "<atom>  ::= <LETTER> | <LETTER><letter>"
#En atom kan vara uppbyggd på 2 sätt, Antingen som 1 bokstav eller som 2 bokstäver, gemensamt är att de börjar med stor bokstav
    print("tio")

    if q.peek().isupper() == True:
        print("14a")
        atomlagring.enqueue(q.dequeue())
    
    else:
        print("15a")
        raise Syntaxfel(f'Saknad stor bokstav vid radslutet {restutskrivare(q)}')

    if q.peek() != None:
        if q.peek().islower():
            atomlagring.enqueue(q.dequeue())
    
    atomcheck(atomlagring,q)
    return
#__________________________________________________________________________________________


def readnum(q):
    "<num>   ::= 2 | 3 | 4 | ..."
    if q.peek().isnumeric() == True:

        #Om tecknet är en 1a
        if q.peek() == "1":
            q.dequeue()
            if q.peek().isnumeric() == False: #Om tecknet efter 1an INTE ÄR en siffra är det syntaxfel
                print("nitton")
                raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
            if q.peek().isnumeric() == True: #Om tecknet efter 1an ÄR en siffra är det ok
                print("tjugo")
                kolla_sifferföljden(q)
                return
        
        if q.peek() == "0":
            print("tjugoett")
            print("sjutton")
            raise Syntaxfel(f'För litet tal vid radslutet {restutskrivare(q)}')
        
        else: #Om det är en större siffra än 1 eller 0
            print("tjugotvå")
            kolla_sifferföljden(q)
            return
            

    if q.peek().isalpha() == True:
        print("här är "+q.peek())
        print("tjugotre")
        return

    if q.peek() == "&":
        print("tjugofyra")
        return
#__________________________________________________________________________________________


def kolla_sifferföljden(q):
    if q.peek().isnumeric() == True:
        print("tjugofem")
        q.dequeue()
        kolla_sifferföljden(q)
    else:
        print("tjugosex")
        return
#__________________________________________________________________________________________


def atomcheck(atomlagring,q):
    print("ATOMCHECK")
    atomlista= ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y",
            "Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir",
            "Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Fl","Lv"]
    atomstr = ""
    while atomlagring.size() != 0:
        atomstr += atomlagring.dequeue()
    print("NU ÄR DEN TOM")
    if atomstr in atomlista:
        print("femton")
        return atomlagring
    #Nu vet vi att atomen vi testa är korrekt. Nu tömmer vi därför atomlagringen och returnerar den
    else:
        print("sexton")
        raise Syntaxfel(f'Okänd atom vid radslutet  {restutskrivare(q)}')
#__________________________________________________________________________________________


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
def main():
    with open("test1.txt", "r") as molekylfil:
        molekyllista = molekylfil.read().splitlines()

    for varje_rad in molekyllista:

        if varje_rad.strip() =="#":
            break

        resultat = dela_upp_molekyl(varje_rad)
        print(resultat)



if __name__ == "__main__":
    main()



