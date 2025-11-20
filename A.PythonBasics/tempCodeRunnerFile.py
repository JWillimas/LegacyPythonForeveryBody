full_dot = '●'
# empty_dot = '○'

# def create_character(name,STR,INT,CHA):
    
#     if not isinstance(name,str):
#         return("The character name should be a string")

#     if len(name)>10:
#         return("The character name is too long")
#     if (" "in name):
#         return("The character name should not contain spaces")
    

#     if not (isinstance(STR,int) or isinstance(INT,int) or isinstance(CHA,int)):

#         return "All stats should be integers"
        
    
#     if  STR<1 or INT<1 or CHA<1:
#         return "All stats should be no less than 1"

#     if  STR>4 or INT>4 or CHA>4:
#         return "All stats should be no more than 4"

#     if  (STR+INT+CHA )!=7:
#         return "The character should start with 7 points"

    
#     strength=STR*'●'+(10-STR)*'○'
#     intelligence=INT*'●'+(10-INT)*'○'
#     charisma=CHA*'●'+(10-CHA)*'○'

#     return (f"""
#     {name}
#     STR {strength}
#     INT {intelligence}
#     CHA {charisma}
#     """
#     )



# print(create_character("ren",3.5,2.5,1))