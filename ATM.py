print ("WELCOME TO SBI ATM")
print ("type 'y' to continue")
print ("type 'e' to Exit")
pin=['2345','0987','8765','1234']
lis=[]
am=0
dep=0
balance=98765
n=raw_input(" ")
if n=='e' or n=='E':
    print("THANK YOU")
elif(n=='y' or n=='Y'):
    print("ENTER 4 DIGIT PIN")
    for i in range(0,5):
        if i<4:
            pinn=raw_input("")
            if pinn not in pin:
                print "pin is incorrect"
            else:
                while True:
                    print "PRESS 1 FOR WITHDRAW"
                    print "PRESS 2 FOR DEPOSIT"
                    print "PRESS 3 FOR BALANCE ENQUIRY"
                    print "PRESS 4 FOR MINI STATEMENT"
                    print "PRESS 5 TO EXIT"
                      
                    press=raw_input(" ")
                    if press=='1':
                        print("ENTER AMOUNT TO WITHDRAW")
                        am=int(raw_input(" "))
                        if balance>am:
                            print("COLLECT YOUR CASH")
                            balance=balance-am
                            lis.append("{} amount is withdrawn".format(am))
                            print "YOUR BALANCE IS",balance
                            raw_input("press any key to exit")
                        else:
                            print("NOT ENOUGH BALANCE IN YOUR ACCOUNT")
                        
                    elif press=='2':
                        print("ENTER AMOUNT TO DEPOSIT")
                        dep=int(raw_input(" "))
                        balance=balance+dep
                        lis.append("{} amount is deposit".format(dep))
                        print "YOUR BALANCE IS",balance
                        raw_input("press any key to exit")
                      
                    elif press=='3':
                        print "YOUR BALANCE IS",balance
                        raw_input("press any key to exit")
                      
                    elif press=='4':
                        print("MINI STATEMENT")
                        print 'current balance = ',balance
                        for k in lis:
                            print k
                        raw_input("press any key to exit")
                    
                    elif press=='5':
                        exit()
                    else:
                         print("pressed wrong key")
                       
        else:
            print "YOUR ATM GOT BLOCKES, PLEASE CONTACT TO BANK"
