from tax import tax


def dekorator_podatku(func):
    
    def wrapper():
        
        if amount<=100000:
            rate = 19
            return rate*amount/100
        elif amount<=200000:
            rate = 22
            return 100000*0.19 + rate*(amount-100000)/100
        elif amount>200000:
            rate = 25
            return 100000*0.19 + 100000*0.22 + rate*(amount-200000)/100
        func()
        
    return wrapper
amount = 99999        
tax=dekorator_podatku(tax)
tax()

print(tax())