class Dog:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def bark(self) -> str:
        if self.weight >= 100:
            return "WOOF"
        return "woof"


class PetStore:
    def __init__(self, pets: list[Dog]):
        self.pets = pets
        number_of_pets = len(pets)

        if number_of_pets > 8:
            raise ValueError("[!] Too many pets")

    def add_pet(self, pet: Dog) -> None:
        if not isinstance(pet, Dog):
            raise TypeError("[!] PetStore only accepts objects of Dog class")

        self.pets.append(pet)

    def pets_for_sale(self) -> str:
        print("Our pets:")
        for pet in self.pets:
            print(pet.name)


if __name__ == "__main__":
    mutt = Dog('Mutt', 65)
    spot = Dog('Spot', 32)
    gruff = Dog('Gruff', 95)

    store = PetStore([mutt, spot, gruff])

    bingo = Dog('Bingo', 103)
    store.add_pet(bingo)

    store.pets_for_sale()
