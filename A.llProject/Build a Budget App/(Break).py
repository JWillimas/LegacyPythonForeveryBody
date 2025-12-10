print("*"*50)#------------------------------------------------------------------------

#Question0:for item in self.ledger: 
    #This sentence would iterate each element from self.ledger to item
    
#Question0.5:if we want to use the  element from dict
    #We can loop the list and give it the key as index   

#Question1:f"{self.name:*^30}\n"
    #':*'---means padding with '*' 
        #'^'----center the name
            # '30'-----total_width 30

#Question1.5: list,dict and str operation
    #get element(dict) from list 
        #use dict key to take the context from dict
            #print the str with specific form

#Question2:Quote other class in certain class

#Question3:Calculate the total spend 
    # and write a bar-gra
        #Using Multi loop to write


print("*"*50)#------------------------------------------------------------------------

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
    
    def withdraw(self,amount,description):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        return False
    
    def get_balance(self):
        total=0
        for item in self.ledger:
            total+=item["amount"]
        return total

    def transfer(self,amount,other_Category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to [{other_Category.name}]")
            other_Category.deposit(amount,f"Transfer from [{self.name}]")
            return True
        return False


    def check_funds(self,amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items=""
        for e in self.ledger:
            amt=f"{e["amount"]:.2f}"[:7].rjust(7)
                #[:7]the amount take 7 characters and left aligned
                    #because the value of amount is int
                        #use format to make it subscriptable
            des=e["description"][:23].ljust(23)
            items+=f"{des}{amt}\n"
        total=f"Total:{self.get_balance():.2f}"

        return title+items+total

print("*"*50)#------------------------------------------------------------------------

def create_spend_chart(categories):

    output=f"Percentage spent by category\n"
    spends=[]
    total_spend=0

    for cat in categories:
        spend=0
        for item in cat.ledger:
            if item["amount"]<0 :
                spend+=item["amount"]
        total_spend+=spend
        spends.append(spend)

    percents=[(spend/total_spend*100)//10*10 
              for spend in spends]       

    for level in range(100,-1,-10):
        row=f"{level:>3}|"
        for i in percents:
            row+=" o "  if i>=level else "   "
        output+=row+"\n"
    
    output += "   "+ "-" * (len(categories) * 3 + 1) + "\n"

    max_len=max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row="     "
        for cat in categories:
            char=cat.name[i] if i<len(cat.name) else " "
            row+=char+"  "
        if i< max_len -1 :
            row+="\n"
        output +=row

    print("spends:"+f"{spends}")
    print("percents:"+f"{percents}")
    print(output)



food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(200, "groceries")
food.withdraw(50, "restaurant")

clothing.deposit(500)
clothing.withdraw(100, "jacket")

auto.deposit(1000)
auto.withdraw(300, "fuel")
auto.withdraw(50, "repair")

print(food)

print("*"*50)#------------------------------------------------------------------------

create_spend_chart([food, clothing, auto])




print("*"*50)#------------------------------------------------------------------------
print("*"*50)#------------------------------------------------------------------------