def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('You cannot divide by zero')
    return a / b

try:
    divide(1, 0)

except ZeroDivisionError as e:
    print(f"{e}\n\n")


print("-"*50)#----------------------------------------------------


class InvalidCredentialsError(Exception):
    def __init__(self, message="Invalid username or password"):
        self.message = message+"132132131"
        super().__init__(self.message)#to store the error information


def login(username, password):
    stored_username = "admin"
    stored_password = "password123"
    
    if username != stored_username or password != stored_password:
        raise InvalidCredentialsError()
    
    return f"Welcome, {username}!"

try:
    login(1213,46545)

except InvalidCredentialsError as e:
    print(e)


print("-"*50)#----------------------------------------------------

#In try argument ,use raise to manually add a
#Error as needy

#In except Use raise with from to substitue
#the error key word for needy



def parse_config(filename):

  try:
      with open(filename, 'r') as file:
          data = file.read()
          return int(data)
      
  except FileNotFoundError: #(the key word here is None):
      raise ValueError('Configuration file is missing') from None
  except ValueError as e:#e is the error key word here
      raise ValueError('Invalid configuration format') from e
  except OSError :
     print("don't worry the program would continue\n\n\n\n")


config = parse_config(123)

print("-"*50+"\n")#----------------------------------------------------











print("-"*50+"\n")#----------------------------------------------------








print("-"*50+"\n")#----------------------------------------------------