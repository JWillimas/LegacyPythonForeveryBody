#My_Version:

# full_dot = '●'
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

#Optimize_Version:


full_dot = '●'
empty_dot = '○'

def create_character(name, STR, INT, CHA):

    # --- Name checks ---
    if not isinstance(name, str):
        return "The character name should be a string"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # --- Stat type checks ---
    if not all(isinstance(x, int) for x in (STR, INT, CHA)):
        #Use iterable to judge the argument
        #Syntax: all(isinstance()--iterable, for x in (STR, INT, CHA)--iterable object) 
        return "All stats should be integers"
    
    print(type((STR, INT, CHA)))

    # --- Stat value checks ---
    if min(STR, INT, CHA) < 1:
        return "All stats should be no less than 1"

    if max(STR, INT, CHA) > 4:
        return "All stats should be no more than 4"

    if STR + INT + CHA != 7:
        return "The character should start with 7 points"

    # --- Function to create 10-dot stat bar ---
    #No duplicate

    def make_bar(value):
        return full_dot * value + empty_dot * (10 - value)

    # --- Build and return formatted character sheet ---
    return (
        f"{name}\n"
        f"STR {make_bar(STR)}\n"
        f"INT {make_bar(INT)}\n"
        f"CHA {make_bar(CHA)}"
    )


# Example
print(create_character("ren", 3, 3, 1))

