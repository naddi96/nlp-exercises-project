# CYK algorithm

simple implementation of cyk algorithm for parsing strings of a grammar

## how to run

after installing the dependency 

- `pip3 install -r requirements.txt`

run it with python3

- `python3 cyk.pys`

## where to put things

put the string that you want to parse into the file 

- **stri.txt**

put your grammar into the file
- **BinaryGrammar.txt**

  
## tree visualization

you can visualaze the parsing tree in your browser by launching this commands
- `cd './tree graph/'`

- `python3 -m  http.server`

and by going to the following urls in your browses

- `http://localhost:8000/cluster-dendrogram`
- `http://localhost:8000/expandable-tree`