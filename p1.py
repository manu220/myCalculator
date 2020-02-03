#calculator
from math import*
print("What Operations you wanna peform?")
l=['1.Addition','2.Subtraction','3.Division','4.Square Root',]
x=[]

def getting_input():
    x.clear()
    print("*"*80);print("Enter numbers followed by 'Enter' command or type 'done' from keyboard to proceed further.");print("*"*80);
    while True:
       core_input=input("enter a number : ")
       try:
            if core_input=='done':
             break
            else:
             e=eval(core_input)
             x.append(e)
       except:
           print('*'*100);print(" "*10+"WARNING:Enter a valid input (either a number or done)");print('*' * 100)

def add_sub():
    SUM = 0
    for i in x:
        SUM += i
    print("*"*80);print(" "*10+"answer : ", SUM);print("*"*80);

def div(x):
    if len(x)==2:
        if x[1]==0:
           print("*"*80); print(" "*10+"OOPs can not divide by zero"); print("*"*80);
        else:
         print("*"*80);print(" "*10+"answer :",x[0]/x[1]);print("*"*80);
    else:
        print("*"*80); print(" "*10+"Division requires only two numbers"); print("*"*80)



while True:

 for i in l:
    print("Press",i)
 try:
   number=eval(input("enter a the respective number: "))


   if number==1:
     getting_input()
     add_sub()

   if number==2:
     print(); print("enter numbers with sign")
     getting_input()
     add_sub()

   if number==3:
     print("Enter two numbers: ")
     getting_input()
     div(x)
   if number==4:
      core_input=eval(input("please enter a number : "))
      print("*" * 80);print(" "*10+"answer :",sqrt(core_input));print("*" * 80);
   else:
       print("Please enter a choice between 1 and 4")
 except:
   print("*"*80);print(" "*10+"Please Enter a valid choice");print("*"*80);