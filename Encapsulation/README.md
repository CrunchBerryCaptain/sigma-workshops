The Dog class has a constructor that takes a name and weight. It also has a bark() function that will print("WOOF") if the dog is equal to or larger 100 and print("woof") if the dog is smaller than 100.

Next, the PetStore contains an array of pets. It has a add_pet(pet) function that allows a user to add a pet to the pet store, which is then stored in a list. The PetStore should raise an error if the user tries to put more than 8 Dogs in it. The PetStore should have a pets_for_sale() function that returns the whole pets list. The PetStore should raise an error if the user tries to put something that isn't a Dog in it.

When complete, this code should run successfully.

mutt = Dog('Mutt', 65)
spot = Dog('Spot', 32)
gruff = Dog('Gruff', 95)

store = PetStore([mutt, spot, gruff])

bingo = Dog('Bingo', 103)
store.add_pet(bingo)
