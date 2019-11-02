#Pro-8    ATM with EXCEL


import xlrd
import time
wb=xlrd.open_workbook(r'C:\Users\HP\Desktop\PYTHON\Excel\abcd.xlsx')
s=wb.sheet_by_index(0)
u=s.col_values(1)
p=s.col_values(0)
amt=s.col_values(2)
print('Welcome to sign in interface')
while(1):
    h=input('Enter your username ')
    j=0
    for i in range(0,len(u)):
        if(h==u[i]):
            j=1
            break
    while(1):    
        if(j==1):
            a=int(input('Enter your password '))
            if(a==p[i]):
                c=int(input('Choose your options :\n 1.Cash withdrawl\n 2.Cash deposit\n 3.Balance inquery\n 4.Change Password\n'))
                if(c==1):
                    d=int(input('Enter your amount: '))
                    if(d<=amt[i]):
                         time.sleep(4)
                         print('please collect your cash')
                         amt[i]=amt[i]-d
                         print('Remaining amount is ',amt[i])
                         time.sleep(3)
                         break
                    else:
                        print('SORRY! Insufficient money in account')
                        time.sleep(3)
                        break
                if(c==2):
                    e=int(input('Enter your amount'))
                    amt[i]=amt[i]+e
                    print('Your new balance is:- ',amt[i])
                    time.sleep(3)
                    break
                if(c==3):
                    print('Your account balance is:-',amt[i])
                    time.sleep(3)
                    break
                if(c==4):
                    f=input('Please enter current Password:- ')
                    if(f==p[i]):
                        f=input('Please enter new Password:- ')
                        p[i]=f
                        time.sleep(3)
                        print('Password changed succesfully')
                        time.sleep(3)
                        break
                    else:
                        print('Incorrect Password')
                        time.sleep(3)
                        break
                else:
                    print('Please choose correct options')
                    break
            else:
                print('Please enter a correct password')
                break
        else:
            print('SORRY..you have entered a worng username')
            break

                
            
            
