class GameCharacter:
    def __init__(self,name):
        self._name=name
        self._health=100
        self._mana=50
        self._level=1
    
    
#Define a getter for read-only access to the character's name
    @property
    def name(self):
        return self._name
    

#Define a getter that returns the current mana.
    @property
    def health(self):
        return self._health
    
    @health.setter
#Define a health setter
    def health(self,new_health):
#Prevents health from being set below 0
        if new_health<0:
            new_health=0
#Caps the health at 100
        if new_health>100:
            new_health=100
        else:self._health=new_health
        

#Define a getter that returns the current mana.
    @property
    def mana(self):
        return self._mana
    
    @mana.setter
#Define a mana setter
    def mana(self,new_mana):
#Prevents mana from being set below 0
        if new_mana<0:
            new_mana=0
#Caps the mana at 50
        if new_mana>50:
            new_mana=50
        self._mana=new_mana

#Return recently level
    @property
    def level(self):
        return self._level
    
#Define a Level_up method
    def level_up(self):
        self._level+=1
        self.health=100
        self.mana=50
        print(f"{self._name} leveled up to {self._level}!")

#Define a __str__ method that returns formatted string
    def __str__(self):
        return f"\
Name: {self.name}\n\
Level: {self.level}\n\
Health: {self.health}\n\
Mana: {self.mana}"


hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats


# Decreases health by 30
    #hero.health=hero.health(getter:100)-30
        #setter:hero.health=70
hero.health -= 110 

hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up