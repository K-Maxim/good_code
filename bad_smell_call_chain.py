# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, planet, country, city, city_population, street, room_num):
        self.planet = planet
        self.country = country
        self.city = city
        self.city_popultaion = city_population
        self.street = street
        self.room_num = room_num

    def get_adress(self):
        return f'{self.planet} {self.country} {self.city} {self.street} {self.room_num}'

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_popultaion

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.


planet = Planet()
country = Country()
city = City()
street = Street()
room = Room()



population = city.population()

person = Person(planet.get_contry(), country.get_city(), city.get_street(), city.population(), street.get_room(), room.get_name())
print(person.get_person_room())
print(person.get_city_population())
print(person.get_adress())

