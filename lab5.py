from enum import Enum
import math


class PlanetType(Enum):
    TERRESTRIAL = 1
    JOVIAN = 2


class Planet:
    def __init__(self, name, mass, orbital_velocity, mean_temperature,
                 length_of_day, distance_from_sun, planet_type):
        self.name = name 
        self.mass = mass                  
        self.orbital_velocity = orbital_velocity 
        self.mean_temperature = mean_temperature 
        self.length_of_day = length_of_day  
        self.distance_from_sun = distance_from_sun  
        self.planet_type = planet_type 

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def get_length_of_day(self):
        return self.length_of_day

    def get_distance_from_sun(self):
        return self.distance_from_sun

    def print_info(self):
        print("Назва:", self.name)
        print("Маса:", self.mass, "кг")
        print("Орбітальна швидкість:", self.orbital_velocity)
        print("Середня температура:", self.mean_temperature)
        print("Довжина дня:", self.length_of_day)
        print("Відстань від Сонця:", self.distance_from_sun, "млн км")
        print("Тип планети:", self.planet_type.name)
        print("-------------------------------")

    def __del__(self):
        pass


class Planetary:
    def __init__(self, planets):
        self.planets = planets

    def sort_by_day_length(self):
        self.planets.sort(key=lambda p: p.get_length_of_day())

    def find_average_mass(self):
        if len(self.planets) == 0:
            return 0
        total = 0
        for p in self.planets:
            total += p.get_mass()
        return total / len(self.planets)


def findDistanceBetween(planetA, planetB):
    return abs(planetA.get_distance_from_sun() - planetB.get_distance_from_sun())


def main():
    earth = Planet("Earth", 5.97e24, 29.8, 15, 24, 149.6, PlanetType.TERRESTRIAL)
    mars = Planet("Mars", 6.39e23, 24.1, -63, 24.6, 227.9, PlanetType.TERRESTRIAL)
    jupiter = Planet("Jupiter", 1.898e27, 13.1, -108, 9.9, 778.5, PlanetType.JOVIAN)

    earth.print_info()
    mars.print_info()
    jupiter.print_info()

    system = Planetary([earth, mars, jupiter])

    print("Сортування за довжиною дня:")
    system.sort_by_day_length()
    for p in system.planets:
        print(p.get_name(), "-", p.get_length_of_day())

    avg_mass = system.find_average_mass()
    print("\nСередня маса планет =", avg_mass, "кг")

    dist = findDistanceBetween(earth, mars)
    print("\nВідстань між Землею та Марсом =", dist, "млн км")


main()
