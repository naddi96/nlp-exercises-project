# CYK algorithm

simple implementation of cyk algorithm for parsing strings of a grammar

## how to run

after installing the dependency (just numpy)

- `pip3 install -r requirements.txt`

run it with python3

- `python3 cyk.pys`

## where to put things

put the string that you want to parse into the file 

- **stri.txt**

put your grammar into the file
- **gram.txt**

## grammar syntax

the grammar has to be in chomschy normal form and should be written in the following syntax

- the starting production has to be **S**
- following put **->** and than the possible pructions divided by the **|** symbol 
  
### example grammar

S->AB|BC
A->BA|a
B->CC|b
C->AB|a
## program out put

[[{'B'} {'C', 'A'} {'C', 'A'} {'B'} {'C', 'A'}]
 [{'S', 'A'} {'B'} {'S', 'C'} {'S', 'A'} 0]
 [set() {'B'} {'B'} 0 0]
 [set() {'A', 'S', 'C'} 0 0 0]
 [{'S', 'C', 'A'} 0 0 0 0]]
S
└── AB
    ├── A
    │   └── BA
    │       ├── A
    │       │   └── a
    │       └── B
    │           └── b
    └── B
        └── CC
            ├── C
            │   └── AB
            │       ├── A
            │       │   └── a
            │       └── B
            │           └── b
            └── C
                └── a

la parola: 'baaba'  appartiene alla grammatica