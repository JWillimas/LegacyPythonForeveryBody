from math import radians ,sin ,cos
from test import *
#the The asterisk is telling Python
#that you want to import everything in that module
import math as m

import greet

#import module with difference name

print(round(m.sqrt(36)))
print(sum(1,2))

print("-"*50,"\n")#-----------------------------------------------------


angle_degrees=30
angle_radians=radians(angle_degrees)

angle_sine=sin(angle_radians)
angle_cose=cos(angle_radians)

print(round(angle_sine,ndigits=1))
print(round(angle_cose,ndigits=1))



print("-"*50,"\n")#-----------------------------------------------------

import math
print(math.pi)




print("-"*50,"\n")#-----------------------------------------------------

#idiom in Python scripts




print(greet.__name__)
#the __name__ used in other file as module
#will display as the file name


#if __name__=='__main__'
# It contains the code that you want to run 
# only if the Python script is running as the main program:

print("-"*50,"\n")#-----------------------------------------------------




