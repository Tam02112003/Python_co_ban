"""
 OOP in Python
"""

from abc import ABC, abstractmethod

# Abstraction + Interface
class Animal(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulation

    @abstractmethod
    def speak(self):
        pass

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self._name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self._name} says Meow!"

# Polymorphism
def make_animal_speak(animal: Animal):
    print(animal.speak())

# Test
if __name__ == "__main__":
    d = Dog("Buddy")
    c = Cat("Mimi")
    make_animal_speak(d)   # Buddy says Woof!
    make_animal_speak(c)   # Mimi says Meow!
