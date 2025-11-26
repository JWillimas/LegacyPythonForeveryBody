class Planet:
    def __init__(self, name, planet_type, star):

        # 4–6: Type checks
        if not all(isinstance(x, str) for x in (name, planet_type, star)):
            raise TypeError("name, planet type, and star must be strings")

        # 7–9: Empty string checks
        if not name or not planet_type or not star:
            raise ValueError("name, planet_type, and star must be non-empty strings")

        # 10–12: Assign attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # 13–14: orbit method
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # 15–16: __str__ method
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# 17: Create planet instances
planet_1 = Planet("Earth", "", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Kepler-22b", "Super-Earth", "Kepler-22")

# 18: Print each planet (__str__)
print(planet_1)
print(planet_2)
print(planet_3)

# 19: Call orbit on each
print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())
