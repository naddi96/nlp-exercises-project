import numpy as np
import itertools

def load_grammar():
    lines=open("gram.txt","r").readlines()
    grammatica=[]
    for line in lines:        
        part=line.split("->")
        array_riga =np.append([part[0]],[np.array(part[1].replace("\n","").split("|"))])
        grammatica.append(array_riga)
    return grammatica

def load_word():
    return open("stri.txt","r").read()

def get_produttori(grammar,produzione):
    prouttori=set()
    for regola in grammar:
        for gram_prod in regola[1:]:
            if produzione == gram_prod:
                prouttori.add(regola[0])
    return prouttori

def prodotto_cartesiano(set1,set2):
    cartesian_product = itertools.product(set1,set2)
    s=set()
    for el in cartesian_product:
        s.add("".join(el))
    return s

def cyk(grammar,string):
    len_parola=len(string)
    matr = np.zeros(shape=(len_parola,len_parola),dtype=object)
    for x in range(0,len_parola):
        matr[0][x]=get_produttori(grammar,string[x])
    j=0
    for riga in range(1,len_parola):
        j=j+1
        for col in range(0,len_parola-j):
                set_prod=set()
                for i in range(0,riga):
                    part1=matr[i][col]
                    part2=matr[riga-i-1][col+i+1]
                    for x in prodotto_cartesiano(part1,part2):
                        for k in get_produttori(grammar,x):
                            set_prod.add(k)
                matr[riga][col]=set_prod
    print(matr)
    if "S" in matr[len_parola-1][0] :
        return True
    else:
        return False

if __name__ == "__main__":
    grammatica = load_grammar()
    parola= load_word()
    if cyk(grammatica,parola):
        print("la parola: '"+parola+"'  appartiene alla grammatica")
    else:
        print("la parola: '"+parola+"'  non appartiene alla grammatica")

    
