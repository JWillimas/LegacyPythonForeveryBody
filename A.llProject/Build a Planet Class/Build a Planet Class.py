print("-"*50)#--------------------------------------------------------->
#Question1:Use method : all() to Loop over the exist iterator then 
    #check the isinstance()
        #Example:all(isinstance(x, str) for x in (name, planet_type, star)):

#Question2:Know clearly about the Usage of 
    # try.....A.....excepet..as...C :......B..... :
        #if the code got X-error in the try block
            #And we already defined it in except:X-error:
                #it will excute the .....B.....
                    #(and the error infomation store in C)
                        #The program would continue
                    
    #raise+CustError+error information
        #custom some Error ,and error infor by self
            #The program would be terminated

    #try....A....except...BError...raise..CError...(CError_Infor)....from...(Berror_Infor or None)...
        #if BError occur in A_Code 
            #Use raise to convert the BError to CError
                #And convert the BError_infor to CError_infor
                    #The program would be terminated
    
print("-"*50)#--------------------------------------------------------->

class Planet:
    def __init__(self, name, planet_type, star):
        
            self.name=name
            self.planet_type=planet_type
            self.star=star

            if  not all(isinstance(x,str) 
                    for x in(name, planet_type, star)):
                raise TypeError ("name, planet type, and star must be strings\n")
            
            if (""in (name,planet_type,star)):
                raise ValueError ("name, planet_type, "
            "and star must be non-empty strings\n")
        
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}...."
    
    def __str__(self):
        return f"Planet: {self.name} |\
            Type: {self.planet_type} |\
                  Star: {self.star}."
       
planet_1=Planet("Earth", "", "Sun")
planet_2=Planet("Jupiter", "Gas Giant", "Sun")
planet_3=Planet("Kepler-22b", "Super-Earth", "Kepler-22")

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())


