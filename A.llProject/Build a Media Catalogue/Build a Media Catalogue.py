print("-"*50)#---------------------------------------------------------------------------------

#Question0:Triple quotation marks 
    # """ are used to create multi-line strings and docstrings
        #multi-line strings:write strings that span multiple line without using \n
        #docstring:check the line below

#Question1:Using Super() to refer to the parent calss 
    # without naming it explicitly super().__init__(arg1,arg2,....)

#Question2: In inheritance,Using Super()to refer to parent class
    #it means that Call Parentclass.__init__ using the same object self
    #So before seasons and total_episodes are set,Python runs everys line
    #in Movie.__init__

#Question3:What is docstring?how to use it?
    #docstring is a string placed as the first statement 
    #in a class or function ,and it's used to provide documentation
    #for that class or function

#Question4:When we use docstring in class or function
    #We can use __doc__ to acess the docstring in these object
        #yeah ,the function is a object it can be assigned variables passed function
        #or printed,stroed data structure
    #And the docstring can't be inherited by any child class

#Question5:Build your own custom exceptions 
    # by inheriting from Exception built-in class
        #Syntax: declare the class Errorname(Exception)
        #def __init__(self,message,obj)---the meassage is the massage of error
        #the obj is one of variable  
    
#Question6:use type function instead of isinstance function
    #to discriminate between parent and child class


print("-"*50)#---------------------------------------------------------------------------------

class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        super().__init__(message)
        self.obj=obj




class Movie:
    """Parent class representing a movie."""
    def __init__(self, title, year, director,duration):
        if not title.strip():
            raise ValueError("Title cannot be empty")
        
        if year<1895:
            raise ValueError("Year must be 1895 or later")
        
        if not director.strip():
            raise ValueError("Director cannot be empty")
        
        if  duration<=0:
            raise ValueError("Duration must be positive")
        
        self.title=title    
        self.year=year    
        self.director=director    
        self.duration=duration

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.duration} min, {self.director}"

class TVSeries(Movie):
        """Child class representing an entire TV series."""
        def __init__(self, title, year, director, duration, seasons,total_episodes):
            
            super().__init__(title, year, director, duration)
            if seasons<1:
                raise ValueError("Seasons must be 1 or greater")
        
            if total_episodes<1:
                raise ValueError("Total episodes must be 1 or greater")
        
            self.seasons=seasons
            self.total_episodes=total_episodes
        
        def __str__(self):
            return f"{self.title} ({self.year}) -\
{self.seasons} seasons, {self.total_episodes} episodes,\
{self.duration} min avg, {self.director}"
            

class MediaCatalogue:
    def __init__(self):
        self.items=[]

    def add(self,media_item):
        if not isinstance(media_item,Movie):
            raise MediaError("Only Movie or TVSeries instances can be added",
                            media_item)
        
        self.items.append(media_item)

    def get_movies(self):
        Movie_filter=[]
        for item in self.items:
            if type(item)==Movie:
                Movie_filter.append(item)
                # print(f"{item.title} ({item.year})")
        return Movie_filter
    
    def get_tv_series(self):
        return [item for item in self.items if isinstance(item, TVSeries)]

    def __str__(self):
        if not self.items:
            return 'Media Catalogue (empty)'
        result=f"Media Catalogue ({len(self.items)} items):\n\n"
        for N,movie in enumerate(self.items,start=1):
            result+=f"{N}. {movie}\n"
        return result

catalogue=MediaCatalogue()

try:
    movie1=Movie("ET",2003,"Sp",123)
    catalogue.add(movie1)
    print(catalogue)
except MediaError as e:
    print(f"Validation Error: {e}")
    print(f'Unable to add {e.obj}: {type(e.obj)}')

print("-"*50)#---------------------------------------------------------------------------------

#Test example00:
movie2=Movie('Dances with Wolves', 1990, 'Kevin Costner', 224)
movie3=Movie('Annie Hall', 1977, 'Woody Allen', 93)
TVSeries1=TVSeries('BCS', 2010, 'Saul', 60,5,50)

catalogue1=MediaCatalogue()
catalogue1.add(movie2)
catalogue1.add(movie3)
catalogue1.add(TVSeries1)

print(catalogue1)

print("-"*50)#---------------------------------------------------------------------------------


#Test example000:
catalogue1.get_movies()


print("-"*50)#---------------------------------------------------------------------------------

#Test example01:
print(movie2.__doc__)
print(TVSeries1.__doc__)

print("-"*50)#---------------------------------------------------------------------------------

#Test example02:Class Error

# catalogue3=MediaCatalogue()
# catalogue3.add(123)

print("-"*50)#---------------------------------------------------------------------------------
