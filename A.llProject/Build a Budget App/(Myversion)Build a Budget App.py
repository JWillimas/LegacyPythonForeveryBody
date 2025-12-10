class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
        self.balance=0

    def deposit(self,amount,description) :
        if not amount or description:
            print ("please input a description")
            return
        
        trans_dic={"amount":amount,'description': description}
        
        self.balance+=amount
        self.ledger.append(trans_dic)
    
    def withdraw(self,amount,description) :
        if amount>0:
            return False
        #amount subtracting sucess
        
        self.balance-=amount
        trans_dic={"amount":amount,'description': description}
        self.ledger.append(trans_dic)
        return True 

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        text=self.name.strip()
        starts=30-len(text)
        left=starts//2
        right=starts-left

        lines = [
        f"{t['description'][:23]:<23}{t['amount']:7.2f}"
        for t in self.ledger
    ]


        return f"{'*'*left}{text}{'*'*right}\n\
        {"\n".join(lines)}"
    
    # def transfer(self,amount,Category):
    #     #how to distinguish withdraw and deposit?
    #     self.withdraw(amount,f"Transfer to [{Destination}]")
    #     self.deposit(amount,f"Transfer from [{Source}]")

    # def check_funds(self,amount):
    #     if amount>self.balance:
    #         return False
        
    #     self.withdraw(amount,"")
    #     return True


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
print(food)



