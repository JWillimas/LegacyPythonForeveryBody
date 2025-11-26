print("-"*50,"\n")#---------------------------------------------------------


#when you want a code to run when the error might occur
#use try and except method to implement the code

x=10
print(x)

try:
#the block of code 
#where you anticipate an error might occur

    x=10/1

except ZeroDivisionError:
#This block runs 
#If an error of the specified type is raised inside the try.

    print ("You Can't divide by zero!") 

else:
    print("Division successful:", x )

finally:
    print("This block always runs.")

y=10000

print(y)

try:
    y=10/"0"

except (TypeError, ZeroDivisionError) as e:
    print(f"\nError occurred: {e}\n")

#syntax: except any kind of Error
#The e contain the information of These kind of Error
# when it was triggered it just print that out   


#raise statement : control over when and how errors are generated
#enabling you to create custom error conditions enforce specific 
#program behavior.

#put it brifly use raise statement to warp a type of
#Error to customly

print("-"*50,"\n")#---------------------------------------------------------


def check_num(age):
    if age <0:
        raise ValueError ("the age must be larger than 0")
    return age

try:
    check_num(-5)
except ValueError as e :
    print(f"the Error is here :{e}\n\n")

print("-"*50,"\n")#---------------------------------------------------------


class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        self.balance=balance
        self.amount=amount
        super().__init__(f"Insufficient funds: ${balance} available, \
                         ${amount} requested")
        #super() is calling the parent class’s constructor.
        
def withdraw(balance,amount):
    if amount>balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed: {e}\n\n\n')


#---------------------------------------------------------------------
print("-"*50,"\n")#---------------------------------------------------------

#raise ....from None
# suppresses the original exception context:

def parse_config(filename):

    try:
        with open(filename,"r") as file:
            data=file.read()
            return int(data)
        
        
    # except FileNotFoundError:
    #     raise ValueError("1231321321") from None
    
    except FileNotFoundError as e:
        raise ValueError("dwqdqwdwdw")from e
    #change the original exception context(e) to ValueError
    #by using raise
    


#---------------------------------------------------------------------
print("-"*50,"\n")#---------------------------------------------------------

#raise exceptions conditionally using assert statements

def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
#assert is the number must be execute the context inside
#or it will got assertionError
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')



#---------------------------------------------------------------------
print("-"*50,"\n")#---------------------------------------------------------


#Using raise without arguments

def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')


#---------------------------------------------------------------------
print("-"*50,"\n")#---------------------------------------------------------
