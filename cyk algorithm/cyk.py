import numpy as np
import itertools
import random
import printTree 

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


def generate_possible_random_tree(matr,node,pro):
    lis=matr[node[0]][node[1]]
    possible_path=[]
    for k in lis:
        if k[3] == pro:
            possible_path.append(k)
    chosen=random.choice(possible_path)
    if chosen[2].islower():
        return [pro,[chosen[2]]]
    return [pro,[chosen[2],
    generate_possible_random_tree(matr,chosen[0],chosen[2][0]),
    generate_possible_random_tree(matr,chosen[1],chosen[2][1])]]



def cyk(grammar,string):
    len_parola=len(string)
    back_matr=np.zeros(shape=(len_parola+1,len_parola),dtype=object)
    matr = np.zeros(shape=(len_parola,len_parola),dtype=object)
    
    for x in range(0,len_parola):
        prod=get_produttori(grammar,string[x])
        matr[0][x]=prod
        back_matr[1][x]=[]
        
        for k in prod:
            back_matr[1][x].append([[0,x],[0,x],string[x],k])
        back_matr[0][x]=string[x]
    
    j=0


    for riga in range(1,len_parola):
        j=j+1
        
        for col in range(0,len_parola-j):
                back_matr[riga+1][col]=[]
                set_prod=set()
                for i in range(0,riga):
                    part1=matr[i][col]
                    part2=matr[riga-i-1][col+i+1]
                    for x in prodotto_cartesiano(part1,part2):
                        for k in get_produttori(grammar,x):
                            set_prod.add(k)
                            if k!={}:
                                back_matr[riga+1][col].append([[i+1,col],[riga-i-1+1,col+i+1],x,k])
                matr[riga][col]=set_prod
    print(matr)
    printTree.print_tree(generate_possible_random_tree(back_matr,[len_parola,0],"S"))
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

    
