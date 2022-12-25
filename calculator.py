d=str(input('operator(add,sub,multi,div):'))
a=int(input('input a number:'))
b=int(input('input a number:'))
def add(a,b):
    print('the result:',a+b)
def sub(a,b):
    print('the result:',a-b)
def multi(a,b):
    print('the result:',a*b)
def div(a,b):
     print('the result:',a/b)   

    
if d=='add':
    add(a,b)
elif d=='sub':
    sub(a,b)  
elif d=='multi':
    multi(a,b) 
elif d=='div':
    div(a/b)         