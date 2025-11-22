def say_hello():
    print("Hello from say_hello!")

print("This always runs")

if __name__=="__main__":
    
#When a Python file is executed directly
#Python sets 
#the value of this variable to the string "__main__"


    print("This runs ONLY when greet.py is executed directly")
    say_hello()