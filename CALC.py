#PRO-5 CALC



def Add(a,b):      #def is used to defining user defined function #(a,b) shows argument
    c=a+b                                                         #user give input as a,b
    print('Addition is ')
    return(c)      #function used to return value to varible function
    
def Sub(a,b):
    d=a-b
    print('Substraction is ')
    return(d)
    
def Multiply(a,b):
    e=a*b
    print('Multiplication is ')
    return(e)

def Divide(a,b):
    f=a/b
    print('Division is ')
    return(f)

while(1):
    k=int(input('1. Addition \n2. Substraction \n3. Multiplication \n4. Division \n'))
    n1=float(input('enter first no. '))
    n2=float(input('enter second no. '))
    if(k==1):
      print(Add(n1,n2))
    elif(k==2):
       print(Sub(n1,n2))
    elif(k==3):
        print(Multiply(n1,n2))
    elif(k==4):
        if(n2==0):
            print('Zero cannot use for division in denominator')
        else:
            print(Divide(n1,n2))
    else:
        print('None of above operations performed')
    
        
        
