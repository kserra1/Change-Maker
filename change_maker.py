#from curses.ascii import isdigit
def is_float(n):
    try:
        float(n)
        return True
    except:
        return False

stockNickel=25
stockDimes=25
stockQuarters=25
stockOnes=0
stockFives=0

 


print("Welcome to the vending machine change maker program")
print('Change maker initialized.')
print('Stock contains:')
print(f'   {stockNickel} nickels \n   {stockDimes} dimes \n   {stockQuarters} quarters \n   {stockOnes} ones \n   {stockFives} fives')
print()
priceInput=(input(f'Enter the purchase price (xx.xx) or \`q\' to quit: '))


while (priceInput != 'q'):

    if(is_float(priceInput)!=True ):
        print('Invalid purchase price. Try again\n')
        priceInput=(input(f'Enter the purchase price (xx.xx) or \`q\' to quit: \n'))
        continue    
    inputFloat=float(priceInput)
    price_in_cents=round(inputFloat*100)
    price_in_dollars=price_in_cents//100
    leftoverCents=price_in_cents-(price_in_dollars*100) 
    giveBackChange=0

    if(price_in_cents >0 and price_in_cents%5==0):
        print("Menu for deposits:")
        print(f"  \'n' - deposit a nickel")
        print(f"  \'d' - deposit a dime")
        print(f"  \'q' - deposit a quarter")
        print(f"  \'o' - deposit a one dollar bill")
        print(f"  \'f' - deposit a five dollar bill")
        print(f"  \'c' - cancel the purchase")
        print()

        if(price_in_dollars>0):
            print(f'Payment due: {price_in_dollars} dollars and {leftoverCents} cents')
        elif(price_in_dollars==0):
            print(f'Payment due: {leftoverCents} cents')
       
        depositAmount=input(f'Indicate your deposit: ')

        while(price_in_cents>0):

            continueTransaction=True

            if (depositAmount.isdigit()==False):

                if (depositAmount=='n'):
                    price_in_cents-=5
                    stockNickel+=1
                    price_in_dollars=price_in_cents//100
                    leftoverCents=price_in_cents-(price_in_dollars*100)
                    giveBackChange+=5

                elif (depositAmount == 'd'):
                    price_in_cents-=10
                    stockDimes+=1
                    price_in_dollars=price_in_cents//100
                    leftoverCents=price_in_cents-(price_in_dollars*100)
                    giveBackChange+=10

                elif (depositAmount == 'q'):
                    price_in_cents-=25
                    stockQuarters+=1
                    price_in_dollars=price_in_cents//100
                    leftoverCents=price_in_cents-(price_in_dollars*100)
                    giveBackChange+=25

                elif (depositAmount == 'o'):
                    price_in_cents-=100
                    stockOnes+=1
                    price_in_dollars=price_in_cents//100
                    leftoverCents=price_in_cents-(price_in_dollars*100)
                    giveBackChange+=100

                elif (depositAmount == 'f'):
                    price_in_cents-=500
                    stockFives+=1
                    price_in_dollars=price_in_cents//100
                    leftoverCents=price_in_cents-(price_in_dollars*100)
                    giveBackChange+=500

                elif (depositAmount == 'c'):

                    if(giveBackChange==0):
                        print(f'Please take the change below.')
                        print(f' No change due.')
                        print()
                        print('Stock contains:')
                        print(f'   {stockNickel} nickels \n   {stockDimes} dimes \n   {stockQuarters} quarters \n   {stockOnes} ones \n   {stockFives} fives')
                        print()
                        break
                    giveBackQuarters=abs(giveBackChange)//25

                    if(giveBackQuarters>stockQuarters):
                        giveBackQuarters=stockQuarters
                        stockQuarters=0
                    else:
                        stockQuarters-=giveBackQuarters
                    giveBackChange-=giveBackQuarters*25
                    giveBackDimes=abs(giveBackChange)//10

                    if(giveBackDimes>stockDimes):
                        giveBackDimes=stockDimes
                        stockDimes=0
                    else:
                        stockDimes-=giveBackDimes
                    giveBackChange-=giveBackDimes*10
                    giveBackNickels=abs(giveBackChange)//5

                    if(giveBackNickels>stockNickel):
                        giveBackNickels=stockNickel
                        stockNickel=0
                    else:
                        stockNickel-=giveBackNickels
                        giveBackChange-=giveBackNickels*5
                    print(f'Please take the change below.')

                    if(giveBackQuarters>0):
                        print(f' {giveBackQuarters} quarters')

                    if(giveBackDimes>0):
                        print(f' {giveBackDimes} dimes')

                    if(giveBackNickels>0):
                        print(f' {giveBackNickels} nickels')

                    if(giveBackChange>0):
                        price_in_dollars = abs(giveBackChange) // 100
                        leftoverCents = (abs(giveBackChange) - (price_in_dollars * 100))
                        price_in_dollars-=1
                        leftoverCents-=10
                        print(f'{price_in_dollars} test ')
                        print(f'Machine is out of change.')
                        print(f'See store manager for remaining refund.')   

                        if(price_in_dollars!=0):
                            print(f'Amount due is: {price_in_dollars} dollars and {leftoverCents} cents')
                        else:
                            print(f'Amount due is: {leftoverCents} cents')
                    print()
                    print('Stock contains:')
                    print(f'   {stockNickel} nickels \n   {stockDimes} dimes \n   {stockQuarters} quarters \n   {stockOnes} ones \n   {stockFives} fives')
                    print()
                    break                      

                else:
                    print(f'Illegal deposit: {priceInput}')

                if (price_in_cents>0 and price_in_dollars>0):
                    print(f'Payment due: {price_in_dollars} dollars and {leftoverCents} cents')
                    depositAmount=input(f'Indicate your deposit: ')
                elif(price_in_cents>0 and price_in_dollars==0):
                    print(f'Payment due: {leftoverCents} cents')
                    depositAmount=input(f'Indicate your deposit: ')
                    
                else:

                    if(price_in_cents==0):
                        print(f'Please take the change below.')
                        print(f' No change due.')
                        print()
                        print('Stock contains:')
                        print(f'   {stockNickel} nickels \n   {stockDimes} dimes \n   {stockQuarters} quarters \n   {stockOnes} ones \n   {stockFives} fives')
                        print()
                        print()
                        break

                    change_in_quarters=abs(price_in_cents)//25

                    if(change_in_quarters>stockQuarters):
                        change_in_quarters=stockQuarters
                        stockQuarters=0
                    else:
                        stockQuarters-=change_in_quarters
                    price_in_cents+=change_in_quarters*25
                    change_in_dimes=abs(price_in_cents)//10

                    if(change_in_dimes>stockDimes):
                        change_in_dimes=stockDimes
                        stockDimes=0
                    else:
                        stockDimes-=change_in_dimes
                    price_in_cents+=change_in_dimes*10
                    change_in_nickels=abs(price_in_cents)//5

                    if(change_in_nickels>stockNickel):
                        change_in_nickels=stockNickel
                        stockNickel=0
                    else:
                        stockNickel-=change_in_nickels
                    price_in_cents+=change_in_nickels*5
                    print(f'Please take the change below.')

                    if(change_in_quarters>0):
                        print(f' {change_in_quarters} quarters')

                    if(change_in_dimes>0):
                        print(f' {change_in_dimes} dimes')        

                    if(change_in_nickels>0):
                        print(f' {change_in_nickels} nickels')              

                    if(price_in_cents<0):
                        price_in_dollars = abs(price_in_cents) // 100
                        leftoverCents = (abs(price_in_cents) - (price_in_dollars * 100))
                        print(f'Machine is out of change.')
                        print(f'See store manager for remaining refund.')

                        if(price_in_dollars!=0):
                            print(f'Amount due is: {price_in_dollars} dollars and {leftoverCents} cents')
                            print()
                        else:
                            print(f'Amount due is: {leftoverCents} cents')
                        print()
                        print()   
                    print()
                    print('Stock contains:')
                    print(f'   {stockNickel} nickels \n   {stockDimes} dimes \n   {stockQuarters} quarters \n   {stockOnes} ones \n   {stockFives} fives')
                    print()
                    print()                     
                    break
            else:
                print(f'Illegal selection: {depositAmount}')
                if(price_in_dollars>0):
                    print(f'Payment due: {price_in_dollars} dollars and {leftoverCents} cents')
                elif(price_in_dollars==0):
                    print(f'Payment due: {leftoverCents} cents')
                depositAmount=input(f'Indicate your deposit: ')
                
    else:
        print(f'\nIllegal price: Must be a non-negative multiple of 5 cents.')
        print()
    
    priceInput=(input(f'Enter the purchase price (xx.xx) or \`q\' to quit: '))

totalEndDollars=(stockQuarters*25+stockDimes*10+stockNickel*5)//100
totalEndCents=(stockQuarters*25+stockDimes*10+stockNickel*5)-(totalEndDollars*100)
print(f'Total: {totalEndDollars} dollars and {totalEndCents} cents')



  
                

                    
                    



