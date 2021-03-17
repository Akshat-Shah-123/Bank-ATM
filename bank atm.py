#bank atm prog using nested loops

print("\n\n🏧🏧💰💰 WELCOME TO WORLDS BEST ATM SERVICE 🏧🏧💰💰")
restart=('Y')
chances=3
balance=1100000
print("================================================")
while(chances>=0):
  pin=int(input(" ENTER THE 4 DIGIT PIN :=="))


  if pin == (1234):

    print("YOU HAVE ENTERED CORRECTED PIN ")
    print("================================================")
    while restart not in ('n','no',"NO","N"):
      print("PLEASE PRESS 1 FOR YOUR BALANCE")
      print("PLEASE PRESS 2 FOR YOUR MAKING WITHDRAW")
      print("PLEASE PRESS 3 FOR MAKING PAY IN")
      print("PLEASE PRESS 4 FOR RETURN CARD")
      print("================================================")
      option=int(input("what would you like to choose?  "))

      if option==1:
        print("your balance is" ,balance,"\n")
        restart=input("would you like to go back??")
        if restart in ('n','no','NO','N'):
          print("THANK YOU!!!")
          break

      elif option==2:
        withdraw= float(input("HOW MUCH YOU WANT TO WITHDRAW ? \n 1000 2000 3000 4000 5000"))
        if withdraw in [1000, 2000, 3000, 4000 ,5000]:
          balance=balance-withdraw
          print("YOUR BALANCE IS ",balance,"\n")
          restart=input("would you like to go back??")
          if restart in ('n','no','NO','N'):
           print("THANK YOU!!!")
           break
        elif withdraw!= [1000,2000,3000,4000,5000] :
          print("INVALID AMOUNT PLEASE TRY AGAIN..")
          restart=('y')
      elif option==3:
        pay_in=float(input("how much you want to pay in...\n"))
        balance=balance+pay_in
        print("YOUR UPDARED BALANCE IS",balance,"\n")
        restart=input("would you like to go back??")
        if restart in ('n','no','NO','N'):
           print("THANK YOU!!!")
           break
      elif option==4:
        print("PLEASE WAIT WHILE YOUR CARD IS BEING RETURNED..\n")
        restart=('y')

  elif pin!=("1234"):
    print("INCORRECT PASSWORD!!!!")
    chances=chances-1
    if chances == 0:
      print(" NO MORE TRIES...")
      break


