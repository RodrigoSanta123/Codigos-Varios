word=input('ingrese la palabra base a evaluar ')
mut=input('ingrese la mutacion a evaluar ')
k=[]
import string
alph=list(string.ascii_lowercase)
x=[word.replace(x,'',1) for x in word]
num=range(len(x))
y=[(str(k[:n])+str(l)+str(k[n:])) for k in x for l in alph for n in num if k==x[n]]
num=range(len(word))
z=[(str(word[:n])+str(l)+str(word[n:])) for l in alph for n in num]
w=[(str(word[:n-1])+str(l)+str(r)+str(word[n+1:])) for l in word for r in word for n in num if word.index(l)==word.index(r)+1 and n==word.index(r)+1]
finale=x+y+w
print(mut in finale)
