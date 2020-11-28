import numpy as np
import itertools
import random
import printTree 
import json

def load_grammar():
    lines=open("BinaryGrammar.txt","r").readlines()
    grammatica={}
    for line in lines:        
        part=line.split("->")
        value=part[0].replace(" ","")
        key=tuple(part[1].replace("\n","")[1:].split(" "))
        if key in grammatica:
            grammatica[key].add(value)
        else:
            grammatica[key]={value}
    return grammatica

def load_word():
    stri=open("stri.txt","r").read().lower()
    return stri.split("\t")
    

def get_produttori(grammar,produzione):
    
    if tuple(produzione) in grammar:
        return grammar[tuple(produzione)]
    else:
        return {}
    


def prodotto_cartesiano(set1,set2):
    cartesian_product = itertools.product(set1,set2)
    s=set()
    for el in cartesian_product:
        s.add(el)
    return s




def generate_all_tree(matr,node,pro):
    lis=matr[node[0]][node[1]]
    possible_path=[]
    for k in lis:
        if k[3] == pro:
            possible_path.append(k)
    if (possible_path ==[]):
        return [0]    
    list_path=["possibili sottoalberi",]
    k=len(possible_path)
    for chosen in possible_path:    
        if  type(chosen[2]) != type(tuple()):
            return [pro,[chosen[2]]]
        if k==1:
            return [pro,[chosen[2],
        generate_all_tree(matr,chosen[0],chosen[2][0]),
        generate_all_tree(matr,chosen[1],chosen[2][1])]]
        else:
            list_path.append([pro,[chosen[2],
            generate_all_tree(matr,chosen[0],chosen[2][0]),
            generate_all_tree(matr,chosen[1],chosen[2][1])]])
    return list_path

def generate_all_tree_d3j_format(matr,node,pro):
    lis=matr[node[0]][node[1]]
    possible_path=[]
    for k in lis:
        if k[3] == pro:
            possible_path.append(k)
    if (possible_path ==[]):
        return [0]    
    list_path={"name":"possibili sottoalberi","children":[]}
    k=len(possible_path)
    for chosen in possible_path:    
        if  type(chosen[2]) != type(tuple()):
           return {"name":pro,"children":[{"name":chosen[2]}]}
        if k==1:
            li=chosen[2]
            return {"name":pro,"children":[{"name":" ".join(li),"children":[
    generate_all_tree_d3j_format(matr,chosen[0],chosen[2][0]),
    generate_all_tree_d3j_format(matr,chosen[1],chosen[2][1])]}]}
        else:
            li=chosen[2]
            list_path["children"].append({"name":pro,"children":[{"name":" ".join(li),"children":[
    generate_all_tree_d3j_format(matr,chosen[0],chosen[2][0]),
    generate_all_tree_d3j_format(matr,chosen[1],chosen[2][1])]}]})
    return list_path



def generate_possible_random_tree_d3j_format(matr,node,pro):
    lis=matr[node[0]][node[1]]
    possible_path=[]
    for k in lis:
        if k[3] == pro:
            possible_path.append(k)
    if (possible_path ==[]):
        return [0]    
    chosen=random.choice(possible_path)
    
    if type(chosen[2]) != type(tuple()):
        return {"name":pro,"children":[{"name":chosen[2]}]}
    
    li=chosen[2]

    return {"name":pro,"children":[{"name":" ".join(li),"children":[
    generate_possible_random_tree_d3j_format(matr,chosen[0],chosen[2][0]),
    generate_possible_random_tree_d3j_format(matr,chosen[1],chosen[2][1])]}]}


def generate_possible_random_tree(matr,node,pro):
    lis=matr[node[0]][node[1]]
    possible_path=[]
    for k in lis:
        if k[3] == pro:
            possible_path.append(k)
    if (possible_path ==[]):
        return [0]    
    chosen=random.choice(possible_path)
    
    if type(chosen[2]) != type(tuple()):
        return [pro,[chosen[2]]]
    li=list(chosen[2])

    return [pro,[" ".join(li),
    generate_possible_random_tree(matr,chosen[0],chosen[2][0]),
    generate_possible_random_tree(matr,chosen[1],chosen[2][1])]]




def cyk(grammar,string):
    len_parola=len(string)
    back_matr=np.zeros(shape=(len_parola+1,len_parola),dtype=object)
    matr = np.zeros(shape=(len_parola,len_parola),dtype=object)
    
    for x in range(0,len_parola):
        prod=get_produttori(grammar,[string[x]])
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
    
    if "S" in matr[len_parola-1][0] :
        return True,back_matr,matr
    else:
        return False,back_matr,matr




if __name__ == "__main__":
   
    
    parola= load_word()

    grammatica = load_grammar()
    parola= load_word()
    result=cyk(grammatica,parola)
    if result[0]:
        print("la parola: '",parola,"'  appartiene alla grammatica")
    else:
        print("la parola: '",parola,"'  non appartiene alla grammatica")

    
    x=generate_possible_random_tree_d3j_format(result[1],[len(parola),0],"S")
    y=json.dumps(x)
    #print(y)
#    open("tree graph/expandable-tree/2flare.json","w").write(json.dumps(k))

    open("tree graph/expandable-tree/flare.json","w").write(y)
    open("tree graph/cluster-dendrogram/flare.json","w").write(y)
   # print(generate_all_tree(result[1],[len(parola),0],"S"))

    #printTree.print_tree(x)
 #  printTree.print_tree(generate_all_tree(result[1],[len(parola),0],"S"))
