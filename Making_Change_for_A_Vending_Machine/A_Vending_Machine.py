print ("************" * 1)
print ("Making Change for a Vending Machine")
print ("************\n" * 1)
from decimal import *



#### Define function ###

nkl = 25
dime = 25
qrt = 25
ones = 0
fives = 0

def store():
    print ("Stock contains:")
    print ("   %d nickels" % nkl)
    print ("   %d dimes" % dime)
    print ("   %d quarters" % qrt)
    print ("   %d ones" % ones)
    print ("   %d fives" % fives)

def initialization():
    print ("Welcome to the vending machine change make program")
    nkl = 25
    dime = 25
    qrt = 25
    ones = 0
    fives = 0
    print ("Change maker initialized.")
    store()

def manu():
    print ("'n' - deposite a nickel")
    print ("'d' - deposite a dime")
    print ("'q' - deposite a quarter")
    print ("'o' - deposite a one dollar bill")
    print ("'f' - deposite a five dollar bill")
    print ("'c' - cancel the purchase")
    manu_list = ['n','d','q','o','f','c']
    
def quit():
    print ("Thank you. Welcome to use our vending machine again!")

def payment_due(pp_input):
    pp_input = float(pp_input)
    pp_1 = pp_input // 1
    pp_2 = round(pp_input * 100 - pp_1 * 100)
    print("Payment due: %d dollars and %d cents" % (int(pp_1),int(pp_2)))

def payment(deposit):
    if deposit == 'n':
        nkl = nkl + 1
        pp = float(int(pp) - 5.0)
        pp_input = pp / 100
        payment_due(pp_input)
        store()
    if deposit == 'd':
        dime = dime + 1
        pp = float(int(pp) - 10.0)
        pp_input = pp / 100
        payment_due(pp_input)
        store()
    if deposit == 'q':
        qrt = qrt + 1
        pp = float(int(pp) - 25.0)
        pp_input = pp / 100
        payment_due(pp_input)
        store()
    if deposit == 'o':
        ones = ones + 1
        pp = float(int(pp) - 100.0)
        pp_input = pp / 100
        payment_due(pp_input)
        store()
    if deposit == 'f':
        fives = fives + 1
        pp = float(int(pp) - 500.0)
        pp_input = pp / 100
        payment_due(pp_input)
        store()
    if deposit == 'c':
        print("You have cancelled the payment.")
        payment_due(pp_input)  
#### Function Definition Finished###

initialization()

pp_input = input("Enter the purchase price (xx.xx) or 'q' to quit:")
manu_list = ['n','d','q','o','f','c']
payment = 0

while pp_input != 'q' and float(pp_input):
    pp = int(float(pp_input) * 100)
    while float(pp) % 5 == 0:
        while float(pp_input) > 0: 
            payment_due(pp_input)
            manu()
            deposit = input ("Indicate your deposit:")
            while deposit not in manu_list:
                print("Illegal selecction.")
                deposit = input ("Indicate your deposit:")
            if deposit == 'n':
                nkl = nkl + 1
                pp = float(int(pp) - 5.0)
                pp_input = pp / 100
                payment_due(pp_input)
                payment = payment + 5
                store()
                continue
            if deposit == 'd':
                dime = dime + 1
                pp = float(int(pp) - 10.0)
                print(pp)
                pp_input = pp / 100
                print(pp_input)
                payment_due(pp_input)
                payment = payment + 10
                store()
                continue
            if deposit == 'q':
                qrt = qrt + 1
                pp = float(int(pp) - 25.0)
                pp_input = pp / 100
                payment_due(pp_input)
                payment = payment + 25
                store()
                continue
            if deposit == 'o':
                ones = ones + 1
                pp = float(int(pp) - 100.0)
                pp_input = pp / 100
                payment_due(pp_input)
                payment = payment + 100
                store()
                continue
            if deposit == 'f':
                fives = fives + 1
                pp = float(int(pp) - 500.0)
                pp_input = pp / 100
                payment_due(pp_input)
                payment = payment + 500
                store()
                continue
            if deposit == 'c':
                print("You have cancelled the payment.")
                print("Your total payment:", payment)
                pp_input = round(0 - payment)/100
                print("your refund due:", pp_input)
                payment = 0
                break
        if pp_input == 0:
            print("No change Due.")
            break
        if pp_input < 0:
            qrt_re = 0
            nkl_re = 0
            dime_re = 0
            refund = round((0 - pp_input)*100)
            print("refund:",refund)
            while refund > 0:
                print("refund due:",refund)
                if qrt != 0 and refund >= 25:
                    print("qrt:", qrt)
                    refund = refund - 25
                    qrt = qrt - 1
                    qrt_re = qrt_re + 1
                    continue
                if dime != 0 and refund >= 10:
                    print("dime:",dime)
                    refund = refund - 10
                    dime = dime - 1
                    dime_re = dime_re + 1
                    continue
                if nkl != 0:
                    print("nkl:", nkl)
                    refund = refund - 5
                    nkl = nkl - 1
                    nkl_re = nkl_re + 1
                    continue
                print("Please contact staff for the following amount:", refund)
                refund_due = refund
                refund = 0
                break
            if refund < 0:
                print("Not enough change")
                store()
                print("Please contact staff for the rest of the change:", refund)
                break
            if refund == 0:
                print("refund complete**********")
                print("please take the change bellow.")
                print(qrt_re, "quarters")
                print(dime_re, "dimes")
                print(nkl_re, "nickels")
                store()
                payment = 0
                break
    if float(pp) % 5 != 0:
        print ("Illegal price: Must be a non-negative multiple of 5 cents.")
    pp_input = input("Enter the purchase price (xx.xx) or 'q' to quit:")
quit()
print ("************\n" * 3)

















