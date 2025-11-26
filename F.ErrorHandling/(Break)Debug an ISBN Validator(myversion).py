print("-"*50)#--------------------------------------------------------->
#Question1:In Python, a string behaves like a list of characters
    # so you can index it the same way you index a list.
        #when you quote into other method quikely
            #such as the isbn defined in main() as str and 
                #when it use as parameters in validate_isbn it can be give index to use

#Question2: Make str convert to int-list quiker
    #By use Comprehension Loop
        # main_digits = isbn[0:length-1]
            #main_digits_list = [int(digit) for digit in main_digits]

print("-"*50)#--------------------------------------------------------->

#Test Data:
#1530051126,10
#153005112,10
#9781530051120,13

print("-"*50)#--------------------------------------------------------->

print("-"*50)#--------------------------------------------------------->

#Function context:



def calculate_check_digit(isbn,length:int):
    sum=0

    print(isbn)
    print(len(isbn))

    for index,value in enumerate(isbn):
        sum+=index*int(value)
        print(f"{index}:{value}")

    print(11-sum%11)
    return (11-sum%11)



def Validate_isbn(isbn,length):

    if len(list(isbn))==int(length):

        
        main_digits = int(length)
        given_check_digit =list(isbn[int(length)-1])

        if main_digits==10 :
            expected_check_digit=\
            calculate_check_digit(isbn,10)   
            

        if main_digits==13:
            expected_check_digit=\
            calculate_check_digit(isbn,13) 

        if  given_check_digit==expected_check_digit:
            print("Valid ISBN Code.")
            return
            
        else:
            print("Invalid ISBN Code.")
            return

        
    print("ISBN-length code should " \
    "be length digits long.")
    return
    



def main():
    User_input=input("Enter ISBN,length:")
    values=User_input.split(',')
    isbn=values[0]
    length=values[1]

    print(isbn[7])
    
    if (length=='10') or (length=='13'):
        Validate_isbn(isbn,length)
    
    else :print("please input 10 or 13 digits")

main()
    

print("-"*50)#--------------------------------------------------------->
