i=3.3
print(type(i))
class Employee:
    _base_salaries={
    'trainee': 1000,
    'junior': 2000,
    'mid-level': 3000,
    'senior': 4000
}
    def __init__(self,name,level):
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if not level in self._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name=name
        self._level=level
        self._salary=self._base_salaries[level]
    
    def __str__(self) :
        return f"{self._name}: {self._level}"
    
    def __repr__ (self):
        return f"Employee('{self._name}', '{self._level}')"
    #with __repr__ you can print the object 
        # (that can be used to instantiate it)
            # in the way you want
                #Python does not use __str__ 
                    # for the objects inside the list.
                #Instead, Python uses __repr__ for each element 
                    # inside a container (list, dict, tuple, etc.).

    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary<Employee._base_salaries[self._level]:
            raise ValueError(f"Salary must be higher than minimum salary ${Employee._base_salaries[self._level]}")

        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')
    
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise TypeError("'name' must be a string.") 
        self._name=new_name
        print(f"'name' updated to '{self._name}'.")

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if (Employee._base_salaries[self._level]> Employee._base_salaries[new_level]):
            raise ValueError("Cannot change to lower level.")
        self._level = new_level


charlie_brown=Employee('Charlie Brown','junior')
charlie_brown.salary = 500



print(charlie_brown)
print(f"Base salary: ${charlie_brown.salary}")
